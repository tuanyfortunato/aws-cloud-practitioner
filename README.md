# ☁️ AWS Certified Cloud Practitioner (CLF-C02) — Estudos

Repositório de documentação para a prova **AWS Certified Cloud Practitioner (CLF-C02)**: guia por tópico do exame,
**99 fichas detalhadas de serviços**, **302 flashcards**, resumos de revisão e acompanhamento do estudo.

## 🚀 Comece por aqui

1. [Guia do exame](docs/00-guia-do-exame/README.md) — formato, domínios, o que cai e o que não cai
2. [Plano de estudos](docs/00-guia-do-exame/plano-de-estudos.md) — cronograma de 6 semanas
3. [O que mudou em 2025-2026](docs/00-guia-do-exame/atualizacoes-2025-2026.md) — valor da prova × valor atual
4. [Progresso](progresso.md) — checklist do que já foi estudado

## 📚 Conteúdo por domínio da prova

| # | Domínio | Peso | Tópicos |
|---|---|---|---|
| 1 | [Conceitos de Nuvem](docs/01-conceitos-de-nuvem/README.md) | 24% | Vantagens da nuvem, Well-Architected, CAF, 7 Rs, economia |
| 2 | [Segurança e Conformidade](docs/02-seguranca-e-conformidade/README.md) | 30% | Responsabilidade compartilhada, IAM, criptografia, logs, detecção de ameaças |
| 3 | [Tecnologia e Serviços de Nuvem](docs/03-tecnologia-e-servicos/README.md) | 34% | Infraestrutura global, computação, bancos, armazenamento, rede, IA, migração |
| 4 | [Cobrança, Preços e Suporte](docs/04-cobranca-precos-e-suporte/README.md) | 12% | Modelos de compra, ferramentas de custo, planos de suporte |

Cada tópico traz o conteúdo cobrado, **Cai na prova**, **Perguntas típicas**, as **atualizações 2025-2026**,
links para as fichas dos serviços e um espaço para suas anotações.

## 🔎 Fichas de serviços

[`servicos/`](servicos/README.md) tem uma ficha por serviço (ou família) com: componentes, **configurações e opções**,
limites e números, cobrança, responsabilidade compartilhada, atualizações recentes, pegadinhas e perguntas típicas.

| Categoria | Exemplos |
|---|---|
| [Computação](servicos/README.md) | EC2, Auto Scaling, ELB, Lambda, ECS, EKS, Fargate, Beanstalk |
| [Armazenamento](servicos/README.md) | S3 e classes, EBS, EFS, FSx, Storage Gateway, Backup |
| [Banco de dados](servicos/README.md) | RDS, Aurora, DynamoDB, ElastiCache, Redshift, Neptune |
| [Redes](servicos/README.md) | VPC, Route 53, CloudFront, Direct Connect, VPN, API Gateway |
| [Segurança](servicos/README.md) | IAM, KMS, Shield, WAF, GuardDuty, Inspector, Macie, Artifact |
| [Gerenciamento](servicos/README.md) | CloudWatch, CloudTrail, Config, Organizations, Trusted Advisor |
| [Analytics, IA e integração](servicos/README.md) | Athena, Kinesis, Glue, SageMaker AI, Bedrock, SQS, SNS, EventBridge |
| [Migração e custos](servicos/README.md) | MGN, DMS, Snow, Cost Explorer, Budgets, planos de suporte |

## 🧠 Revisão

| Material | Para quê |
|---|---|
| [Flashcards](flashcards/README.md) | 302 perguntas e respostas por domínio (+ arquivo para importar no Anki) |
| [Pares que confundem](resumos/comparativos.md) | ~55 pares de serviços vizinhos |
| [Palavras-chave → serviço](resumos/palavras-chave.md) | Gatilhos dos enunciados |
| [Números-âncora](resumos/numeros-ancora.md) | Números que decidem a resposta (e o que não decorar) |
| [Glossário](glossario.md) | Termos e siglas |
| [Simulados](simulados/README.md) | Registro de simulados e erros recorrentes |
| [Labs](labs/README.md) | Práticas no console com cuidado de custos |

## 🗂️ Estrutura do repositório

```
.
├── docs/                    # Conteúdo por tópico do exame (gerado a partir de fontes/)
│   ├── 00-guia-do-exame/    # Formato da prova, plano de estudos, atualizações 2025-2026
│   ├── 01-conceitos-de-nuvem/          # 1.1 a 1.7
│   ├── 02-seguranca-e-conformidade/    # 2.1 a 2.10
│   ├── 03-tecnologia-e-servicos/       # 3.1 a 3.18
│   └── 04-cobranca-precos-e-suporte/   # 4.1 a 4.6
├── servicos/                # 99 fichas detalhadas, por categoria
├── flashcards/              # Gerados das "Perguntas típicas" (Markdown + TSV para Anki)
├── resumos/                 # Comparativos, palavras-chave, números-âncora
├── simulados/               # Registro de simulados e erros recorrentes
├── labs/                    # Exercícios práticos no console
├── fontes/                  # Documentos originais (fonte da verdade)
├── templates/               # Modelos de tópico, ficha de serviço e simulado
├── scripts/                 # Geração dos docs e verificação de links
├── recursos/                # Links úteis
├── assets/imagens/          # Diagramas e prints
├── glossario.md
└── progresso.md
```

## ✍️ Como usar e manter

- **Estudou um tópico?** Atualize o status no topo do arquivo (🔴 → 🟡 → 🟢) e em [progresso.md](progresso.md).
- **Anotações pessoais:** escreva na seção *📝 Minhas anotações* de cada tópico (é preservada ao regenerar).
- **Complementos de um tópico:** use o bloco entre `<!-- extra:inicio -->` e `<!-- extra:fim -->` (também preservado).
- **Mudou algo no guia?** Edite [`fontes/guia-completo-clf-c02.md`](fontes/guia-completo-clf-c02.md) e rode:

  ```bash
  python3 scripts/gerar_docs.py      # regenera tópicos, flashcards, resumos e índice de fichas
  python3 scripts/verificar_links.py # confere se todos os links internos funcionam
  ```

- **Novo serviço?** Copie [`templates/servico.md`](templates/servico.md) para a categoria certa em `servicos/` e
  registre o nome em `FICHAS` dentro de `scripts/gerar_docs.py`.
- **Fez um simulado?** Use o [modelo de simulado](templates/simulado.md) e registre os erros em
  [`simulados/erros-recorrentes.md`](simulados/erros-recorrentes.md).

### Convenções

- Nomes de arquivos em minúsculas, sem acento, separados por hífen.
- Legenda nas fichas: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.
- Preços, limites e nomes de planos mudam: confira as páginas oficiais na semana da prova.
- Nunca faça commit de credenciais AWS (chaves de acesso, `.pem`, IDs de conta).
