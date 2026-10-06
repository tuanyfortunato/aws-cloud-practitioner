<!-- autoral -->

# O que mudou na AWS em 2025 e 2026

🏠 [Guia do exame](README.md)

---

A AWS muda preços, limites, nomes e serviços o tempo todo, e materiais de estudo envelhecem rápido. Uma apostila de 2024 ainda diz que o maior objeto do S3 tem 5 TB, que o plano de suporte de entrada se chama Developer e que o QuickSight é um produto separado. Nada disso vale mais.

Esta página reúne as mudanças que alteram respostas ou nomes que aparecem na prova. Cada linha aponta para a aula ou a ficha que explica o assunto e lista a fonte oficial da informação.

## Como interpretar uma mudança

Uma mudança na oferta da AWS não muda a prova no mesmo dia. O guia do exame é atualizado em outro ritmo, e um lançamento não prova que as questões já foram revistas. Por isso, numa questão, não escolha a alternativa só porque ela traz o número mais recente: leia o requisito e veja qual alternativa o atende.

Um número também precisa de contexto. O S3 aceita objetos de até 50 TB, mas só com o envio em partes (*multipart upload*); o envio comum, numa única operação, tem outro limite. Antes de usar um número para decidir uma questão, confira a que ele se refere.

## Mudanças que podem alterar uma resposta

| Tema | Antes | Agora | Onde estudar |
|---|---|---|---|
| Planos de suporte | Basic, Developer, Business, Enterprise On-Ramp e Enterprise | Basic Support, Business Support+ (a partir de US$ 29 por mês), Enterprise Support (a partir de US$ 5.000) e Unified Operations (a partir de US$ 50.000), com resposta a casos críticos em 30, 15 e 5 minutos. Os planos antigos terminam em 01/01/2027, e a tarefa 4.3 do guia já cita os novos | [Aula 4.5](../04-cobranca-precos-e-suporte/05-planos-de-suporte.md) |
| Maior objeto do S3 | 5 TB | 50 TB, com envio em partes | [Ficha do S3](../../servicos/armazenamento/s3.md) |
| Mensagem do SQS | 256 KiB | 1 MiB | [Ficha do SQS](../../servicos/integracao/sqs.md) |
| Mensagem do SNS | 256 KiB | 256 KiB por padrão; até 1 MiB configurando o tópico | [Ficha do SNS](../../servicos/integracao/sns.md) |
| Nível gratuito | 12 meses gratuitos, ofertas sempre gratuitas e testes | Contas novas recebem US$ 100 em créditos e podem ganhar mais US$ 100 em atividades; o plano gratuito dura até seis meses ou até acabar o crédito. Mais de 30 serviços continuam com uso gratuito mensal | [Aula 4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| Categorias do Trusted Advisor | Cinco | Seis: otimização de custos, desempenho, segurança, tolerância a falhas, limites de serviço e excelência operacional | [Ficha do Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md) |
| Tarefas exclusivas do root | Incluíam mudar o nome da conta e o plano de suporte | Nome da conta, contatos e Regiões não exigem mais o root | [Aula 2.2](../02-seguranca-e-conformidade/02-usuario-root.md) |
| Savings Plans | Compute, EC2 Instance e SageMaker AI | Também Database Savings Plans, com até 35% de desconto em serviços de banco de dados | [Aula 4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |

## Nomes novos

A lista oficial de serviços ainda usa alguns nomes antigos. Na prova, reconheça os dois.

| Nome na lista do exame | Nome atual | Onde estudar |
|---|---|---|
| AWS Application Migration Service | AWS Transform MGN | [Ficha](../../servicos/migracao/application-migration-service.md) |
| Amazon AppStream 2.0 | Amazon WorkSpaces Applications | [Ficha](../../servicos/aplicacoes/workspaces-e-appstream.md) |
| Amazon Connect | Amazon Connect Customer | [Ficha](../../servicos/aplicacoes/amazon-connect.md) |
| Amazon Quick Sight | Parte do Amazon Quick | [Ficha](../../servicos/analytics/quicksight.md) |
| AWS Chatbot (lista fora do escopo) | Amazon Q Developer in chat applications | [Ficha](../../servicos/fora-do-escopo/gerenciamento-e-custos.md) |

## Serviços que mudaram de situação

Alguns serviços da lista do exame deixaram de aceitar clientes novos, mas continuam na lista e podem cair na prova. O AWS Migration Hub e o AWS Application Discovery Service não aceitam clientes novos desde 07/11/2025. O WorkSpaces Secure Browser deixa de aceitar em 29/10/2026. O WorkSpaces Pools, uma modalidade do WorkSpaces, não aceita clientes novos desde 31/07/2026, e o suporte termina em 31/12/2027.

Outros serviços que aparecem em materiais de estudo também mudaram. O AWS Audit Manager está em modo de manutenção desde 30/04/2026. O Timestream for LiveAnalytics não aceita clientes novos desde 20/06/2025. A família Snow não oferece mais dispositivos a clientes novos. Nenhum desses três está na lista do exame.

## Serviços encerrados

A AWS publica duas tabelas oficiais: uma com os serviços que vão encerrar (*sunset*) e outra com os que já foram desligados (*full shutdown*). Dos serviços que ainda aparecem em materiais de estudo, já foram desligados:

- o AWS CodeStar (25/07/2024);
- o AWS OpsWorks (01/05/2024);
- o AWS Snowmobile (14/03/2024);
- o Amazon WorkDocs (25/04/2025);
- o Amazon QLDB (31/07/2025);
- o AWS RoboMaker (10/09/2025);
- o Amazon Elastic Transcoder (13/11/2025);
- o AWS Elemental MediaStore (12/11/2025);
- o Amazon Lookout for Metrics (10/10/2025);
- o AWS IQ, o AWS Panorama, o AWS IoT Events e o Amazon Inspector Classic, em maio de 2026.

Vários deles estão na lista de fora do escopo da prova. Se uma alternativa citar um deles, desconfie, mas leia o requisito antes de descartá-la.

Antes da prova, reabra as duas tabelas, porque elas crescem a cada trimestre.

## Fontes oficiais

Verificadas em 06/10/2026.

- [Content Domain 4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html): planos de suporte citados na tarefa 4.3.
- [Upload de objetos no S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html): objetos de até 50 TB com envio em partes.
- [Cotas de mensagens do SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html): mensagem de até 1 MiB.
- [AWS Free Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html): créditos, plano gratuito de seis meses e serviços sempre gratuitos.
- [Referência de verificações do Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html): as seis categorias.
- [WorkSpaces Pools end of support](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html): fim da entrada de clientes novos e do suporte.
- [AWS services sunset](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html) e [Services in full shutdown](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html): serviços que vão encerrar e já encerrados, com as datas.
- As demais mudanças têm a fonte oficial na aula ou na ficha indicada em cada linha.

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Anote aqui mudanças que você encontrar e ainda não estejam nesta página. -->
<!-- notas:fim -->
