# Instruções para o Claude neste repositório

## Fluxo de trabalho (obrigatório)

- **Nunca** faça commit ou push direto na `main`.
- Toda mudança vai numa branch nova (`claude/<descricao-curta>`) e chega à `main` por **Pull Request**.
- Abra o PR e espere a aprovação da dona do repositório; não faça merge por conta própria.

## Antes de abrir um PR

1. Se mexeu em `fontes/`, em `servicos/` ou em `scripts/gerar_docs.py`, rode `python3 scripts/gerar_docs.py`
   (regenera tópicos, flashcards, resumos, índice de fichas e o índice do README).
2. Se mexeu em `scripts/banco_questoes.py`, rode `python3 scripts/gerar_simulado.py`.
3. Rode `python3 scripts/verificar_links.py` — precisa terminar com 0 links quebrados.

## Convenções

- Conteúdo em português (Brasil).
- `fontes/` guarda os documentos originais: não editar sem pedido explícito.
- Em cada tópico de `docs/`, só os blocos `<!-- extra:... -->` e `<!-- notas:... -->` são preservados ao regenerar.
- Fichas novas seguem `templates/servico.md` e precisam ser registradas em `FICHAS` **e** em `ESCOPO` (status na lista oficial da prova) no `scripts/gerar_docs.py`; o gerador falha se faltar o status.
- A seção didática de cada tópico ("🧠 Antes de começar") e a introdução de cada domínio ficam em `scripts/didatica_docs.py` (o gerador falha se faltar um tópico); não edite essa seção direto em `docs/`.
- As aberturas das fichas ("🧠 Comece pelo problema") ficam em `scripts/introducoes_servicos.py`; registre cada ficha também nesse módulo. As aberturas das páginas de apoio de `docs/00-guia-do-exame/` ficam em `APOIO` de `scripts/didatica_docs.py`.
- Ao mudar qualquer conteúdo didático desses módulos, rode `python3 scripts/gerar_docs.py`. Explique primeiro problema, solução, exemplo e limite, e depois os termos e pontos da prova.
- O corpo das fichas é gerado de `scripts/conteudo_servicos/<categoria>.json`; edite essa fonte editorial, não o Markdown gerado. Preserve anotações no bloco `notas`. Páginas de apoio vêm de `scripts/conteudo_apoio.json`.
- A estrutura de apostila fica em `scripts/apostila.py`, as sequências em `scripts/sequencias_servicos.py`, as explicações de capítulos em `scripts/licoes_topicos.py`, casos estendidos em `scripts/casos_apostila.py` e definições em `scripts/vocabulario_apostila.py`. Registre novos serviços também nas bases e sequências; a geração exige cobertura completa.
- Depois de alterações na apostila, execute `python3 scripts/test_apostila.py`, `python3 scripts/gerar_docs.py` e `python3 scripts/verificar_links.py`. Não use definições automáticas que confundam uma sigla com uma palavra comum ou sentidos diferentes do mesmo termo.
- Texto desatualizado vindo de `fontes/guia-completo-clf-c02.md` é corrigido pela lista `CORRECOES` do `scripts/gerar_docs.py` (a fonte não é editada); avisos no topo de tópicos ficam em `AVISOS`.
- Informações novas só entram se confirmadas em fonte oficial da AWS; o que estiver sem confirmação vai para `docs/00-guia-do-exame/pendencias-de-verificacao.md`.
