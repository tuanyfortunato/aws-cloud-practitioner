# 🃏 Flashcards — Domínio 2 — Segurança e Conformidade

Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* de cada tópico (`python3 scripts/gerar_docs.py`).

**Total:** 67 cards


## [2.1 Modelo de responsabilidade compartilhada](../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md)

<details>
<summary>Qual é responsabilidade da AWS?</summary>

Segurança física dos datacenters, hardware, rede global, hipervisor, patch do SO em serviços gerenciados (RDS, Lambda).
</details>

<details>
<summary>Qual é responsabilidade do cliente?</summary>

Dados, IAM, security groups, criptografia, patch do SO no EC2, configuração dos serviços.
</details>

<details>
<summary>Qual é um controle compartilhado?</summary>

Gestão de patches, gestão de configuração ou treinamento.
</details>

<details>
<summary>Qual é um controle herdado da AWS?</summary>

Controles físicos e ambientais.
</details>

<details>
<summary>Ao trocar EC2 por Lambda, o que muda?</summary>

A responsabilidade do cliente diminui (SO e runtime passam para a AWS).
</details>

<details>
<summary>Quem é responsável pela segurança dos dados no S3?</summary>

O cliente (políticas, acesso e criptografia).
</details>


## [2.2 Usuário root](../docs/02-seguranca-e-conformidade/02-usuario-root.md)

<details>
<summary>Qual é a boa prática para o usuário root?</summary>

Ativar MFA, não criar access keys e usá-lo só para tarefas que o exigem.
</details>

<details>
<summary>Qual destas tarefas exige o root?</summary>

Fechar a conta, alterar o e-mail ou a senha do root, restaurar permissões de administrador ou configurar MFA Delete. (🔄 Mudar o plano de suporte e alterar o nome da conta **não** estão mais na lista oficial.)
</details>

<details>
<summary>Qual tarefa NÃO exige o root?</summary>

Criar usuários IAM, ver a fatura (com permissão) ou lançar instâncias.
</details>

<details>
<summary>O que fazer logo após criar a conta?</summary>

Proteger o root com MFA e criar identidades administrativas para o dia a dia.
</details>


## [2.3 AWS IAM (Identity and Access Management)](../docs/02-seguranca-e-conformidade/03-iam.md)

<details>
<summary>Uma aplicação no EC2 precisa ler um bucket S3. Qual a forma mais segura?</summary>

Anexar uma IAM role à instância.
</details>

<details>
<summary>Dez desenvolvedores precisam das mesmas permissões.</summary>

Criar um grupo IAM e anexar a política ao grupo.
</details>

<details>
<summary>Uma política tem Allow e outra tem Deny explícito para a mesma ação. O que vale?</summary>

Deny explícito.
</details>

<details>
<summary>Qual princípio diz para dar só as permissões necessárias?</summary>

Menor privilégio.
</details>

<details>
<summary>Qual relatório lista os usuários e o status de MFA e access keys?</summary>

IAM credential report.
</details>

<details>
<summary>Como dar login único a funcionários em várias contas?</summary>

IAM Identity Center.
</details>

<details>
<summary>Como permitir login com Google em um app mobile?</summary>

Amazon Cognito.
</details>

<details>
<summary>Onde guardar a senha do banco com rotação automática?</summary>

Secrets Manager.
</details>

<details>
<summary>Funcionários usam o Active Directory da empresa e precisam acessar a AWS.</summary>

Federação (via Identity Center ou SAML) ou AWS Directory Service.
</details>

<details>
<summary>Como acessar a AWS por linha de comando?</summary>

AWS CLI com access keys (ou credenciais temporárias).
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
