# Instruções para o Claude neste repositório

## Fluxo de trabalho (obrigatório)

- **Nunca** faça commit ou push direto na `main`.
- Toda mudança vai numa branch nova (`claude/<descricao-curta>`) e chega à `main` por **Pull Request**.
- Abra o PR e espere a aprovação da dona do repositório; não faça merge por conta própria.

## Antes de abrir um PR

1. Se mexeu em `fontes/` ou em `servicos/`, rode `python3 scripts/gerar_docs.py`
   (regenera tópicos, flashcards, resumos, índice de fichas e o índice do README).
2. Rode `python3 scripts/verificar_links.py` — precisa terminar com 0 links quebrados.

## Convenções

- Conteúdo em português (Brasil).
- `fontes/` guarda os documentos originais: não editar sem pedido explícito.
- Em cada tópico de `docs/`, só os blocos `<!-- extra:... -->` e `<!-- notas:... -->` são preservados ao regenerar.
- Fichas novas seguem `templates/servico.md` e precisam ser registradas em `FICHAS` no `scripts/gerar_docs.py`.
