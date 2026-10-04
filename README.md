# ☁️ AWS Certified Cloud Practitioner (CLF-C02) — Estudos

Repositório de documentação e anotações para a prova **AWS Certified Cloud Practitioner (CLF-C02)**.

## 🚀 Comece por aqui

1. [Guia do exame](docs/00-guia-do-exame/README.md) — formato, domínios e dicas
2. [Plano de estudos](docs/00-guia-do-exame/plano-de-estudos.md) — cronograma semanal
3. [Progresso](progresso.md) — checklist do que já foi estudado

## 📚 Conteúdo por domínio da prova

| # | Domínio | Peso |
|---|---|---|
| 1 | [Conceitos de Nuvem](docs/01-conceitos-de-nuvem/README.md) | 24% |
| 2 | [Segurança e Conformidade](docs/02-seguranca-e-conformidade/README.md) | 30% |
| 3 | [Tecnologia e Serviços de Nuvem](docs/03-tecnologia-e-servicos/README.md) | 34% |
| 4 | [Cobrança, Preços e Suporte](docs/04-cobranca-precos-e-suporte/README.md) | 12% |

## 🗂️ Estrutura do repositório

```
.
├── docs/                    # Anotações organizadas pelos domínios oficiais da prova
│   ├── 00-guia-do-exame/    # Formato da prova, plano de estudos
│   ├── 01-conceitos-de-nuvem/
│   ├── 02-seguranca-e-conformidade/
│   ├── 03-tecnologia-e-servicos/
│   └── 04-cobranca-precos-e-suporte/
├── resumos/                 # Cheat sheets: comparativos e palavras-chave
├── flashcards/              # Perguntas e respostas por domínio
├── simulados/               # Registro de simulados e erros recorrentes
├── labs/                    # Exercícios práticos no console AWS
├── templates/               # Modelos para novos tópicos, serviços e simulados
├── recursos/                # Links e materiais de referência
├── assets/imagens/          # Diagramas e prints usados nas anotações
├── glossario.md             # Termos e siglas
└── progresso.md             # Acompanhamento do estudo
```

## ✍️ Como usar

- **Estudou um tema?** Preencha o arquivo do tópico em `docs/` e atualize o status (🔴 → 🟡 → 🟢).
- **Novo tópico ou serviço?** Copie um modelo de [`templates/`](templates/).
- **Fez um simulado?** Crie um arquivo em [`simulados/`](simulados/) com o [modelo de simulado](templates/simulado.md) e anote os erros.
- **Errou o mesmo conceito duas vezes?** Leve para [`simulados/erros-recorrentes.md`](simulados/erros-recorrentes.md).
- **Imagens:** salve em `assets/imagens/` e referencie com `![descrição](../../assets/imagens/arquivo.png)`.

### Convenções

- Nomes de arquivos em minúsculas, sem acento, separados por hífen (`modelos-de-preco.md`).
- Pastas numeradas seguem a ordem dos domínios da prova.
- Nunca faça commit de credenciais AWS (chaves de acesso, `.pem`, IDs de conta).
