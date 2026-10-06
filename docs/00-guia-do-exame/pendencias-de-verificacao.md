# 🔍 Pendências de verificação

<!-- didatico:inicio -->
## 🧭 Antes de ler

**Por que esta página existe?** Algumas afirmações do material ainda precisam de confirmação oficial. Sem uma indicação clara, elas poderiam ser tratadas como fatos seguros.

**Como usar?** Esta página registra pontos em aberto para revisão. Uma pendência é algo a confirmar, não uma regra a decorar.

**Exemplo:** Se encontrar um prazo sem confirmação, use as referências verificadas do tópico para estudar e mantenha esse prazo como pendente até haver evidência adequada.
<!-- didatico:fim -->

> ✅ **Nenhuma pendência aberta** desde a [segunda verificação das pendências](../../fontes/verificacao-pendencias-2026-10-rodada-2.md)
> (04/10/2026), feita com URL oficial e trecho literal para cada item.
>
> Se surgir uma nova dúvida, acrescente aqui: afirmação, onde está no repositório e a task do exam guide.
> Verificações anteriores: [verificação](../../fontes/verificacao-fontes-oficiais-2026-10.md),
> [rodadas 3 e 4](../../fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md) e
> [primeira verificação das pendências (PDF)](../../fontes/verificacao-pendencias-2026-10.pdf).

## 🧭 Para que serve esta página

> 💡 **Em palavras simples:** é a lista de **afirmações que ainda precisam ser confirmadas** em fonte oficial da AWS.
> Enquanto uma informação estiver aqui, trate-a com cuidado. Quando é confirmada, ela sai de *Em aberto* e vai para *Resolvidos*.

## ❔ Em aberto

| # | Afirmação | Onde está | Task |
|---|---|---|---|
| — | — | — | — |

## ⚠️ Correções importantes desta rodada

| Antes no repositório | Resultado oficial | Aplicado em |
|---|---|---|
| "Mudar o plano de suporte" e "alterar o nome da conta" exigem o root | **Não exigem mais.** Nome da conta, contatos e regiões não exigem root; o plano de suporte saiu da lista oficial | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md), [IAM](../../servicos/seguranca/iam.md), [planos de suporte](../../servicos/custos/planos-de-suporte.md), [simulado](../../simulados/simulado-01.md) |
| Intelligent-Tiering "sem taxa de recuperação" | Standard e Bulk grátis, mas **Expedited na camada Archive Access é cobrado**, além do monitoramento por objeto | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| CloudTrail Lake fechado a novos clientes em 30/04/2026 | **31/05/2026** (anúncio de 31/03/2026) | [CloudTrail](../../servicos/gerenciamento/cloudtrail.md) |
| Security Hub "exige" o AWS Config | A maioria dos controles usa o Config; com o Security Hub novo, o recorder é criado automaticamente | [Security Hub](../../servicos/seguranca/security-hub.md) |

## ✔️ Resolvidos

| # | Resultado | Aplicado em |
|---|---|---|
| 1 | Origem AWS (S3, EC2, ELB) → CloudFront grátis; entrada grátis; mesma AZ por IP privado grátis; saída, entre regiões e entre AZs cobradas | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md), [CloudFront](../../servicos/redes/cloudfront.md) |
| 2 | Always Free: SQS (1 milhão de requisições), SNS (1 milhão de publicações), CloudWatch (10 métricas e 10 métricas de alarme), Lambda, DynamoDB e outros 30+ | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| 3 | Capacity Reservations cobradas pela tarifa On-Demand mesmo sem uso; Savings Plans e RIs regionais se aplicam | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 4 | RI zonal reserva capacidade; Convertible é trocável; Standard pode ser vendida e Convertible não; RIs antes dos Savings Plans | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 5 | Cost Explorer: 13 meses de histórico, previsão de 3 meses (diária) e 12 meses (mensal), API a US$ 0,01 | [Cost Explorer](../../servicos/custos/cost-explorer.md) |
| 6 | CUR via Data Exports (CUR 2.0, FOCUS 1.2/1.0); Cost Anomaly Detection gratuito | [Outras ferramentas](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) |
| 7 | Lista oficial de tarefas exclusivas do root (ver correção acima) | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md) |
| 8 | MFA: passkeys/FIDO2, app virtual, token TOTP; até 8 dispositivos | [IAM](../../servicos/seguranca/iam.md) |
| 9 | CloudTrail: data events desativados por padrão; uma cópia de management events grátis; validação de integridade; Event history de 90 dias | [CloudTrail](../../servicos/gerenciamento/cloudtrail.md) |
| 10 | Security Hub: FSBP, CIS, PCI DSS, NIST 800-53 Rev. 5, Resource Tagging | [Security Hub](../../servicos/seguranca/security-hub.md) |
| 11 | GuardDuty: AI Protection e Malware Protection para Backup | [GuardDuty](../../servicos/seguranca/guardduty.md) |
| 12 | Política de pentest: serviços liberados, C2 exige aprovação, atividades proibidas, simulação de DDoS | [2.10](../02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) |
| 13 | S3: SSE-S3, Block Public Access e ACLs desativadas por padrão desde 2023 | [S3](../../servicos/armazenamento/s3.md) |
| 14 | Intelligent-Tiering: 30 e 90 dias, camadas opcionais, < 128 KB não monitorado (ver correção acima) | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 15 | Storage Gateway: FSx File Gateway descontinuado para novos clientes | [Storage Gateway](../../servicos/armazenamento/storage-gateway.md) |
| 16 | Gateway endpoints sem custo; Site-to-Site VPN com 2 túneis | [VPN](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) |
| 17 | Políticas do Route 53 | [Route 53](../../servicos/redes/route-53.md) |
| 18 | RDS: Db2; Multi-AZ DB cluster com 1 writer e 2 readers (MySQL, PostgreSQL) | [RDS](../../servicos/banco-de-dados/rds.md) |
| 19 | WorkSpaces Secure Browser (05/2024); Amazon DCV | [WorkSpaces](../../servicos/aplicacoes/workspaces-e-appstream.md) |
| 20 | Shield SRT com Business Support+, Enterprise ou Unified Operations | [Shield](../../servicos/seguranca/shield.md) |
| 21 | Glacier Flexible Expedited: 1–5 min para objetos < 250 MB | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 22 | CloudFront: OAC recomendado (OAI legado); Functions × Lambda@Edge | [CloudFront](../../servicos/redes/cloudfront.md) |
| 23 | EFS: Elastic é o padrão; classes Standard, IA e Archive | [EFS](../../servicos/armazenamento/efs.md) |
| 24 | Aurora Serverless v2 com auto-pause até 0 ACU | [Aurora](../../servicos/banco-de-dados/aurora.md) |
| 25 | RCPs; SCP padrão (após 10/07/2026) nega sair da organização e fechar a conta | [Organizations](../../servicos/gerenciamento/organizations.md) |
| 26 | CodeWhisperer → Amazon Q Developer (30/04/2024); Bedrock não usa dados do cliente nos modelos base | [Amazon Q](../../servicos/ia-ml/amazon-q.md), [Bedrock](../../servicos/ia-ml/bedrock.md) |
| 27 | Elastic Disaster Recovery: RPO subsegundo, RTO em minutos | [DRS](../../servicos/armazenamento/elastic-disaster-recovery.md) |
| 28 | Snowball Edge: 210 TB e 104 vCPUs; fim do suporte comercial em 31/12/2026 | [Snow Family](../../servicos/migracao/snow-family.md) |
| 29 | WorkDocs encerrado em 25/04/2025; Snowmobile em 14/03/2024 | [Fora do escopo](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md), [Snow Family](../../servicos/migracao/snow-family.md) |
| 30 | Enterprise inclui workshops com o TAM e AWS GameDays | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |
