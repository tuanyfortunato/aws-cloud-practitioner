# 🔍 Pendências de verificação

Fatos do repositório que **ainda não foram conferidos** em fonte oficial. Estão ordenados pela chance de cair na
prova. Ao confirmar, atualize a ficha e mova o item para "Resolvidos".

> Verificações já feitas: [verificação](../../fontes/verificacao-fontes-oficiais-2026-10.md),
> [rodadas 3 e 4](../../fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md) e
> [verificação das pendências (PDF)](../../fontes/verificacao-pendencias-2026-10.pdf).
>
> ⚠️ A verificação das pendências marcou como "não encontrado" vários fatos bem estabelecidos (ex.: Security Hub
> exige AWS Config). "Não encontrado" significa só que a fonte não foi localizada, **não** que o fato esteja errado.

## ❔ Em aberto — prioridade alta (cobrados diretamente nas tasks)

| # | Afirmação | Onde está | Task |
|---|---|---|---|
| 1 | Transferência de uma origem AWS (S3, EC2) para o CloudFront é gratuita | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) | 4.1 |
| 2 | Exemplos de "Always Free": SQS e SNS (1 milhão de requisições/mês), CloudWatch (10 métricas customizadas, 10 alarmes) | [SQS](../../servicos/integracao/sqs.md), [CloudWatch](../../servicos/gerenciamento/cloudwatch.md) | 4.1 |
| 3 | Capacity Reservations são cobradas mesmo sem uso | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) | 4.1 |
| 4 | RI zonal reserva capacidade; Convertible pode ser trocada; Standard pode ser vendida no RI Marketplace | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) | 4.1 |
| 6 | CUR entregue via Data Exports (CUR 2.0, FOCUS); Cost Anomaly Detection gratuito | [Outras ferramentas](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) | 4.2 |
| 9 | CloudTrail: data events desativados por padrão; primeira cópia dos management events grátis; validação de integridade dos logs | [CloudTrail](../../servicos/gerenciamento/cloudtrail.md) | 2.2 |
| 10 | Security Hub: padrões (FSBP, CIS, PCI DSS, NIST 800-53) e exigência do AWS Config | [Security Hub](../../servicos/seguranca/security-hub.md) | 2.2 |
| 12 | Política de pentest: serviços liberados sem aprovação prévia | [2.10](../02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) | 2.4 |
| 14 | S3 Intelligent-Tiering: camadas após 30 e 90 dias, sem taxa de recuperação, objetos < 128 KB não monitorados | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) | 3.6 |
| 16 | Site-to-Site VPN com 2 túneis por conexão | [VPN](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) | 3.5 |
| 18 | RDS Multi-AZ DB cluster com 2 standbys legíveis | [RDS](../../servicos/banco-de-dados/rds.md) | 3.4 |

## ❔ Em aberto — prioridade baixa

| # | Afirmação | Onde está |
|---|---|---|
| 8 | Número máximo de dispositivos MFA por usuário | [IAM](../../servicos/seguranca/iam.md) |
| 21 | Glacier Flexible Retrieval Expedited em 1–5 min | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 22 | CloudFront: OAC substitui OAI; CloudFront Functions × Lambda@Edge | [CloudFront](../../servicos/redes/cloudfront.md) |
| 23 | EFS: modo Elastic como padrão; classes Standard, IA e Archive | [EFS](../../servicos/armazenamento/efs.md) |
| 25 | Qual SCP é aplicada automaticamente em organizações criadas após 10/07/2026 | [Organizations](../../servicos/gerenciamento/organizations.md) |
| 26 | Amazon Q Developer era o CodeWhisperer; Bedrock não usa dados do cliente para treinar modelos base | [Amazon Q](../../servicos/ia-ml/amazon-q.md), [Bedrock](../../servicos/ia-ml/bedrock.md) |
| 28 | Snowball Edge Storage Optimized de 210 TB e Compute Optimized de 104 vCPUs | [Snow Family](../../servicos/migracao/snow-family.md) |
| 29 | Data de fim do WorkDocs; página de aposentadoria do Snowmobile | [Fora do escopo](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) |
| 30 | Treinamentos incluídos em cada plano de suporte novo | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |

## ✔️ Resolvidos (verificação das pendências, 10/2026)

| # | Resultado | Aplicado em |
|---|---|---|
| 1 | Entrada grátis; mesma AZ por IP privado grátis; saída, entre regiões e entre AZs (nos dois sentidos) cobradas; gateway endpoints sem custo na mesma região | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| 3 | Descontos de Savings Plans e RIs regionais se aplicam às Capacity Reservations | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 4 | RI regional tem flexibilidade de tamanho; RIs são aplicadas antes dos Savings Plans | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 5 | Cost Explorer: 13 meses de histórico; previsão de 3 meses (diária) e 12 meses (mensal), intervalo de 80%; API a US$ 0,01 por requisição | [Cost Explorer](../../servicos/custos/cost-explorer.md) |
| 7 | Só o root: alterar nome, e-mail ou senha da conta; fechar a conta; mudar o plano de suporte | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md) |
| 8 | MFA aceita passkeys/FIDO2, app virtual e token TOTP de hardware | [IAM](../../servicos/seguranca/iam.md) |
| 11 | GuardDuty: fontes fundamentais + planos S3, EKS, Runtime Monitoring, Malware (EC2, S3, Backup), RDS, Lambda e **AI Protection**; Extended Threat Detection | [GuardDuty](../../servicos/seguranca/guardduty.md) |
| 13 | S3: SSE-S3 padrão desde 05/01/2023; Block Public Access e ACLs desativadas por padrão em buckets novos | [S3](../../servicos/armazenamento/s3.md) |
| 15 | Storage Gateway: S3 File e Volume continuam; **FSx File Gateway** e Tape Gateway em **Snowball Edge** descontinuados para novos clientes | [Storage Gateway](../../servicos/armazenamento/storage-gateway.md) |
| 16 | Gateway endpoints só para S3 e DynamoDB, sem custo | [Peering, TGW e endpoints](../../servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) |
| 17 | Políticas do Route 53: simple, failover, geolocation, latency, weighted, IP-based, multivalue (geoproximity não citada na fonte, mas existe) | [Route 53](../../servicos/redes/route-53.md) |
| 18 | RDS suporta Db2 | [RDS](../../servicos/banco-de-dados/rds.md) |
| 19 | WorkSpaces Web → **WorkSpaces Secure Browser** (05/2024); NICE DCV → **Amazon DCV** | [WorkSpaces](../../servicos/aplicacoes/workspaces-e-appstream.md) |
| 20 | SRT exige Business Support+, Enterprise ou Unified Operations (+ IAM role com `AWSShieldDRTAccessPolicy`) | [Shield](../../servicos/seguranca/shield.md) |
| 24 | Aurora Serverless v2 com auto-pause até 0 ACU | [Aurora](../../servicos/banco-de-dados/aurora.md) |
| 25 | RCPs e declarative policies existem; raiz recebe `RCPFullAWSAccess`; RCPs não afetam a conta de gerenciamento nem service-linked roles | [Organizations](../../servicos/gerenciamento/organizations.md) |
| 27 | Elastic Disaster Recovery: RPO subsegundo, RTO em minutos | [DRS](../../servicos/armazenamento/elastic-disaster-recovery.md) |
