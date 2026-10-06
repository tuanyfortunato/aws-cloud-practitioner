# 🔄 O que mudou em 2025-2026: valor da prova × valor atual

<!-- didatico:inicio -->
## 🧭 Antes de ler

**Por que esta página existe?** Um número ou nome de um material antigo pode não corresponder mais à oferta comercial ou ao guia do exame.

**Como usar?** Esta página registra diferenças e verificações do material. Leia a observação associada ao tema para saber qual contexto está sendo descrito.

**Exemplo:** Ao estudar suporte, confira se o exemplo descreve um modelo do guia ou uma oferta comercial atual. Não escolha uma resposta apenas porque reconhece um nome antigo.
<!-- didatico:fim -->

> Verificado em fontes oficiais da AWS em **04/10/2026** ([relatório](../../fontes/verificacao-fontes-oficiais-2026-10.md) e [rodadas 3 e 4](../../fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md)).
> Pesquisa original: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md).

## Como interpretar mudanças

A oferta comercial e o conteúdo publicado da prova podem apresentar exemplos diferentes.

A consulta desta revisão encontrou **Developer, Business, Enterprise On-Ramp e Enterprise** na

[task 4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html),

enquanto a [página comercial](https://aws.amazon.com/premiumsupport/plans/) apresenta os planos novos.

Estude ambos com seus nomes e condições. Um lançamento não comprova a data de atualização das questões.

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **TB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **MiB:** Unidades em escala binária: cada nível corresponde a 1.024 do anterior. MiB e MB não são a mesma unidade; preserve a unidade indicada pelo serviço.
- **PUT:** Nomes comuns de operações: enviar ou gravar, obter e excluir. O significado preciso e as permissões dependem da API usada.
- **objeto:** Unidade de dados guardada no armazenamento de objetos: conteúdo, identificação e informações associadas. Não é uma máquina nem um programa em execução.

Números como S3 50 TB e SQS 1 MiB precisam do contexto: tamanho de objeto não é limite de um PUT simples

ou upload pelo console. Não escolha uma resposta apenas porque contém o número mais recente.

As listas de serviços são não exaustivas; ausência não equivale a exclusão formal.

Veja a [auditoria](auditoria-conteudo-2026-10.md) e o [roteiro sem console](estudar-sem-console.md).

## Tabela de mudanças

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **EKS:** O EKS oferece Kubernetes gerenciado.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **Storage Gateway:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.
- **AWS Backup:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.
- **Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.
- **Macie:** Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.
- **Detective:** Detective organiza dados compatíveis e suas relações para apoiar investigações de segurança.
- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **Trusted Advisor:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.
- **Amazon QuickSight / QuickSight:** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis.
- **Amazon SageMaker AI / SageMaker AI:** SageMaker AI oferece recursos para etapas do desenvolvimento e operação de modelos.
- **AI:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **Bedrock:** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **AWS Application Migration Service / Application Migration Service:** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.
- **Budgets:** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **vCPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **IOPS:** Quantidade de operações de leitura e escrita por segundo. Ajuda a descrever o comportamento de um armazenamento, mas não mede sozinha a quantidade de bytes transferidos.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **CDN:** Rede de distribuição de conteúdo. Ela aproxima entrega de conteúdo dos usuários e pode manter cópias em cache conforme as regras.
- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.
- **SCP:** Política de controle de serviços usada na organização para limitar permissões disponíveis em contas às quais se aplica. Ela não concede acesso ao usuário sozinha.
- **ACM:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.
- **DDoS:** Ataque distribuído que tenta sobrecarregar um serviço e impedir seu uso legítimo. É diferente de tentar explorar um campo vulnerável de um programa.
- **BI:** Análise e apresentação de dados para apoiar decisões. Um painel depende de dados adequados e de uma interpretação correta dos indicadores.
- **FIFO:** Primeiro a entrar, primeiro a sair. No SQS, a ordenação considera grupos de mensagens; deduplicação no envio não garante ausência de repetição de efeitos no programa.
- **RI:** Benefício e condições de reserva para configurações compatíveis. Não confunda desconto com qualquer garantia universal de capacidade.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
- **runtime:** Ambiente que executa código de uma linguagem ou plataforma. Compatibilidade de bibliotecas e versões deve ser avaliada.
- **IDE:** Ambiente de desenvolvimento com ferramentas para editar e trabalhar com código. Não é necessariamente o local que hospeda a aplicação em produção.
- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.
- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.
- **provisionado:** Recurso ou capacidade já disponibilizado para uso. Em algumas cobranças, a disponibilidade mantida importa mesmo sem execução de trabalho de negócio.
- **MGN:** Sigla usada para Application Migration Service. Apoia a migração de servidores compatíveis; não reescreve automaticamente a aplicação.
- **PITR:** Recuperação para um ponto no tempo conforme o serviço e a janela configurada. É diferente de manter continuamente uma aplicação alternativa atendendo.

| Tema | Valor antigo | Valor atual (oficial) | Desde | Onde estudar |
|---|---|---|---|---|
| **Planos de suporte** | Basic, Developer, Business, Enterprise On-Ramp, Enterprise | **Basic, Business Support+ (US$ 29/mês por conta, crítico 30 min), Enterprise (US$ 5.000/mês, 15 min), Unified Operations (US$ 50.000/mês, 5 min, compromisso de 90 dias)**. Legados encerram em 01/01/2027 | 02/12/2025 | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |
| Enterprise Support | A partir de US$ 15.000/mês | Mínimo de **US$ 5.000/mês** | 02/12/2025 | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |
| Tamanho máximo de objeto S3 | 5 TB | **50 TB**, em todas as classes (não vale no GovCloud) | 02/12/2025 | [S3](../../servicos/armazenamento/s3.md) |
| Mensagem SQS | 256 KiB | **1 MiB** (Standard e FIFO; Lambda event source mapping também) | 04/08/2025 | [SQS](../../servicos/integracao/sqs.md) |
| Mensagem SNS | 256 KiB | Até **1 MiB** configurando `MaximumMessageSize` no tópico; o **padrão continua 256 KiB** | 18/09/2026 | [SNS](../../servicos/integracao/sns.md) |
| Free Tier | Always Free + 12 meses + trials | US$ 100 no cadastro + até US$ 100 por atividades (EC2, RDS, Lambda, Bedrock, Budgets); Free plan por 6 meses ou até acabar o crédito | 15/07/2025 | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| Categorias do Trusted Advisor | 5 | **6** (+ Operational Excellence) | — | [Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md) |
| Família Snow | Snowcone, Snowball Edge, Snowmobile | Snowball Edge só para clientes existentes; novos → DataSync, AWS Data Transfer Terminal ou parceiros. **Saiu da lista do escopo** | 07/11/2025 | [Snow Family](../../servicos/migracao/snow-family.md) |
| AWS IQ | Contratar especialistas | Encerrado → AWS Marketplace Professional Services. **Fora do escopo** | 28/05/2026 | [Recursos de ajuda](../../servicos/custos/recursos-de-ajuda-e-parceiros.md) |
| Cloud9 / CodeStar / CodeCommit | Ferramentas de dev | Cloud9 fechado a novos clientes; CodeStar descontinuado; CodeCommit de volta a GA. **Nenhum dos três está na lista atual** | 2024–2025 | [Code*](../../servicos/desenvolvimento/code-services.md) |
| QuickSight | Amazon QuickSight | **Amazon Quick Sight** (BI dentro do Amazon Quick Suite, hoje "Amazon Quick") | — | [Quick Sight](../../servicos/analytics/quicksight.md) |
| SageMaker | Amazon SageMaker | **Amazon SageMaker AI** | — | [SageMaker AI](../../servicos/ia-ml/sagemaker-ai.md) |
| Timestream | Séries temporais | LiveAnalytics fechado a novos clientes | 20/06/2025 | [Keyspaces, Timestream e outros](../../servicos/banco-de-dados/keyspaces-timestream-e-outros.md) |
| Savings Plans | Compute, EC2 Instance, SageMaker | + **Database Savings Plans**: até 35% (serverless) / até 20% (provisionado), 1 ano, sem pagamento adiantado | 02/12/2025 | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| Application Migration Service | AWS Application Migration Service (MGN) | Hoje se chama **AWS Transform MGN** (a prova usa o nome antigo) | — | [MGN](../../servicos/migracao/application-migration-service.md) |
| Trusted Advisor no Basic | "7 core checks" (com IAM Use) | Service limits + **5 checks de segurança** (sem IAM Use) | — | [Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md) |
| EBS gp3 | Até 16 TB / 16.000 IOPS | Até **64 TB / 80.000 IOPS** (base continua 3.000 IOPS e 125 MB/s) | — | [EBS](../../servicos/armazenamento/ebs.md) |
| Fargate | Até 16 vCPU / 120 GB | Até **32 vCPU / 244 GB** | — | [Fargate](../../servicos/computacao/fargate.md) |
| DynamoDB PITR | 35 dias fixos | Configurável de **1 a 35 dias** | 01/2025 | [DynamoDB](../../servicos/banco-de-dados/dynamodb.md) |
| Testes gratuitos de segurança | GuardDuty, Macie, Detective (30 dias), Inspector (15 dias) | Mesmos prazos, mas vinculados ao **Paid plan** no Free Tier novo | — | [GuardDuty](../../servicos/seguranca/guardduty.md) |
| **Tarefas exclusivas do root** | Inclui alterar o nome da conta e mudar o plano de suporte | ✔️ **Nome da conta, contatos e regiões não exigem root**; **mudar o plano de suporte saiu da lista**. Continuam: e-mail/senha/access keys do root, fechar conta standalone, restaurar admin IAM, Billing e faturas fiscais, GovCloud, vendedor de RI, recuperação de chave KMS, MFA Delete, desbloquear políticas S3/SQS | 10/2026 | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md) |
| Snowball Edge | Disponível | Fim do suporte comercial em **31/12/2026** (Storage e Compute Optimized, regiões comerciais) | 31/12/2026 | [Snow Family](../../servicos/migracao/snow-family.md) |
| Amazon Q Developer (IDE) | Plugins de IDE | Fim de suporte dos plugins de IDE em **30/04/2027**; alternativa indicada: **Kiro** | 30/04/2027 | [Amazon Q](../../servicos/ia-ml/amazon-q.md) |
| Organizations | Sem SCP padrão | Organizações criadas pelo console após 10/07/2026 recebem SCP que nega sair da organização e fechar a conta | 10/07/2026 | [Organizations](../../servicos/gerenciamento/organizations.md) |
| Storage Gateway | S3 File, FSx File, Volume e Tape Gateway | **FSx File Gateway** (e Tape Gateway em Snowball Edge) descontinuados para novos clientes; S3 File e Volume continuam | — | [Storage Gateway](../../servicos/armazenamento/storage-gateway.md) |
| GuardDuty | Planos S3, EKS, Runtime, Malware, RDS, Lambda | + **AI Protection** e Malware Protection para AWS Backup | — | [GuardDuty](../../servicos/seguranca/guardduty.md) |
| Migration Hub / Application Discovery Service | Abertos | **Fechados a novos clientes** (continuam no escopo) | 07/11/2025 | [Discovery, Hub e Evaluator](../../servicos/migracao/discovery-migration-hub-e-evaluator.md) |
| Amazon Q Business | Assistente corporativo | Em manutenção, sem novos clientes; apps podem ser conectados ao Quick Suite | 30/07/2026 | [Amazon Q](../../servicos/ia-ml/amazon-q.md) |
| ACM | Certificados públicos só em serviços integrados | + certificados públicos **exportáveis** (pagos, validade de 395 dias) | 17/06/2025 | [ACM](../../servicos/seguranca/certificate-manager.md) |
| CloudFront | Pagamento por uso | + **planos de preço fixo** (Free, Pro US$ 15, Business US$ 200, Premium US$ 1.000) com CDN, WAF e DDoS | 18/11/2025 | [CloudFront](../../servicos/redes/cloudfront.md) |

## Serviços em manutenção ou encerrados (não estudar a fundo)

**Antes de ler este trecho:**

- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.

**Fechados a novos clientes desde 07/11/2025:** Amazon Glacier (serviço original de *vaults*, diferente das classes S3 Glacier), S3 Object Lambda, Systems Manager Change Manager e Incident Manager, CodeCatalyst, CodeGuru Reviewer, Cloud Directory, Snowball Edge, Fraud Detector, Migration Hub, Application Discovery Service.

**Antes de ler este trecho:**

- **AWS Audit Manager / Audit Manager:** Audit Manager ajuda a coletar e organizar evidências em avaliações baseadas em estruturas de controles compatíveis.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.

**Desde 30/04/2026:** AWS Audit Manager, AWS App Runner, IoT FleetWise.

**Antes de ler este trecho:**

- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.

**Desde 31/05/2026:** CloudTrail Lake (anúncio de 31/03/2026; trails e Event history continuam).

**Antes de ler este trecho:**

- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **Directory Service:** Directory Service oferece opções para diretórios e integração com Active Directory, conforme a modalidade.
- **AD:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.

**Desde 30/07/2026:** Amazon Kendra, Amazon Q Business, Directory Service Simple AD, Service Catalog AppRegistry, Cognito Sync. Bedrock Agents passou a se chamar "Bedrock Agents Classic".

**Antes de ler este trecho:**

- **CLI:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **DMS:** Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.
- **QLDB:** Quantum Ledger Database: oferta histórica de registro verificável descrita na ficha de bancos especializados. Confira seu encerramento antes de tratar o exemplo como uma opção atual.

**Encerrados:** Application Cost Profiler (30/09/2024), QLDB (31/07/2025), RoboMaker (10/09/2025), Elastic Transcoder e Elemental MediaStore (13/11/2025), Panorama (31/05/2026), Copilot CLI (fim de suporte em 12/06/2026), Lookout for Metrics (12/09/2025), Lookout for Vision (31/10/2025), IoT Analytics (15/12/2025), IoT Events (20/05/2026), AWS IQ (28/05/2026). Anunciados em maio/2025: Inspector Classic, Pinpoint, Panorama, Connect Voice ID, DMS Fleet Advisor.

**WorkSpaces:** PCoIP e Pools em *sunset* (o serviço continua no escopo).

**Antes de ler este trecho:**

- **AMS:** Managed Services: oferta de administração operacional conforme cobertura contratada. Não presuma que inclui toda tarefa de qualquer aplicação.

**Próximos encerramentos (tabela oficial de *sunset*):** App Mesh (30/09/2026), IoT Greengrass V1 (01/10/2026), Proton, FinSpace e Lookout for Equipment (07/10/2026), Pinpoint (30/10/2026), AMS Advanced (30/06/2027). Monitron fechado a novos clientes.

**Encerrado em 29/09/2026:** Amazon Mechanical Turk (a lista oficial de tarefas do root ainda cita o vínculo com o MTurk).

**Encerrados antes:** Snowmobile (14/03/2024) e WorkDocs (25/04/2025), confirmados na página "Services in Full Shutdown".

**Antes de ler este trecho:**

- **O3DE:** Motor de desenvolvimento 3D. Desenvolver o conteúdo e operar os recursos necessários são trabalhos diferentes.

**Renomeações:** AWS Chatbot → Amazon Q Developer in chat applications (19/02/2025); Lumberyard não é mais oferecido (sucessor: O3DE).

Tabela oficial: [AWS services sunset](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html).

## Divergências antigas resolvidas pela verificação

**Antes de ler este trecho:**

- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **IEM:** Nome histórico de uma oferta de acompanhamento de eventos de infraestrutura. Leia o contexto e a oferta atual indicados na ficha.

| Antes | Resultado oficial |
|---|---|
| Read replicas de Oracle/SQL Server: 5 ou 15? | **Até 5** (Oracle, SQL Server); **até 3** (Db2); até 15 (MySQL, MariaDB, PostgreSQL) |
| Desconto máximo de Convertible RI: 66% ou 54%? | **Até 66%** (guia de Savings Plans/RIs) |
| Glacier Flexible Retrieval Expedited 1–5 min | Não confirmado em página oficial consultada (Standard 3–5 h e Bulk 5–12 h confirmados) |
| Enterprise On-Ramp inclui 1 IEM por ano | A página fala em **1 engajamento AWS Countdown por ano** |
| Preços clássicos de Developer (US$ 29), Business (US$ 100), On-Ramp (US$ 5.500) | Não aparecem mais nas páginas oficiais; trate como valores históricos |
