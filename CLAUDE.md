# Instruções para o Claude neste repositório

## Fluxo de trabalho (obrigatório)

- **Nunca** faça commit ou push direto na `main`.
- Toda mudança vai numa branch nova (`claude/<descricao-curta>`) e chega à `main` por **Pull Request**.
- Abra o PR e, quando o gerador, os testes e o verificador de links passarem (ver abaixo), faça você mesmo o merge na `main`. A dona do repositório decidiu assim em 06/10/2026; ela pode revisar e reverter depois.

## Antes de abrir um PR

1. Se mexeu em aulas, fichas, resumos, glossário ou `scripts/gerar_docs.py`, rode `python3 scripts/gerar_docs.py`
   (regenera os índices dos domínios e das fichas, os flashcards e os blocos do README) e `python3 scripts/test_apostila.py`.
2. Se mexeu em `scripts/banco_questoes.py`, rode `python3 scripts/gerar_simulado.py`.
3. Rode `python3 scripts/verificar_links.py` — precisa terminar com 0 links quebrados.
4. Se mexeu em conteúdo de aulas ou fichas, rode `python3 scripts/metricas_apostila.py` e registre a
   tabela na descrição do PR (as métricas apontam problemas; não são metas de quantidade).
5. Se mexeu no gerador da edição impressa ou na `assets/impressao.css`, rode `python3 scripts/gerar_impressa.py`
   e confira as páginas afetadas (precisa de Pandoc, WeasyPrint e mermaid-cli; a saída fica em `build/`, fora do git).

## Convenções

- Conteúdo em português (Brasil).
- `fontes/` guarda os documentos originais: não editar sem pedido explícito.
- Aulas (`docs/`), fichas (`servicos/`), páginas do guia do exame, resumos e glossário começam com `<!-- autoral -->`
  e são **escritos à mão**, no próprio Markdown. O `gerar_docs.py` não reescreve nenhum deles e falha se algum
  perder o marcador. Ele só gera os índices dos domínios e das fichas, os flashcards e os blocos do README.
  Ver [plano de implementação](pendencias/plano-de-implementacao.md).
- Os flashcards de cada aula vêm da seção `## Revisão` do próprio arquivo: uma pergunta por subtítulo `###`, com a
  resposta recolhida num `<details>`; o primeiro parágrafo da resposta vira o flashcard.
- Aulas novas partem de `templates/topico.md`; fichas novas, de `templates/servico.md`, e são registradas em
  `FICHAS` no `scripts/gerar_docs.py`. O índice das fichas lê do cabeçalho de cada ficha o título, o grupo
  (`**Ficha:**`), a frase-resumo e o status do escopo.
- O [glossário](glossario.md) é o único lugar de consulta rápida de termos, em ordem alfabética. Nas aulas, cada termo é
  explicado em prosa no primeiro uso; o glossário serve para relembrar e aponta para a aula que ensina. Definições dizem o que
  o termo é e para que serve, sem frases defensivas (o `test_apostila.py` confere ordem e repetição).
- Explique primeiro o problema, a solução, um exemplo e o limite, e depois os termos e os pontos da prova.
- `fontes/` é registro histórico e não participa da geração.
- A edição impressa (`scripts/gerar_impressa.py`) lê os mesmos Markdown; não duplique conteúdo para o papel.

## Validação das informações (obrigatório)

- **Nunca suponha.** Toda informação sobre a AWS (serviços, limites, preços, nomes, regiões, níveis de suporte, conteúdo e formato da prova) deve ser validada na documentação oficial e atual da AWS antes de entrar no material, inclusive o que parece óbvio ou já está escrito no repositório.
- A AWS muda o tempo todo: não confie em memória, em material antigo nem em fontes de terceiros. Confira a versão vigente na fonte oficial (documentação, páginas de produto e de preços, guia oficial do exame) e, quando possível, cite o link.
- Informações novas só entram se confirmadas em fonte oficial da AWS; o que estiver sem confirmação vai para `docs/00-guia-do-exame/pendencias-de-verificacao.md`.
