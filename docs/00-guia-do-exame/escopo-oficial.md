# 🎯 Escopo oficial da CLF-C02 (verificado em 04/10/2026)

<!-- didatico:inicio -->
## 🧭 Antes de ler

**Por que esta página existe?** Um serviço pode existir na AWS e, ainda assim, não estar na lista de estudo do exame. Também há listas antigas circulando.

**Como usar?** Esta página separa tarefas e serviços conforme o guia oficial consultado. Use-a para priorizar o estudo e interpretar as marcações das fichas.

**Exemplo:** Ao encontrar uma ficha de referência, confira a marcação antes de investir tempo em detalhes. ‘Não listado’ e ‘explicitamente fora do escopo’ não são a mesma classificação.
<!-- didatico:fim -->

> Fontes: [verificação em fontes oficiais](../../fontes/verificacao-fontes-oficiais-2026-10.md) e [rodadas 3 e 4](../../fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md), feitas no
> [exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
> e na [lista de serviços no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html).
>
> ⚠️ O código da prova continua **CLF-C02**, mas a AWS atualiza o conteúdo do guia **sem trocar o código**.
> Reabra as duas páginas alguns dias antes da prova. A própria AWS avisa que as listas não são exaustivas.

## 🧭 Em resumo


> 💡 **Em palavras simples:** a AWS publica **o que pode cair** na prova (as *task statements* e a lista de serviços) e
> **o que não cai** (a lista de fora do escopo). Esta página traduz essas listas e liga cada item ao tópico deste repositório.


**Como ler os símbolos desta página (e das fichas):**


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Símbolo | Significado | O que fazer |
|---|---|---|
| ✅ | Está na lista oficial de serviços **no escopo** | Estude |
| ❌ | Está na lista oficial **fora do escopo** | Prioridade baixa; não use apenas o nome para decidir uma questão |
| ⚪ | Não aparece em **nenhuma** das duas listas | Baixa prioridade: saiba para que serve |
| 🔀 | Ficha com serviços de status diferentes | Veja o status de cada serviço na linha *Escopo oficial* da ficha |


## Task statements oficiais → tópicos deste repositório



Os tópicos de `docs/` seguem a numeração do guia de estudo (1.1 a 4.6), que é **diferente** da numeração

oficial das tasks. A tabela abaixo liga uma à outra.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **IAM Identity Center:** Serviço de acesso central para a força de trabalho. Atribuições de contas e aplicações não são o cadastro de clientes de um aplicativo.
- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **Trusted Advisor:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.
- **Health Dashboard:** AWS Health apresenta eventos sobre a saúde dos serviços e informações relevantes aos recursos da conta, conforme a visão consultada.
- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.
- **Glue:** Glue oferece catálogo e ferramentas de integração e transformação de dados.
- **SageMaker AI:** SageMaker AI oferece recursos para etapas do desenvolvimento e operação de modelos.
- **AI:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.
- **compliance:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
- **APN:** Rede de parceiros AWS. Parceiros oferecem serviços e soluções conforme seus próprios contratos e competências.
- **CAF:** Cloud Adoption Framework: orientação para preparar capacidades da organização na adoção de nuvem. Não é uma ferramenta que transfere servidores.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Task oficial | Texto oficial | Tópicos do repositório |
|---|---|---|
| **1.1** | Define the benefits of the AWS Cloud | [1.1](../01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) · [1.2](../01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) · [3.2](../03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| **1.2** | Identify design principles of the AWS Cloud | [1.3](../01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) · [1.4 Well-Architected (6 pilares)](../01-conceitos-de-nuvem/04-well-architected-framework.md) |
| **1.3** | Understand the benefits of and strategies for migration to the AWS Cloud | [1.5 CAF](../01-conceitos-de-nuvem/05-cloud-adoption-framework.md) · [1.6 7 Rs](../01-conceitos-de-nuvem/06-estrategias-de-migracao.md) · [3.17](../03-tecnologia-e-servicos/17-migracao-e-transferencia.md) |
| **1.4** | Understand concepts of cloud economics | [1.7](../01-conceitos-de-nuvem/07-economia-da-nuvem.md) |
| **2.1** | Understand the AWS shared responsibility model | [2.1](../02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) |
| **2.2** | Understand AWS Cloud security, governance, and compliance concepts | [2.5](../02-seguranca-e-conformidade/05-criptografia.md) · [2.6](../02-seguranca-e-conformidade/06-compliance-e-governanca.md) · [2.7](../02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| **2.3** | Identify AWS access management capabilities (inclui **IAM Identity Center**, proteção do root e tarefas exclusivas do root) | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md) · [2.3](../02-seguranca-e-conformidade/03-iam.md) · [2.4](../02-seguranca-e-conformidade/04-governanca-multi-conta.md) |
| **2.4** | Identify components and resources for security | [2.8](../02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) · [2.9](../02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) · [2.10](../02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) |
| **3.1** | Define methods of deploying and operating in the AWS Cloud | [3.1](../03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) · [3.16](../03-tecnologia-e-servicos/16-gestao-e-governanca.md) |
| **3.2** | Define the AWS global infrastructure | [3.2](../03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| **3.3** | Identify AWS compute services | [3.3](../03-tecnologia-e-servicos/03-ec2.md) · [3.4](../03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) · [3.5](../03-tecnologia-e-servicos/05-containers-e-serverless.md) · [3.6](../03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) |
| **3.4** | Identify AWS database services | [3.7](../03-tecnologia-e-servicos/07-bancos-de-dados.md) |
| **3.5** | Identify AWS network services | [3.10](../03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| **3.6** | Identify AWS storage services | [3.8](../03-tecnologia-e-servicos/08-s3.md) · [3.9](../03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| **3.7** | Identify AWS AI/ML services and analytics services (SageMaker AI, Lex, Athena, Kinesis, Glue, Quick Sight…) | [3.11](../03-tecnologia-e-servicos/11-analytics.md) · [3.12](../03-tecnologia-e-servicos/12-ia-e-machine-learning.md) |
| **3.8** | Identify services from other in-scope AWS service categories | [3.13](../03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) · [3.14](../03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md) · [3.15](../03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md) · [3.18](../03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md) |
| **4.1** | Compare AWS pricing models (On-Demand, RIs, Spot, Savings Plans, Dedicated Hosts/Instances, Capacity Reservations; flexibilidade de RIs e RIs no Organizations) | [4.1](../04-cobranca-precos-e-suporte/01-principios-de-preco.md) · [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) · [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| **4.2** | Understand resources for billing, budget, and cost management | [4.4](../04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| **4.3** | Identify AWS technical resources and AWS Support options (**Developer, Business, Enterprise On-Ramp, Enterprise** nos exemplos consultados; comparar com os planos comerciais novos; Trusted Advisor, Health Dashboard e Health API; Trust and Safety, APN, Marketplace, Professional Services, Prescriptive Guidance, Knowledge Center, re:Post) | [4.5](../04-cobranca-precos-e-suporte/05-planos-de-suporte.md) · [4.6](../04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md) |


## 🔍 O que cada task cita (termos do exam guide)


> Resumo fiel das listas "Knowledge of / Skills in", com todos os termos citados ([verificação, seção A](../../fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md)).
> Texto literal no [exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html).

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **EKS:** O EKS oferece Kubernetes gerenciado.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **EFS:** O EFS oferece um sistema de arquivos compartilhado.
- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **Storage Gateway:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.
- **AWS Backup:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **ElastiCache:** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **Direct Connect:** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.
- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.
- **Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.
- **Security Hub:** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.
- **Artifact:** Artifact disponibiliza relatórios e acordos de conformidade aplicáveis, conforme o acesso e as condições de cada documento.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.
- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.
- **CLI:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
- **X-Ray:** X-Ray ajuda a acompanhar requisições em aplicações instrumentadas, reunindo rastreamentos e relações entre componentes.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **SES:** SES oferece envio de e-mail para aplicações, com recursos de identidade, acompanhamento e controle de envio.
- **Cost Explorer:** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.
- **Budgets:** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **híbrido:** Combinação de ambiente próprio e nuvem. É necessário definir quais partes ficam em cada lado e como se comunicam.
- **elasticidade:** Ajuste da capacidade para crescer e reduzir conforme a necessidade, dentro das regras e dos limites da solução.
- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **menor privilégio:** Conceder apenas o acesso necessário ao trabalho. Evita que uma tarefa simples carregue poder desnecessário sobre outros recursos.
- **instance store:** Armazenamento local temporário da máquina física. Não é lugar seguro para a única cópia de dados que precisam sobreviver às ações descritas no ciclo de vida.
- **BYOL:** Trazer licença própria elegível. É necessário verificar o direito de uso e as condições do software; a AWS não cria automaticamente essa licença.
- **rightsizing:** Ajustar capacidade à necessidade observada. Reduzir demais pode prejudicar a aplicação; a recomendação precisa ser avaliada pelo uso real.
- **implantação:** Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.
- **IaC:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **SCT:** Ferramenta de conversão de estrutura de banco em migrações compatíveis. Nem toda estrutura ou regra da aplicação é convertida automaticamente.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **licença:** Direito de usar um software sob condições. Instalar o programa ou inventariá-lo não concede automaticamente esse direito.
- **DMS:** Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.
- **ESG:** Conjunto de aspectos ambientais, sociais e de governança. É uma perspectiva de avaliação organizacional, não uma função de configuração de um recurso.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Task | Termos e serviços citados |
|---|---|
| 1.1 | Proposta de valor da nuvem; infraestrutura global (velocidade de implantação, alcance global); alta disponibilidade, elasticidade, agilidade |
| 1.2 | Well-Architected Framework e os 6 pilares, e as diferenças entre eles |
| 1.3 | Estratégias de adoção; recursos de apoio à migração; CAF (menor risco, melhor ESG, mais receita, eficiência operacional); estratégias de migração (ex.: replicação de banco de dados) |
| 1.4 | Economia ao migrar; custos fixos × variáveis; custos on-premises; BYOL × licença incluída; rightsizing; automação; economias de escala |
| 2.1 | Responsabilidades do cliente, da AWS e compartilhadas; como mudam em RDS, Lambda e EC2 |
| 2.2 | Compliance e governança; Artifact; compliance por região ou setor; Inspector, Security Hub, GuardDuty, Shield; criptografia em trânsito e em repouso; CloudWatch, CloudTrail, Config; relatórios de acesso; onde ficam os logs |
| 2.3 | IAM; proteção do root e tarefas exclusivas do root; menor privilégio; IAM Identity Center; access keys, políticas de senha; armazenamento de credenciais (Secrets Manager, Systems Manager); MFA; cross-account roles; grupos, usuários, políticas customizadas e gerenciadas; identidade federada |
| 2.4 | WAF, Firewall Manager, Shield, GuardDuty; produtos de segurança de terceiros no Marketplace; Knowledge Center, Security Center, Security Blog; Trusted Advisor para problemas de segurança |
| 3.1 | APIs, SDKs, CLI × Console × IaC; operação pontual × processo repetível; modelos cloud, híbrido e on-premises |
| 3.2 | Regiões, AZs, edge locations e a relação entre elas; HA com várias AZs; AZs sem ponto único de falha compartilhado; várias regiões para DR, continuidade, latência e soberania de dados |
| 3.3 | Tipos de instância EC2; ECS, EKS; Fargate, Lambda; Auto Scaling (elasticidade); load balancers |
| 3.4 | Banco no EC2 × gerenciado; RDS, Aurora; DynamoDB; ElastiCache; DMS, SCT |
| 3.5 | Subnets e gateways da VPC; network ACLs, security groups, Inspector; Route 53; VPN, Direct Connect |
| 3.6 | Armazenamento de objetos e classes do S3; EBS, instance store; EFS, FSx; Storage Gateway (cache); lifecycle policies; AWS Backup |
| 3.7 | SageMaker AI, Lex; Athena, Kinesis, Glue, Quick Sight |
| 3.8 | EventBridge, SNS, SQS; Connect, SES; AWS Support; CodeBuild, CodePipeline, X-Ray; AppStream 2.0, WorkSpaces, WorkSpaces Secure Browser; Amplify; IoT Core |
| 4.1 | On-Demand, RIs, Spot, Savings Plans, Dedicated Hosts, Dedicated Instances, Capacity Reservations; flexibilidade de RIs; RIs no Organizations; transferência de dados (entrada, saída, entre regiões, na mesma região); preço por tier de armazenamento |
| 4.2 | Billing; Organizations e faturamento consolidado; cost allocation tags; Budgets, Cost Explorer, Pricing Calculator; Cost and Usage Report |
| 4.3 | Documentação, whitepapers, blogs; Prescriptive Guidance, Knowledge Center, re:Post; customer service e comunidades; Developer, Business, Enterprise On-Ramp, Enterprise nos exemplos consultados; Trusted Advisor, Health Dashboard, Health API; Trust and Safety; APN (ISVs, integradores) e benefícios de ser parceiro; Marketplace (custos, governança, entitlement); Professional Services; solutions architects; Support Center |



**Destaques da revisão:**

**3.8 (outras categorias):** end-user computing = AppStream 2.0, WorkSpaces e WorkSpaces Secure Browser; frontend = **só Amplify**; IoT = **só IoT Core**; developer tools = **CodeBuild, CodePipeline e X-Ray** (e a CLI).

**Antes de ler este trecho:**

- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.


**4.3:** o guia consultado cita exemplos clássicos, e a página comercial oferece planos novos; não se presume substituição de questões. Veja [planos de suporte](../../servicos/custos/planos-de-suporte.md).


## ✅ Serviços no escopo (lista oficial)


**Antes de ler este trecho:**

- **ECR:** O ECR é um repositório de imagens de containers.
- **Elastic Beanstalk:** O Elastic Beanstalk ajuda a implantar aplicações em plataformas compatíveis, provisionando e coordenando recursos AWS para esse ambiente.
- **Lightsail:** O Lightsail reúne recursos como servidores virtuais, armazenamento e rede em ofertas simplificadas.
- **Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.
- **Elastic Disaster Recovery:** Elastic Disaster Recovery replica dados de servidores compatíveis para preparar sua recuperação em máquinas AWS.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **DocumentDB:** DocumentDB armazena e consulta documentos, como registros estruturados de produtos.
- **Neptune:** Neptune é um banco de grafos: representa entidades e as conexões entre elas para consultar relações.
- **AWS VPN:** Site-to-Site VPN liga redes por um túnel criptografado.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **Directory Service:** Directory Service oferece opções para diretórios e integração com Active Directory, conforme a modalidade.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **CloudHSM:** CloudHSM fornece módulos de segurança de hardware para operações e armazenamento criptográfico.
- **Macie:** Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.
- **Detective:** Detective organiza dados compatíveis e suas relações para apoiar investigações de segurança.
- **Control Tower:** Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.
- **EMR:** EMR oferece ambientes gerenciados para frameworks de processamento de dados, com modalidades diferentes de execução.
- **OpenSearch Service:** OpenSearch oferece busca e análise de dados indexados.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **Step Functions:** Step Functions coordena fluxos de trabalho entre etapas e serviços compatíveis.
- **Application Migration Service:** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.
- **RAM:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **ACM:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.
- **MGN:** Sigla usada para Application Migration Service. Apoia a migração de servidores compatíveis; não reescreve automaticamente a aplicação.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Categoria | Serviços → ficha |
|---|---|
| Analytics | [Athena](../../servicos/analytics/athena.md) · [EMR](../../servicos/analytics/emr.md) · [Glue](../../servicos/analytics/glue.md) · [Kinesis](../../servicos/analytics/kinesis.md) · [OpenSearch Service](../../servicos/analytics/opensearch.md) · [Quick Sight](../../servicos/analytics/quicksight.md) · [Redshift](../../servicos/banco-de-dados/redshift.md) |
| Application Integration | [EventBridge](../../servicos/integracao/eventbridge.md) · [SNS](../../servicos/integracao/sns.md) · [SQS](../../servicos/integracao/sqs.md) · [Step Functions](../../servicos/integracao/step-functions.md) |
| Business Applications | [Amazon Connect](../../servicos/aplicacoes/amazon-connect.md) · [SES](../../servicos/aplicacoes/ses.md) |
| Cloud Financial Management | [Budgets](../../servicos/custos/budgets.md) · [Cost and Usage Reports](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) · [Cost Explorer](../../servicos/custos/cost-explorer.md) · [Marketplace](../../servicos/custos/recursos-de-ajuda-e-parceiros.md) |
| Compute | [Batch](../../servicos/computacao/batch.md) · [EC2](../../servicos/computacao/ec2.md) · [Elastic Beanstalk](../../servicos/computacao/elastic-beanstalk.md) · [Lightsail](../../servicos/computacao/lightsail.md) · [Outposts](../../servicos/computacao/outposts-local-zones-wavelength.md) |
| Containers | [ECR](../../servicos/computacao/ecr.md) · [ECS](../../servicos/computacao/ecs.md) · [EKS](../../servicos/computacao/eks.md) |
| Customer Enablement | [AWS Support](../../servicos/custos/planos-de-suporte.md) |
| Database | [Aurora](../../servicos/banco-de-dados/aurora.md) · [DocumentDB](../../servicos/banco-de-dados/documentdb.md) · [DynamoDB](../../servicos/banco-de-dados/dynamodb.md) · [ElastiCache](../../servicos/banco-de-dados/elasticache.md) · [Neptune](../../servicos/banco-de-dados/neptune.md) · [RDS](../../servicos/banco-de-dados/rds.md) |
| Developer Tools | [AWS CLI](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [CodeBuild, CodePipeline](../../servicos/desenvolvimento/code-services.md) · [X-Ray](../../servicos/desenvolvimento/x-ray.md) |
| End User Computing | [AppStream 2.0, WorkSpaces, WorkSpaces Secure Browser](../../servicos/aplicacoes/workspaces-e-appstream.md) |
| Frontend Web and Mobile | [Amplify](../../servicos/aplicacoes/amplify-e-appsync.md) |
| Internet of Things | [IoT Core](../../servicos/aplicacoes/iot-core-e-greengrass.md) |
| Machine Learning | [Comprehend, Lex, Polly, Rekognition, Textract, Transcribe, Translate](../../servicos/ia-ml/servicos-de-ia-prontos.md) · [Amazon Q](../../servicos/ia-ml/amazon-q.md) · [SageMaker AI](../../servicos/ia-ml/sagemaker-ai.md) |
| Management and Governance | [Auto Scaling](../../servicos/computacao/ec2-auto-scaling.md) · [CloudFormation](../../servicos/gerenciamento/cloudformation.md) · [CloudTrail](../../servicos/gerenciamento/cloudtrail.md) · [CloudWatch](../../servicos/gerenciamento/cloudwatch.md) · [Compute Optimizer, License Manager, Service Quotas](../../servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) · [Config](../../servicos/gerenciamento/config.md) · [Control Tower](../../servicos/gerenciamento/control-tower.md) · [Health Dashboard](../../servicos/gerenciamento/health-dashboard.md) · [Management Console](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [Organizations](../../servicos/gerenciamento/organizations.md) · [Service Catalog](../../servicos/gerenciamento/service-catalog-e-ram.md) · [Systems Manager](../../servicos/gerenciamento/systems-manager.md) · [Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md) · [Well-Architected Tool](../01-conceitos-de-nuvem/04-well-architected-framework.md) |
| Migration and Transfer | [Application Discovery Service, Migration Evaluator, Migration Hub](../../servicos/migracao/discovery-migration-hub-e-evaluator.md) · [Application Migration Service](../../servicos/migracao/application-migration-service.md) · [DMS e SCT](../../servicos/migracao/dms-e-sct.md) — o Application Migration Service hoje se chama **AWS Transform MGN** |
| Networking and Content Delivery | [API Gateway](../../servicos/redes/api-gateway.md) · [CloudFront](../../servicos/redes/cloudfront.md) · [Direct Connect](../../servicos/redes/direct-connect.md) · [Global Accelerator](../../servicos/redes/global-accelerator.md) · [PrivateLink, Transit Gateway](../../servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) · [Route 53](../../servicos/redes/route-53.md) · [VPC](../../servicos/redes/vpc.md) · [AWS VPN, Site-to-Site VPN, Client VPN](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) |
| Security, Identity, and Compliance | [Artifact](../../servicos/seguranca/artifact.md) · [ACM](../../servicos/seguranca/certificate-manager.md) · [CloudHSM](../../servicos/seguranca/cloudhsm.md) · [Cognito](../../servicos/seguranca/cognito.md) · [Detective](../../servicos/seguranca/detective.md) · [Directory Service](../../servicos/seguranca/directory-service.md) · [Firewall Manager](../../servicos/seguranca/firewall-manager-e-network-firewall.md) · [GuardDuty](../../servicos/seguranca/guardduty.md) · [IAM](../../servicos/seguranca/iam.md) · [IAM Identity Center](../../servicos/seguranca/iam-identity-center.md) · [Inspector](../../servicos/seguranca/inspector.md) · [KMS](../../servicos/seguranca/kms.md) · [Macie](../../servicos/seguranca/macie.md) · [RAM](../../servicos/gerenciamento/service-catalog-e-ram.md) · [Secrets Manager](../../servicos/seguranca/secrets-manager-e-parameter-store.md) · [Security Hub](../../servicos/seguranca/security-hub.md) · [Shield](../../servicos/seguranca/shield.md) · [WAF](../../servicos/seguranca/waf.md) |
| Serverless | [Fargate](../../servicos/computacao/fargate.md) · [Lambda](../../servicos/computacao/lambda.md) |
| Storage | [AWS Backup](../../servicos/armazenamento/aws-backup.md) · [EBS](../../servicos/armazenamento/ebs.md) · [EFS](../../servicos/armazenamento/efs.md) · [Elastic Disaster Recovery](../../servicos/armazenamento/elastic-disaster-recovery.md) · [FSx](../../servicos/armazenamento/fsx.md) · [S3 e S3 Glacier](../../servicos/armazenamento/s3-classes-de-armazenamento.md) · [Storage Gateway](../../servicos/armazenamento/storage-gateway.md) |


## ❌ Fora do escopo (lista oficial, não exaustiva)



Estes serviços não são prioridade do conteúdo oficial consultado. Leia o requisito e as alternativas; o nome sozinho não constitui uma regra universal de eliminação. **Todos estão documentados** no repositório, com

aviso de que não caem na prova — use para reconhecer os distratores e para o dia a dia.

**Antes de ler este trecho:**

- **MemoryDB:** MemoryDB oferece um banco em memória com mecanismos de durabilidade.
- **MSK:** Kafka é uma plataforma de fluxo de eventos; MSK é a oferta gerenciada compatível da AWS. A aplicação ainda precisa produzir e consumir os registros.
- **workflow:** Fluxo de trabalho descrito por etapas, decisões e estados. Coordenar etapas é diferente de escrever o programa que realiza cada tarefa.
- **refactor:** Redesenhar partes da aplicação para atender novos objetivos. Pode trazer vantagens, mas demanda mudanças, testes e esforço.
- **SWF:** Simple Workflow Service: serviço de coordenação de trabalhos distribuídos com modelo próprio. É referência especializada, não sinônimo de todas as ferramentas de fluxo.
- **AMS:** Managed Services: oferta de administração operacional conforme cobertura contratada. Não presuma que inclui toda tarefa de qualquer aplicação.
- **IVS:** Interactive Video Service: serviço associado à transmissão de vídeo. Seus canais e condições precisam ser escolhidos conforme a experiência desejada.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Categoria | Serviços → onde estão documentados |
|---|---|
| Analytics | [AppFlow, Clean Rooms, Data Exchange, DataZone, MSK](../../servicos/analytics/lake-formation-msk-e-outros.md) |
| Application Integration | [AppFabric, Simple Workflow Service (SWF)](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) |
| Business Applications | [WorkDocs](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) |
| Compute | [Copilot](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) · [Wavelength](../../servicos/computacao/outposts-local-zones-wavelength.md) |
| Cost / Financial Management | [Application Cost Profiler, DevPay](../../servicos/fora-do-escopo/gerenciamento-e-custos.md) · [Billing Conductor](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) |
| Customer Enablement | [AWS Activate, AWS IQ, AWS Managed Services (AMS)](../../servicos/custos/recursos-de-ajuda-e-parceiros.md) |
| Database | [Keyspaces](../../servicos/banco-de-dados/keyspaces-timestream-e-outros.md) · [MemoryDB](../../servicos/banco-de-dados/memorydb.md) · [AppConfig (listado assim na página)](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) |
| Developer Tools | [Application Composer, CodeGuru](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) · [CodeArtifact, CodeDeploy](../../servicos/desenvolvimento/code-services.md) · [CloudShell](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [Device Farm](../../servicos/aplicacoes/amplify-e-appsync.md) |
| Game Tech | [GameLift, Lumberyard](../../servicos/fora-do-escopo/midia-e-jogos.md) |
| IoT | [IoT Device Defender, Monitron](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) · [IoT Greengrass](../../servicos/aplicacoes/iot-core-e-greengrass.md) |
| Machine Learning | [Fraud Detector, Personalize](../../servicos/ia-ml/servicos-de-ia-prontos.md) · [Lookout for Metrics, Panorama](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) |
| Management and Governance | [Chatbot, Data Lifecycle Manager, Launch Wizard](../../servicos/fora-do-escopo/gerenciamento-e-custos.md) · [Elastic Transcoder](../../servicos/fora-do-escopo/midia-e-jogos.md) |
| Media Services | [Elemental (MediaConnect, MediaConvert, MediaLive, MediaPackage, MediaStore, MediaTailor, Appliances and Software), IVS](../../servicos/fora-do-escopo/midia-e-jogos.md) |
| Migration and Transfer | [Migration Hub Refactor Spaces](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) · [Transfer Family](../../servicos/migracao/datasync-e-transfer-family.md) |
| Networking | [Cloud Map, Network Access Analyzer, VPC Lattice](../../servicos/fora-do-escopo/rede-e-diretorio.md) · [Ground Station](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) |
| Security | [Cloud Directory](../../servicos/fora-do-escopo/rede-e-diretorio.md) · [Network Firewall](../../servicos/seguranca/firewall-manager-e-network-firewall.md) |
| Robotics | [RoboMaker](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) |
| Storage | [FSx for Lustre](../../servicos/armazenamento/fsx.md) |


> Nas fichas, os serviços fora do escopo aparecem com ❌ *fora do escopo* ao lado do nome. A categoria
> [❌ Fora do escopo da prova](../../servicos/README.md) reúne os que não pertencem a nenhuma outra ficha.

## ⚪ Nem dentro nem fora: não aparecem em nenhuma das listas



Continuam úteis como contexto, mas têm baixa chance de cair: **Local Zones**, **família Snow** (Snowball Edge),
**Antes de ler este trecho:**

- **Audit Manager:** Audit Manager ajuda a coletar e organizar evidências em avaliações baseadas em estruturas de controles compatíveis.
- **Bedrock:** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.
- **Amazon MQ:** Amazon MQ oferece brokers gerenciados compatíveis com tecnologias suportadas, como ActiveMQ e RabbitMQ.
- **MQ:** Intermediário de mensagens entre componentes. Sua interface e seus protocolos precisam ser compatíveis com as aplicações conectadas.


**DataSync**, **Bedrock**, **Kendra**, **Audit Manager**, **AppSync**, **Amazon MQ**, **Cloud9**, **CodeCommit**,
**Antes de ler este trecho:**

- **STS:** Serviço que fornece credenciais temporárias AWS. Essas credenciais permitem uma sessão autorizada dentro das permissões aplicáveis.


**CodeStar**, **Timestream**, **Lake Formation**, **STS**.

> Versões traduzidas antigas da lista ainda citam Audit Manager, AppSync e Kendra; a lista atual em inglês não.

## ⏸️ No escopo, mas fechados a novos clientes



**AWS Migration Hub** e **AWS Application Discovery Service** (desde 07/11/2025). Ainda podem cair na prova.
