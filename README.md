# Apostila AWS Cloud Practitioner — do primeiro conceito à revisão

Esta apostila gratuita, em português, foi feita para quem está começando em tecnologia e quer estudar para a **AWS Certified Cloud Practitioner (CLF-C02)**. AWS é a Amazon Web Services, uma plataforma que oferece recursos de computação pela internet: computadores, armazenamento, bancos de dados e outros serviços.

Você vai aprender **qual problema cada recurso resolve, como ele funciona e quais são seus limites**, antes de memorizar nomes para a prova. Para acompanhar a leitura, não é necessário abrir o console da AWS, programar ou criar uma conta.

## Comece aqui

**Sua primeira aula é [1.1 — O que é computação em nuvem](docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md).** Ela explica o ponto de partida: por que uma empresa usaria recursos pela internet em vez de comprar e manter todos os equipamentos.

Se você chegou agora, faça esta sequência:

1. Leia [como estudar sem usar o console](docs/00-guia-do-exame/estudar-sem-console.md).
2. Abra a [primeira aula](docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) e siga as aulas do capítulo 1 na ordem do sumário abaixo.
3. Ao terminar uma aula, explique o exemplo com suas palavras e responda às perguntas de revisão.
4. Marque a aula no [controle de progresso](progresso.md). Na próxima sessão, volte a este sumário e abra a seguinte.

**Hoje, basta concluir a primeira aula.** Não é preciso estudar todo o catálogo de serviços antes de começar.

## Como usar a apostila

Pense neste README como o sumário de um livro. As **aulas** constroem a base em sequência. As **fichas** aprofundam um serviço quando ele aparece na aula. **Flashcards** são cartões de pergunta e resposta para relembrar o que você já estudou. As **questões e o simulado** ajudam a aplicar esse conhecimento.

Por exemplo: ao chegar à [aula de EC2](docs/03-tecnologia-e-servicos/03-ec2.md), entenda primeiro o que é um computador virtual. Depois abra a [ficha de EC2](servicos/computacao/ec2.md) para estudar as escolhas de máquina, disco, acesso, segurança e custo. As fichas indicadas em cada aula ajudam a aprofundar esse assunto.

Em cada sessão, leia uma aula, acompanhe o caso resolvido e tente responder à revisão antes de consultar a resposta. Se conseguir explicar **o problema, a solução e uma limitação**, avance. Se ainda confundir dois conceitos, retome a explicação e registre a dúvida em suas anotações. O [plano de estudos](docs/00-guia-do-exame/plano-de-estudos.md) distribui a leitura em semanas; adapte o ritmo à sua disponibilidade.

**Navegação rápida:** [Sumário](#sumário-da-apostila) · [Capítulo 1](#capítulo-1-conceitos-de-nuvem) · [Capítulo 2](#capítulo-2-segurança-e-conformidade) · [Capítulo 3](#capítulo-3-tecnologia-e-serviços) · [Capítulo 4](#capítulo-4-cobrança-preços-e-suporte) · [Fichas](#caderno-de-serviços) · [Revisão](#pratique-e-revise) · [Materiais](#materiais-e-acompanhamento)

## Antes dos capítulos: conheça a prova

A certificação avalia o entendimento geral da nuvem AWS. Você precisa reconhecer necessidades, comparar soluções e distinguir as responsabilidades da AWS e do cliente. Uma **responsabilidade** é aquilo de que cada parte precisa cuidar; por exemplo, conceder acesso às pessoas certas continua exigindo decisões do cliente.

Leia o [guia do exame](docs/00-guia-do-exame/README.md) para conhecer formato, duração e avaliação. Consulte o [escopo oficial](docs/00-guia-do-exame/escopo-oficial.md) para saber quais serviços fazem parte da prova. “Domínio” é o nome dado a cada grande área de conhecimento do exame; nesta apostila, cada domínio corresponde a um capítulo.

Os percentuais no sumário indicam o peso dos domínios na prova, não a ordem de leitura nem o tempo que você precisa dedicar a cada um. A sequência começa pelos fundamentos porque eles ajudam a compreender os outros capítulos.

<!-- indice:inicio -->
## Sumário da apostila

Leia do capítulo 0 ao 4. Os números das aulas indicam sua posição: **3.3**, por exemplo, é a terceira aula do capítulo 3. Clique no título para abrir o texto.

### Capítulo 0: Fundamentos de TI

**A pergunta deste capítulo:** O que são servidor, rede, dados, API e criptografia, as peças sobre as quais a AWS oferece serviços?

Para quem nunca trabalhou com TI. Se você já conhece esses termos, leia só os resumos no fim de cada aula e siga para o capítulo 1.

Não corresponde a um domínio da prova. [Apresentação do capítulo](docs/fundamentos/README.md).

| Aula | Assunto |
|---|---|
| 0.1 | [Computador, servidor e virtualização](docs/fundamentos/01-servidor-e-virtualizacao.md) |
| 0.2 | [Rede: endereço IP, porta, DNS e HTTPS](docs/fundamentos/02-rede.md) |
| 0.3 | [Dados: arquivo, bloco, objeto e banco de dados](docs/fundamentos/03-dados.md) |
| 0.4 | [Como programas conversam: API, requisição e fila](docs/fundamentos/04-api-e-filas.md) |
| 0.5 | [Segurança básica: identidade, autenticação, autorização e criptografia](docs/fundamentos/05-seguranca-basica.md) |

**Comece pela [aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md).**

**Confira seu entendimento:** [flashcards do capítulo 0](flashcards/capitulo-0.md).

**Próxima etapa:** [capítulo 1](#capítulo-1-conceitos-de-nuvem).

### Capítulo 1: Conceitos de nuvem

**A pergunta deste capítulo:** Por que usar recursos pela internet e como pensar em crescimento, falhas e migração?

Comece pela ideia de nuvem. Depois estude as vantagens, a arquitetura, as boas práticas e a economia.

Corresponde ao domínio 1 — conceitos de nuvem — **24% da prova**. [Apresentação do capítulo](docs/01-conceitos-de-nuvem/README.md).

| Aula | Assunto |
|---|---|
| 1.1 | [O que é computação em nuvem](docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) |
| 1.2 | [As 6 vantagens da computação em nuvem](docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) |
| 1.3 | [Conceitos de arquitetura que a prova cobra](docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| 1.4 | [AWS Well-Architected Framework](docs/01-conceitos-de-nuvem/04-well-architected-framework.md) |
| 1.5 | [AWS Cloud Adoption Framework (CAF)](docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md) |
| 1.6 | [Estratégias de migração (os 7 Rs)](docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md) |
| 1.7 | [Economia da nuvem](docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md) |

**Comece pela [aula 1.1](docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md).**

**Antes de avançar:** Explique a diferença entre comprar infraestrutura e contratar recursos, e reconheça as vantagens e os limites de cada escolha.

**Confira seu entendimento:** [questões do capítulo 1](simulados/questoes/dominio-1.md) · [flashcards do capítulo 1](flashcards/dominio-1.md).

**Próxima etapa:** [capítulo 2](#capítulo-2-segurança-e-conformidade).

### Capítulo 2: Segurança e conformidade

**A pergunta deste capítulo:** Quem pode acessar os recursos e quem precisa cuidar da segurança?

Com a base do capítulo 1, separe as responsabilidades. Em seguida, estude identidades, permissões, proteção de dados e acompanhamento do ambiente.

Corresponde ao domínio 2 — segurança e conformidade — **30% da prova**. [Apresentação do capítulo](docs/02-seguranca-e-conformidade/README.md).

| Aula | Assunto |
|---|---|
| 2.1 | [Modelo de responsabilidade compartilhada](docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) |
| 2.2 | [Usuário root](docs/02-seguranca-e-conformidade/02-usuario-root.md) |
| 2.3 | [AWS IAM (Identity and Access Management)](docs/02-seguranca-e-conformidade/03-iam.md) |
| 2.4 | [Governança multi-conta](docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md) |
| 2.5 | [Criptografia](docs/02-seguranca-e-conformidade/05-criptografia.md) |
| 2.6 | [Compliance e governança](docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md) |
| 2.7 | [Logs, monitoramento e auditoria](docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| 2.8 | [Proteção de rede e aplicações](docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) |
| 2.9 | [Detecção de ameaças e postura de segurança](docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| 2.10 | [Outros pontos de segurança](docs/02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) |

**Comece pela [aula 2.1](docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md).**

**Antes de avançar:** Diferencie as responsabilidades da AWS e do cliente, explique permissões e escolha ferramentas de proteção e auditoria.

**Confira seu entendimento:** [questões do capítulo 2](simulados/questoes/dominio-2.md) · [flashcards do capítulo 2](flashcards/dominio-2.md).

**Próxima etapa:** [capítulo 3](#capítulo-3-tecnologia-e-serviços).

### Capítulo 3: Tecnologia e serviços

**A pergunta deste capítulo:** Como montar uma solução usando computação, dados, armazenamento e redes?

Use a base de nuvem e segurança para entender as peças de uma aplicação. Leia as aulas em ordem e abra as fichas indicadas dentro de cada uma.

Corresponde ao domínio 3 — tecnologia e serviços de nuvem — **34% da prova**. [Apresentação do capítulo](docs/03-tecnologia-e-servicos/README.md).

| Aula | Assunto |
|---|---|
| 3.1 | [Formas de acessar e implantar na AWS](docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) |
| 3.2 | [Infraestrutura global](docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| 3.3 | [Amazon EC2](docs/03-tecnologia-e-servicos/03-ec2.md) |
| 3.4 | [Escalabilidade e balanceamento de carga](docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) |
| 3.5 | [Containers e serverless](docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) |
| 3.6 | [Outros serviços de computação](docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) |
| 3.7 | [Bancos de dados](docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) |
| 3.8 | [Amazon S3 — armazenamento de objetos](docs/03-tecnologia-e-servicos/08-s3.md) |
| 3.9 | [Outros serviços de armazenamento](docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| 3.10 | [Rede e entrega de conteúdo](docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| 3.11 | [Analytics](docs/03-tecnologia-e-servicos/11-analytics.md) |
| 3.12 | [IA e machine learning](docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md) |
| 3.13 | [Integração de aplicações](docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) |
| 3.14 | [Aplicações de negócio, usuário final, front-end e IoT](docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md) |
| 3.15 | [Ferramentas de desenvolvimento](docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md) |
| 3.16 | [Gestão e governança](docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md) |
| 3.17 | [Migração e transferência](docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) |
| 3.18 | [Serviços menos conhecidos que podem aparecer](docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md) |

**Comece pela [aula 3.1](docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md).**

**Antes de avançar:** Relacione uma necessidade ao serviço apropriado e explique o que ele entrega, suas limitações e as decisões que ficam com o cliente.

**Confira seu entendimento:** [questões do capítulo 3](simulados/questoes/dominio-3.md) · [flashcards do capítulo 3](flashcards/dominio-3.md).

**Próxima etapa:** [capítulo 4](#capítulo-4-cobrança-preços-e-suporte).

### Capítulo 4: Cobrança, preços e suporte

**A pergunta deste capítulo:** Como entender a conta, controlar gastos e obter ajuda?

Agora que você conhece os recursos, estude como o uso vira cobrança, quando compromissos de compra fazem sentido e quais ferramentas ajudam a acompanhar custos.

Corresponde ao domínio 4 — cobrança, preços e suporte — **12% da prova**. [Apresentação do capítulo](docs/04-cobranca-precos-e-suporte/README.md).

| Aula | Assunto |
|---|---|
| 4.1 | [Princípios de preço da AWS](docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md) |
| 4.2 | [Modelos de compra do EC2](docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 4.3 | [Como outros recursos são cobrados](docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| 4.4 | [Ferramentas de custo e faturamento](docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| 4.5 | [Planos de AWS Support](docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) |
| 4.6 | [Outros recursos de ajuda](docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md) |

**Comece pela [aula 4.1](docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md).**

**Antes de avançar:** Diferencie os modelos de compra e as ferramentas de estimativa, acompanhamento e orçamento, além das opções de suporte.

**Confira seu entendimento:** [questões do capítulo 4](simulados/questoes/dominio-4.md) · [flashcards do capítulo 4](flashcards/dominio-4.md).

**Próxima etapa:** [pratique e revise](#pratique-e-revise).

## Caderno de serviços

As fichas são leituras de aprofundamento. Quando uma aula citar um serviço, abra a ficha indicada nela; depois retorne à aula. Se você já conhece o nome do serviço e quer consultá-lo, abra uma categoria abaixo.

Cada ficha explica o problema resolvido, o funcionamento, as opções, os limites, a segurança, o custo e um caso resolvido. O status da prova aparece na própria ficha: consulte-o antes de dedicar tempo a um serviço.

Exemplos: [EC2 — computadores virtuais](servicos/computacao/ec2.md) · [S3 — armazenamento de objetos](servicos/armazenamento/s3.md) · [IAM — identidades e permissões](servicos/seguranca/iam.md).

Você também pode abrir o [índice completo das fichas, com descrições e escopo](servicos/README.md).

<details>
<summary>🖥️ Computação — 12 fichas (clique para abrir)</summary>

- [Amazon EC2](servicos/computacao/ec2.md)
- [Amazon EC2 Auto Scaling](servicos/computacao/ec2-auto-scaling.md)
- [Elastic Load Balancing](servicos/computacao/elastic-load-balancing.md)
- [AWS Lambda](servicos/computacao/lambda.md)
- [Amazon ECS](servicos/computacao/ecs.md)
- [Amazon EKS](servicos/computacao/eks.md)
- [AWS Fargate](servicos/computacao/fargate.md)
- [Amazon ECR](servicos/computacao/ecr.md)
- [AWS Elastic Beanstalk](servicos/computacao/elastic-beanstalk.md)
- [Amazon Lightsail](servicos/computacao/lightsail.md)
- [AWS Batch](servicos/computacao/batch.md)
- [AWS Outposts, Local Zones e Wavelength](servicos/computacao/outposts-local-zones-wavelength.md)

</details>

<details>
<summary>🗄️ Armazenamento — 8 fichas (clique para abrir)</summary>

- [Amazon S3](servicos/armazenamento/s3.md)
- [Classes de armazenamento do S3](servicos/armazenamento/s3-classes-de-armazenamento.md)
- [Amazon EBS](servicos/armazenamento/ebs.md)
- [Amazon EFS](servicos/armazenamento/efs.md)
- [Amazon FSx](servicos/armazenamento/fsx.md)
- [AWS Storage Gateway](servicos/armazenamento/storage-gateway.md)
- [AWS Backup](servicos/armazenamento/aws-backup.md)
- [AWS Elastic Disaster Recovery](servicos/armazenamento/elastic-disaster-recovery.md)

</details>

<details>
<summary>🛢️ Banco de dados — 9 fichas (clique para abrir)</summary>

- [Amazon RDS](servicos/banco-de-dados/rds.md)
- [Amazon Aurora](servicos/banco-de-dados/aurora.md)
- [Amazon DynamoDB](servicos/banco-de-dados/dynamodb.md)
- [Amazon ElastiCache](servicos/banco-de-dados/elasticache.md)
- [Amazon MemoryDB](servicos/banco-de-dados/memorydb.md)
- [Amazon Redshift](servicos/banco-de-dados/redshift.md)
- [Amazon DocumentDB](servicos/banco-de-dados/documentdb.md)
- [Amazon Neptune](servicos/banco-de-dados/neptune.md)
- [Amazon Keyspaces, Timestream e outros bancos especializados](servicos/banco-de-dados/keyspaces-timestream-e-outros.md)

</details>

<details>
<summary>🌐 Redes e entrega de conteúdo — 8 fichas (clique para abrir)</summary>

- [Amazon VPC](servicos/redes/vpc.md)
- [VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink](servicos/redes/vpc-peering-transit-gateway-e-endpoints.md)
- [AWS VPN](servicos/redes/site-to-site-vpn-e-client-vpn.md)
- [AWS Direct Connect](servicos/redes/direct-connect.md)
- [Amazon Route 53](servicos/redes/route-53.md)
- [Amazon CloudFront](servicos/redes/cloudfront.md)
- [AWS Global Accelerator](servicos/redes/global-accelerator.md)
- [Amazon API Gateway](servicos/redes/api-gateway.md)

</details>

<details>
<summary>🔐 Segurança, identidade e compliance — 18 fichas (clique para abrir)</summary>

- [AWS IAM](servicos/seguranca/iam.md)
- [AWS IAM Identity Center](servicos/seguranca/iam-identity-center.md)
- [Amazon Cognito](servicos/seguranca/cognito.md)
- [AWS Directory Service](servicos/seguranca/directory-service.md)
- [AWS KMS](servicos/seguranca/kms.md)
- [AWS CloudHSM](servicos/seguranca/cloudhsm.md)
- [AWS Certificate Manager](servicos/seguranca/certificate-manager.md)
- [AWS Secrets Manager e Systems Manager Parameter Store](servicos/seguranca/secrets-manager-e-parameter-store.md)
- [AWS Shield](servicos/seguranca/shield.md)
- [AWS WAF](servicos/seguranca/waf.md)
- [AWS Firewall Manager e AWS Network Firewall](servicos/seguranca/firewall-manager-e-network-firewall.md)
- [Amazon GuardDuty](servicos/seguranca/guardduty.md)
- [Amazon Inspector](servicos/seguranca/inspector.md)
- [Amazon Macie](servicos/seguranca/macie.md)
- [Amazon Detective](servicos/seguranca/detective.md)
- [AWS Security Hub](servicos/seguranca/security-hub.md)
- [AWS Artifact](servicos/seguranca/artifact.md)
- [AWS Audit Manager](servicos/seguranca/audit-manager.md)

</details>

<details>
<summary>⚙️ Gerenciamento e governança — 11 fichas (clique para abrir)</summary>

- [Amazon CloudWatch](servicos/gerenciamento/cloudwatch.md)
- [AWS CloudTrail](servicos/gerenciamento/cloudtrail.md)
- [AWS Config](servicos/gerenciamento/config.md)
- [AWS Systems Manager](servicos/gerenciamento/systems-manager.md)
- [AWS CloudFormation](servicos/gerenciamento/cloudformation.md)
- [AWS Organizations](servicos/gerenciamento/organizations.md)
- [AWS Control Tower](servicos/gerenciamento/control-tower.md)
- [AWS Service Catalog e AWS Resource Access Manager](servicos/gerenciamento/service-catalog-e-ram.md)
- [AWS Trusted Advisor](servicos/gerenciamento/trusted-advisor.md)
- [AWS Health Dashboard](servicos/gerenciamento/health-dashboard.md)
- [AWS Compute Optimizer, Service Quotas, License Manager e outros](servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md)

</details>

<details>
<summary>📊 Analytics — 7 fichas (clique para abrir)</summary>

- [Amazon Athena](servicos/analytics/athena.md)
- [AWS Glue](servicos/analytics/glue.md)
- [Amazon Kinesis e Amazon Data Firehose](servicos/analytics/kinesis.md)
- [Amazon EMR](servicos/analytics/emr.md)
- [Amazon QuickSight](servicos/analytics/quicksight.md)
- [Amazon OpenSearch Service](servicos/analytics/opensearch.md)
- [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](servicos/analytics/lake-formation-msk-e-outros.md)

</details>

<details>
<summary>🤖 IA e machine learning — 4 fichas (clique para abrir)</summary>

- [Amazon SageMaker AI](servicos/ia-ml/sagemaker-ai.md)
- [Amazon Bedrock](servicos/ia-ml/bedrock.md)
- [Amazon Q](servicos/ia-ml/amazon-q.md)
- [Serviços de IA prontos](servicos/ia-ml/servicos-de-ia-prontos.md)

</details>

<details>
<summary>🔗 Integração de aplicações — 5 fichas (clique para abrir)</summary>

- [Amazon SQS](servicos/integracao/sqs.md)
- [Amazon SNS](servicos/integracao/sns.md)
- [Amazon EventBridge](servicos/integracao/eventbridge.md)
- [AWS Step Functions](servicos/integracao/step-functions.md)
- [Amazon MQ](servicos/integracao/amazon-mq.md)

</details>

<details>
<summary>🛠️ Ferramentas de desenvolvedor — 3 fichas (clique para abrir)</summary>

- [Formas de acesso: Console, CLI, SDKs, CloudShell](servicos/desenvolvimento/cli-sdk-e-cloudshell.md)
- [Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact](servicos/desenvolvimento/code-services.md)
- [AWS X-Ray](servicos/desenvolvimento/x-ray.md)

</details>

<details>
<summary>💼 Aplicações de negócio, usuário final e IoT — 5 fichas (clique para abrir)</summary>

- [Amazon Connect](servicos/aplicacoes/amazon-connect.md)
- [Amazon SES](servicos/aplicacoes/ses.md)
- [Amazon WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser](servicos/aplicacoes/workspaces-e-appstream.md)
- [AWS Amplify, AWS AppSync e AWS Device Farm](servicos/aplicacoes/amplify-e-appsync.md)
- [AWS IoT Core, IoT Greengrass e outros serviços de IoT](servicos/aplicacoes/iot-core-e-greengrass.md)

</details>

<details>
<summary>🚚 Migração e transferência — 5 fichas (clique para abrir)</summary>

- [Migration Evaluator, Application Discovery Service e Migration Hub](servicos/migracao/discovery-migration-hub-e-evaluator.md)
- [AWS Application Migration Service](servicos/migracao/application-migration-service.md)
- [AWS Database Migration Service](servicos/migracao/dms-e-sct.md)
- [Família AWS Snow](servicos/migracao/snow-family.md)
- [AWS DataSync e AWS Transfer Family](servicos/migracao/datasync-e-transfer-family.md)

</details>

<details>
<summary>💰 Custos e suporte — 5 fichas (clique para abrir)</summary>

- [AWS Cost Explorer](servicos/custos/cost-explorer.md)
- [AWS Budgets](servicos/custos/budgets.md)
- [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md)
- [Planos de AWS Support](servicos/custos/planos-de-suporte.md)
- [Recursos de ajuda, parceiros e serviços ao cliente](servicos/custos/recursos-de-ajuda-e-parceiros.md)

</details>

<details>
<summary>❌ Fora do escopo da prova (só para referência) — 5 fichas (clique para abrir)</summary>

Leitura complementar; estas fichas reúnem serviços fora do escopo da prova.

- [Serviços de mídia e jogos](servicos/fora-do-escopo/midia-e-jogos.md)
- [IoT, robótica, satélite e visão computacional na borda](servicos/fora-do-escopo/iot-robotica-e-satelite.md)
- [Desenvolvimento e aplicações](servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md)
- [Rede e diretório](servicos/fora-do-escopo/rede-e-diretorio.md)
- [Gerenciamento e custos](servicos/fora-do-escopo/gerenciamento-e-custos.md)

</details>

<!-- indice:fim -->

## Pratique e revise

Ao terminar cada capítulo, faça as questões dele e explique por que escolheu uma alternativa. Se errar, volte à aula correspondente, registre o motivo no [caderno de erros](simulados/erros-recorrentes.md) e tente novamente depois de revisar.

| Etapa | Abra este material | O que fazer |
|---|---|---|
| Durante a leitura | [Flashcards por domínio](flashcards/README.md) | Revise os cartões das aulas já estudadas; use o [arquivo para Anki](flashcards/anki-clf-c02.tsv) se preferir esse aplicativo. |
| Depois de um capítulo | [Questões por domínio](simulados/questoes/README.md) | Responda sem consulta e confira as explicações. |
| Depois dos quatro capítulos | [Simulado 01](simulados/simulado-01.md) | Reserve o tempo indicado no simulado, responda sem consulta e depois examine cada erro. |
| Na revisão | [Serviços que se parecem](resumos/comparativos.md) | Explique qual necessidade distingue cada par. |
| Na revisão | [Palavras-chave dos enunciados](resumos/palavras-chave.md) | Relacione as pistas ao problema completo; uma palavra isolada não substitui a leitura da questão. |
| Na revisão | [Números-âncora](resumos/numeros-ancora.md) | Retome os números destacados depois de entender o conceito. |

O simulado e as questões por domínio usam o mesmo banco. Refazer questões ajuda a revisar, mas reconhecer uma resposta já vista não demonstra, sozinho, domínio do assunto. Tente justificar a escolha antes de abrir o gabarito.

## Materiais e acompanhamento

Use esta tabela para encontrar um recurso específico. Para a primeira leitura, siga os capítulos do sumário.

<!-- conteudo:inicio -->
| Material | O que é | Quando usar |
|---|---|---|
| 📖 [Tópicos da prova](#sumário-da-apostila) | **41 tópicos** que cobrem os 4 domínios, com conceitos explicados, casos resolvidos e perguntas de revisão | Estudo principal, na ordem do roteiro |
| 🔎 [Fichas de serviços](#caderno-de-serviços) | **105 fichas** (uma por serviço ou família), com funcionamento, opções, limites, segurança, custo e casos resolvidos; 5 reúnem serviços **fora da prova** | Quando um tópico citar o serviço, ou para tirar dúvidas |
| 🃏 [Flashcards](flashcards/README.md) | **255 perguntas e respostas** por capítulo, também em arquivo para o Anki | Todos os dias, para memorizar |
| 📝 [Simulado 01](simulados/simulado-01.md) | **65 questões** no formato da prova, com gabarito comentado | Depois de estudar os 4 domínios (90 min, sem consulta) |
| ❓ [Questões por domínio](simulados/questoes/README.md) | As mesmas questões, agrupadas por tópico | Ao terminar cada domínio |
| ⚖️ [Pares que confundem](resumos/comparativos.md) | **55 pares** de serviços parecidos e a diferença em uma linha | Revisão final |
| 🔑 [Palavras-chave → serviço](resumos/palavras-chave.md) | **28 gatilhos** do enunciado que apontam a resposta | Revisão final |
| 📌 [Números-âncora](resumos/numeros-ancora.md) | Os números que decidem a resposta (e o que **não** precisa decorar) | Revisão final |
| 📖 [Glossário](glossario.md) | **129 termos** e siglas | Sempre que travar num termo |
| ✅ [Progresso](progresso.md) | Checklist de todos os tópicos e marcos | Para acompanhar o seu avanço |
| 🧪 [Labs](labs/README.md) | Exercícios práticos no console AWS, com cuidado de custos | Opcional, para fixar |
<!-- conteudo:fim -->

Para entender a organização dos textos, leia [como esta apostila ensina](docs/00-guia-do-exame/estrutura-da-apostila.md). As [práticas no console](labs/README.md) são opcionais e devem ser feitas depois de ler as instruções de custos e limpeza de recursos.

## Fontes e atualizações

O conteúdo vem de um guia de estudo e de uma pesquisa próprios, conferidos depois em várias rodadas nas páginas
oficiais da AWS. Quando a verificação encontrou algo diferente, o repositório foi corrigido e a mudança aparece
marcada com 🔄 ou ✔️.

| Documento | O que é |
|---|---|
| [Índice das fontes](fontes/README.md) | Como cada fonte foi usada |
| [Guia completo CLF-C02](fontes/guia-completo-clf-c02.md) | Guia de estudo original, base dos tópicos e flashcards |
| [Pesquisa 2025-2026](fontes/pesquisa-atualizacoes-2025-2026.md) | Pesquisa sobre números que caem e mudanças recentes |
| [Verificação oficial (10/2026)](fontes/verificacao-fontes-oficiais-2026-10.md) | Exam guide, escopo, mudanças e números |
| [Verificação — rodadas 3 e 4](fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md) | Termos de cada task, planos de suporte, status de serviços |
| [Verificação das pendências (PDF)](fontes/verificacao-pendencias-2026-10.pdf) | Primeira rodada das pendências |
| [Verificação das pendências — rodada 2](fontes/verificacao-pendencias-2026-10-rodada-2.md) | Rodada final, com trecho literal de cada página oficial |
| [Pendências de verificação](docs/00-guia-do-exame/pendencias-de-verificacao.md) | O que ainda falta conferir (hoje: nada) |

> Preços, limites e nomes de planos mudam. Na semana da prova, confira o
> [exam guide oficial](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
> e a [lista de serviços no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html).

---

## Manutenção do material

<details>
<summary>Orientações para quem contribui com a apostila</summary>

Siga as [regras do repositório](CLAUDE.md): as mudanças chegam por Pull Request. Os capítulos e índices gerados devem ser alterados nas suas fontes editoriais; consulte os caminhos e convenções nesse documento.

As melhorias planejadas e seus critérios de conclusão estão na [pasta de pendências](pendencias/README.md), começando pela [especificação da apostila digital e impressa](pendencias/apostila-digital-e-impressa.md).

| Arquivo | Uso |
|---|---|
| [Gerador](scripts/gerar_docs.py) | Regenera aulas, fichas, flashcards, resumos e os blocos do sumário deste README. |
| [Estrutura da apostila](scripts/apostila.py) | Organiza o corpo das aulas e fichas. |
| [Fontes editoriais das fichas](scripts/conteudo_servicos/) | Conteúdo de cada categoria, antes da geração do Markdown. |
| [Banco de questões](scripts/banco_questoes.py) | Enunciados, alternativas e explicações. |
| [Gerador do simulado](scripts/gerar_simulado.py) | Atualiza o simulado e as questões por domínio. |
| [Verificador de links](scripts/verificar_links.py) | Confere os destinos dos links internos. |
| [Modelo de ficha](templates/servico.md) | Orienta a criação de fichas de serviços. |

Execute a partir da raiz:

```bash
python3 scripts/test_apostila.py
python3 scripts/gerar_docs.py
python3 scripts/gerar_simulado.py # se o banco de questões foi alterado
python3 scripts/verificar_links.py
```

Anotações pessoais devem ficar nos blocos preservados indicados nas regras do repositório. Nunca inclua credenciais AWS nos arquivos.

</details>
