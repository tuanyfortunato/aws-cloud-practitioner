# 📖 Glossário

Termos e siglas que aparecem na prova, em ordem alfabética.

| Termo | Significado |
|---|---|
| **ABAC** | *Attribute-based access control*: permissões baseadas em tags/atributos |
| **Access key** | Par de credenciais (ID + segredo) de longo prazo para CLI/SDK/API |
| **ACL** | *Access control list* (S3 legado; Network ACL na VPC) |
| **Agilidade** | Reduzir tempo e custo de experimentar e entregar |
| **Alias record** | Registro do Route 53 que aponta para recursos AWS e funciona no apex do domínio |
| **AMI** | *Amazon Machine Image*: modelo para lançar instâncias EC2 |
| **API** | Conjunto de operações que um programa oferece a outros; os serviços da AWS são usados por API ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **Armazenamento de arquivos** | Pastas compartilhadas pela rede entre várias máquinas; na AWS, EFS ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **Armazenamento de objetos** | Cada arquivo vira um objeto com conteúdo, chave e metadados, gravado e lido inteiro por API; na AWS, S3 ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **Armazenamento em bloco** | Disco dividido em blocos e formatado pelo sistema operacional; na AWS, EBS ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **ARN** | *Amazon Resource Name*: identificador único de um recurso (`arn:aws:s3:::bucket`) |
| **Alta disponibilidade (HA)** | Sistema continua acessível com falhas, em geral usando várias AZs |
| **ASG** | *Auto Scaling Group* |
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
| **CDN** | *Content delivery network* (CloudFront) |
| **CIDR** | Notação de blocos de IP (`10.0.0.0/16`) |
| **Cold start** | Latência extra ao iniciar um novo ambiente de execução do Lambda |
| **Comunicação assíncrona** | Quem pede deixa a mensagem, por exemplo numa fila, e segue sem esperar a resposta ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **Consolidated billing** | Fatura única de várias contas no AWS Organizations |
| **Criptografia em trânsito / em repouso** | Proteção dos dados enquanto viajam pela rede (como HTTPS) / enquanto estão guardados ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **CVE** | *Common Vulnerabilities and Exposures*: vulnerabilidade catalogada (Inspector) |
| **DaaS** | *Desktop as a Service* (WorkSpaces) |
| **DDoS** | Ataque distribuído de negação de serviço (Shield) |
| **Desacoplamento** | Componentes se comunicam por filas/eventos; falha de um não derruba o outro |
| **DNS** | *Domain Name System*: traduz nomes de domínio em endereços IP; na AWS, Route 53 ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **DR** | *Disaster recovery*: Backup & Restore → Pilot Light → Warm Standby → Multi-site |
| **Edge location** | Ponto de presença usado por CloudFront, Route 53, Global Accelerator, Shield e WAF |
| **Elasticidade** | Aumentar **e reduzir** recursos automaticamente conforme a demanda |
| **Endereço IP** | Endereço de uma máquina na rede; o público vale na internet, o privado só dentro de uma rede interna ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **ENI** | *Elastic Network Interface*: placa de rede virtual |
| **Escalabilidade** | Capacidade de crescer: vertical (scale up) ou horizontal (scale out) |
| **ETL** | *Extract, transform, load* (Glue) |
| **Event-driven** | Arquitetura que reage a eventos (Lambda, EventBridge) |
| **FaaS** | *Function as a Service* (Lambda) |
| **Fila** | Guarda mensagens entre componentes para processamento no ritmo do consumidor; na AWS, SQS ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **FIPS 140** | Padrão de validação de módulos criptográficos (KMS, CloudHSM nível 3) |
| **FinOps** | Gestão financeira da nuvem |
| **Free Tier** | Uso gratuito limitado (clássico: Always Free, 12 meses, trials; novo: créditos) |
| **GB-segundo** | Unidade de cobrança do Lambda (memória × duração) |
| **Graviton** | Processadores ARM da AWS: melhor preço/desempenho e eficiência energética |
| **HPC** | *High performance computing* |
| **HSM** | *Hardware security module* (KMS usa HSMs compartilhados; CloudHSM é dedicado) |
| **Hipervisor** | Camada que divide um servidor físico em máquinas virtuais (na AWS, Nitro) — responsabilidade da AWS ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **Híbrido** | Parte on-premises, parte na nuvem, conectadas |
| **HTTPS** | HTTP cifrado por TLS, com certificado que prova a identidade do site ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **IaaS / PaaS / SaaS** | Infraestrutura / Plataforma / Software como serviço |
| **IaC** | Infraestrutura como código (CloudFormation, CDK, Terraform) |
| **IEM / AWS Countdown** | Apoio da AWS para eventos de grande escala; hoje se chama **AWS Countdown** (incluído no Unified Operations, pago à parte nos demais) |
| **IGW** | *Internet Gateway* |
| **IMDS** | *Instance Metadata Service* do EC2 (use IMDSv2) |
| **Instance store** | Disco local efêmero de uma instância EC2 |
| **Instância** | Servidor virtual do Amazon EC2; o tipo de instância define processador, memória, armazenamento e rede ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **Least privilege** | Menor privilégio: só as permissões necessárias ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **Lift-and-shift** | Rehost: migrar sem mudanças |
| **Máquina virtual (VM)** | Computador simulado por software sobre um servidor físico, com seu próprio sistema operacional ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **MFA** | Autenticação multifator: um segundo fator, como código no celular, além da senha ([aula 0.5](docs/fundamentos/05-seguranca-basica.md)) |
| **Microsserviços** | Serviços pequenos e independentes que se comunicam por APIs/filas |
| **MPP** | *Massively parallel processing* (Redshift) |
| **Multi-AZ** | Implantação em várias AZs para alta disponibilidade |
| **NAT Gateway** | Permite que subnets privadas saiam para a internet sem receber conexões |
| **NACL** | *Network ACL*: firewall stateless da subnet |
| **NLP** | Processamento de linguagem natural (Comprehend) |
| **OAC** | *Origin Access Control*: bucket S3 privado acessível só pelo CloudFront |
| **OLAP / OLTP** | Processamento analítico (Redshift) / transacional (RDS, Aurora) |
| **On-premises** | Infraestrutura no datacenter próprio |
| **OpEx** | Despesa operacional — paga conforme o uso |
| **OU** | *Organizational Unit* do AWS Organizations |
| **Patch** | Correção publicada para um software, como o sistema operacional; no EC2, aplicar patches no SO da instância é do cliente |
| **Pay-as-you-go** | Pagar conforme o uso, sem compromisso |
| **PII** | Informação pessoal identificável (Macie) |
| **PoP** | *Point of presence* (edge location) |
| **Porta** | Número que indica qual programa da máquina recebe os dados: 443 (HTTPS), 80 (HTTP), 22 (SSH) ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **Presigned URL** | URL temporária para acessar um objeto privado do S3 |
| **Publicação e inscrição (pub/sub)** | Uma mensagem publicada num tópico chega a todos os inscritos; na AWS, SNS ([aula 0.4](docs/fundamentos/04-api-e-filas.md)) |
| **RAG** | *Retrieval-augmented generation*: IA generativa usando seus documentos (Bedrock Knowledge Bases) |
| **RCU / WCU** | Unidades de capacidade de leitura/escrita do DynamoDB |
| **Região** | Área geográfica com no mínimo 3 AZs |
| **RI** | *Reserved Instance*: desconto por compromisso de 1 ou 3 anos |
| **Rightsizing** | Ajustar o tamanho dos recursos ao uso real |
| **Role** | Identidade IAM com credenciais temporárias |
| **RPO / RTO** | Perda máxima de dados aceitável / tempo máximo para restaurar |
| **SCP** | *Service Control Policy*: teto de permissões de contas/OUs (não afeta a conta de gerenciamento) |
| **Security group** | Firewall stateful da instância/ENI |
| **Serverless** | Sem gerenciar servidores, escala automática, paga pelo uso |
| **Servidor** | Computador que atende pedidos de outros computadores, os clientes ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **Sistema operacional (SO)** | Software entre o hardware e os programas, como Linux ou Windows; numa VM, chama-se SO convidado ([aula 0.1](docs/fundamentos/01-servidor-e-virtualizacao.md)) |
| **SLA** | Acordo de nível de serviço (Route 53: 100%) |
| **Snapshot** | Cópia pontual de um volume/banco |
| **Spot** | Capacidade ociosa com até 90% de desconto, interrompível com aviso de 2 min |
| **SQL** | Linguagem de consulta de bancos relacionais ([aula 0.3](docs/fundamentos/03-dados.md)) |
| **SSO** | *Single sign-on* (IAM Identity Center) |
| **Stateful / stateless** | Guarda (ou não) estado da conexão/sessão |
| **STS** | *Security Token Service*: emite credenciais temporárias |
| **Subnet pública / privada** | Com / sem rota para o Internet Gateway ([aula 0.2](docs/fundamentos/02-rede.md)) |
| **Support plans** | Basic, Business Support+, Enterprise, Unified Operations (atuais); Developer, Business, Enterprise On-Ramp (clássicos, até 01/01/2027) |
| **Sustentabilidade** | 6º pilar do Well-Architected (impacto ambiental) |
| **TAM** | *Technical Account Manager*: designado no Enterprise e no Unified Operations (no clássico Enterprise On-Ramp: pool) |
| **TCO** | *Total cost of ownership*: custo total on-premises × nuvem |
| **Tolerância a falhas** | Continuar funcionando sem interrupção percebida quando um componente falha |
| **TTL** | *Time to live* (DNS, cache, expiração de itens no DynamoDB) |
| **VPC** | *Virtual Private Cloud*: rede privada isolada numa região |
| **Well-Architected** | Framework com 6 pilares de boas práticas |
| **WORM** | *Write once, read many* (S3 Object Lock, Backup Vault Lock) |
| **7 Rs** | Retire, Retain, Rehost, Relocate, Replatform, Repurchase, Refactor |
