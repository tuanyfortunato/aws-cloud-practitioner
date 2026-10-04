# 🔍 Pendências de verificação

Fatos do repositório que **ainda não foram conferidos** em fonte oficial (foram escritos com base em conhecimento
geral e nas fontes originais). Estão ordenados pela chance de cair na prova. Ao confirmar, atualize a ficha e
mova o item para a [página de atualizações](atualizacoes-2025-2026.md).

> Já verificados: ver [verificação](../../fontes/verificacao-fontes-oficiais-2026-10.md) e
> [rodadas 3 e 4](../../fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md).

## Prioridade alta (cobrados diretamente nas tasks)

| # | Afirmação | Onde está | Task |
|---|---|---|---|
| 1 | Transferência: entrada grátis; saída para internet cobrada; entre regiões cobrada; entre AZs cobrada; mesma AZ por IP privado grátis; origem AWS → CloudFront grátis | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) | 4.1 |
| 2 | Exemplos de "Always Free": SQS e SNS (1 milhão de requisições/mês), CloudWatch (10 métricas customizadas, 10 alarmes) | [SQS](../../servicos/integracao/sqs.md), [CloudWatch](../../servicos/gerenciamento/cloudwatch.md) | 4.1 |
| 3 | Capacity Reservations: cobradas mesmo sem uso; combinam com Savings Plans e RIs regionais | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) | 4.1 |
| 4 | RI regional com flexibilidade de tamanho (Linux, tenancy padrão); RI zonal reserva capacidade; ordem de aplicação RIs → Savings Plans | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) | 4.1 |
| 5 | Cost Explorer: granularidade horária paga, horizonte da previsão e do histórico | [Cost Explorer](../../servicos/custos/cost-explorer.md) | 4.2 |
| 6 | CUR hoje é entregue via Data Exports (CUR 2.0, formato FOCUS); Cost Anomaly Detection gratuito | [Outras ferramentas](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) | 4.2 |
| 7 | Lista oficial de tarefas que só o root pode fazer | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md) | 2.3 |
| 8 | Tipos de MFA aceitos (passkeys/FIDO2, app virtual, token TOTP de hardware) | [IAM](../../servicos/seguranca/iam.md) | 2.3 |
| 9 | CloudTrail: data events não registrados por padrão; primeira cópia dos management events num trail é grátis; validação de integridade dos logs | [CloudTrail](../../servicos/gerenciamento/cloudtrail.md) | 2.2 |
| 10 | Security Hub: padrões (FSBP, CIS, PCI DSS, NIST 800-53) e exigência do AWS Config | [Security Hub](../../servicos/seguranca/security-hub.md) | 2.2 |
| 11 | GuardDuty: fontes fundamentais (CloudTrail, VPC Flow Logs, DNS) e planos de proteção | [GuardDuty](../../servicos/seguranca/guardduty.md) | 2.2 |
| 12 | Política de pentest: serviços liberados sem aprovação prévia | [2.10](../02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) | 2.4 |
| 13 | S3: SSE-S3 padrão para objetos novos, Block Public Access e ACLs desativadas por padrão | [S3](../../servicos/armazenamento/s3.md) | 3.6 |
| 14 | S3 Intelligent-Tiering: camadas após 30 e 90 dias, sem taxa de recuperação, objetos < 128 KB não monitorados | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) | 3.6 |
| 15 | Tipos de Storage Gateway (S3 File, FSx File, Volume, Tape) | [Storage Gateway](../../servicos/armazenamento/storage-gateway.md) | 3.6 |
| 16 | Gateway endpoints só para S3 e DynamoDB, gratuitos; Site-to-Site VPN com 2 túneis | [Peering, TGW e endpoints](../../servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) | 3.5 |
| 17 | Políticas de roteamento do Route 53 (inclui IP-based) | [Route 53](../../servicos/redes/route-53.md) | 3.5 |
| 18 | Motores do RDS (inclui Db2) e Multi-AZ DB cluster com 2 standbys legíveis | [RDS](../../servicos/banco-de-dados/rds.md) | 3.4 |
| 19 | Nomes atuais de AppStream 2.0 e WorkSpaces Secure Browser (houve renomeação?) | [WorkSpaces e AppStream](../../servicos/aplicacoes/workspaces-e-appstream.md) | 3.8 |
| 20 | Qual plano novo dá acesso ao Shield Response Team | [Shield](../../servicos/seguranca/shield.md) | 2.4 |

## Prioridade baixa (detalhe ou fora do escopo)

| # | Afirmação | Onde está |
|---|---|---|
| 21 | Glacier Flexible Retrieval Expedited em 1–5 min | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 22 | CloudFront: OAC substitui OAI; diferenças entre CloudFront Functions e Lambda@Edge | [CloudFront](../../servicos/redes/cloudfront.md) |
| 23 | EFS: modo de throughput Elastic como padrão; classes Standard, IA e Archive | [EFS](../../servicos/armazenamento/efs.md) |
| 24 | Aurora Serverless v2 escala até zero | [Aurora](../../servicos/banco-de-dados/aurora.md) |
| 25 | Organizations: RCPs e declarative policies; qual SCP é aplicada automaticamente após 10/07/2026 | [Organizations](../../servicos/gerenciamento/organizations.md) |
| 26 | Amazon Q Developer era o CodeWhisperer; Bedrock não usa dados do cliente para treinar modelos base | [Amazon Q](../../servicos/ia-ml/amazon-q.md), [Bedrock](../../servicos/ia-ml/bedrock.md) |
| 27 | Elastic Disaster Recovery: RPO de segundos e RTO de minutos | [DRS](../../servicos/armazenamento/elastic-disaster-recovery.md) |
| 28 | Snowball Edge Storage Optimized de 210 TB e Compute Optimized de 104 vCPUs | [Snow Family](../../servicos/migracao/snow-family.md) |
| 29 | Data de fim do WorkDocs e página de aposentadoria do Snowmobile | [Fora do escopo](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) |
| 30 | Treinamentos incluídos em cada plano de suporte novo | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |
