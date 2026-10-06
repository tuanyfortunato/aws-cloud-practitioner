# 🃏 Flashcards — Domínio 2 — Segurança e Conformidade

Clique na pergunta para ver a resposta. Gerado a partir da seção *Revisão* de cada aula (`python3 scripts/gerar_docs.py`).

**Total:** 50 cards


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
<summary>Por que a AWS recomenda usar várias contas?</summary>

Porque cada conta é uma fronteira de permissões, segurança, custos e cargas de trabalho. Separar ambientes isola dados sensíveis, limita o impacto de incidentes, separa custos e distribui as cotas de serviço.
</details>

<details>
<summary>Uma SCP permite o S3, mas o usuário não tem nenhuma política do IAM para o S3. Ele consegue acessar?</summary>

Não. A SCP só define o máximo possível; ela não concede permissão. O acesso exige que a SCP e uma política do IAM liberem a ação.
</details>

<details>
<summary>Uma SCP nega uma ação numa OU. Um usuário com AdministratorAccess numa conta dessa OU consegue fazer a ação?</summary>

Não. O bloqueio da SCP vale para todos os usuários e funções das contas-membro abaixo da OU, inclusive o root delas. A exceção é a conta de gerenciamento, que as SCPs não afetam.
</details>

<details>
<summary>O que o faturamento consolidado faz?</summary>

Junta as contas da organização numa fatura e soma o uso de todas para compartilhar descontos por volume, de Instâncias Reservadas e de Savings Plans, sem custo adicional.
</details>

<details>
<summary>Qual é a diferença entre o AWS Organizations e o AWS Control Tower?</summary>

O Organizations é a base: agrupa contas em OUs, aplica SCPs e consolida a fatura. O Control Tower usa o Organizations e outros serviços para montar automaticamente uma landing zone com boas práticas, controles e criação padronizada de contas.
</details>


## [2.5 Criptografia](../docs/02-seguranca-e-conformidade/05-criptografia.md)

<details>
<summary>Qual é a diferença entre o AWS KMS e o AWS CloudHSM?</summary>

O KMS é um serviço gerenciado de chaves, com HSMs compartilhados e gerenciados pela AWS e integração com muitos serviços. O CloudHSM oferece HSMs dedicados a um único cliente, que administra os próprios usuários e chaves.
</details>

<details>
<summary>Um usuário tem permissão de leitura num bucket, mas o objeto está cifrado com SSE-KMS e uma chave gerenciada pelo cliente. Ele consegue ler?</summary>

Só se também tiver permissão para usar a chave (`kms:Decrypt`). Permissão no bucket sozinha não basta.
</details>

<details>
<summary>Para que serve o AWS Certificate Manager?</summary>

Para criar, guardar e renovar certificados SSL/TLS usados no HTTPS de serviços como o Elastic Load Balancing, o CloudFront e o API Gateway. Com validação por DNS, a renovação é automática.
</details>

<details>
<summary>Como saber quem usou uma chave do KMS?</summary>

Pelo AWS CloudTrail, que registra todas as chamadas ao KMS, inclusive as feitas por outros serviços em nome do cliente.
</details>

<details>
<summary>Um objeto enviado hoje ao S3 sem nenhuma configuração fica cifrado?</summary>

Sim. Desde 5 de janeiro de 2023, todo objeto novo no S3 é cifrado automaticamente com SSE-S3, sem custo adicional.
</details>


## [2.6 Compliance e governança](../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)

<details>
<summary>Onde baixar o relatório SOC 2 da AWS?</summary>

No AWS Artifact, portal gratuito de autoatendimento com os documentos de segurança e compliance da AWS, como relatórios SOC, PCI e ISO.
</details>

<details>
<summary>Qual é a diferença entre o AWS Artifact e o AWS Audit Manager?</summary>

O Artifact fornece os relatórios e acordos de compliance da própria AWS. O Audit Manager coleta continuamente evidências das contas do cliente e as organiza por controle, para as auditorias do cliente.
</details>

<details>
<summary>Usar apenas serviços que estão no escopo do PCI DSS coloca a aplicação em conformidade com o PCI DSS?</summary>

Não. A AWS cobre a parte dela; o cliente ainda precisa configurar e operar sua aplicação do jeito que a norma exige. A responsabilidade de compliance é compartilhada.
</details>

<details>
<summary>Como garantir que os dados de clientes fiquem num país específico?</summary>

Escolhendo uma Região nesse país para guardar os dados. A AWS não move nem replica o conteúdo para fora das Regiões escolhidas, exceto quando necessário para o serviço iniciado pelo cliente ou para cumprir a lei.
</details>

<details>
<summary>Para que servem as regras do AWS Config?</summary>

Para avaliar continuamente se a configuração dos recursos segue a configuração desejada, como "nenhum bucket público". Recursos fora da regra podem ser corrigidos com remediação automática.
</details>


## [2.7 Logs, monitoramento e auditoria](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)

<details>
<summary>Qual serviço registra quem encerrou uma instância e quando?</summary>

O AWS CloudTrail, que registra as chamadas de API da conta como eventos, com a identidade, a ação, o horário, a origem e o recurso.
</details>

<details>
<summary>Como guardar os eventos do CloudTrail por anos?</summary>

Criando uma trilha que entrega os eventos num bucket S3, onde ficam pelo tempo que a escola quiser. A trilha pode cobrir todas as Regiões e, numa organização, todas as contas.
</details>

<details>
<summary>Qual é a diferença entre o CloudTrail e o Config?</summary>

O CloudTrail registra ações: quem fez cada chamada de API e quando. O Config registra estados: como cada recurso estava configurado ao longo do tempo e se seguia as regras.
</details>

<details>
<summary>Como coletar o uso de memória de uma instância EC2 no CloudWatch?</summary>

Instalando o agente do CloudWatch na instância. A memória usada dentro do sistema operacional não está entre as métricas que o EC2 envia por padrão.
</details>

<details>
<summary>Como ser avisado quando os gastos da conta passarem de um valor?</summary>

Criando um alarme de cobrança no CloudWatch, com notificação por um tópico do SNS. A métrica de gastos estimados fica na Região Leste dos EUA (Norte da Virgínia).
</details>


## [2.8 Proteção de rede e aplicações](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)

<details>
<summary>Qual é a diferença entre um security group e uma ACL de rede?</summary>

O security group atua no recurso, só tem regras de permitir e é stateful (a resposta volta sozinha). A ACL de rede atua na sub-rede, tem regras de permitir e negar, avaliadas em ordem numérica, e é stateless (a resposta precisa de regra própria).
</details>

<details>
<summary>Um security group novo deixa algum tráfego entrar?</summary>

Não. Um security group novo não tem regras de entrada, então nada entra até alguém liberar; ele já vem com uma regra que permite todo o tráfego de saída.
</details>

<details>
<summary>Qual serviço protege contra injeção de SQL num site atrás de um load balancer?</summary>

O AWS WAF, com um web ACL associado ao Application Load Balancer e regras que inspecionam os pedidos HTTP em busca de código SQL malicioso.
</details>

<details>
<summary>Qual é a diferença entre o Shield Standard e o Shield Advanced?</summary>

O Standard protege todos os clientes automaticamente, sem custo adicional, contra os ataques DDoS de rede e transporte mais comuns. O Advanced é pago, com compromisso de um ano, e acrescenta proteção contra ataques maiores e na camada de aplicação, acesso 24 horas ao Shield Response Team e proteção contra aumentos de cobrança causados por DDoS.
</details>

<details>
<summary>Para que serve o AWS Firewall Manager?</summary>

Para administrar de forma central regras do WAF, do Shield Advanced, de security groups, de ACLs de rede e do Network Firewall em todas as contas de uma organização, aplicando-as também às contas e recursos novos.
</details>


## [2.9 Detecção de ameaças](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)

<details>
<summary>Qual serviço detecta uma instância EC2 se comunicando com um servidor de mineração de criptomoeda?</summary>

O Amazon GuardDuty, que analisa continuamente fontes como Flow Logs, eventos do CloudTrail e consultas DNS, usando inteligência de ameaças e aprendizado de máquina.
</details>

<details>
<summary>Qual é a diferença entre o GuardDuty e o Inspector?</summary>

O GuardDuty detecta ameaças e atividade maliciosa em andamento. O Inspector encontra vulnerabilidades de software e exposição de rede em instâncias EC2, imagens no ECR e funções Lambda.
</details>

<details>
<summary>Qual serviço encontra dados pessoais guardados no S3?</summary>

O Amazon Macie, que usa aprendizado de máquina e reconhecimento de padrões para descobrir dados sensíveis nos objetos do S3 e também avalia a segurança dos buckets.
</details>

<details>
<summary>Para que serve o Amazon Detective?</summary>

Para investigar a causa raiz de achados de segurança e atividades suspeitas, com visualizações que mostram como identidades e recursos se relacionaram ao longo do tempo.
</details>

<details>
<summary>O que o AWS Security Hub faz?</summary>

Reúne, correlaciona e prioriza os achados de serviços como GuardDuty, Inspector e Macie e verifica as contas contra padrões de segurança, como AWS Foundational Security Best Practices, CIS e PCI DSS.
</details>


## [2.10 Outros pontos de segurança](../docs/02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md)

<details>
<summary>O cliente precisa de aprovação da AWS para fazer um teste de intrusão na própria instância EC2?</summary>

Não. EC2 está na lista de serviços que o cliente pode testar na própria infraestrutura sem aprovação prévia.
</details>

<details>
<summary>Um teste de intrusão pode incluir uma simulação de DDoS livremente?</summary>

Não. DoS e DDoS, reais ou simulados, estão entre as atividades proibidas pela política de testes de intrusão e só podem seguir a política específica de simulação de DDoS.
</details>

<details>
<summary>A quem denunciar spam ou ataques vindos de um endereço IP da AWS?</summary>

À equipe AWS Trust & Safety, pelo formulário de abuso da AWS.
</details>

<details>
<summary>Onde a AWS publica avisos sobre vulnerabilidades que afetam seus serviços?</summary>

Nos Security Bulletins, a página de boletins de segurança da AWS. Outras fontes oficiais de informação de segurança são a página de segurança da AWS, o AWS Security Blog e o AWS Knowledge Center.
</details>

<details>
<summary>Onde encontrar produtos de segurança de outros fabricantes para usar na AWS?</summary>

No AWS Marketplace, catálogo curado de software, dados e serviços de terceiros, com categoria própria de segurança.
</details>
