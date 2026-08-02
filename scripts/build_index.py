#!/usr/bin/env python3
"""Gera posts.json a partir dos artigos em posts/*.md.

Lê o frontmatter YAML de cada artigo, valida os campos obrigatórios,
ignora rascunhos (published: false) e arquivos inválidos (com aviso),
calcula tempo de leitura e grava o índice ordenado por data (mais novo
primeiro). Roda na GitHub Action a cada push — ver AGENT.md.
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
OUT_FILE = ROOT / "posts.json"

REQUIRED = ["title", "excerpt", "category", "author", "date", "published"]
CATEGORIES = {
    "Saúde Emocional",
    "Espiritualidade",
    "Relacionamentos",
    "Família",
    "Autoconhecimento",
}
WORDS_PER_MINUTE = 200


def parse_post(path: Path) -> tuple[dict | None, str | None]:
    """Retorna (entrada, erro). Se erro, entrada é None."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not match:
        return None, "frontmatter ausente ou mal formado (esperado bloco --- ... ---)"

    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return None, f"YAML inválido: {exc}"

    if not isinstance(meta, dict):
        return None, "frontmatter não é um mapa de campos"

    missing = [f for f in REQUIRED if f not in meta]
    if missing:
        return None, f"campos obrigatórios faltando: {', '.join(missing)}"

    if meta.get("published") is not True:
        return None, "rascunho (published: false) — ignorado"

    if meta["category"] not in CATEGORIES:
        return None, f"categoria inválida: {meta['category']!r} (ver AGENT.md)"

    body = match.group(2).strip()
    if not body:
        return None, "corpo do artigo vazio"

    words = len(re.findall(r"\S+", body))
    entry = {
        "slug": path.stem,
        "title": str(meta["title"]),
        "excerpt": str(meta["excerpt"]),
        "category": meta["category"],
        "tags": [str(t) for t in (meta.get("tags") or [])],
        "author": str(meta["author"]),
        "authorRole": str(meta.get("author_role", "")),
        "date": meta["date"].isoformat() if hasattr(meta["date"], "isoformat") else str(meta["date"]),
        "readingTime": max(1, round(words / WORDS_PER_MINUTE)),
        "url": f"posts/{path.name}",
    }
    if meta.get("cover"):
        entry["cover"] = str(meta["cover"])
    if meta.get("youtube"):
        entry["youtube"] = str(meta["youtube"])

    return entry, None


def main() -> int:
    posts, warnings = [], []
    for path in sorted(POSTS_DIR.glob("*.md")):
        entry, error = parse_post(path)
        if error:
            warnings.append(f"AVISO: {path.name}: {error}")
        else:
            posts.append(entry)

    posts.sort(key=lambda p: p["date"], reverse=True)

    index = {
        "generatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "posts": posts,
    }
    OUT_FILE.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"posts.json gerado: {len(posts)} artigo(s) publicado(s).")
    for warning in warnings:
        print(warning, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
