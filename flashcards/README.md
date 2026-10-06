# 🃏 Flashcards

Gerados automaticamente (`python3 scripts/gerar_docs.py`) a partir da seção *Revisão* de cada aula: cada pergunta da revisão vira um card.
Clique na pergunta para revelar a resposta.

| Arquivo | Capítulo |
|---|---|
| [capitulo-0.md](capitulo-0.md) | Fundamentos de TI |
| [dominio-1.md](dominio-1.md) | Conceitos de Nuvem |
| [dominio-2.md](dominio-2.md) | Segurança e Conformidade |
| [dominio-3.md](dominio-3.md) | Tecnologia e Serviços |
| [dominio-4.md](dominio-4.md) | Cobrança, Preços e Suporte |
| [anki-clf-c02.tsv](anki-clf-c02.tsv) | Todos, para importar no Anki |

## Importar no Anki

1. Anki → **Arquivo → Importar** → selecione `anki-clf-c02.tsv`.
2. Separador: **Tab**. Campos: 1 = Frente, 2 = Verso, 3 = **Tags** (ex.: `capitulo-0 aula-0_3` ou `dominio-2 secao-2_7`).
3. Use as tags para estudar por domínio ou tópico.

## Adicionar cards

Acrescente uma pergunta na seção `## Revisão` da própria aula: um subtítulo `###` com a pergunta e a resposta
recolhida num `<details>` logo abaixo. O primeiro parágrafo da resposta vira o card. Depois rode
`python3 scripts/gerar_docs.py`; os arquivos desta pasta são sobrescritos a cada execução.
