# 🃏 Flashcards

Gerados automaticamente a partir das *Perguntas típicas* de cada tópico (`python3 scripts/gerar_docs.py`).
Clique na pergunta para revelar a resposta.

| Arquivo | Domínio |
|---|---|
| [dominio-1.md](dominio-1.md) | Conceitos de Nuvem |
| [dominio-2.md](dominio-2.md) | Segurança e Conformidade |
| [dominio-3.md](dominio-3.md) | Tecnologia e Serviços |
| [dominio-4.md](dominio-4.md) | Cobrança, Preços e Suporte |
| [anki-clf-c02.tsv](anki-clf-c02.tsv) | Todos, para importar no Anki |

## Importar no Anki

1. Anki → **Arquivo → Importar** → selecione `anki-clf-c02.tsv`.
2. Separador: **Tab**. Campos: 1 = Frente, 2 = Verso, 3 = **Tags** (ex.: `dominio-2 secao-2_7`).
3. Use as tags para estudar por domínio ou tópico.

## Adicionar cards

Acrescente a pergunta na seção *Perguntas típicas* do tópico em
[`fontes/guia-completo-clf-c02.md`](../fontes/guia-completo-clf-c02.md), no formato:

```markdown
- "Pergunta?" → Resposta.
```

e rode o script. Os arquivos desta pasta são sobrescritos a cada execução.

## ⚠️ Atenção: planos de suporte

Os cards de planos de suporte vêm do guia original (modelo clássico). As respostas foram **ajustadas na geração**
para indicar o plano atual (ex.: "Business Support+ (no modelo clássico, Business)"), conforme as correções em
`CORRECOES` no `scripts/gerar_docs.py`. Tabela completa na [ficha de planos de suporte](../servicos/custos/planos-de-suporte.md).
