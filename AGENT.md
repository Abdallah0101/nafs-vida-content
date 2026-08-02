# AGENT.md — Instruções para publicação de artigos (Nafs & Vida)

> Este arquivo é o **contrato** entre o agente de IA (Telegram) e este repositório.
> Siga-o à risca. Se algo não estiver previsto aqui, NÃO improvise a estrutura —
> pergunte ao mantenedor humano.

## 1. O que é este repositório

Repositório de **conteúdo** do blog Nafs & Vida (Psicologia Islâmica).
Contém apenas artigos em Markdown, imagens de capa e o índice `posts.json`.
O site lê este repositório em tempo de execução e renderiza os artigos
automaticamente.

## 2. Publicar um artigo = 2 arquivos (3 com capa)

Para cada artigo novo, o agente DEVE entregar no mesmo commit:

1. **`posts/<slug>.md`** — o artigo (formato abaixo)
2. **`posts.json` ATUALIZADO** — o objeto do artigo adicionado ao array `posts`,
   mantendo a ordem por data (mais novo PRIMEIRO)
3. *(opcional)* **`covers/<imagem>.jpg`** — a capa

- **NUNCA** edite artigos de outros autores sem instrução explícita do humano.
- Não crie pastas novas, não mexa em `AGENT.md`, `README.md`, `.gitignore`.

## 3. O artigo: `posts/<slug>.md`

### 3.1 Nome do arquivo (slug)

- Minúsculas, sem acentos, sem espaços — palavras separadas por hífen.
- Termina com `.md`. O nome do arquivo (sem `.md`) vira a URL do artigo.
- Ex.: `posts/ansiedade-mente-acelerada.md` → `/blog/ansiedade-mente-acelerada`
- O slug do arquivo DEVE ser igual ao campo `"slug"` no `posts.json`.

### 3.2 Cabeçalho (frontmatter YAML) — obrigatório

```yaml
---
title: "Título do artigo"
excerpt: "Resumo de 1 a 2 frases, até 160 caracteres."
category: Saúde Emocional
tags: [ansiedade, dhikr]
author: "Nome do Autor"
author_role: "Psicóloga"        # ou "Sheikh", "Conselheiro", etc.
date: 2026-08-02                # AAAA-MM-DD
published: true                 # false = rascunho (não aparece no site)
cover: covers/nome-da-imagem.jpg   # OPCIONAL — apagar a linha se não houver
youtube: "https://youtu.be/VIDEO_ID" # OPCIONAL — apagar a linha se não houver
---
```

Campos **obrigatórios**: `title`, `excerpt`, `category`, `author`, `date`, `published`.
Campos **opcionais**: `tags`, `author_role`, `cover`, `youtube` (se não usar, REMOVA a linha — não deixe vazio).

### 3.3 Categorias permitidas

Use EXATAMENTE uma destas (respeite acentos e maiúsculas):

- `Saúde Emocional`
- `Espiritualidade`
- `Relacionamentos`
- `Família`
- `Autoconhecimento`

Se o artigo pedir uma categoria nova, confirme com o humano antes.

### 3.4 Corpo do artigo (Markdown)

- Idioma: **português (pt-BR)**.
- **NÃO** use título de nível 1 (`#`). O título já vem do frontmatter.
  Use `##` para seções e `###` para subseções.
- Recursos permitidos: `**negrito**`, `*itálico*`, listas com `-`,
  citações com `>`, termos em árabe (ex.: نَفْس) quando fizer sentido.
- **PROIBIDO**: HTML, iframes, scripts, links encurtados (bit.ly etc.).
- Vídeo/podcast NÃO vai no corpo — use o campo `youtube:` do frontmatter.
- Tamanho ideal: 400 a 900 palavras.
- Tom: acolhedor, profissional, respeitoso com a tradição islâmica.

## 4. O índice: `posts.json`

Arquivo JSON na raiz. Estrutura:

```json
{
  "generatedAt": "2026-08-02T12:00:00Z",
  "posts": [
    {
      "slug": "dhikr-e-presenca-atencao-plena-no-isla",
      "title": "Dhikr e presença: a atenção plena que sempre esteve no Islã",
      "excerpt": "Muito antes da atenção plena virar tema da psicologia...",
      "category": "Espiritualidade",
      "tags": ["dhikr", "atenção plena"],
      "author": "Equipe Nafs & Vida",
      "authorRole": "Psicologia Islâmica",
      "date": "2026-06-28",
      "readingTime": 3,
      "url": "posts/dhikr-e-presenca-atencao-plena-no-isla.md",
      "cover": "covers/dhikr.jpg",
      "youtube": "https://youtu.be/VIDEO_ID"
    }
  ]
}
```

Regras do JSON:

- Sempre **JSON válido**: aspas duplas, sem vírgula sobrando, UTF-8.
- `posts` ordenado por `date` **decrescente** (artigo novo entra na posição
  correta da data — normalmente o topo).
- `"slug"` igual ao nome do arquivo sem `.md`; `"url"` = `posts/<slug>.md`.
- `"readingTime"`: palavras do corpo ÷ 200, arredondado (mínimo 1).
- `"cover"` e `"youtube"`: incluir só quando existirem (senão, omitir o campo).
- `"generatedAt"`: data/hora UTC do momento da publicação (ISO 8601).
- Rascunho (`published: false` no .md): o artigo NÃO entra no `posts.json`.
- Antes de commitar, valide mentalmente o JSON — um JSON quebrado derruba a
  listagem do blog. Se não tiver certeza, regrave o arquivo inteiro com cuidado.

## 5. Imagens de capa (opcional)

- Pasta `covers/`, formatos `.jpg` ou `.webp`, até ~500 KB, proporção ~16:9.
- Nome do arquivo segue a regra do slug (minúsculas, hífens, sem acentos).
- Referencie como `cover: covers/arquivo.jpg` (no .md e no posts.json).
- Sem imagem? Omita o campo — o site usa uma arte padrão.

## 6. O que acontece depois do push

1. O GitHub recebe o commit com o `.md` + `posts.json`.
2. O site lê o `posts.json` atualizado e publica o artigo em ~1–2 minutos,
   em `/blog/<slug>`. Nenhuma outra ação é necessária.

## 7. Exemplo completo de corpo (modelo)

```markdown
Muito antes de a atenção plena ganhar manuais de psicologia, o Islã já
ensinava a arte de estar presente: o **dhikr**, a lembrança constante de Allah.

## A mente que vaga

Pesquisas em psicologia mostram que uma mente errante tende à ansiedade...

## O dhikr como treino de presença

> "Por isso, lembrai-vos de Mim, e Eu Me lembrarei de vós." (Alcorão 2:152)

Praticar o dhikr é, em essência, ancorar a atenção...
```

## 8. Checklist antes de publicar

- [ ] Arquivo em `posts/` com slug válido
- [ ] Todos os campos obrigatórios no frontmatter
- [ ] `category` é uma das 5 permitidas (escrita exata)
- [ ] `date` no formato AAAA-MM-DD
- [ ] `posts.json` atualizado, JSON válido, ordem por data desc
- [ ] `"slug"` no JSON igual ao nome do arquivo
- [ ] Sem `#` (H1), sem HTML, sem iframe no corpo
- [ ] Autor e função conferidos com o humano que enviou o texto
