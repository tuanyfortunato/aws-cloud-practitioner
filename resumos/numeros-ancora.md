# 📌 Números-âncora (e o que NÃO precisa decorar)

A CLF-C02 cobra "qual serviço resolve este cenário". Os números abaixo aparecem como **gatilhos de decisão**:
se o enunciado traz o número, ele aponta (ou elimina) um serviço.

## Âncoras de decisão

| Se aparecer... | Pense em... | Ficha |
|---|---|---|
| Execução **> 15 min** | **Não** é Lambda → Fargate/ECS, Batch ou EC2 | [Lambda](../servicos/computacao/lambda.md) |
| Lambda: memória **128 MB – 10.240 MB**; CPU proporcional | Não existe "configurar vCPU" no Lambda | [Lambda](../servicos/computacao/lambda.md) |
| **Aviso de 2 minutos** | Spot Instance | [EC2](../servicos/computacao/ec2.md) |
| Desconto **até 90%** | Spot | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| Desconto **até 72%** | Standard RI / EC2 Instance Savings Plans | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| Desconto **até 66%** + EC2, Fargate e Lambda | Compute Savings Plans | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| Cobrança **por segundo**, mínimo **60 s** | EC2 (maioria das AMIs Linux/Windows) | [EC2](../servicos/computacao/ec2.md) |
| **11 noves** (99,999999999%) | Durabilidade de todas as classes do S3 | [S3](../servicos/armazenamento/s3.md) |
| **1 AZ** / dado recriável | S3 One Zone-IA | [Classes S3](../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| Mínimo **30 dias** | Standard-IA / One Zone-IA | [Classes S3](../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| Mínimo **90 dias** | Glacier Instant / Flexible Retrieval | [Classes S3](../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| Mínimo **180 dias** / recuperação **até 48 h** | Glacier Deep Archive (o mais barato) | [Classes S3](../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| Objeto **5 TB** (🔄 hoje 50 TB) / upload grande | S3 multipart upload | [S3](../servicos/armazenamento/s3.md) |
| **16 instâncias, mesma AZ**, um volume | EBS Multi-Attach (io1/io2) | [EBS](../servicos/armazenamento/ebs.md) |
| Várias instâncias, **várias AZs**, mesmos arquivos | EFS | [EFS](../servicos/armazenamento/efs.md) |
| **400 KB** por item | DynamoDB → blobs vão para o S3 | [DynamoDB](../servicos/banco-de-dados/dynamodb.md) |
| **15 réplicas** | Aurora Replicas (também RDS MySQL/MariaDB/PostgreSQL; Oracle e SQL Server: 5; Db2: 3) | [Aurora](../servicos/banco-de-dados/aurora.md) |
| **6 cópias em 3 AZs** | Armazenamento do Aurora | [Aurora](../servicos/banco-de-dados/aurora.md) |
| Backup automático **até 35 dias** | RDS (point-in-time recovery) | [RDS](../servicos/banco-de-dados/rds.md) |
| **SLA de 100%** | Route 53 | [Route 53](../servicos/redes/route-53.md) |
| **2 IPs anycast estáticos** | Global Accelerator | [Global Accelerator](../servicos/redes/global-accelerator.md) |
| Portas **1/10/100/400 Gbps** | Direct Connect dedicado | [Direct Connect](../servicos/redes/direct-connect.md) |
| SQS: **4 dias** padrão, **14 dias** máx., visibility **30 s** | SQS | [SQS](../servicos/integracao/sqs.md) |
| Mensagem **256 KB** (🔄 SQS hoje 1 MiB; SNS 1 MiB se configurado) | SQS/SNS | [SQS](../servicos/integracao/sqs.md) |
| **90 dias** de eventos grátis | CloudTrail Event history | [CloudTrail](../servicos/gerenciamento/cloudtrail.md) |
| Métricas a cada **5 min** (detalhado: **1 min**) | CloudWatch para EC2 | [CloudWatch](../servicos/gerenciamento/cloudwatch.md) |
| **US$ 3.000/mês**, 1 ano | Shield Advanced | [Shield](../servicos/seguranca/shield.md) |
| Resposta **5 min** / mínimo **US$ 50.000/mês** | Unified Operations (plano novo) | [Planos de suporte](../servicos/custos/planos-de-suporte.md) |
| Resposta **< 15 min** + TAM designado / **US$ 5.000/mês** | Enterprise Support (nos dois modelos) | [Planos de suporte](../servicos/custos/planos-de-suporte.md) |
| Resposta **30 min** / **US$ 29/mês por conta** | Business Support+ (plano novo) — ⚠️ 30 min também era o Enterprise On-Ramp clássico | [Planos de suporte](../servicos/custos/planos-de-suporte.md) |
| Resposta **< 1 h** para produção fora do ar | Business (clássico, até 01/01/2027) | [Planos de suporte](../servicos/custos/planos-de-suporte.md) |
| **< 24 h / < 12 h** úteis, e-mail | Developer (clássico, até 01/01/2027) | [Planos de suporte](../servicos/custos/planos-de-suporte.md) |
| **3 AZs** no mínimo | Cada região AWS | [3.2](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) |

## 🧊 Não precisa decorar

A própria AWS declara fora de escopo codificação, design de arquitetura, troubleshooting, implementação e testes de carga. Não gaste tempo com:

- Preços unitários (US$/GB, US$/requisição, US$/regra do WAF, preço por hora de instância).
- Quotas finas: ENIs, camadas Lambda, número de VIFs (51), regras de LAG, quotas de VPC/subnet, escalonamento de concorrência do Lambda.
- Contagem exata de checks do Trusted Advisor.
- IOPS/throughput por tipo de EBS; tamanhos antigos de Snowball (80 TB).
- Contagem exata de regiões, AZs e PoPs; códigos de região.
- RCU/WCU por tamanho de item; versões de motores.
- Mensagens in-flight do SQS, blocos de 64 KB, throughput exato do FIFO.
