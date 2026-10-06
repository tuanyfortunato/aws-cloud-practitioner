# 📖 Glossário

Termos e siglas que aparecem na prova, em ordem alfabética. O glossário serve para **relembrar** um termo; para aprender o conceito, siga o link da aula indicada. As aulas explicam cada termo no primeiro uso, dentro do raciocínio.

| Termo | Significado |
|---|---|
| **ABAC** | *Attribute-based access control*: permissões baseadas em tags/atributos |
| **Access key** | Par de credenciais (ID + segredo) de longo prazo para CLI/SDK/API |
| **ACL** | *Access control list* (S3 legado; Network ACL na VPC) |
| **Agilidade** | Reduzir tempo e custo de experimentar e entregar |
| **Alias record** | Registro do Route 53 que aponta para recursos AWS e funciona no apex do domínio |
| **Alta disponibilidade (HA)** | Sistema continua acessível com falhas, em geral usando várias AZs |
| **AMI** | *Amazon Machine Image*: modelo para lançar instâncias EC2 |
| **API** | Conjunto de operações que um programa oferece a outros; os serviços da AWS são usados por API ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **Armazenamento de arquivos** | Pastas compartilhadas pela rede entre várias máquinas; na AWS, EFS ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **Armazenamento de objetos** | Cada arquivo vira um objeto com conteúdo, chave e metadados, gravado e lido inteiro por API; na AWS, S3 ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **Armazenamento em bloco** | Disco dividido em blocos e formatado pelo sistema operacional; na AWS, EBS ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **ARN** | *Amazon Resource Name*: identificador único de um recurso (`arn:aws:s3:::bucket`) |
| **ASG** | *Auto Scaling Group*: grupo de instâncias EC2 que o EC2 Auto Scaling mantém na quantidade desejada, trocando as que falham e somando ou retirando instâncias entre o mínimo e o máximo |
| **Autenticação** | Provar quem é a identidade, com senha e, de preferência, MFA ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **Autorização** | Decidir o que uma identidade já autenticada pode fazer, por meio de permissões ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **AZ** | *Availability Zone*: um ou mais datacenters isolados dentro de uma região |
| **BAA** | *Business Associate Addendum* (HIPAA), aceito no AWS Artifact |
| **Banco de dados não relacional (NoSQL)** | Dados acessados por chave, com esquema flexível e escala horizontal; na AWS, DynamoDB ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **Banco de dados relacional** | Tabelas com esquema definido que se relacionam, consultadas com SQL e com transações; na AWS, RDS ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **Bastion host** | Instância pública usada como ponte para acessar recursos privados |
| **BYOL** | *Bring Your Own License*: usar licenças já compradas |
| **CAF** | *Cloud Adoption Framework*: 6 perspectivas para a transformação na nuvem |
| **CapEx** | Despesa de capital — investimento antecipado em infraestrutura |
| **CDC** | *Change data capture*: replicação contínua de mudanças (DMS) |
| **CDN** | *Content delivery network*: rede de servidores espalhados pelo mundo que guarda cópias do conteúdo perto dos usuários para entregá-lo mais rápido; na AWS, CloudFront |
| **Chave (criptografia)** | Valor secreto usado para cifrar e decifrar dados; quem tem a chave lê os dados. Na AWS, o KMS cria e controla as chaves ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **CIDR** | Notação de um bloco de endereços IP: o número depois da barra diz quantos bits iniciais são fixos (`10.0.0.0/16` tem 65.536 endereços) |
| **Cold start** | Latência extra ao iniciar um novo ambiente de execução do Lambda |
| **Comunicação assíncrona** | Quem pede deixa a mensagem, por exemplo numa fila, e segue sem esperar a resposta ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **Console / CLI / SDK** | Formas de usar a AWS: o console é a interface web; a CLI chama as APIs por comandos no terminal; os SDKs, de dentro de um programa ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **Consolidated billing** | Fatura única de várias contas no AWS Organizations |
| **Criptografia em trânsito / em repouso** | Proteção dos dados enquanto viajam pela rede (como HTTPS) / enquanto estão guardados ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **CVE** | *Common Vulnerabilities and Exposures*: vulnerabilidade catalogada (Inspector) |
| **DaaS** | *Desktop as a Service*: área de trabalho virtual que roda na nuvem e é acessada de qualquer dispositivo; na AWS, WorkSpaces |
| **Datacenter** | Prédio com servidores, rede, energia e refrigeração; na nuvem, quem constrói e mantém os datacenters é o provedor ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **DDoS** | Ataque distribuído de negação de serviço: muitas máquinas enviam tráfego ao mesmo tempo para derrubar um sistema; na AWS, a proteção é o Shield |
| **Desacoplamento** | Ligar componentes por filas ou eventos, para que a lentidão ou a falha de um não pare o outro; na AWS, SQS e SNS ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **DNS** | *Domain Name System*: traduz nomes de domínio em endereços IP; na AWS, Route 53 ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **DR** | *Disaster recovery*: Backup & Restore → Pilot Light → Warm Standby → Multi-site |
| **Edge location** | Ponto de presença usado por CloudFront, Route 53, Global Accelerator, Shield e WAF |
| **Elasticidade** | Aumentar **e reduzir** recursos automaticamente, acompanhando a demanda |
| **Endereço IP** | Endereço de uma máquina na rede; o público vale na internet, o privado só dentro de uma rede interna ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **ENI** | *Elastic Network Interface*: placa de rede virtual |
| **Escalabilidade** | Capacidade de crescer: vertical (scale up) ou horizontal (scale out) |
| **ETL** | *Extract, transform, load*: extrair dados de várias fontes, transformá-los e carregá-los num destino para análise; na AWS, Glue |
| **Event-driven** | Arquitetura que reage a eventos (Lambda, EventBridge) |
| **FaaS** | *Function as a Service*: você envia só o código de uma função e a plataforma a executa quando ela é chamada, sem servidores para administrar; na AWS, Lambda |
| **Fila** | Guarda mensagens entre componentes para processamento no ritmo do consumidor; na AWS, SQS ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **FinOps** | Prática de gestão financeira da nuvem: dar visibilidade aos gastos e dividir com as equipes a responsabilidade pelo custo |
| **FIPS 140** | Padrão de validação de módulos criptográficos (KMS, CloudHSM nível 3) |
| **Free Tier** | Uso gratuito limitado (clássico: Always Free, 12 meses, trials; novo: créditos) |
| **GB-segundo** | Unidade de cobrança do Lambda (memória × duração) |
| **GPU** | Processador especializado em fazer muitos cálculos em paralelo, usado em gráficos e em aprendizado de máquina |
| **Graviton** | Processadores ARM da AWS: melhor preço/desempenho e eficiência energética |
| **Híbrido** | Parte on-premises, parte na nuvem, conectadas |
| **Hipervisor** | Camada que divide um servidor físico em máquinas virtuais (na AWS, Nitro) — responsabilidade da AWS ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **HPC** | *High performance computing*: cálculos intensivos, como simulações, divididos entre muitos processadores trabalhando juntos |
| **HSM** | *Hardware security module* (KMS usa HSMs compartilhados; CloudHSM é dedicado) |
| **HTTP** | Protocolo de pedidos e respostas usado pela web e pela maioria das APIs; o HTTPS é a versão cifrada ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **HTTPS** | HTTP cifrado por TLS, com certificado que prova a identidade do site ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **IaaS / PaaS / SaaS** | Infraestrutura / Plataforma / Software como serviço: quanto mais à direita, mais camadas o provedor administra, da máquina virtual à aplicação pronta |
| **IaC** | Infraestrutura como código: descrever servidores, redes e outros recursos em arquivos de texto que criam e atualizam o ambiente de forma repetível; na AWS, CloudFormation e CDK (Terraform é de terceiros) |
| **Identidade** | Quem faz um pedido ao sistema, pessoa ou programa; cada um deve ter a sua, para receber só o que precisa e deixar registro do que fez ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **IEM / AWS Countdown** | Apoio da AWS para eventos de grande escala; hoje se chama **AWS Countdown** (incluído no Unified Operations, pago à parte nos demais) |
| **IGW** | *Internet Gateway*: componente da VPC que permite a comunicação entre a VPC e a internet; é o destino da rota das subnets públicas |
| **IMDS** | *Instance Metadata Service* do EC2 (use IMDSv2) |
| **Instance store** | Disco local efêmero de uma instância EC2 |
| **Instância** | Servidor virtual do Amazon EC2; o tipo de instância define processador, memória, armazenamento e rede ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **IOPS** | Operações de leitura e escrita por segundo de um armazenamento; é uma das medidas de desempenho dos volumes EBS |
| **Latência** | Tempo que um pedido leva para ir e voltar; diferente de throughput, que mede quanto passa por segundo |
| **Least privilege** | Menor privilégio: só as permissões necessárias ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **Lift-and-shift** | Rehost: levar uma aplicação para a nuvem sem mudar o código nem a arquitetura |
| **Máquina virtual (VM)** | Computador simulado por software sobre um servidor físico, com seu próprio sistema operacional ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **MFA** | Autenticação multifator: um segundo fator, como código no celular, além da senha ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **Microsserviços** | Serviços pequenos e independentes que se comunicam por APIs/filas |
| **MPP** | *Massively parallel processing*: uma consulta é dividida entre vários nós, que processam partes dos dados ao mesmo tempo; é a arquitetura do Redshift |
| **Multi-AZ** | Implantação em várias AZs para alta disponibilidade |
| **NACL** | *Network ACL*: firewall stateless da subnet |
| **NAT Gateway** | Permite que subnets privadas saiam para a internet sem receber conexões |
| **NLP** | Processamento de linguagem natural: extrair sentido de texto escrito por pessoas, como sentimento, entidades e frases-chave; na AWS, Comprehend |
| **OAC** | *Origin Access Control*: bucket S3 privado acessível só pelo CloudFront |
| **OLAP / OLTP** | Processamento analítico (Redshift) / transacional (RDS, Aurora) |
| **On-premises** | Infraestrutura no datacenter próprio |
| **OpEx** | Despesa operacional: gasto recorrente, pago à medida que se usa |
| **OU** | *Organizational Unit*: grupo de contas dentro do AWS Organizations, usado para aplicar as mesmas políticas a todas |
| **Patch** | Correção publicada para um software, como o sistema operacional; no EC2, aplicar patches no SO da instância é do cliente |
| **Pay-as-you-go** | Pagar só pelo que usar, sem compromisso antecipado |
| **PII** | Informação pessoal identificável (Macie) |
| **Política (IAM)** | Documento, em geral JSON, que diz quais ações uma identidade ou um recurso pode realizar, sobre quais recursos e em quais condições ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **PoP** | *Point of presence*: o mesmo que edge location, um ponto da rede da AWS perto dos usuários |
| **Porta** | Número que indica qual programa da máquina recebe os dados: 443 (HTTPS), 80 (HTTP), 22 (SSH) ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **Presigned URL** | URL temporária para acessar um objeto privado do S3 |
| **Publicação e inscrição (pub/sub)** | Uma mensagem publicada num tópico chega a todos os inscritos; na AWS, SNS ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **Quota** | Limite de uso de um serviço numa conta, em geral por região; algumas podem ser aumentadas por pedido no Service Quotas, outras não |
| **RAG** | *Retrieval-augmented generation*: IA generativa usando seus documentos (Bedrock Knowledge Bases) |
| **RCU / WCU** | Unidades de capacidade de leitura/escrita do DynamoDB |
| **Recurso** | Algo que você cria e administra num serviço, como uma instância, um bucket ou uma tabela |
| **Região** | Área geográfica com no mínimo 3 AZs isoladas e fisicamente separadas; a maioria dos recursos é criada numa região específica |
| **RI** | *Reserved Instance*: desconto por compromisso de 1 ou 3 anos |
| **Rightsizing** | Ajustar o tamanho dos recursos ao uso real |
| **Role** | Identidade IAM com credenciais temporárias |
| **RPO / RTO** | Perda máxima de dados aceitável / tempo máximo para restaurar |
| **SCP** | *Service Control Policy*: teto de permissões de contas/OUs (não afeta a conta de gerenciamento) |
| **Security group** | Firewall stateful da instância/ENI |
| **Serverless** | Sem gerenciar servidores, escala automática, paga pelo uso |
| **Serviço gerenciado** | Serviço em que a AWS cuida de parte da operação, como servidores e atualizações de software; o cliente continua responsável pelos dados e pelas configurações |
| **Servidor** | Computador que atende pedidos de outros computadores, os clientes ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **Sistema operacional (SO)** | Software entre o hardware e os programas, como Linux ou Windows; numa VM, chama-se SO convidado ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **SLA** | Acordo de nível de serviço (Route 53: 100%) |
| **Snapshot** | Cópia pontual de um volume/banco |
| **Spot** | Capacidade ociosa com até 90% de desconto, interrompível com aviso de 2 min |
| **SQL** | Linguagem de consulta de bancos relacionais ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **SSO** | *Single sign-on*: um único login dá acesso a várias contas e aplicações; na AWS, IAM Identity Center |
| **Stateful / stateless** | Que guarda (ou não) informação sobre conexões ou sessões anteriores; o security group é stateful e a NACL é stateless |
| **STS** | *Security Token Service*: emite credenciais temporárias |
| **Subnet pública / privada** | Com / sem rota para o Internet Gateway ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **Support plans** | Basic, Business Support+, Enterprise, Unified Operations (atuais); Developer, Business, Enterprise On-Ramp (clássicos, até 01/01/2027) |
| **Sustentabilidade** | 6º pilar do Well-Architected (impacto ambiental) |
| **TAM** | *Technical Account Manager*: designado no Enterprise e no Unified Operations (no clássico Enterprise On-Ramp: pool) |
| **TCO** | *Total cost of ownership*: custo total on-premises × nuvem |
| **Throughput** | Quantidade de dados transferida por unidade de tempo, em geral em bytes por segundo |
| **Tolerância a falhas** | Continuar funcionando sem interrupção percebida quando um componente falha |
| **TTL** | *Time to live*: por quanto tempo um dado continua válido antes de expirar, como um registro DNS em cache ou um item do DynamoDB |
| **vCPU** | Processador virtual de uma instância; na maioria das instâncias x86 do EC2, cada vCPU é uma thread de um núcleo do processador |
| **VPC** | *Virtual Private Cloud*: rede privada isolada numa região |
| **Well-Architected** | Framework com 6 pilares de boas práticas |
| **Workload** | Conjunto de recursos e código que entrega um resultado de negócio, como uma aplicação inteira |
| **WORM** | *Write once, read many* (S3 Object Lock, Backup Vault Lock) |
| **7 Rs** | Retire, Retain, Rehost, Relocate, Replatform, Repurchase, Refactor |
