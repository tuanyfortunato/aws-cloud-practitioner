# 🃏 Flashcards — Domínio 2 — Segurança e Conformidade

Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* de cada tópico (`python3 scripts/gerar_docs.py`).

**Total:** 62 cards


## [2.1 Modelo de responsabilidade compartilhada](../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md)

<details>
<summary>Qual é a diferença entre segurança da nuvem e segurança na nuvem?</summary>

Segurança da nuvem é proteger a infraestrutura que roda os serviços, e é da AWS; segurança na nuvem é proteger o que o cliente coloca e configura nos serviços, e é do cliente.
</details>

<details>
<summary>Por que a escola tem menos trabalho de segurança no RDS do que num banco instalado numa instância EC2?</summary>

Porque no RDS a AWS assume o sistema operacional e o software do banco, incluindo instalação, patches e backups, que no EC2 seriam da escola.
</details>

<details>
<summary>Uma biblioteca empacotada numa função Lambda tem uma falha de segurança. Quem corrige?</summary>

O cliente, que precisa atualizar a biblioteca e publicar a função de novo.
</details>

<details>
<summary>O que é um controle compartilhado? Dê um exemplo.</summary>

É um controle que vale para as duas camadas, com cada lado fazendo a sua parte; a gestão de patches é o exemplo clássico: a AWS corrige a infraestrutura e o cliente corrige o SO convidado e as aplicações.
</details>

<details>
<summary>Num serviço como o S3, o que continua sendo responsabilidade do cliente?</summary>

Os dados e o acesso a eles: as opções de criptografia, a classificação do que é sensível e as permissões que dizem quem pode ler e gravar.
</details>


## [2.2 Usuário root](../docs/02-seguranca-e-conformidade/02-usuario-root.md)

<details>
<summary>O que é o usuário root de uma conta AWS?</summary>

É a identidade criada junto com a conta, que entra com o e-mail e a senha usados na criação e tem acesso completo a todos os serviços e recursos da conta.
</details>

<details>
<summary>Por que a AWS recomenda não usar o root nas tarefas do dia a dia?</summary>

Porque ele tem poder total sobre a conta: qualquer erro ou vazamento da credencial afeta tudo, inclusive a cobrança e o encerramento da conta. O trabalho diário deve usar identidades com só as permissões necessárias.
</details>

<details>
<summary>Quais são as principais proteções do root?</summary>

Ativar MFA (hoje exigido em todos os tipos de conta), usar uma senha forte e exclusiva, não criar chaves de acesso para o root e usar e-mail de grupo e aprovação por várias pessoas.
</details>

<details>
<summary>Mudar o nome da conta exige entrar como root?</summary>

Não. Nome da conta, dados de contato, contatos alternativos, moeda de pagamento e Regiões podem ser mudados sem o root. Mudar o e-mail, a senha e as chaves de acesso do root de uma conta independente exige o root.
</details>

<details>
<summary>Cite três tarefas que exigem o root.</summary>

Encerrar uma conta independente, restaurar as permissões de um administrador do IAM que se trancou do lado de fora e ativar o acesso do IAM ao console de faturamento. Também valem destravar uma política de bucket S3 ou de fila SQS que nega acesso a todos e configurar MFA Delete num bucket S3.
</details>


## [2.3 AWS IAM (Identity and Access Management)](../docs/02-seguranca-e-conformidade/03-iam.md)

<details>
<summary>Qual é a diferença entre um usuário do IAM e uma função do IAM?</summary>

O usuário representa uma pessoa ou programa e tem credenciais de longo prazo (senha e chaves de acesso). A função não pertence a ninguém: é assumida por quem precisa dela e entrega credenciais temporárias, geradas pelo AWS STS.
</details>

<details>
<summary>Uma política permite ler um bucket e outra nega a mesma ação. O que acontece?</summary>

O pedido é negado, porque uma negação explícita sempre vence uma permissão.
</details>

<details>
<summary>Como dar a uma aplicação numa instância EC2 acesso a um bucket S3 sem gravar credenciais no servidor?</summary>

Criar uma função do IAM com a permissão necessária e anexá-la à instância por meio de um perfil de instância. A aplicação recebe credenciais temporárias renovadas automaticamente.
</details>

<details>
<summary>Quando usar o IAM Identity Center e quando usar o Amazon Cognito?</summary>

O Identity Center dá a funcionários acesso a várias contas AWS e aplicações, com login único. O Cognito cuida do cadastro e do login dos usuários de um aplicativo, como clientes de um site.
</details>

<details>
<summary>Qual serviço guarda a senha de um banco de dados com rotação automática?</summary>

O AWS Secrets Manager, que guarda, recupera e troca segredos automaticamente num calendário.
</details>


## [2.4 Governança multi-conta](../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)

<details>
<summary>Como impedir que todas as contas de desenvolvimento usem uma região?</summary>

SCP no Organizations.
</details>

<details>
<summary>Uma SCP permite S3, mas o usuário não tem política IAM para S3. Ele consegue acessar?</summary>

Não; a SCP só limita, não concede.
</details>

<details>
<summary>Como obter desconto por volume somando o uso de várias contas?</summary>

Consolidated billing no Organizations.
</details>

<details>
<summary>Como criar rapidamente um ambiente multi-conta seguro com guardrails?</summary>

AWS Control Tower.
</details>

<details>
<summary>Como deixar times criarem só recursos aprovados pela empresa?</summary>

AWS Service Catalog.
</details>

<details>
<summary>Como compartilhar uma subnet com outra conta?</summary>

AWS RAM.
</details>


## [2.5 Criptografia](../docs/02-seguranca-e-conformidade/05-criptografia.md)

<details>
<summary>Qual serviço cria e controla chaves de criptografia integradas a S3, EBS e RDS?</summary>

AWS KMS.
</details>

<details>
<summary>A empresa exige HSM dedicado, com chaves sob controle exclusivo dela.</summary>

AWS CloudHSM.
</details>

<details>
<summary>Como obter certificados SSL/TLS gratuitos com renovação automática?</summary>

AWS Certificate Manager.
</details>

<details>
<summary>Como proteger dados em trânsito?</summary>

TLS/HTTPS.
</details>

<details>
<summary>E em repouso?</summary>

Criptografia com KMS.
</details>

<details>
<summary>Quem é responsável por ativar a criptografia dos dados?</summary>

O cliente.
</details>

<details>
<summary>Como auditar quem usou uma chave do KMS?</summary>

CloudTrail.
</details>


## [2.6 Compliance e governança](../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)

<details>
<summary>Onde baixar o relatório SOC 2 ou o atestado PCI da AWS?</summary>

AWS Artifact.
</details>

<details>
<summary>Onde aceitar um acordo como o BAA (HIPAA)?</summary>

AWS Artifact (Agreements).
</details>

<details>
<summary>Como coletar evidências continuamente para a auditoria da empresa?</summary>

AWS Audit Manager.
</details>

<details>
<summary>Os dados podem sair da região sem ação do cliente?</summary>

Não; o cliente escolhe a região e controla onde os dados ficam.
</details>

<details>
<summary>Usar um serviço certificado garante que a aplicação está em conformidade?</summary>

Não; o cliente também precisa configurar e operar de forma conforme (responsabilidade compartilhada).
</details>


## [2.7 Logs, monitoramento e auditoria](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)

<details>
<summary>Qual serviço registra quem encerrou uma instância e quando?</summary>

CloudTrail.
</details>

<details>
<summary>Por quanto tempo o CloudTrail guarda eventos sem configurar nada?</summary>

90 dias (event history).
</details>

<details>
<summary>Como guardar logs do CloudTrail por anos?</summary>

Criar um trail que envia para o S3.
</details>

<details>
<summary>Qual serviço mostra o histórico de configuração de um recurso e se ele segue as regras?</summary>

AWS Config.
</details>

<details>
<summary>Como receber alerta quando a CPU passar de 80%?</summary>

Alarme do CloudWatch (com notificação pelo SNS).
</details>

<details>
<summary>Como coletar a memória usada pelo EC2?</summary>

Instalar o CloudWatch agent.
</details>

<details>
<summary>Como capturar o tráfego de rede da VPC?</summary>

VPC Flow Logs.
</details>

<details>
<summary>Onde ver logs de aplicação?</summary>

CloudWatch Logs.
</details>


## [2.8 Proteção de rede e aplicações](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)

<details>
<summary>Qual firewall atua no nível da instância e é stateful?</summary>

Security group.
</details>

<details>
<summary>Qual firewall atua no nível da subnet e é stateless?</summary>

Network ACL.
</details>

<details>
<summary>Como bloquear um endereço IP malicioso?</summary>

Regra de negação na NACL (ou regra no WAF para tráfego web).
</details>

<details>
<summary>Qual proteção DDoS todo cliente tem sem custo?</summary>

Shield Standard.
</details>

<details>
<summary>Qual serviço dá acesso a especialistas 24/7 e proteção de custo durante ataques DDoS?</summary>

Shield Advanced.
</details>

<details>
<summary>Como bloquear SQL injection e XSS?</summary>

AWS WAF.
</details>

<details>
<summary>Como bloquear acesso de certos países ao site?</summary>

WAF (regra geográfica) ou restrição geográfica do CloudFront.
</details>

<details>
<summary>Em quais serviços o WAF pode ser usado?</summary>

CloudFront, ALB, API Gateway, AppSync e Cognito.
</details>

<details>
<summary>Como aplicar as mesmas regras de WAF em todas as contas?</summary>

AWS Firewall Manager.
</details>


## [2.9 Detecção de ameaças e postura de segurança](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)

<details>
<summary>Qual serviço detecta atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS?</summary>

GuardDuty.
</details>

<details>
<summary>Qual serviço varre instâncias EC2 e imagens de container em busca de vulnerabilidades?</summary>

Amazon Inspector.
</details>

<details>
<summary>Qual serviço encontra dados pessoais em buckets S3?</summary>

Amazon Macie.
</details>

<details>
<summary>Qual serviço ajuda a investigar a causa raiz de um achado de segurança?</summary>

Amazon Detective.
</details>

<details>
<summary>Qual serviço reúne os achados de segurança de vários serviços num só painel?</summary>

AWS Security Hub.
</details>

<details>
<summary>Qual serviço recomenda melhorias de custo, segurança, performance e limites?</summary>

Trusted Advisor.
</details>

<details>
<summary>Qual plano de suporte libera todas as verificações do Trusted Advisor?</summary>

Business Support+ ou superior (no modelo clássico, Business).
</details>

<details>
<summary>Qual verificação de segurança o Trusted Advisor faz?</summary>

Buckets S3 públicos, MFA no root, portas abertas em security groups.
</details>


## [2.10 Outros pontos de segurança](../docs/02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md)

<details>
<summary>É preciso pedir autorização para fazer pentest no EC2?</summary>

Não, para os serviços da lista permitida; simulação de DDoS e alguns testes são proibidos.
</details>

<details>
<summary>Uma instância da AWS está enviando spam para a sua empresa. Quem contatar?</summary>

AWS Trust & Safety.
</details>

<details>
<summary>Onde encontrar boletins e boas práticas de segurança?</summary>

AWS Security Center, Security Blog e Knowledge Center.
</details>

<details>
<summary>Onde comprar ferramentas de segurança de terceiros?</summary>

AWS Marketplace.
</details>
