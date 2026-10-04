# 🔄 O que mudou em 2025-2026: valor da prova × valor atual

> Verificado em fontes oficiais da AWS em **04/10/2026** ([relatório completo](../../fontes/verificacao-fontes-oficiais-2026-10.md)).
> Pesquisa original: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md).

## A regra mudou: o exam guide foi atualizado

O código continua **CLF-C02**, mas o conteúdo do guia foi atualizado sem troca de código. A consequência mais
importante:

- ✅ **Planos de suporte:** a task 4.3 do guia atual cita **Basic, AWS Business Support+, AWS Enterprise Support e
  AWS Unified Operations**. Estude os **planos novos** primeiro. Os planos clássicos (Developer, Business,
  Enterprise On-Ramp) valem até 01/01/2027 e ainda podem aparecer em questões antigas do banco.
- ✅ **Nomes:** o guia usa **Amazon Quick Sight** e **Amazon SageMaker AI**.
- ✅ **Lista de serviços:** vários serviços saíram ou foram declarados fora do escopo — ver [escopo oficial](escopo-oficial.md).
- ⚠️ **Números que mudaram** (S3 50 TB, SQS 1 MiB): o guia não cita esses valores. Regra prática: marque o valor
  que existir entre as alternativas; se as duas versões aparecerem, prefira o valor atual.

## Tabela de mudanças

| Tema | Valor antigo | Valor atual (oficial) | Desde | Onde estudar |
|---|---|---|---|---|
| **Planos de suporte** | Basic, Developer, Business, Enterprise On-Ramp, Enterprise | **Basic, Business Support+ (US$ 29/mês por conta, crítico 30 min), Enterprise (US$ 5.000/mês, 15 min), Unified Operations (US$ 50.000/mês, 5 min, compromisso de 90 dias)**. Legados encerram em 01/01/2027 | 02/12/2025 | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |
| Enterprise Support | A partir de US$ 15.000/mês | Mínimo de **US$ 5.000/mês** | 02/12/2025 | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |
| Tamanho máximo de objeto S3 | 5 TB | **50 TB**, em todas as classes (não vale no GovCloud) | 02/12/2025 | [S3](../../servicos/armazenamento/s3.md) |
| Mensagem SQS | 256 KiB | **1 MiB** (Standard e FIFO; Lambda event source mapping também) | 04/08/2025 | [SQS](../../servicos/integracao/sqs.md) |
| Mensagem SNS | 256 KiB | Até **1 MiB** configurando `MaximumMessageSize` no tópico; o **padrão continua 256 KiB** | 18/09/2026 | [SNS](../../servicos/integracao/sns.md) |
| Free Tier | Always Free + 12 meses + trials | US$ 100 no cadastro + até US$ 100 por atividades (EC2, RDS, Lambda, Bedrock, Budgets); Free plan por 6 meses ou até acabar o crédito | 15/07/2025 | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| Categorias do Trusted Advisor | 5 | **6** (+ Operational Excellence) | — | [Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md) |
| Família Snow | Snowcone, Snowball Edge, Snowmobile | Snowball Edge só para clientes existentes; novos → DataSync, AWS Data Transfer Terminal ou parceiros. **Saiu da lista do escopo** | 07/11/2025 | [Snow Family](../../servicos/migracao/snow-family.md) |
| AWS IQ | Contratar especialistas | Encerrado → AWS Marketplace Professional Services. **Fora do escopo** | 28/05/2026 | [Recursos de ajuda](../../servicos/custos/recursos-de-ajuda-e-parceiros.md) |
| Cloud9 / CodeStar / CodeCommit | Ferramentas de dev | Cloud9 fechado a novos clientes; CodeStar descontinuado; CodeCommit de volta a GA. **Nenhum dos três está na lista atual** | 2024–2025 | [Code*](../../servicos/desenvolvimento/code-services.md) |
| QuickSight | Amazon QuickSight | **Amazon Quick Sight** (BI dentro do Amazon Quick Suite, hoje "Amazon Quick") | — | [Quick Sight](../../servicos/analytics/quicksight.md) |
| SageMaker | Amazon SageMaker | **Amazon SageMaker AI** | — | [SageMaker AI](../../servicos/ia-ml/sagemaker-ai.md) |
| Timestream | Séries temporais | LiveAnalytics fechado a novos clientes | 20/06/2025 | [Keyspaces, Timestream e outros](../../servicos/banco-de-dados/keyspaces-timestream-e-outros.md) |
| Savings Plans | Compute, EC2 Instance, SageMaker | + **Database Savings Plans**: até 35% (serverless) / até 20% (provisionado), 1 ano, sem pagamento adiantado | 02/12/2025 | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| Migration Hub / Application Discovery Service | Abertos | **Fechados a novos clientes** (continuam no escopo) | 07/11/2025 | [Discovery, Hub e Evaluator](../../servicos/migracao/discovery-migration-hub-e-evaluator.md) |
| Amazon Q Business | Assistente corporativo | Em manutenção, sem novos clientes; apps podem ser conectados ao Quick Suite | 30/07/2026 | [Amazon Q](../../servicos/ia-ml/amazon-q.md) |
| ACM | Certificados públicos só em serviços integrados | + certificados públicos **exportáveis** (pagos, validade de 395 dias) | 17/06/2025 | [ACM](../../servicos/seguranca/certificate-manager.md) |
| CloudFront | Pagamento por uso | + **planos de preço fixo** (Free, Pro US$ 15, Business US$ 200, Premium US$ 1.000) com CDN, WAF e DDoS | 18/11/2025 | [CloudFront](../../servicos/redes/cloudfront.md) |

## Serviços em manutenção ou encerrados (não estudar a fundo)

- **Fechados a novos clientes desde 07/11/2025:** Amazon Glacier (serviço original de *vaults*, diferente das classes S3 Glacier), S3 Object Lambda, Systems Manager Change Manager e Incident Manager, CodeCatalyst, CodeGuru Reviewer, Cloud Directory, Snowball Edge, Fraud Detector, Migration Hub, Application Discovery Service.
- **Desde 30/04/2026:** AWS Audit Manager, CloudTrail Lake, AWS App Runner, IoT FleetWise.
- **Desde 30/07/2026:** Amazon Kendra, Amazon Q Business, Directory Service Simple AD, Service Catalog AppRegistry, Cognito Sync. Bedrock Agents passou a se chamar "Bedrock Agents Classic".
- **Encerrados:** QLDB (31/07/2025), Lookout for Metrics (12/09/2025), Lookout for Vision (31/10/2025), IoT Analytics (15/12/2025), IoT Events (20/05/2026), AWS IQ (28/05/2026). Anunciados em maio/2025: Inspector Classic, Pinpoint, Panorama, Connect Voice ID, DMS Fleet Advisor.
- **WorkSpaces:** PCoIP e Pools em *sunset* (o serviço continua no escopo).

## Divergências antigas resolvidas pela verificação

| Antes | Resultado oficial |
|---|---|
| Read replicas de Oracle/SQL Server: 5 ou 15? | **Até 5** (Oracle, SQL Server); **até 3** (Db2); até 15 (MySQL, MariaDB, PostgreSQL) |
| Desconto máximo de Convertible RI: 66% ou 54%? | **Até 66%** (guia de Savings Plans/RIs) |
| Glacier Flexible Retrieval Expedited 1–5 min | Não confirmado em página oficial consultada (Standard 3–5 h e Bulk 5–12 h confirmados) |
| Enterprise On-Ramp inclui 1 IEM por ano | A página fala em **1 engajamento AWS Countdown por ano** |
| Preços clássicos de Developer (US$ 29), Business (US$ 100), On-Ramp (US$ 5.500) | Não aparecem mais nas páginas oficiais; trate como valores históricos |
