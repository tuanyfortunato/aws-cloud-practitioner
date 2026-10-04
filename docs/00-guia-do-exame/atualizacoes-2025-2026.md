# 🔄 O que mudou em 2025-2026: valor da prova × valor atual

O exam guide da CLF-C02 (versão 1.0) **não foi reescrito** após as mudanças abaixo. A regra prática é:
**responda com a opção que existe entre as alternativas, priorizando o modelo do exam guide**. Quando um
simulado recente usar os nomes novos (ex.: Business Support+), trate como conhecimento atual.

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). As recomendações de
> "responder pelo modelo clássico" são inferência, não regra oficial.

| Tema | Valor "da prova" (clássico) | Valor atual | Desde | Onde estudar |
|---|---|---|---|---|
| Tamanho máximo de objeto S3 | 5 TB | **50 TB** | 02/12/2025 | [S3](../../servicos/armazenamento/s3.md) |
| Mensagem SQS (e SNS) | 256 KB | **1 MiB** | 04/08/2025 | [SQS](../../servicos/integracao/sqs.md) |
| Free Tier | Always Free + 12 meses + trials | Créditos (US$ 100 + até US$ 100); Free plan por 6 meses ou até acabar o crédito | 15/07/2025 | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| Planos de suporte | Basic, Developer, Business, Enterprise On-Ramp, Enterprise | Basic, **Business Support+**, Enterprise, **Unified Operations** (legados acabam em 01/01/2027) | dez/2025 | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |
| Categorias do Trusted Advisor | 5 | **6** (+ Operational Excellence) | — | [Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md) |
| Família Snow | Snowcone, Snowball Edge, Snowmobile | Snowball Edge só para clientes existentes; novos → DataSync / Data Transfer Terminal | 07/11/2025 | [Snow Family](../../servicos/migracao/snow-family.md) |
| AWS IQ | Contratar especialistas freelancers | Encerrado → **AWS Marketplace Professional Services** | 28/05/2026 | [4.6](../04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md) |
| Cloud9 | IDE no navegador | Fechado a novos clientes → **CloudShell** | 25/07/2024 | [CLI, SDK e CloudShell](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) |
| CodeStar | Projetos de CI/CD | Descontinuado | 31/07/2024 | [Code*](../../servicos/desenvolvimento/code-services.md) |
| CodeCommit | Repositório Git | Fechado em 2024, **voltou a GA** | 24/11/2025 | [Code*](../../servicos/desenvolvimento/code-services.md) |
| QuickSight / SageMaker | Amazon QuickSight / Amazon SageMaker | **Amazon Quick Sight** / **Amazon SageMaker AI** | — | [QuickSight](../../servicos/analytics/quicksight.md) · [SageMaker AI](../../servicos/ia-ml/sagemaker-ai.md) |
| Timestream | Séries temporais | Timestream for LiveAnalytics fechado a novos clientes | 20/06/2025 | [Keyspaces, Timestream e outros](../../servicos/banco-de-dados/keyspaces-timestream-e-outros.md) |
| Enterprise Support | A partir de US$ 15.000/mês | Mínimo de **US$ 5.000/mês** | dez/2025 | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |
| Savings Plans | Compute, EC2 Instance, SageMaker | + **Database Savings Plans** (até 35%) | 2025 | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |

## Fontes conflitantes (registradas sem escolher lado)

- Desconto máximo de **Convertible RIs**: 66% (página de preços de RI) × 54% (Well-Architected SAP Lens).
- Limite de **read replicas** para Oracle/SQL Server no RDS: 5 × 15.
- Número de **checks do Trusted Advisor**: vários números em fontes de terceiros.
- Duração mínima do **S3 Intelligent-Tiering**: 30 dias × nenhuma.

Nenhum desses é cobrança típica de prova.
