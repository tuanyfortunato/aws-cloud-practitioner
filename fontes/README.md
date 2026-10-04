# 📚 Fontes originais

Documentos-base do repositório, mantidos **sem edição** como fonte da verdade.

| Arquivo | O que é | Para onde foi o conteúdo |
|---|---|---|
| [guia-completo-clf-c02.md](guia-completo-clf-c02.md) | Guia de estudo completo, por tópico do exame, com perguntas típicas | Dividido em `docs/` (um arquivo por tópico), `flashcards/`, `resumos/comparativos.md` e `resumos/palavras-chave.md` pelo script `scripts/gerar_docs.py` |
| [pesquisa-atualizacoes-2025-2026.md](pesquisa-atualizacoes-2025-2026.md) | Pesquisa sobre números que caem e mudanças de 2025-2026 | Seções "🔄 Atualizações 2025-2026" dos tópicos (`scripts/extras_pesquisa.py`), [atualizações](../docs/00-guia-do-exame/atualizacoes-2025-2026.md), [números-âncora](../resumos/numeros-ancora.md) e fichas em `servicos/` |

## Como atualizar

1. Edite `guia-completo-clf-c02.md` (ex.: nova pergunta típica, novo tópico).
2. Rode `python3 scripts/gerar_docs.py` — os tópicos, flashcards e resumos são regenerados.
3. O bloco entre `<!-- extra:inicio -->` e `<!-- extra:fim -->` de cada tópico é **preservado**: use-o para complementos próprios.
4. A seção "📝 Minhas anotações" (entre `<!-- notas:inicio -->` e `<!-- notas:fim -->`) também é preservada.
