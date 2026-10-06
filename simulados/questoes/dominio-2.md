# ❓ Questões — Domínio 2 — Segurança e Conformidade (30%)

20 questões no formato da prova, em ordem de tópico. Responda antes de abrir "Ver resposta".

⬅️ [Todas as questões por domínio](README.md)

---

### Questão 1

<sub>Domínio 2 · tópico [2.1](../../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md)</sub>

Segundo o modelo de responsabilidade compartilhada, quem é responsável por aplicar patches no sistema operacional convidado de uma instância Amazon EC2?

- **A)** O cliente
- **B)** A AWS e o cliente, em partes iguais
- **C)** A AWS
- **D)** O fornecedor do sistema operacional

<details>
<summary>Ver resposta</summary>

**Resposta: A**

No EC2 (IaaS), o **cliente** gerencia o SO convidado, os patches, as aplicações e os security groups. A AWS cuida do hardware, da rede física e do hipervisor.

</details>

### Questão 2

<sub>Domínio 2 · tópico [2.1](../../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md)</sub>

Uma empresa usa o Amazon RDS for MySQL. Quem é responsável por aplicar os patches do mecanismo de banco de dados?

- **A)** A AWS
- **B)** Um parceiro da AWS Partner Network
- **C)** O cliente
- **D)** O administrador de banco de dados do cliente, manualmente

<details>
<summary>Ver resposta</summary>

**Resposta: A**

Em serviços gerenciados como o RDS, a **AWS** aplica os patches do SO e do mecanismo do banco (na janela de manutenção definida pelo cliente). O cliente cuida de usuários do banco, acesso de rede, criptografia e dados.

</details>

### Questão 3

<sub>Domínio 2 · tópico [2.1](../../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) · **múltipla resposta**</sub>

Quais DUAS tarefas são de responsabilidade do CLIENTE segundo o modelo de responsabilidade compartilhada? (Escolha DUAS.)

- **A)** Manter o hipervisor das instâncias EC2
- **B)** Destruir os discos físicos ao fim da vida útil
- **C)** Garantir a segurança física dos datacenters
- **D)** Configurar os security groups das instâncias
- **E)** Ativar a criptografia dos dados armazenados no Amazon S3

<details>
<summary>Ver resposta</summary>

**Resposta: D, E**

Security groups e criptografia dos dados são segurança **na** nuvem (cliente). Segurança física, hipervisor e descarte de discos são segurança **da** nuvem (AWS).

</details>

### Questão 4

<sub>Domínio 2 · tópico [2.2](../../docs/02-seguranca-e-conformidade/02-usuario-root.md)</sub>

Qual destas tarefas só pode ser realizada pelo usuário root da conta AWS?

- **A)** Visualizar a fatura mensal
- **B)** Fechar uma conta AWS independente (standalone)
- **C)** Criar um usuário IAM com permissões de administrador
- **D)** Alterar o nome da conta

<details>
<summary>Ver resposta</summary>

**Resposta: B**

**Fechar uma conta standalone** está na lista oficial de tarefas exclusivas do root, junto com alterar o e-mail ou a senha do root, restaurar permissões de um administrador IAM e configurar MFA Delete. ⚠️ Pegadinha: segundo a documentação atual do IAM, **o nome da conta, contatos e regiões não exigem root**, e mudar o plano de suporte também saiu da lista. Criar usuários IAM e ver faturas (com permissão) podem ser feitos por identidades IAM.

</details>

### Questão 5

<sub>Domínio 2 · tópico [2.3](../../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Uma aplicação executada em instâncias EC2 precisa ler objetos de um bucket S3. Qual é a forma MAIS segura de conceder esse acesso?

- **A)** Anexar uma IAM role com as permissões necessárias às instâncias
- **B)** Guardar access keys de um usuário IAM no código da aplicação
- **C)** Usar as credenciais do usuário root na aplicação
- **D)** Tornar o bucket público

<details>
<summary>Ver resposta</summary>

**Resposta: A**

Uma **IAM role** (via instance profile) entrega credenciais **temporárias** e rotacionadas automaticamente. Access keys no código podem vazar; bucket público expõe os dados a todos; o root nunca deve ser usado em aplicações.

</details>

### Questão 6

<sub>Domínio 2 · tópico [2.3](../../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Um usuário IAM recebe uma política que permite (Allow) apagar objetos de um bucket S3 e, por meio de um grupo, outra política que nega explicitamente (Deny) a mesma ação. O que acontece quando ele tenta apagar um objeto?

- **A)** O IAM retorna erro de política conflitante e bloqueia o usuário
- **B)** A ação é permitida, porque políticas de usuário prevalecem sobre as de grupo
- **C)** A ação é negada, porque um Deny explícito sempre prevalece
- **D)** A ação é permitida, porque a política mais recente prevalece

<details>
<summary>Ver resposta</summary>

**Resposta: C**

Na avaliação de políticas do IAM, tudo começa negado, um Allow libera e um **Deny explícito sempre vence**, independentemente de onde a política esteja anexada ou de quando foi criada.

</details>

### Questão 7

<sub>Domínio 2 · tópico [2.3](../../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Uma empresa com 30 contas AWS quer que os funcionários façam login uma única vez, usando o diretório corporativo, e acessem as contas permitidas para cada um. Qual serviço atende a essa necessidade?

- **A)** AWS Secrets Manager
- **B)** Amazon Cognito
- **C)** AWS IAM Identity Center
- **D)** Usuários IAM criados em cada conta

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **IAM Identity Center** oferece login único (SSO) para várias contas do Organizations e aplicações, integrado a diretórios externos. Cognito é para usuários finais de aplicações; criar usuários em cada conta não escala; Secrets Manager guarda segredos.

</details>

### Questão 8

<sub>Domínio 2 · tópico [2.3](../../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Um aplicativo móvel precisa permitir que clientes se cadastrem e façam login com suas contas do Google ou do Facebook. Qual serviço AWS deve ser usado?

- **A)** AWS IAM
- **B)** AWS IAM Identity Center
- **C)** Amazon Cognito
- **D)** AWS Directory Service

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **Cognito** (user pools) oferece cadastro, login e login social para **usuários finais** de aplicações web e mobile. Identity Center e Directory Service são para funcionários; usuários IAM não são para clientes de uma aplicação.

</details>

### Questão 9

<sub>Domínio 2 · tópico [2.3](../../docs/02-seguranca-e-conformidade/03-iam.md)</sub>

Uma empresa precisa armazenar a senha do banco de dados Amazon RDS de forma criptografada e trocá-la automaticamente a cada 30 dias, sem alterar o código a cada troca. Qual serviço atende MELHOR a esse requisito?

- **A)** AWS Systems Manager Parameter Store
- **B)** AWS Secrets Manager
- **C)** Amazon S3 com criptografia SSE-KMS
- **D)** AWS Key Management Service (AWS KMS)

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Secrets Manager** tem **rotação automática nativa** de credenciais do RDS. O Parameter Store guarda parâmetros e segredos, mas sem rotação nativa; o KMS gerencia chaves de criptografia, não segredos; o S3 não é um cofre de segredos.

</details>

### Questão 10

<sub>Domínio 2 · tópico [2.4](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)</sub>

Uma empresa usa o AWS Organizations e quer impedir que qualquer conta da OU de desenvolvimento use a região sa-east-1, inclusive administradores dessas contas. O que deve ser usado?

- **A)** Uma bucket policy do S3
- **B)** Uma regra do AWS Config em cada conta
- **C)** Uma Service Control Policy (SCP) aplicada à OU
- **D)** Uma política IAM anexada a cada usuário administrador

<details>
<summary>Ver resposta</summary>

**Resposta: C**

A **SCP** define o limite máximo de permissões de todas as contas de uma OU e vale até para administradores. Políticas IAM podem ser alteradas pelos próprios administradores; o Config detecta, mas não impede; bucket policy só controla um bucket.

</details>

### Questão 11

<sub>Domínio 2 · tópico [2.5](../../docs/02-seguranca-e-conformidade/05-criptografia.md)</sub>

Uma instituição financeira precisa, por regulação, de módulos de segurança de hardware (HSM) dedicados exclusivamente a ela, validados FIPS 140 nível 3, com controle exclusivo das chaves. Qual serviço atende a esse requisito?

- **A)** AWS CloudHSM
- **B)** AWS Secrets Manager
- **C)** AWS Key Management Service (AWS KMS) com chaves gerenciadas pela AWS
- **D)** AWS Certificate Manager (ACM)

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **CloudHSM** oferece HSM **single-tenant**, com chaves sob controle exclusivo do cliente. O KMS usa HSMs compartilhados gerenciados pela AWS; o ACM gerencia certificados TLS; o Secrets Manager guarda segredos.

</details>

### Questão 12

<sub>Domínio 2 · tópico [2.6](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)</sub>

O auditor de uma empresa pediu o relatório SOC 2 da AWS para avaliar os controles do provedor. Onde a empresa obtém esse documento?

- **A)** AWS Config
- **B)** AWS Artifact
- **C)** AWS Trusted Advisor
- **D)** AWS Audit Manager

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **AWS Artifact** é o portal de autoatendimento para baixar relatórios de conformidade **da AWS** (SOC, PCI, ISO) e aceitar acordos como o BAA. O Audit Manager coleta evidências **da conta do cliente** para a auditoria dele.

</details>

### Questão 13

<sub>Domínio 2 · tópico [2.7](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)</sub>

Uma instância EC2 de produção foi encerrada e o time precisa descobrir qual usuário fez isso, quando e de qual endereço IP. Qual serviço fornece essa informação?

- **A)** Amazon CloudWatch
- **B)** AWS Config
- **C)** VPC Flow Logs
- **D)** AWS CloudTrail

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **CloudTrail** registra as chamadas de API (quem, o quê, quando, de onde). O CloudWatch monitora métricas e logs de desempenho; o Config registra o estado da configuração; os Flow Logs registram tráfego de rede, não ações de API.

</details>

### Questão 14

<sub>Domínio 2 · tópico [2.7](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)</sub>

O time de segurança precisa saber como estavam configuradas as regras de um security group na semana passada e ser alertado sempre que algum security group permitir SSH a partir de qualquer IP. Qual serviço atende a esses requisitos?

- **A)** Amazon Macie
- **B)** AWS CloudTrail
- **C)** AWS Config
- **D)** Amazon Inspector

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **AWS Config** guarda o histórico de configuração dos recursos e avalia continuamente a conformidade com regras (ex.: `restricted-ssh`). O CloudTrail mostra quem fez a mudança, mas não avalia regras; Inspector busca vulnerabilidades; Macie busca dados sensíveis no S3.

</details>

### Questão 15

<sub>Domínio 2 · tópico [2.8](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) · **múltipla resposta**</sub>

Quais DUAS afirmações sobre security groups e network ACLs estão corretas? (Escolha DUAS.)

- **A)** Security groups são aplicados a subnets inteiras
- **B)** Security groups aceitam regras de negação para bloquear um IP específico
- **C)** Security groups são stateful: o tráfego de retorno é liberado automaticamente
- **D)** Network ACLs são stateful e atuam no nível da instância
- **E)** Network ACLs atuam no nível da subnet e aceitam regras de permissão e de negação

<details>
<summary>Ver resposta</summary>

**Resposta: C, E**

Security groups atuam na instância/ENI, são **stateful** e só têm regras de permissão. Network ACLs atuam na **subnet**, são **stateless** e aceitam **permitir e negar** — por isso são usadas para bloquear um IP específico.

</details>

### Questão 16

<sub>Domínio 2 · tópico [2.8](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)</sub>

Uma loja virtual atrás de um Application Load Balancer está sofrendo tentativas de SQL injection e cross-site scripting (XSS). Qual serviço deve ser usado para bloquear essas requisições?

- **A)** AWS WAF
- **B)** Amazon GuardDuty
- **C)** Security groups
- **D)** AWS Shield Standard

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **WAF** é um firewall de camada 7 que filtra requisições web (SQL injection, XSS, rate limiting) e se associa ao ALB. O Shield protege contra DDoS; security groups filtram por IP/porta; o GuardDuty detecta ameaças, mas não bloqueia requisições.

</details>

### Questão 17

<sub>Domínio 2 · tópico [2.8](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)</sub>

Uma empresa de jogos quer proteção ampliada contra DDoS, acesso 24/7 a uma equipe especializada durante ataques e créditos pelos custos de escalonamento causados por ataques. Qual serviço atende a esses requisitos?

- **A)** AWS WAF
- **B)** AWS Shield Advanced
- **C)** AWS Firewall Manager
- **D)** AWS Shield Standard

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Shield Advanced** inclui o Shield Response Team (SRT) 24/7 e **proteção de custo**. O Shield Standard é gratuito e automático, mas não tem esses extras; o WAF filtra requisições web; o Firewall Manager gerencia regras centralmente.

</details>

### Questão 18

<sub>Domínio 2 · tópico [2.9](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)</sub>

Uma empresa quer detectar automaticamente atividades maliciosas, como uma instância EC2 minerando criptomoedas ou se comunicando com IPs conhecidos de ataque, analisando CloudTrail, VPC Flow Logs e logs de DNS. Qual serviço atende a esse requisito?

- **A)** Amazon Macie
- **B)** AWS Artifact
- **C)** Amazon Inspector
- **D)** Amazon GuardDuty

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **GuardDuty** detecta ameaças ativas com ML e inteligência de ameaças a partir desses logs, sem agentes. O Inspector busca vulnerabilidades de software; o Macie, dados sensíveis no S3; o Artifact fornece relatórios de conformidade.

</details>

### Questão 19

<sub>Domínio 2 · tópico [2.9](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)</sub>

O time de segurança precisa descobrir quais buckets S3 contêm dados pessoais, como números de cartão de crédito e documentos de identidade. Qual serviço deve ser usado?

- **A)** AWS Shield
- **B)** Amazon Macie
- **C)** Amazon Inspector
- **D)** Amazon Detective

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Macie** usa ML e padrões para descobrir dados sensíveis (PII) no **S3**. O Inspector busca CVEs em EC2, ECR e Lambda; o Detective investiga a causa raiz de achados; o Shield protege contra DDoS.

</details>

### Questão 20

<sub>Domínio 2 · tópico [2.9](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)</sub>

Uma empresa quer varrer continuamente suas instâncias EC2 e as imagens de contêiner no Amazon ECR em busca de vulnerabilidades de software conhecidas (CVEs). Qual serviço deve ser usado?

- **A)** Amazon GuardDuty
- **B)** AWS Trusted Advisor
- **C)** AWS Config
- **D)** Amazon Inspector

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Inspector** avalia vulnerabilidades de software e exposição de rede em EC2, ECR e Lambda. O GuardDuty detecta ameaças em andamento; o Trusted Advisor dá recomendações de boas práticas; o Config avalia configurações, não CVEs.

</details>
