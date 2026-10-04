# 📝 Simulado 01 — CLF-C02

Simulado no formato da prova: **65 questões**, distribuídas como os pesos oficiais (Domínio 1: 16 · Domínio 2: 20 · Domínio 3: 21 · Domínio 4: 8), em ordem aleatória, com questões de **múltipla escolha** (1 correta) e **múltipla resposta** (2 corretas).

## Como fazer

1. Reserve **90 minutos** sem interrupção.
2. Anote suas respostas num papel (ex.: `1-B, 2-A`) **sem abrir** o "Ver resposta".
3. Ao terminar, confira no [gabarito](#gabarito) e preencha a folha de correção.
4. Leia a explicação de **todas** as questões que errou e registre os erros num arquivo a partir do [modelo de simulado](../templates/simulado.md).

> Na prova real, a nota mínima é 700/1000 (≈ 70%). Meta de treino: **≥ 80%**.

---

### Questão 1

<sub>Domínio 4 · tópico [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)</sub>

Uma empresa com uma única conta AWS precisa saber quanto cada departamento gasta para fazer o rateio interno dos custos. Qual é a forma recomendada?

- **A)** Abrir um caso no AWS Support pedindo o relatório
- **B)** Usar o AWS Pricing Calculator mensalmente
- **C)** Criar um usuário IAM para cada departamento
- **D)** Aplicar cost allocation tags aos recursos e ativá-las no console de Billing

<details>
<summary>Ver resposta</summary>

**Resposta: D**

As **cost allocation tags** (ex.: `departamento=marketing`), depois de **ativadas** no Billing, separam os custos no Cost Explorer e no CUR. Usuários IAM não separam custos de recursos; a calculadora estima custos futuros; o suporte não faz rateio.

</details>

### Questão 2

<sub>Domínio 3 · tópico [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)</sub>

O time de BI precisa executar consultas SQL analíticas complexas sobre petabytes de dados históricos de vendas, alimentando dashboards. Qual serviço é o mais indicado?

- **A)** Amazon Redshift
- **B)** Amazon RDS for MySQL
- **C)** Amazon DynamoDB
- **D)** Amazon ElastiCache

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Redshift** é o data warehouse colunar para análises (OLAP) em grande escala. RDS é otimizado para transações (OLTP); DynamoDB é NoSQL chave-valor; ElastiCache é cache em memória.

</details>

### Questão 3

<sub>Domínio 1 · tópico [1.2](../docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) · **múltipla resposta**</sub>

Quais DUAS opções são vantagens da computação em nuvem segundo a AWS? (Escolha DUAS.)

- **A)** Beneficiar-se de economias de escala massivas
- **B)** Trocar despesa de capital por despesa variável
- **C)** Ter acesso físico aos servidores do datacenter da AWS
- **D)** Pagar antecipadamente pelas licenças de todos os serviços
- **E)** Eliminar toda a responsabilidade do cliente pela segurança

<details>
<summary>Ver resposta</summary>

**Resposta: A, B**

As duas fazem parte das 6 vantagens oficiais. Clientes **não** têm acesso físico aos datacenters; a segurança é **compartilhada** (o cliente continua responsável pela segurança *na* nuvem); e o modelo é pagar conforme o uso, não antecipadamente.

</details>

### Questão 4

<sub>Domínio 2 · tópico [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) · **múltipla resposta**</sub>

Quais DUAS afirmações sobre security groups e network ACLs estão corretas? (Escolha DUAS.)

- **A)** Network ACLs são stateful e atuam no nível da instância
- **B)** Security groups aceitam regras de negação para bloquear um IP específico
- **C)** Security groups são stateful: o tráfego de retorno é liberado automaticamente
- **D)** Network ACLs atuam no nível da subnet e aceitam regras de permissão e de negação
- **E)** Security groups são aplicados a subnets inteiras

<details>
<summary>Ver resposta</summary>

**Resposta: C, D**

Security groups atuam na instância/ENI, são **stateful** e só têm regras de permissão. Network ACLs atuam na **subnet**, são **stateless** e aceitam **permitir e negar** — por isso são usadas para bloquear um IP específico.

</details>

### Questão 5

<sub>Domínio 4 · tópico [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)</sub>

Antes de migrar, uma empresa quer estimar o custo mensal de uma nova arquitetura com EC2, RDS e S3, e compartilhar a estimativa com a diretoria. Qual ferramenta deve ser usada?

- **A)** AWS Cost and Usage Report
- **B)** AWS Cost Explorer
- **C)** AWS Budgets
- **D)** AWS Pricing Calculator

<details>
<summary>Ver resposta</summary>

**Resposta: D**

A **Pricing Calculator** estima custos **antes** de criar recursos e gera estimativas compartilháveis. Cost Explorer, Budgets e CUR trabalham com gastos **reais** de recursos já em uso.

</details>

### Questão 6

<sub>Domínio 1 · tópico [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)</sub>

Uma empresa aceita perder no máximo 15 minutos de dados em caso de desastre. Esse requisito define qual métrica?

- **A)** Acordo de nível de serviço (SLA)
- **B)** Recovery Time Objective (RTO)
- **C)** Recovery Point Objective (RPO)
- **D)** Tempo médio entre falhas (MTBF)

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **RPO** mede a perda máxima aceitável de dados, expressa em tempo. O **RTO** é o tempo máximo para restaurar o serviço; SLA é o compromisso de disponibilidade do provedor; MTBF mede a confiabilidade de um componente.

</details>

### Questão 7

<sub>Domínio 3 · tópico [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)</sub>

Um jogo online precisa armazenar o perfil e o progresso de milhões de jogadores com latência de milissegundos de um dígito, em qualquer escala, sem gerenciar servidores. Qual banco de dados atende melhor?

- **A)** Amazon Redshift
- **B)** Amazon Neptune
- **C)** Amazon DynamoDB
- **D)** Amazon RDS for PostgreSQL

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **DynamoDB** é NoSQL chave-valor serverless, com latência de milissegundos de um dígito em qualquer escala. RDS é relacional e exige dimensionar instâncias; Redshift é data warehouse (OLAP); Neptune é banco de grafos.

</details>

### Questão 8

<sub>Domínio 4 · tópico [4.5](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)</sub>

Uma grande empresa precisa de um Technical Account Manager (TAM) designado e de resposta em até 15 minutos quando um sistema crítico estiver fora do ar, pelo MENOR custo. Qual plano de suporte atende a esses requisitos?

- **A)** AWS Enterprise Support
- **B)** AWS Business Support+
- **C)** Basic
- **D)** AWS Unified Operations

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Enterprise Support** inclui TAM **designado** e resposta em 15 minutos para casos críticos, a partir de US$ 5.000/mês — atende ao requisito com o menor custo. O Business Support+ responde em 30 minutos e não tem TAM designado; o Basic não tem suporte técnico; o Unified Operations (5 min) também atenderia, mas custa a partir de US$ 50.000/mês.

</details>

### Questão 9

<sub>Domínio 3 · tópico [3.9](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)</sub>

Dezenas de instâncias Linux distribuídas em várias zonas de disponibilidade precisam ler e gravar os mesmos arquivos ao mesmo tempo. Qual serviço de armazenamento atende a esse requisito?

- **A)** Amazon EFS
- **B)** Amazon EBS
- **C)** Instance store
- **D)** Amazon FSx for Windows File Server

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **EFS** é um sistema de arquivos NFS compartilhado entre muitas instâncias Linux em várias AZs. O EBS fica preso a uma AZ (Multi-Attach só io1/io2, mesma AZ); instance store é local e efêmero; FSx for Windows é SMB para Windows.

</details>

### Questão 10

<sub>Domínio 1 · tópico [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)</sub>

Qual estratégia de recuperação de desastres tem o MENOR custo, aceitando o maior tempo de recuperação?

- **A)** Backup and Restore
- **B)** Warm Standby
- **C)** Pilot Light
- **D)** Multi-site active/active

<details>
<summary>Ver resposta</summary>

**Resposta: A**

Do mais barato e lento ao mais caro e rápido: **Backup and Restore** → Pilot Light → Warm Standby → Multi-site active/active.

</details>

### Questão 11

<sub>Domínio 2 · tópico [2.3](../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Uma empresa precisa armazenar a senha do banco de dados Amazon RDS de forma criptografada e trocá-la automaticamente a cada 30 dias, sem alterar o código a cada troca. Qual serviço atende MELHOR a esse requisito?

- **A)** AWS Secrets Manager
- **B)** AWS Key Management Service (AWS KMS)
- **C)** Amazon S3 com criptografia SSE-KMS
- **D)** AWS Systems Manager Parameter Store

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Secrets Manager** tem **rotação automática nativa** de credenciais do RDS. O Parameter Store guarda parâmetros e segredos, mas sem rotação nativa; o KMS gerencia chaves de criptografia, não segredos; o S3 não é um cofre de segredos.

</details>

### Questão 12

<sub>Domínio 3 · tópico [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)</sub>

Uma empresa transfere grandes volumes de dados todos os dias entre o datacenter e a AWS e precisa de uma conexão privada, dedicada, que não passe pela internet e tenha desempenho consistente. Qual serviço atende a esse requisito?

- **A)** AWS Site-to-Site VPN
- **B)** AWS Client VPN
- **C)** Amazon CloudFront
- **D)** AWS Direct Connect

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Direct Connect** é um link físico dedicado e privado, com banda estável. A Site-to-Site VPN passa pela internet (criptografada); a Client VPN é para usuários remotos; CloudFront é CDN.

</details>

### Questão 13

<sub>Domínio 3 · tópico [3.9](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)</sub>

Uma empresa quer acabar com o backup em fitas físicas, mas sem trocar o software de backup que já usa. Qual solução atende a esse requisito?

- **A)** AWS Storage Gateway com Tape Gateway
- **B)** AWS DataSync
- **C)** Amazon EFS
- **D)** AWS Snowball Edge

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Tape Gateway** apresenta fitas virtuais (VTL) ao software de backup e arquiva os dados no S3 Glacier. DataSync transfere arquivos; EFS é sistema de arquivos; Snowball Edge é transferência física pontual.

</details>

### Questão 14

<sub>Domínio 2 · tópico [2.3](../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Um usuário IAM recebe uma política que permite (Allow) apagar objetos de um bucket S3 e, por meio de um grupo, outra política que nega explicitamente (Deny) a mesma ação. O que acontece quando ele tenta apagar um objeto?

- **A)** O IAM retorna erro de política conflitante e bloqueia o usuário
- **B)** A ação é permitida, porque a política mais recente prevalece
- **C)** A ação é negada, porque um Deny explícito sempre prevalece
- **D)** A ação é permitida, porque políticas de usuário prevalecem sobre as de grupo

<details>
<summary>Ver resposta</summary>

**Resposta: C**

Na avaliação de políticas do IAM, tudo começa negado, um Allow libera e um **Deny explícito sempre vence**, independentemente de onde a política esteja anexada ou de quando foi criada.

</details>

### Questão 15

<sub>Domínio 2 · tópico [2.6](../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)</sub>

O auditor de uma empresa pediu o relatório SOC 2 da AWS para avaliar os controles do provedor. Onde a empresa obtém esse documento?

- **A)** AWS Artifact
- **B)** AWS Config
- **C)** AWS Audit Manager
- **D)** AWS Trusted Advisor

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **AWS Artifact** é o portal de autoatendimento para baixar relatórios de conformidade **da AWS** (SOC, PCI, ISO) e aceitar acordos como o BAA. O Audit Manager coleta evidências **da conta do cliente** para a auditoria dele.

</details>

### Questão 16

<sub>Domínio 4 · tópico [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)</sub>

Uma empresa usa Amazon EC2 em várias regiões, AWS Fargate e AWS Lambda, e quer um desconto com compromisso de 1 ano que se aplique automaticamente a todos esses serviços, mesmo se mudar a família de instâncias. Qual opção atende a esse requisito?

- **A)** EC2 Instance Savings Plans
- **B)** Compute Savings Plans
- **C)** Reserved Instances Standard
- **D)** Spot Instances

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Compute Savings Plans** vale para EC2 de qualquer família e região, Fargate e Lambda. O EC2 Instance Savings Plans fica preso a uma família numa região; RIs Standard ficam presas a um tipo de instância; Spot não tem compromisso nem cobre Lambda.

</details>

### Questão 17

<sub>Domínio 3 · tópico [3.11](../docs/03-tecnologia-e-servicos/11-analytics.md)</sub>

Um analista quer consultar com SQL padrão os logs armazenados em um bucket S3, sem provisionar servidores e pagando apenas pelos dados lidos em cada consulta. Qual serviço atende a esse requisito?

- **A)** Amazon Athena
- **B)** Amazon RDS
- **C)** Amazon Redshift
- **D)** Amazon EMR

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Athena** executa SQL serverless direto no S3 e cobra por dados escaneados. Redshift exige carregar dados num data warehouse; EMR exige clusters de big data; RDS é banco transacional.

</details>

### Questão 18

<sub>Domínio 1 · tópico [1.5](../docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md)</sub>

Na adoção de nuvem de uma empresa, um grupo cuida de treinar os funcionários, gerenciar a mudança cultural e redesenhar a estrutura organizacional. Qual perspectiva do AWS Cloud Adoption Framework (CAF) cobre essas atividades?

- **A)** Operations
- **B)** Governance
- **C)** Business
- **D)** People

<details>
<summary>Ver resposta</summary>

**Resposta: D**

**People** trata de cultura, treinamento, gestão da mudança e desenho organizacional. Business cuida do valor de negócio; Governance, de risco, orçamento e gestão do programa; Operations, de monitoramento e gestão de incidentes.

</details>

### Questão 19

<sub>Domínio 2 · tópico [2.2](../docs/02-seguranca-e-conformidade/02-usuario-root.md)</sub>

Qual destas tarefas só pode ser realizada pelo usuário root da conta AWS?

- **A)** Criar um usuário IAM com permissões de administrador
- **B)** Alterar o nome da conta
- **C)** Fechar uma conta AWS independente (standalone)
- **D)** Visualizar a fatura mensal

<details>
<summary>Ver resposta</summary>

**Resposta: C**

**Fechar uma conta standalone** está na lista oficial de tarefas exclusivas do root, junto com alterar o e-mail ou a senha do root, restaurar permissões de um administrador IAM e configurar MFA Delete. ⚠️ Pegadinha: segundo a documentação atual do IAM, **o nome da conta, contatos e regiões não exigem root**, e mudar o plano de suporte também saiu da lista. Criar usuários IAM e ver faturas (com permissão) podem ser feitos por identidades IAM.

</details>

### Questão 20

<sub>Domínio 2 · tópico [2.1](../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md)</sub>

Uma empresa usa o Amazon RDS for MySQL. Quem é responsável por aplicar os patches do mecanismo de banco de dados?

- **A)** Um parceiro da AWS Partner Network
- **B)** O cliente
- **C)** A AWS
- **D)** O administrador de banco de dados do cliente, manualmente

<details>
<summary>Ver resposta</summary>

**Resposta: C**

Em serviços gerenciados como o RDS, a **AWS** aplica os patches do SO e do mecanismo do banco (na janela de manutenção definida pelo cliente). O cliente cuida de usuários do banco, acesso de rede, criptografia e dados.

</details>

### Questão 21

<sub>Domínio 2 · tópico [2.3](../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Uma empresa com 30 contas AWS quer que os funcionários façam login uma única vez, usando o diretório corporativo, e acessem as contas permitidas para cada um. Qual serviço atende a essa necessidade?

- **A)** Usuários IAM criados em cada conta
- **B)** AWS IAM Identity Center
- **C)** Amazon Cognito
- **D)** AWS Secrets Manager

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **IAM Identity Center** oferece login único (SSO) para várias contas do Organizations e aplicações, integrado a diretórios externos. Cognito é para usuários finais de aplicações; criar usuários em cada conta não escala; Secrets Manager guarda segredos.

</details>

### Questão 22

<sub>Domínio 1 · tópico [1.5](../docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md)</sub>

Qual é a ordem correta das fases da jornada de transformação na nuvem descritas no AWS CAF?

- **A)** Envision, Align, Launch, Scale
- **B)** Plan, Build, Run, Optimize
- **C)** Assess, Mobilize, Migrate, Modernize
- **D)** Align, Envision, Scale, Launch

<details>
<summary>Ver resposta</summary>

**Resposta: A**

As quatro fases do CAF são **Envision** (enxergar oportunidades), **Align** (alinhar stakeholders e lacunas), **Launch** (pilotos em produção) e **Scale** (expandir). *Assess, Mobilize, Migrate* são fases de um programa de migração, não do CAF.

</details>

### Questão 23

<sub>Domínio 1 · tópico [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)</sub>

Uma aplicação adiciona instâncias automaticamente quando o tráfego aumenta à noite e as remove de madrugada, quando o tráfego cai. Qual conceito isso demonstra?

- **A)** Escalabilidade vertical
- **B)** Elasticidade
- **C)** Alta disponibilidade
- **D)** Tolerância a falhas

<details>
<summary>Ver resposta</summary>

**Resposta: B**

**Elasticidade** é crescer **e encolher** automaticamente conforme a carga. Escalabilidade vertical é aumentar o tamanho de uma instância; tolerância a falhas e alta disponibilidade tratam de continuar funcionando quando algo falha, não de acompanhar a demanda.

</details>

### Questão 24

<sub>Domínio 2 · tópico [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)</sub>

Uma empresa quer detectar automaticamente atividades maliciosas, como uma instância EC2 minerando criptomoedas ou se comunicando com IPs conhecidos de ataque, analisando CloudTrail, VPC Flow Logs e logs de DNS. Qual serviço atende a esse requisito?

- **A)** Amazon Macie
- **B)** Amazon Inspector
- **C)** AWS Artifact
- **D)** Amazon GuardDuty

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **GuardDuty** detecta ameaças ativas com ML e inteligência de ameaças a partir desses logs, sem agentes. O Inspector busca vulnerabilidades de software; o Macie, dados sensíveis no S3; o Artifact fornece relatórios de conformidade.

</details>

### Questão 25

<sub>Domínio 2 · tópico [2.1](../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md)</sub>

Segundo o modelo de responsabilidade compartilhada, quem é responsável por aplicar patches no sistema operacional convidado de uma instância Amazon EC2?

- **A)** A AWS
- **B)** O fornecedor do sistema operacional
- **C)** A AWS e o cliente, em partes iguais
- **D)** O cliente

<details>
<summary>Ver resposta</summary>

**Resposta: D**

No EC2 (IaaS), o **cliente** gerencia o SO convidado, os patches, as aplicações e os security groups. A AWS cuida do hardware, da rede física e do hipervisor.

</details>

### Questão 26

<sub>Domínio 2 · tópico [2.3](../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Um aplicativo móvel precisa permitir que clientes se cadastrem e façam login com suas contas do Google ou do Facebook. Qual serviço AWS deve ser usado?

- **A)** AWS IAM
- **B)** AWS Directory Service
- **C)** Amazon Cognito
- **D)** AWS IAM Identity Center

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **Cognito** (user pools) oferece cadastro, login e login social para **usuários finais** de aplicações web e mobile. Identity Center e Directory Service são para funcionários; usuários IAM não são para clientes de uma aplicação.

</details>

### Questão 27

<sub>Domínio 1 · tópico [1.6](../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)</sub>

Uma empresa precisa sair do datacenter em 3 meses e quer mover centenas de VMs para o Amazon EC2 sem nenhuma alteração. Qual estratégia de migração é a mais adequada?

- **A)** Rehost
- **B)** Replatform
- **C)** Retain
- **D)** Refactor

<details>
<summary>Ver resposta</summary>

**Resposta: A**

**Rehost** (lift-and-shift) é a estratégia mais rápida e move as VMs sem mudanças, normalmente com o AWS Application Migration Service. Retain manteria as aplicações on-premises; Replatform e Refactor exigem alterações.

</details>

### Questão 28

<sub>Domínio 2 · tópico [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)</sub>

O time de segurança precisa descobrir quais buckets S3 contêm dados pessoais, como números de cartão de crédito e documentos de identidade. Qual serviço deve ser usado?

- **A)** Amazon Detective
- **B)** AWS Shield
- **C)** Amazon Macie
- **D)** Amazon Inspector

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **Macie** usa ML e padrões para descobrir dados sensíveis (PII) no **S3**. O Inspector busca CVEs em EC2, ECR e Lambda; o Detective investiga a causa raiz de achados; o Shield protege contra DDoS.

</details>

### Questão 29

<sub>Domínio 2 · tópico [2.7](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)</sub>

O time de segurança precisa saber como estavam configuradas as regras de um security group na semana passada e ser alertado sempre que algum security group permitir SSH a partir de qualquer IP. Qual serviço atende a esses requisitos?

- **A)** AWS CloudTrail
- **B)** AWS Config
- **C)** Amazon Inspector
- **D)** Amazon Macie

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **AWS Config** guarda o histórico de configuração dos recursos e avalia continuamente a conformidade com regras (ex.: `restricted-ssh`). O CloudTrail mostra quem fez a mudança, mas não avalia regras; Inspector busca vulnerabilidades; Macie busca dados sensíveis no S3.

</details>

### Questão 30

<sub>Domínio 1 · tópico [1.6](../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)</sub>

Uma empresa quer migrar seu banco de dados MySQL de um servidor próprio para o Amazon RDS, reduzindo a administração, sem alterar o código da aplicação. Qual estratégia de migração é essa?

- **A)** Refactor
- **B)** Replatform
- **C)** Repurchase
- **D)** Rehost

<details>
<summary>Ver resposta</summary>

**Resposta: B**

**Replatform** (lift-tinker-and-shift) faz pequenas otimizações, como trocar o banco autogerenciado por um serviço gerenciado, sem reescrever a aplicação. Rehost move sem mudanças; Refactor reescreve para cloud-native; Repurchase troca por outro produto (geralmente SaaS).

</details>

### Questão 31

<sub>Domínio 1 · tópico [1.4](../docs/01-conceitos-de-nuvem/04-well-architected-framework.md)</sub>

Um arquiteto quer revisar uma carga de trabalho existente contra as boas práticas dos pilares da AWS e gerar um plano de melhorias, sem custo. Qual serviço ele deve usar?

- **A)** AWS Security Hub
- **B)** AWS Trusted Advisor
- **C)** AWS Well-Architected Tool
- **D)** AWS Config

<details>
<summary>Ver resposta</summary>

**Resposta: C**

A **Well-Architected Tool** revisa uma carga de trabalho contra os 6 pilares e gera um plano de melhorias. O Trusted Advisor faz verificações automáticas da conta; o Config avalia a configuração de recursos contra regras; o Security Hub centraliza achados de segurança.

</details>

### Questão 32

<sub>Domínio 2 · tópico [2.4](../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)</sub>

Uma empresa usa o AWS Organizations e quer impedir que qualquer conta da OU de desenvolvimento use a região sa-east-1, inclusive administradores dessas contas. O que deve ser usado?

- **A)** Uma regra do AWS Config em cada conta
- **B)** Uma bucket policy do S3
- **C)** Uma Service Control Policy (SCP) aplicada à OU
- **D)** Uma política IAM anexada a cada usuário administrador

<details>
<summary>Ver resposta</summary>

**Resposta: C**

A **SCP** define o limite máximo de permissões de todas as contas de uma OU e vale até para administradores. Políticas IAM podem ser alteradas pelos próprios administradores; o Config detecta, mas não impede; bucket policy só controla um bucket.

</details>

### Questão 33

<sub>Domínio 1 · tópico [1.1](../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md)</sub>

Uma empresa precisa manter dados de clientes em seu datacenter por exigência regulatória, mas quer usar a AWS para o restante das aplicações, com as duas partes conectadas. Qual modelo de implantação atende a esse cenário?

- **A)** On-premises (nuvem privada)
- **B)** Híbrido
- **C)** Nuvem pública (all-in)
- **D)** Software como serviço (SaaS)

<details>
<summary>Ver resposta</summary>

**Resposta: B**

Parte on-premises e parte na nuvem, conectadas (VPN, Direct Connect, Outposts), é o modelo **híbrido**. SaaS é um modelo de *serviço*, não de implantação.

</details>

### Questão 34

<sub>Domínio 2 · tópico [2.3](../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Uma aplicação executada em instâncias EC2 precisa ler objetos de um bucket S3. Qual é a forma MAIS segura de conceder esse acesso?

- **A)** Tornar o bucket público
- **B)** Anexar uma IAM role com as permissões necessárias às instâncias
- **C)** Usar as credenciais do usuário root na aplicação
- **D)** Guardar access keys de um usuário IAM no código da aplicação

<details>
<summary>Ver resposta</summary>

**Resposta: B**

Uma **IAM role** (via instance profile) entrega credenciais **temporárias** e rotacionadas automaticamente. Access keys no código podem vazar; bucket público expõe os dados a todos; o root nunca deve ser usado em aplicações.

</details>

### Questão 35

<sub>Domínio 3 · tópico [3.8](../docs/03-tecnologia-e-servicos/08-s3.md)</sub>

Por exigência regulatória, uma empresa precisa guardar registros por 7 anos. Eles quase nunca são lidos e uma recuperação de até 48 horas é aceitável. Qual é a opção de MENOR custo?

- **A)** S3 Standard-IA
- **B)** S3 Intelligent-Tiering
- **C)** S3 Glacier Instant Retrieval
- **D)** S3 Glacier Deep Archive

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Glacier Deep Archive** é a classe mais barata, para retenção de longo prazo, com recuperação em até 12 h (padrão) ou 48 h (bulk). Instant Retrieval e Standard-IA custam mais por oferecerem acesso em milissegundos.

</details>

### Questão 36

<sub>Domínio 3 · tópico [3.5](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)</sub>

Uma empresa já usa Kubernetes on-premises e quer migrar seus manifestos e ferramentas para um serviço gerenciado na AWS, com o plano de controle operado pela AWS. Qual serviço atende melhor?

- **A)** AWS Batch
- **B)** AWS Elastic Beanstalk
- **C)** Amazon ECS
- **D)** Amazon EKS

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **EKS** é Kubernetes gerenciado e preserva manifestos e ferramentas do ecossistema. O ECS é o orquestrador próprio da AWS (não Kubernetes); Beanstalk é PaaS para aplicações; Batch é para jobs em lote.

</details>

### Questão 37

<sub>Domínio 3 · tópico [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)</sub>

Uma empresa quer que seu banco Amazon RDS continue disponível mesmo se uma zona de disponibilidade inteira falhar, com failover automático. Qual recurso deve ser habilitado?

- **A)** Snapshots manuais diários
- **B)** Read replicas na mesma região
- **C)** Amazon ElastiCache na frente do banco
- **D)** RDS Multi-AZ

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Multi-AZ** mantém um standby síncrono em outra AZ com **failover automático** — o objetivo é disponibilidade. Read replicas escalam leitura; snapshots exigem restauração manual; ElastiCache é cache, não alta disponibilidade do banco.

</details>

### Questão 38

<sub>Domínio 4 · tópico [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)</sub>

Uma empresa executa renderizações de vídeo em lote que podem ser interrompidas e retomadas depois, sem prazo rígido. Qual opção de compra do EC2 oferece o MENOR custo?

- **A)** Spot Instances
- **B)** On-Demand Instances
- **C)** Reserved Instances Standard de 3 anos
- **D)** Dedicated Hosts

<details>
<summary>Ver resposta</summary>

**Resposta: A**

As **Spot Instances** oferecem até 90% de desconto para cargas tolerantes a interrupção (aviso de 2 minutos). On-Demand é mais caro; Dedicated Hosts são os mais caros; RIs exigem compromisso de 1 ou 3 anos e fazem sentido para cargas estáveis.

</details>

### Questão 39

<sub>Domínio 2 · tópico [2.1](../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) · **múltipla resposta**</sub>

Quais DUAS tarefas são de responsabilidade do CLIENTE segundo o modelo de responsabilidade compartilhada? (Escolha DUAS.)

- **A)** Destruir os discos físicos ao fim da vida útil
- **B)** Ativar a criptografia dos dados armazenados no Amazon S3
- **C)** Configurar os security groups das instâncias
- **D)** Garantir a segurança física dos datacenters
- **E)** Manter o hipervisor das instâncias EC2

<details>
<summary>Ver resposta</summary>

**Resposta: B, C**

Security groups e criptografia dos dados são segurança **na** nuvem (cliente). Segurança física, hipervisor e descarte de discos são segurança **da** nuvem (AWS).

</details>

### Questão 40

<sub>Domínio 1 · tópico [1.4](../docs/01-conceitos-de-nuvem/04-well-architected-framework.md)</sub>

Uma empresa passou a usar instâncias com processadores AWS Graviton e a desligar recursos ociosos com o objetivo de reduzir o impacto ambiental das suas cargas. Qual pilar do Well-Architected Framework orienta essas práticas?

- **A)** Segurança
- **B)** Sustentabilidade
- **C)** Confiabilidade
- **D)** Excelência operacional

<details>
<summary>Ver resposta</summary>

**Resposta: B**

Reduzir impacto ambiental (maximizar utilização, hardware mais eficiente como Graviton) é o pilar **Sustentabilidade**, o sexto e mais recente pilar. O objetivo declarado na questão é ambiental, não de segurança, resiliência ou operação.

</details>

### Questão 41

<sub>Domínio 1 · tópico [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)</sub>

Um time quer que a falha no serviço de processamento de pedidos não derrube o site da loja, e que picos de pedidos sejam absorvidos sem perda. Qual abordagem de arquitetura atende melhor a esse objetivo?

- **A)** Usar um único banco de dados para guardar sessões e pedidos
- **B)** Desacoplar os componentes com uma fila do Amazon SQS
- **C)** Colocar o site e o processamento na mesma instância EC2
- **D)** Aumentar o tamanho da instância do site (escala vertical)

<details>
<summary>Ver resposta</summary>

**Resposta: B**

**Acoplamento fraco** com uma fila (SQS) faz o site apenas enfileirar pedidos; se o processamento falhar ou ficar lento, as mensagens esperam na fila. As demais opções aumentam o acoplamento ou não resolvem a falha de um componente.

</details>

### Questão 42

<sub>Domínio 3 · tópico [3.13](../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)</sub>

Quando um pedido é criado, a mesma mensagem precisa ser entregue a três sistemas diferentes e também enviada por e-mail ao time financeiro. Qual serviço deve receber a publicação do evento?

- **A)** Amazon SNS
- **B)** Amazon SQS
- **C)** AWS Step Functions
- **D)** Amazon Kinesis Data Streams

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **SNS** é pub/sub: publica num tópico e empurra a mensagem para vários assinantes (filas SQS, Lambda, HTTP, e-mail). Uma fila SQS é consumida por um processador; Step Functions orquestra etapas; Kinesis é para streaming em tempo real.

</details>

### Questão 43

<sub>Domínio 1 · tópico [1.2](../docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md)</sub>

Uma varejista comprava servidores extras todo ano para aguentar a Black Friday, e eles ficavam ociosos no resto do tempo. Ao migrar para a AWS, a empresa passou a provisionar capacidade conforme a demanda real. Qual vantagem da computação em nuvem descreve esse ganho?

- **A)** Beneficiar-se de economias de escala massivas
- **B)** Parar de adivinhar a capacidade
- **C)** Tornar-se global em minutos
- **D)** Trocar despesa variável por despesa de capital

<details>
<summary>Ver resposta</summary>

**Resposta: B**

Dimensionar pela demanda real, sem comprar para o pico, é **parar de adivinhar a capacidade**. Economias de escala tratam de preços menores pelo volume da AWS; ficar global trata de várias regiões; e a troca correta é de despesa de **capital** por despesa **variável** (a alternativa inverte a ordem).

</details>

### Questão 44

<sub>Domínio 4 · tópico [4.3](../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) · **múltipla resposta**</sub>

Quais DOIS tipos de transferência de dados são GRATUITOS na AWS? (Escolha DUAS.)

- **A)** Transferência de uma origem na AWS (como o S3) para o Amazon CloudFront
- **B)** Saída de dados da AWS para a internet
- **C)** Transferência entre zonas de disponibilidade da mesma região
- **D)** Transferência entre regiões AWS
- **E)** Entrada de dados da internet para a AWS

<details>
<summary>Ver resposta</summary>

**Resposta: A, E**

A **entrada** de dados da internet e a transferência de **origens AWS para o CloudFront** são gratuitas. A saída para a internet, a transferência entre regiões e a transferência entre AZs são cobradas.

</details>

### Questão 45

<sub>Domínio 2 · tópico [2.7](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)</sub>

Uma instância EC2 de produção foi encerrada e o time precisa descobrir qual usuário fez isso, quando e de qual endereço IP. Qual serviço fornece essa informação?

- **A)** VPC Flow Logs
- **B)** AWS Config
- **C)** AWS CloudTrail
- **D)** Amazon CloudWatch

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **CloudTrail** registra as chamadas de API (quem, o quê, quando, de onde). O CloudWatch monitora métricas e logs de desempenho; o Config registra o estado da configuração; os Flow Logs registram tráfego de rede, não ações de API.

</details>

### Questão 46

<sub>Domínio 3 · tópico [3.2](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md)</sub>

Um hospital precisa processar dados localmente, no próprio datacenter, por exigência de residência de dados, mas quer usar as mesmas APIs, ferramentas e serviços da AWS. Qual solução atende a esse requisito?

- **A)** AWS Local Zones
- **B)** AWS Outposts
- **C)** AWS Wavelength
- **D)** Amazon CloudFront

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Outposts** instala racks ou servidores da AWS **no datacenter do cliente**. Local Zones ficam em cidades e são operadas pela AWS; Wavelength fica dentro de redes 5G de operadoras; CloudFront é uma CDN.

</details>

### Questão 47

<sub>Domínio 2 · tópico [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)</sub>

Uma loja virtual atrás de um Application Load Balancer está sofrendo tentativas de SQL injection e cross-site scripting (XSS). Qual serviço deve ser usado para bloquear essas requisições?

- **A)** AWS Shield Standard
- **B)** AWS WAF
- **C)** Security groups
- **D)** Amazon GuardDuty

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **WAF** é um firewall de camada 7 que filtra requisições web (SQL injection, XSS, rate limiting) e se associa ao ALB. O Shield protege contra DDoS; security groups filtram por IP/porta; o GuardDuty detecta ameaças, mas não bloqueia requisições.

</details>

### Questão 48

<sub>Domínio 3 · tópico [3.8](../docs/03-tecnologia-e-servicos/08-s3.md)</sub>

Uma empresa armazena milhões de objetos no Amazon S3 com padrão de acesso imprevisível: alguns são lidos com frequência e outros ficam meses sem acesso. Qual classe de armazenamento otimiza o custo automaticamente sem afetar o desempenho?

- **A)** S3 Glacier Deep Archive
- **B)** S3 Intelligent-Tiering
- **C)** S3 One Zone-IA
- **D)** S3 Standard

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Intelligent-Tiering** move os objetos entre camadas automaticamente conforme o acesso, sem taxa de recuperação nas camadas automáticas (cobra só uma pequena taxa de monitoramento por objeto). Standard não otimiza custo; One Zone-IA cobra recuperação e guarda em uma AZ; Deep Archive tem recuperação de horas.

</details>

### Questão 49

<sub>Domínio 3 · tópico [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)</sub>

Uma empresa de mídia quer reduzir a latência na entrega de vídeos e imagens para usuários no mundo todo, fazendo cache do conteúdo perto deles. Qual serviço deve ser usado?

- **A)** AWS Direct Connect
- **B)** Amazon Route 53
- **C)** Amazon CloudFront
- **D)** AWS Global Accelerator

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **CloudFront** é a CDN da AWS e faz **cache** nas edge locations. O Global Accelerator otimiza o caminho de rede TCP/UDP, mas **não faz cache**; o Route 53 é DNS; o Direct Connect liga datacenters à AWS.

</details>

### Questão 50

<sub>Domínio 3 · tópico [3.2](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) · **múltipla resposta**</sub>

Quais DOIS fatores uma empresa deve considerar ao escolher a região AWS para uma nova aplicação? (Escolha DUAS.)

- **A)** Requisitos de conformidade e residência de dados
- **B)** O número de buckets S3 já existentes
- **C)** Proximidade dos clientes para reduzir a latência
- **D)** A quantidade de usuários IAM da conta
- **E)** A data de criação da conta AWS

<details>
<summary>Ver resposta</summary>

**Resposta: A, C**

Os quatro fatores clássicos são **conformidade/residência de dados**, **latência para os clientes**, **serviços disponíveis na região** e **preço**. Usuários IAM, idade da conta e buckets existentes não influenciam a escolha.

</details>

### Questão 51

<sub>Domínio 3 · tópico [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)</sub>

Instâncias EC2 em uma subnet privada precisam baixar atualizações de segurança da internet, mas não podem receber conexões iniciadas de fora. O que deve ser configurado?

- **A)** Um VPC peering com a VPC padrão
- **B)** Um gateway VPC endpoint para o Amazon S3
- **C)** Um Internet Gateway com rota direta a partir da subnet privada
- **D)** Um NAT Gateway em uma subnet pública, com rota a partir da subnet privada

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **NAT Gateway** permite apenas a **saída** para a internet a partir de subnets privadas. Uma rota direta para o Internet Gateway tornaria a subnet pública; o gateway endpoint só acessa S3/DynamoDB; peering liga VPCs, não dá acesso à internet.

</details>

### Questão 52

<sub>Domínio 2 · tópico [2.5](../docs/02-seguranca-e-conformidade/05-criptografia.md)</sub>

Uma instituição financeira precisa, por regulação, de módulos de segurança de hardware (HSM) dedicados exclusivamente a ela, validados FIPS 140 nível 3, com controle exclusivo das chaves. Qual serviço atende a esse requisito?

- **A)** AWS Certificate Manager (ACM)
- **B)** AWS CloudHSM
- **C)** AWS Secrets Manager
- **D)** AWS Key Management Service (AWS KMS) com chaves gerenciadas pela AWS

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **CloudHSM** oferece HSM **single-tenant**, com chaves sob controle exclusivo do cliente. O KMS usa HSMs compartilhados gerenciados pela AWS; o ACM gerencia certificados TLS; o Secrets Manager guarda segredos.

</details>

### Questão 53

<sub>Domínio 2 · tópico [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)</sub>

Uma empresa quer varrer continuamente suas instâncias EC2 e as imagens de contêiner no Amazon ECR em busca de vulnerabilidades de software conhecidas (CVEs). Qual serviço deve ser usado?

- **A)** Amazon Inspector
- **B)** AWS Config
- **C)** Amazon GuardDuty
- **D)** AWS Trusted Advisor

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Inspector** avalia vulnerabilidades de software e exposição de rede em EC2, ECR e Lambda. O GuardDuty detecta ameaças em andamento; o Trusted Advisor dá recomendações de boas práticas; o Config avalia configurações, não CVEs.

</details>

### Questão 54

<sub>Domínio 3 · tópico [3.3](../docs/03-tecnologia-e-servicos/03-ec2.md)</sub>

Uma aplicação grava arquivos temporários de cache no instance store de uma instância EC2. O que acontece com esses dados quando a instância é PARADA (stop)?

- **A)** Os dados são perdidos
- **B)** Os dados são preservados e ficam disponíveis quando a instância voltar
- **C)** Os dados são copiados automaticamente para um snapshot do EBS
- **D)** Os dados são movidos automaticamente para o Amazon S3

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **instance store** é armazenamento local **efêmero**: os dados se perdem ao parar, hibernar ou encerrar a instância (sobrevivem só ao reboot). Para persistência, use EBS.

</details>

### Questão 55

<sub>Domínio 3 · tópico [3.3](../docs/03-tecnologia-e-servicos/03-ec2.md)</sub>

Uma empresa vai executar um banco de dados em memória de alto desempenho no Amazon EC2. Qual família de instâncias é a mais indicada?

- **A)** Otimizada para memória (por exemplo, R ou X)
- **B)** Uso geral com desempenho expansível (por exemplo, T)
- **C)** Computação acelerada (por exemplo, P ou G)
- **D)** Otimizada para computação (por exemplo, C)

<details>
<summary>Ver resposta</summary>

**Resposta: A**

Bancos em memória e análises em tempo real usam instâncias **otimizadas para memória** (R, X). C é para uso intenso de CPU; T é para cargas leves com picos; P e G são para GPU/ML.

</details>

### Questão 56

<sub>Domínio 1 · tópico [1.1](../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md)</sub>

Um desenvolvedor quer apenas enviar o código da sua aplicação web Java e deixar a AWS cuidar de provisionamento, balanceamento de carga e escalonamento. Qual modelo de serviço e qual serviço AWS atendem a esse cenário?

- **A)** SaaS, com o Amazon WorkSpaces
- **B)** IaaS, com o Amazon EC2
- **C)** PaaS, com o AWS Elastic Beanstalk
- **D)** IaaS, com o Amazon VPC

<details>
<summary>Ver resposta</summary>

**Resposta: C**

No **PaaS** o cliente entrega o código e a plataforma gerencia o resto; o **Elastic Beanstalk** é o exemplo clássico. EC2 e VPC são IaaS (o cliente gerencia o SO e a rede); WorkSpaces é um desktop virtual pronto.

</details>

### Questão 57

<sub>Domínio 3 · tópico [3.17](../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)</sub>

Uma empresa quer migrar um banco Oracle on-premises para o Amazon Aurora PostgreSQL, mantendo o banco de origem em operação durante a migração. Quais serviços devem ser usados?

- **A)** Somente o AWS Application Migration Service
- **B)** AWS DataSync e AWS Transfer Family
- **C)** AWS Snowball Edge e Amazon S3
- **D)** AWS Schema Conversion Tool (SCT) e AWS Database Migration Service (DMS)

<details>
<summary>Ver resposta</summary>

**Resposta: D**

Migração **heterogênea**: o **SCT** converte o schema e o código do Oracle para PostgreSQL, e o **DMS** move os dados com replicação contínua (CDC). O Application Migration Service migra servidores inteiros; DataSync, Transfer Family e Snowball transferem arquivos.

</details>

### Questão 58

<sub>Domínio 1 · tópico [1.4](../docs/01-conceitos-de-nuvem/04-well-architected-framework.md)</sub>

Uma empresa implanta sua aplicação em várias zonas de disponibilidade e configura recuperação automática de falhas. Qual pilar do AWS Well-Architected Framework ela está aplicando?

- **A)** Eficiência de performance
- **B)** Excelência operacional
- **C)** Otimização de custos
- **D)** Confiabilidade

<details>
<summary>Ver resposta</summary>

**Resposta: D**

Recuperar-se automaticamente de falhas e usar várias AZs são princípios do pilar **Confiabilidade**. Excelência operacional trata de operar e melhorar processos; eficiência de performance, de usar os recursos certos; otimização de custos, de evitar gastos desnecessários.

</details>

### Questão 59

<sub>Domínio 3 · tópico [3.12](../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)</sub>

Uma seguradora recebe milhares de formulários escaneados e quer extrair automaticamente o texto, os campos (chave-valor) e as tabelas. Qual serviço deve ser usado?

- **A)** Amazon Transcribe
- **B)** Amazon Textract
- **C)** Amazon Rekognition
- **D)** Amazon Comprehend

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Textract** extrai texto, formulários e tabelas de documentos digitalizados. O Rekognition analisa imagens e vídeos (rostos, objetos); o Comprehend analisa texto já extraído (sentimento, entidades); o Transcribe converte fala em texto.

</details>

### Questão 60

<sub>Domínio 3 · tópico [3.5](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)</sub>

Um processamento de vídeo leva cerca de 2 horas por arquivo. A empresa quer executá-lo em contêineres, sem provisionar nem gerenciar servidores. Qual opção é a mais adequada?

- **A)** Amazon EC2 com Auto Scaling
- **B)** Amazon Lightsail
- **C)** AWS Lambda
- **D)** Amazon ECS com AWS Fargate

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Fargate** executa contêineres sem servidores e sem limite de duração. O Lambda tem limite de **15 minutos** por execução; EC2 e Lightsail exigem gerenciar servidores.

</details>

### Questão 61

<sub>Domínio 4 · tópico [4.5](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)</sub>

Uma startup quer o plano de AWS Support pago de MENOR custo, que começa em US$ 29 por mês por conta e oferece resposta em até 30 minutos para casos críticos. Qual plano atende a esse requisito?

- **A)** Basic
- **B)** AWS Business Support+
- **C)** AWS Unified Operations
- **D)** AWS Enterprise Support

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Business Support+** é o plano pago de entrada do modelo atual (task 4.3 do exam guide): a partir de US$ 29/mês por conta, com resposta de 30 minutos para casos críticos. O Basic é gratuito e não tem suporte técnico; o Enterprise começa em US$ 5.000/mês (15 min); o Unified Operations, em US$ 50.000/mês (5 min).

</details>

### Questão 62

<sub>Domínio 4 · tópico [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)</sub>

O gerente financeiro quer ser notificado por e-mail quando o gasto PREVISTO do mês ultrapassar US$ 5.000. Qual serviço deve ser configurado?

- **A)** AWS Trusted Advisor
- **B)** AWS Cost Explorer
- **C)** AWS Pricing Calculator
- **D)** AWS Budgets

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Budgets** dispara alertas quando o gasto real **ou previsto** passa de um limite (e pode até executar ações). O Cost Explorer analisa e prevê, mas não alerta por limite; a Pricing Calculator estima antes de usar; o Trusted Advisor dá recomendações.

</details>

### Questão 63

<sub>Domínio 2 · tópico [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)</sub>

Uma empresa de jogos quer proteção ampliada contra DDoS, acesso 24/7 a uma equipe especializada durante ataques e créditos pelos custos de escalonamento causados por ataques. Qual serviço atende a esses requisitos?

- **A)** AWS Shield Advanced
- **B)** AWS Firewall Manager
- **C)** AWS WAF
- **D)** AWS Shield Standard

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Shield Advanced** inclui o Shield Response Team (SRT) 24/7 e **proteção de custo**. O Shield Standard é gratuito e automático, mas não tem esses extras; o WAF filtra requisições web; o Firewall Manager gerencia regras centralmente.

</details>

### Questão 64

<sub>Domínio 3 · tópico [3.4](../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)</sub>

Uma aplicação de microsserviços precisa enviar requisições com caminho /api para um grupo de contêineres e /imagens para outro, usando o mesmo endereço. Qual load balancer deve ser usado?

- **A)** Network Load Balancer
- **B)** Application Load Balancer
- **C)** Classic Load Balancer
- **D)** Gateway Load Balancer

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **ALB** opera na camada 7 e roteia por caminho, host e cabeçalho. O NLB opera na camada 4 (TCP/UDP); o GWLB encaminha tráfego para appliances de segurança; o Classic é legado e não recomendado.

</details>

### Questão 65

<sub>Domínio 1 · tópico [1.7](../docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md)</sub>

A diretoria de uma empresa pede uma estimativa do custo total de propriedade (TCO) de mover todo o ambiente on-premises para a AWS, para montar o caso de negócio da migração. Qual serviço ajuda nisso?

- **A)** AWS Budgets
- **B)** AWS Migration Hub
- **C)** AWS Cost Explorer
- **D)** Migration Evaluator

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Migration Evaluator** analisa o ambiente atual e monta o caso de negócio (TCO) da migração. Cost Explorer e Budgets trabalham com gastos de recursos que já estão na AWS; o Migration Hub acompanha o progresso das migrações.

</details>

---

## Gabarito

| Questão | Resposta | Domínio | Tópico |
|---|---|---|---|
| 1 | **D** | 4 | [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| 2 | **A** | 3 | [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) |
| 3 | **A, B** | 1 | [1.2](../docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) |
| 4 | **C, D** | 2 | [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) |
| 5 | **D** | 4 | [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| 6 | **C** | 1 | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| 7 | **C** | 3 | [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) |
| 8 | **A** | 4 | [4.5](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) |
| 9 | **A** | 3 | [3.9](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| 10 | **A** | 1 | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| 11 | **A** | 2 | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| 12 | **D** | 3 | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| 13 | **A** | 3 | [3.9](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| 14 | **C** | 2 | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| 15 | **A** | 2 | [2.6](../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md) |
| 16 | **B** | 4 | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 17 | **A** | 3 | [3.11](../docs/03-tecnologia-e-servicos/11-analytics.md) |
| 18 | **D** | 1 | [1.5](../docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md) |
| 19 | **C** | 2 | [2.2](../docs/02-seguranca-e-conformidade/02-usuario-root.md) |
| 20 | **C** | 2 | [2.1](../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) |
| 21 | **B** | 2 | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| 22 | **A** | 1 | [1.5](../docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md) |
| 23 | **B** | 1 | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| 24 | **D** | 2 | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| 25 | **D** | 2 | [2.1](../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) |
| 26 | **C** | 2 | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| 27 | **A** | 1 | [1.6](../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md) |
| 28 | **C** | 2 | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| 29 | **B** | 2 | [2.7](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| 30 | **B** | 1 | [1.6](../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md) |
| 31 | **C** | 1 | [1.4](../docs/01-conceitos-de-nuvem/04-well-architected-framework.md) |
| 32 | **C** | 2 | [2.4](../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md) |
| 33 | **B** | 1 | [1.1](../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) |
| 34 | **B** | 2 | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| 35 | **D** | 3 | [3.8](../docs/03-tecnologia-e-servicos/08-s3.md) |
| 36 | **D** | 3 | [3.5](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) |
| 37 | **D** | 3 | [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) |
| 38 | **A** | 4 | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 39 | **B, C** | 2 | [2.1](../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) |
| 40 | **B** | 1 | [1.4](../docs/01-conceitos-de-nuvem/04-well-architected-framework.md) |
| 41 | **B** | 1 | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| 42 | **A** | 3 | [3.13](../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) |
| 43 | **B** | 1 | [1.2](../docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) |
| 44 | **A, E** | 4 | [4.3](../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| 45 | **C** | 2 | [2.7](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| 46 | **B** | 3 | [3.2](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| 47 | **B** | 2 | [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) |
| 48 | **B** | 3 | [3.8](../docs/03-tecnologia-e-servicos/08-s3.md) |
| 49 | **C** | 3 | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| 50 | **A, C** | 3 | [3.2](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| 51 | **D** | 3 | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| 52 | **B** | 2 | [2.5](../docs/02-seguranca-e-conformidade/05-criptografia.md) |
| 53 | **A** | 2 | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| 54 | **A** | 3 | [3.3](../docs/03-tecnologia-e-servicos/03-ec2.md) |
| 55 | **A** | 3 | [3.3](../docs/03-tecnologia-e-servicos/03-ec2.md) |
| 56 | **C** | 1 | [1.1](../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) |
| 57 | **D** | 3 | [3.17](../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) |
| 58 | **D** | 1 | [1.4](../docs/01-conceitos-de-nuvem/04-well-architected-framework.md) |
| 59 | **B** | 3 | [3.12](../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md) |
| 60 | **D** | 3 | [3.5](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) |
| 61 | **B** | 4 | [4.5](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) |
| 62 | **D** | 4 | [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| 63 | **A** | 2 | [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) |
| 64 | **B** | 3 | [3.4](../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) |
| 65 | **D** | 1 | [1.7](../docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md) |

## Folha de correção

| Domínio | Peso | Questões | Acertos | % |
|---|---|---|---|---|
| Domínio 1 — Conceitos de Nuvem | 24% | 16 |  |  |
| Domínio 2 — Segurança e Conformidade | 30% | 20 |  |  |
| Domínio 3 — Tecnologia e Serviços de Nuvem | 34% | 21 |  |  |
| Domínio 4 — Cobrança, Preços e Suporte | 12% | 8 |  |  |
| **Total** | 100% | 65 |  |  |

> Domínio com menos de 70%? Volte aos tópicos dele e às [questões por domínio](questoes/README.md).
