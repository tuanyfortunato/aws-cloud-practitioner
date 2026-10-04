# ⚖️ Pares que confundem

Revise esta seção a cada poucos dias. A maioria dos erros de quem já usa AWS vem de trocar serviços vizinhos.

| Par | Diferença em uma linha |
| --- | --- |
| CloudTrail vs CloudWatch | CloudTrail = quem fez qual chamada de API (auditoria); CloudWatch = métricas, logs e alarmes de desempenho |
| CloudTrail vs Config | CloudTrail = ações executadas; Config = estado e histórico de configuração dos recursos e conformidade |
| Shield vs WAF | Shield = DDoS (camadas 3 e 4; Advanced também 7); WAF = filtragem de requisições web (SQL injection, XSS) |
| WAF vs Firewall Manager | WAF = regras numa aplicação; Firewall Manager = gerencia regras em todas as contas |
| GuardDuty vs Inspector | GuardDuty = ameaças em andamento a partir de logs; Inspector = vulnerabilidades nos recursos |
| GuardDuty vs Detective | GuardDuty detecta; Detective investiga a causa raiz |
| Macie vs Inspector | Macie = dados sensíveis no S3; Inspector = falhas de software em EC2, ECR e Lambda |
| Trusted Advisor vs Security Hub | Trusted Advisor = boas práticas de custo, segurança, performance e cotas; Security Hub = achados de segurança centralizados |
| Artifact vs Audit Manager | Artifact = relatórios de compliance da AWS; Audit Manager = evidências da sua conta para a sua auditoria |
| KMS vs CloudHSM | KMS = chaves gerenciadas em HSM compartilhado; CloudHSM = HSM dedicado controlado pelo cliente |
| Secrets Manager vs Parameter Store | Secrets Manager = segredos com rotação automática (pago); Parameter Store = configurações e segredos simples (tem camada grátis) |
| IAM Identity Center vs Cognito | Identity Center = funcionários acessando contas AWS (SSO); Cognito = usuários finais de um aplicativo |
| User vs Role | User = credencial de longo prazo; Role = credencial temporária assumida por quem precisa |
| Organizations vs Control Tower | Organizations = gerencia contas, SCPs e fatura; Control Tower = monta landing zone padronizada sobre o Organizations |
| Security group vs NACL | SG = instância, stateful, só permite; NACL = subnet, stateless, permite e nega |
| NAT Gateway vs Internet Gateway | IGW = entrada e saída da internet para subnet pública; NAT = só saída para subnet privada |
| VPC Peering vs Transit Gateway | Peering = liga duas VPCs, não transitivo; Transit Gateway = hub para muitas VPCs e on-premises |
| VPN vs Direct Connect | VPN = criptografada pela internet, rápida de montar; Direct Connect = link físico dedicado, estável, demora semanas |
| CloudFront vs Global Accelerator | CloudFront faz cache de conteúdo; Global Accelerator não faz cache e dá IPs estáticos |
| Route 53 vs CloudFront | Route 53 = DNS (para onde ir); CloudFront = entrega e cache do conteúdo |
| SQS vs SNS | SQS = fila, consumidor puxa; SNS = pub/sub, empurra para vários |
| SNS vs EventBridge | SNS = notificações simples; EventBridge = roteamento de eventos com regras, inclusive de SaaS |
| SNS vs SES | SNS = notificações (e-mail simples, SMS, push); SES = e-mails formatados em volume |
| EventBridge vs Step Functions | EventBridge = reage e roteia eventos; Step Functions = orquestra um fluxo de várias etapas |
| EBS vs EFS vs S3 | EBS = disco de uma instância; EFS = arquivos compartilhados por várias; S3 = objetos via API |
| EBS vs instance store | EBS = persistente; instance store = temporário, some ao parar |
| EFS vs FSx | EFS = arquivos Linux (NFS); FSx = Windows (SMB), Lustre, ONTAP, OpenZFS |
| Snow vs DataSync | Snow = transferência offline em dispositivo físico; DataSync = transferência online pela rede |
| RDS Multi-AZ vs Read Replica | Multi-AZ = disponibilidade (failover); Read Replica = performance de leitura |
| RDS vs Aurora | Aurora = relacional da AWS, mais rápido, 6 cópias em 3 AZs; RDS = vários motores comerciais e open source |
| RDS vs DynamoDB | RDS = relacional (SQL, joins); DynamoDB = NoSQL chave-valor, escala massiva |
| Redshift vs RDS | Redshift = análise (OLAP); RDS = transações (OLTP) |
| Athena vs Redshift | Athena = SQL sob demanda direto no S3; Redshift = data warehouse carregado e sempre disponível |
| Kinesis vs SQS | Kinesis = streaming em tempo real, vários consumidores relendo dados; SQS = fila de mensagens para desacoplar |
| Glue vs EMR | Glue = ETL serverless; EMR = clusters Spark/Hadoop gerenciados |
| Lambda vs Fargate | Lambda = funções por evento, até 15 min; Fargate = containers sem servidor, sem limite de duração |
| ECS vs EKS | ECS = orquestrador próprio da AWS; EKS = Kubernetes |
| Elastic Beanstalk vs CloudFormation | Beanstalk = sobe a aplicação sem pensar em infra; CloudFormation = descreve qualquer infraestrutura como código |
| Elastic Beanstalk vs Lightsail | Beanstalk = PaaS que escala; Lightsail = servidor simples com preço fixo |
| WorkSpaces vs AppStream 2.0 | WorkSpaces = desktop inteiro; AppStream = só a aplicação no navegador |
| Outposts vs Local Zones vs Wavelength | Outposts = AWS no seu datacenter; Local Zones = AWS perto de cidades; Wavelength = AWS na rede 5G |
| Region vs AZ vs Edge location | Região = área geográfica; AZ = datacenter(s) isolado(s) dentro dela; edge = cache e DNS perto do usuário |
| Cost Explorer vs Budgets | Cost Explorer = analisa e prevê; Budgets = alerta e age |
| Cost Explorer vs CUR | Cost Explorer = gráficos e filtros; CUR = dados brutos mais detalhados |
| Pricing Calculator vs Cost Explorer | Calculator = antes de usar; Cost Explorer = depois, com dados reais |
| Reserved Instances vs Savings Plans | RI = tipo de instância específico; Savings Plans = compromisso de gasto por hora, mais flexível |
| Dedicated Host vs Dedicated Instance | Host = servidor físico com visibilidade de sockets e núcleos (licenças); Instance = hardware isolado sem esse controle |
| Business Support+ vs Enterprise vs Unified Operations (atuais) | Business Support+ = US$ 29/conta, 30 min, Trusted Advisor completo; Enterprise = TAM designado, TA Priority, 15 min; Unified Operations = 5 min, monitoramento 24/7 |
| Business vs Enterprise On-Ramp vs Enterprise (clássicos, até 01/01/2027) | Business = 24/7 e Trusted Advisor completo; On-Ramp = pool de TAMs, 30 min; Enterprise = TAM dedicado, 15 min |
| Professional Services vs Managed Services | Professional Services = consultoria para projetos; Managed Services = a AWS opera a infraestrutura |
| Application Migration Service vs DMS | MGN = migra servidores inteiros; DMS = migra bancos de dados |
| DMS vs SCT | DMS = move os dados; SCT = converte o schema entre motores diferentes |
| Rehost vs Replatform vs Refactor | Rehost = sem mudanças; Replatform = pequenos ajustes (ex.: para RDS); Refactor = reescrever cloud-native |
| Escalabilidade vs Elasticidade | Escalabilidade = conseguir crescer; Elasticidade = crescer e encolher automaticamente |
| Alta disponibilidade vs Tolerância a falhas | HA = continua acessível com pouca interrupção; tolerância a falhas = zero interrupção percebida |

> Veja também: [palavras-chave → serviço](palavras-chave.md) · [números-âncora](numeros-ancora.md)
