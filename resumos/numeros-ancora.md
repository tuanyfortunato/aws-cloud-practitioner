<!-- autoral -->

# Números que decidem questões

A prova de Cloud Practitioner pergunta qual serviço ou qual opção resolve um cenário, e não pede contas. Mesmo assim, alguns números funcionam como pistas: uma tarefa que dura 40 minutos elimina o Lambda, e um aviso de dois minutos antes da interrupção só existe nas instâncias Spot. Esta página reúne esses números e diz para onde cada um aponta.

Um número só vale com o contexto dele. O S3 aceita objetos de até 50 TB, mas só com o envio em partes; o limite de 15 minutos é o de uma execução comum do Lambda. Antes de usar um número numa questão, confira a que ele se refere na ficha indicada.

## Computação

| Número | O que significa | Onde estudar |
|---|---|---|
| 15 minutos | Duração máxima de uma execução comum do Lambda; tarefas mais longas vão para Fargate, Batch ou EC2 | [Ficha do Lambda](../servicos/computacao/lambda.md) |
| 128 MB a 10.240 MB | Memória de uma função Lambda; a capacidade de processamento acompanha a memória escolhida | [Ficha do Lambda](../servicos/computacao/lambda.md) |
| 2 minutos | Aviso que a instância Spot recebe antes de ser interrompida | [Ficha do EC2](../servicos/computacao/ec2.md) |
| Por segundo, mínimo de 60 segundos | Cobrança sob demanda do EC2 para sistemas como Amazon Linux, Windows e Ubuntu | [Ficha do EC2](../servicos/computacao/ec2.md) |

## Modelos de compra

| Número | O que significa | Onde estudar |
|---|---|---|
| Até 90% | Desconto das instâncias Spot, que podem ser interrompidas | [Aula 4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| Até 72% | Desconto das Reserved Instances e dos EC2 Instance Savings Plans, presos a uma configuração ou a uma família de instâncias | [Aula 4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| Até 66% | Desconto dos Compute Savings Plans, que valem para EC2, Fargate e Lambda | [Aula 4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| Até 35% | Desconto dos Database Savings Plans, em serviços como Aurora, RDS e DynamoDB | [Aula 4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 1 ou 3 anos | Prazo do compromisso das Reserved Instances e dos Savings Plans de EC2 e de computação | [Aula 4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |

## Armazenamento

| Número | O que significa | Onde estudar |
|---|---|---|
| 11 noves (99,999999999%) | Durabilidade projetada do S3 | [Ficha do S3](../servicos/armazenamento/s3.md) |
| 50 TB | Maior objeto do S3, com envio em partes (*multipart upload*) | [Ficha do S3](../servicos/armazenamento/s3.md) |
| 1 zona | Onde o S3 One Zone-IA guarda os dados; serve para dados que podem ser recriados | [Classes do S3](../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 30, 90 e 180 dias | Prazo mínimo cobrado: 30 dias no Standard-IA e no One Zone-IA, 90 no Glacier Instant e no Flexible Retrieval, 180 no Deep Archive | [Classes do S3](../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 12 ou 48 horas | Restauração no Glacier Deep Archive: até 12 horas na opção padrão, até 48 horas na opção em massa | [Classes do S3](../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 16 instâncias | Máximo de instâncias, na mesma zona, ligadas a um volume EBS com Multi-Attach (só volumes io1 e io2) | [Ficha do EBS](../servicos/armazenamento/ebs.md) |

## Bancos de dados

| Número | O que significa | Onde estudar |
|---|---|---|
| 400 KB | Maior item do DynamoDB; arquivos grandes vão para o S3, e o item guarda a referência | [Ficha do DynamoDB](../servicos/banco-de-dados/dynamodb.md) |
| 15 réplicas | Máximo de réplicas do Aurora num cluster | [Ficha do Aurora](../servicos/banco-de-dados/aurora.md) |
| 3 zonas | Onde o armazenamento do Aurora guarda cópias dos dados | [Ficha do Aurora](../servicos/banco-de-dados/aurora.md) |
| Até 35 dias | Retenção dos backups automáticos do RDS, que permitem restaurar o banco num momento escolhido | [Ficha do RDS](../servicos/banco-de-dados/rds.md) |

## Rede e infraestrutura global

| Número | O que significa | Onde estudar |
|---|---|---|
| 3 ou mais zonas | Quantidade de zonas de disponibilidade em cada Região atual | [Aula 3.2](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| 2 IPs estáticos | O que o Global Accelerator entrega à aplicação (quatro, com IPv6) | [Ficha do Global Accelerator](../servicos/redes/global-accelerator.md) |
| 1, 10, 100 ou 400 Gbps | Velocidades de uma conexão dedicada do Direct Connect | [Ficha do Direct Connect](../servicos/redes/direct-connect.md) |

## Integração e monitoramento

| Número | O que significa | Onde estudar |
|---|---|---|
| 1 MiB | Maior mensagem do SQS; no SNS, 256 KiB por padrão e até 1 MiB configurando o tópico | [Ficha do SQS](../servicos/integracao/sqs.md) e [ficha do SNS](../servicos/integracao/sns.md) |
| 4 e 14 dias | Retenção de uma mensagem no SQS: 4 dias por padrão, até 14 dias | [Ficha do SQS](../servicos/integracao/sqs.md) |
| 30 segundos | Prazo de invisibilidade padrão de uma mensagem recebida no SQS (*visibility timeout*) | [Ficha do SQS](../servicos/integracao/sqs.md) |
| 90 dias | Eventos de gerenciamento que o histórico do CloudTrail guarda sem configuração | [Ficha do CloudTrail](../servicos/gerenciamento/cloudtrail.md) |
| 5 e 1 minuto | Intervalo das métricas do EC2 no CloudWatch: 5 minutos no monitoramento básico, 1 minuto no detalhado, que é cobrado | [Ficha do CloudWatch](../servicos/gerenciamento/cloudwatch.md) |

## Segurança e suporte

| Número | O que significa | Onde estudar |
|---|---|---|
| US$ 3.000 por mês | Preço do Shield Advanced por organização, com compromisso de um ano | [Ficha do Shield](../servicos/seguranca/shield.md) |
| 30, 15 e 5 minutos | Resposta a casos críticos no Business Support+, no Enterprise Support e no Unified Operations | [Aula 4.5](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) |
| US$ 29, US$ 5.000 e US$ 50.000 | Preço mínimo mensal do Business Support+ (por conta), do Enterprise Support e do Unified Operations | [Aula 4.5](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) |

## O que não precisa decorar

O guia do exame diz que o candidato não precisa programar, desenhar arquiteturas, resolver problemas técnicos, implementar nem fazer testes de carga. Por isso, não gaste tempo com:

- preços unitários, como o valor por GB, por requisição ou por hora de cada instância;
- cotas detalhadas, como o número de interfaces de rede, de sub-redes ou de execuções simultâneas do Lambda;
- o número exato de verificações do Trusted Advisor;
- o desempenho de cada tipo de volume EBS;
- a contagem atual de Regiões, zonas e locais de borda, e os códigos das Regiões.

## Fontes oficiais

Cada número foi conferido em 06/10/2026 na página oficial citada pela ficha ou pela aula indicada na linha. As páginas a seguir foram conferidas diretamente:

- [EBS Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html): volumes io1 e io2 ligados a até 16 instâncias Nitro na mesma zona.
- [Guia do exame CLF-C02](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html): tarefas fora do escopo do candidato.
- [Tipos de Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html) e [o que são Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html): os quatro tipos, o desconto de até 35% do Database Savings Plans e os prazos de 1 ou 3 anos.

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Anote aqui os números que você confundiu. -->
<!-- notas:fim -->
