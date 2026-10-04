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
| **API** | Interface programática; tudo na AWS é uma chamada de API |
| **ARN** | *Amazon Resource Name*: identificador único de um recurso (`arn:aws:s3:::bucket`) |
| **Alta disponibilidade (HA)** | Sistema continua acessível com falhas, em geral usando várias AZs |
| **ASG** | *Auto Scaling Group* |
| **AZ** | *Availability Zone*: um ou mais datacenters isolados dentro de uma região |
| **BAA** | *Business Associate Addendum* (HIPAA), aceito no AWS Artifact |
| **Bastion host** | Instância pública usada como ponte para acessar recursos privados |
| **BYOL** | *Bring Your Own License*: usar licenças já compradas |
| **CAF** | *Cloud Adoption Framework*: 6 perspectivas para a transformação na nuvem |
| **CapEx** | Despesa de capital — investimento antecipado em infraestrutura |
| **CDC** | *Change data capture*: replicação contínua de mudanças (DMS) |
| **CDN** | *Content delivery network* (CloudFront) |
| **CIDR** | Notação de blocos de IP (`10.0.0.0/16`) |
| **Cold start** | Latência extra ao iniciar um novo ambiente de execução do Lambda |
| **Consolidated billing** | Fatura única de várias contas no AWS Organizations |
| **CVE** | *Common Vulnerabilities and Exposures*: vulnerabilidade catalogada (Inspector) |
| **DaaS** | *Desktop as a Service* (WorkSpaces) |
| **DDoS** | Ataque distribuído de negação de serviço (Shield) |
| **Desacoplamento** | Componentes se comunicam por filas/eventos; falha de um não derruba o outro |
| **DR** | *Disaster recovery*: Backup & Restore → Pilot Light → Warm Standby → Multi-site |
| **Edge location** | Ponto de presença usado por CloudFront, Route 53, Global Accelerator, Shield e WAF |
| **Elasticidade** | Aumentar **e reduzir** recursos automaticamente conforme a demanda |
| **ENI** | *Elastic Network Interface*: placa de rede virtual |
| **Escalabilidade** | Capacidade de crescer: vertical (scale up) ou horizontal (scale out) |
| **ETL** | *Extract, transform, load* (Glue) |
| **Event-driven** | Arquitetura que reage a eventos (Lambda, EventBridge) |
| **FaaS** | *Function as a Service* (Lambda) |
| **FIPS 140** | Padrão de validação de módulos criptográficos (KMS, CloudHSM nível 3) |
| **FinOps** | Gestão financeira da nuvem |
| **Free Tier** | Uso gratuito limitado (clássico: Always Free, 12 meses, trials; novo: créditos) |
| **GB-segundo** | Unidade de cobrança do Lambda (memória × duração) |
| **Graviton** | Processadores ARM da AWS: melhor preço/desempenho e eficiência energética |
| **HPC** | *High performance computing* |
| **HSM** | *Hardware security module* (KMS usa HSMs compartilhados; CloudHSM é dedicado) |
| **Hipervisor** | Camada de virtualização (Nitro) — responsabilidade da AWS |
| **Híbrido** | Parte on-premises, parte na nuvem, conectadas |
| **IaaS / PaaS / SaaS** | Infraestrutura / Plataforma / Software como serviço |
| **IaC** | Infraestrutura como código (CloudFormation, CDK, Terraform) |
| **IEM / AWS Countdown** | Apoio da AWS para eventos de grande escala; hoje se chama **AWS Countdown** (incluído no Unified Operations, pago à parte nos demais) |
| **IGW** | *Internet Gateway* |
| **IMDS** | *Instance Metadata Service* do EC2 (use IMDSv2) |
| **Instance store** | Disco local efêmero de uma instância EC2 |
| **Least privilege** | Menor privilégio: só as permissões necessárias |
| **Lift-and-shift** | Rehost: migrar sem mudanças |
| **MFA** | Autenticação multifator |
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
| **Pay-as-you-go** | Pagar conforme o uso, sem compromisso |
| **PII** | Informação pessoal identificável (Macie) |
| **PoP** | *Point of presence* (edge location) |
| **Presigned URL** | URL temporária para acessar um objeto privado do S3 |
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
| **SLA** | Acordo de nível de serviço (Route 53: 100%) |
| **Snapshot** | Cópia pontual de um volume/banco |
| **Spot** | Capacidade ociosa com até 90% de desconto, interrompível com aviso de 2 min |
| **SSO** | *Single sign-on* (IAM Identity Center) |
| **Stateful / stateless** | Guarda (ou não) estado da conexão/sessão |
| **STS** | *Security Token Service*: emite credenciais temporárias |
| **Subnet pública / privada** | Com / sem rota para o Internet Gateway |
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
