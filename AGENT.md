# AGENT.md — Instruções para publicação de artigos (Nafs & Vida)

> Este arquivo é o **contrato** entre o agente de IA (Telegram) e este repositório.
> Siga-o à risca. Se algo não estiver previsto aqui, NÃO improvise a estrutura —
> pergunte ao mantenedor humano.

## 1. O que é este repositório

Repositório de **conteúdo** do blog Nafs & Vida (Psicologia Islâmica).
Contém apenas artigos em Markdown e imagens de capa. O site lê este
repositório em tempo de execução e renderiza os artigos automaticamente.

## 2. Regra de ouro

- A ÚNICA ação permitida: **criar novos arquivos** em `posts/<slug>.md`
  e, opcionalmente, imagens em `covers/`.
- **NUNCA** edite ou crie `posts.json` manualmente — ele é gerado
  automaticamente por uma GitHub Action a cada push.
- **NUNCA** edite artigos de outros autores sem instrução explícita do humano.
- Não crie pastas novas, não mexa em `.github/`, `scripts/`, `AGENT.md`, `README.md`.

## 3. Criando um artigo

### 3.1 Nome do arquivo (slug)

- Minúsculas, sem acentos, sem espaços — palavras separadas por hífen.
- Termina com `.md`. O nome do arquivo (sem `.md`) vira a URL do artigo.
- Ex.: `posts/ansiedade-mente-acelerada.md` → `/blog/ansiedade-mente-acelerada`

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

### 3.5 Imagens de capa (opcional)

- Pasta `covers/`, formatos `.jpg` ou `.webp`, até ~500 KB, proporção ~16:9.
- Nome do arquivo segue a regra do slug (minúsculas, hífens, sem acentos).
- Referencie no frontmatter como `cover: covers/arquivo.jpg`.
- Sem imagem? Remova a linha `cover:` — o site usa uma arte padrão.

## 4. O que acontece depois do push

1. A GitHub Action lê `posts/*.md`, valida os cabeçalhos e gera `posts.json`.
2. O site publica o artigo em ~2 minutos, em `/blog/<slug>`.
3. Se o cabeçalho estiver inválido, o artigo é **ignorado** (não quebra o site).

## 5. Exemplo completo (modelo para copiar)

```markdown
---
title: "Dhikr e presença: a atenção plena que sempre esteve no Islã"
excerpt: "Muito antes da atenção plena virar tema da psicologia, o Islã já ensinava a arte de estar presente."
category: Espiritualidade
tags: [dhikr, atenção plena]
author: "Equipe Nafs & Vida"
author_role: "Psicologia Islâmica"
date: 2026-06-28
published: true
---

Muito antes de a atenção plena ganhar manuais de psicologia, o Islã já
ensinava a arte de estar presente: o **dhikr**, a lembrança constante de Allah.

## A mente que vaga

Pesquisas em psicologia mostram que uma mente errante tende à ansiedade...

## O dhikr como treino de presença

> "Por isso, lembrai-vos de Mim, e Eu Me lembrarei de vós." (Alcorão 2:152)

Praticar o dhikr é, em essência, ancorar a atenção...
```

## 6. Checklist antes de publicar

- [ ] Arquivo em `posts/` com slug válido
- [ ] Todos os campos obrigatórios preenchidos
- [ ] `category` é uma das 5 permitidas (escrita exata)
- [ ] `date` no formato AAAA-MM-DD
- [ ] `published: true` (ou `false` se for rascunho)
- [ ] Sem `#` (H1), sem HTML, sem iframe no corpo
- [ ] Autor e função conferidos com o humano que enviou o texto
