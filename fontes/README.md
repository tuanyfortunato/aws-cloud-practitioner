# 📚 Fontes originais

Documentos-base do repositório, mantidos **sem edição** como fonte da verdade.

| Arquivo | O que é | Para onde foi o conteúdo |
|---|---|---|
| [guia-completo-clf-c02.md](guia-completo-clf-c02.md) | Guia de estudo completo, por tópico do exame, com perguntas típicas | Dividido em `docs/` (um arquivo por tópico), `flashcards/`, `resumos/comparativos.md` e `resumos/palavras-chave.md` pelo script `scripts/gerar_docs.py` |
| [verificacao-fontes-oficiais-2026-10.md](verificacao-fontes-oficiais-2026-10.md) | Verificação em fontes oficiais da AWS (04/10/2026): exam guide, escopo, mudanças e números | [Escopo oficial](../docs/00-guia-do-exame/escopo-oficial.md), [atualizações](../docs/00-guia-do-exame/atualizacoes-2025-2026.md), avisos no topo dos tópicos, status de escopo das fichas e correções pontuais. **Prevalece** sobre a pesquisa quando houver conflito |
| [verificacao-fontes-oficiais-2026-10-rodadas-3-4.md](verificacao-fontes-oficiais-2026-10-rodadas-3-4.md) | Versão ampliada da verificação (rodadas 1 a 4): termos de cada task, comparação completa dos planos de suporte novos, status de serviços e mais números | Detalhe das tasks no [escopo oficial](../docs/00-guia-do-exame/escopo-oficial.md), [ficha de planos de suporte](../servicos/custos/planos-de-suporte.md), status nas fichas de fora do escopo e correções pontuais. Mesma prioridade da verificação anterior |
| [verificacao-pendencias-2026-10-rodada-2.md](verificacao-pendencias-2026-10-rodada-2.md) | Segunda verificação das pendências (10/2026), com URL oficial e **trecho literal** em cada item — a mais confiável | Lista de tarefas do root, Intelligent-Tiering, pentest, Free Tier, Capacity Reservations, RIs, SCP padrão e demais itens; [pendências](../docs/00-guia-do-exame/pendencias-de-verificacao.md) zeradas |
| [verificacao-pendencias-2026-10.pdf](verificacao-pendencias-2026-10.pdf) | Verificação das 30 pendências (PDF, 10/2026). Qualidade menor: muitos itens "não encontrado" | Só os itens confirmados com URL oficial foram aplicados; ver [pendências](../docs/00-guia-do-exame/pendencias-de-verificacao.md) |
| [pesquisa-atualizacoes-2025-2026.md](pesquisa-atualizacoes-2025-2026.md) | Pesquisa sobre números que caem e mudanças de 2025-2026 | Seções "🔄 Atualizações 2025-2026" dos tópicos (`scripts/extras_pesquisa.py`), [atualizações](../docs/00-guia-do-exame/atualizacoes-2025-2026.md), [números-âncora](../resumos/numeros-ancora.md) e fichas em `servicos/` |

## Como atualizar

1. Edite `guia-completo-clf-c02.md` (ex.: nova pergunta típica, novo tópico).
2. Rode `python3 scripts/gerar_docs.py` — os tópicos, flashcards e resumos são regenerados.
3. O bloco entre `<!-- extra:inicio -->` e `<!-- extra:fim -->` de cada tópico é **preservado**: use-o para complementos próprios.
4. A seção "📝 Minhas anotações" (entre `<!-- notas:inicio -->` e `<!-- notas:fim -->`) também é preservada.
