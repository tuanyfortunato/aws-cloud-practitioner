# Auditoria de cobertura e aprofundamento — CLF-C02

<!-- didatico:inicio -->
## 🧭 Antes de ler

**Por que esta página existe?** Você precisa saber o que foi conferido no material e quais limites essa revisão tem, em vez de assumir que uma lista de arquivos prova domínio do exame.

**Como usar?** Esta página documenta a revisão realizada, sua cobertura e suas ressalvas. Ela serve para acompanhar a qualidade do material; não é uma aula sobre um serviço.

**Exemplo:** Use a auditoria para localizar a revisão de um tema e depois leia sua explicação. Um tópico coberto ainda pode precisar de estudo e confirmação de entendimento.
<!-- didatico:fim -->

Revisão iniciada em **04/10/2026**, a partir do commit `1bdfdbff098dc1648c633fb86c39ff6f968a4b85`.

A data identifica a consulta; não assegura que páginas e ofertas permanecerão iguais até sua prova.

## Resultado

O repositório tem **cobertura temática ampla dos quatro domínios e das 19 tasks oficiais**, distribuída em

41 tópicos e 105 fichas de serviços/famílias. Não foi identificado um domínio ou categoria inteira ausente.
**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

Isso não prova que cada possibilidade de questão esteja coberta: a própria AWS declara que o guia e as listas

não são exaustivos. Não é correto prometer “100% do que cairá”.

O material original já tinha analogias, configurações, comparações e questões. A profundidade era desigual:

algumas fichas explicavam detalhadamente componentes, e outras se concentravam em associação de nome e função.

Faltava um caminho uniforme para explicar a sequência de uso, pré-requisitos e o sentido de “pode/não pode”.

## Cobertura por domínio

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.
- **federação:** Uso de uma identidade de um provedor em outro ambiente por uma relação de confiança. Não significa que todos os usuários passam a ser administradores.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.
- **compliance / conformidade:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.
- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **CAF:** Cloud Adoption Framework: orientação para preparar capacidades da organização na adoção de nuvem. Não é uma ferramenta que transfere servidores.

| Domínio oficial | Tasks | Tópicos locais | Cobertura encontrada e aprofundamento |
|---|---|---|---|
| 1 — Conceitos de nuvem | 1.1–1.4 | 7 | Benefícios, arquitetura, seis pilares, CAF, migração e economia; decisões e exemplos sobre limites de cada conceito |
| 2 — Segurança e conformidade | 2.1–2.4 | 10 | Responsabilidades, root, IAM/federação, criptografia, compliance, logs e proteção; separação de rede, autorização, detecção e correção |
| 3 — Tecnologia e serviços | 3.1–3.8 | 18 | Acesso, infraestrutura, compute, banco, rede, armazenamento, analytics/IA e outras categorias; recursos e fluxo de uso sem depender da tela |
| 4 — Cobrança, preços e suporte | 4.1–4.3 | 6 | Compras, custos, relatórios, suporte e recursos de ajuda; custo residual, compromissos, alertas e primeira resposta |

A ligação de **cada task** aos arquivos está em [Escopo oficial](escopo-oficial.md).

A numeração local é editorial: tópico local 3.7 (bancos) não é task oficial 3.7 (IA/analytics).

## Categorias da lista oficial e onde estão

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **EKS:** O EKS oferece Kubernetes gerenciado.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **ECR:** O ECR é um repositório de imagens de containers.
- **Lightsail:** O Lightsail reúne recursos como servidores virtuais, armazenamento e rede em ofertas simplificadas.
- **Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **EFS:** O EFS oferece um sistema de arquivos compartilhado.
- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **Storage Gateway:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **ElastiCache:** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **DocumentDB:** DocumentDB armazena e consulta documentos, como registros estruturados de produtos.
- **Neptune:** Neptune é um banco de grafos: representa entidades e as conexões entre elas para consultar relações.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **Direct Connect:** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.
- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.
- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.
- **Glue:** Glue oferece catálogo e ferramentas de integração e transformação de dados.
- **EMR:** EMR oferece ambientes gerenciados para frameworks de processamento de dados, com modalidades diferentes de execução.
- **SageMaker AI:** SageMaker AI oferece recursos para etapas do desenvolvimento e operação de modelos.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.
- **Step Functions:** Step Functions coordena fluxos de trabalho entre etapas e serviços compatíveis.
- **CLI:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
- **X-Ray:** X-Ray ajuda a acompanhar requisições em aplicações instrumentadas, reunindo rastreamentos e relações entre componentes.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **SES:** SES oferece envio de e-mail para aplicações, com recursos de identidade, acompanhamento e controle de envio.
- **Cost Explorer:** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.
- **Budgets:** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.
- **RAM:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **ML / machine learning:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **SCT:** Ferramenta de conversão de estrutura de banco em migrações compatíveis. Nem toda estrutura ou regra da aplicação é convertida automaticamente.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.
- **CUR:** Relatório de custos e uso. Ele ajuda a analisar consumo registrado; é diferente de uma estimativa antes de criar recursos.
- **DRS:** Sigla usada para Elastic Disaster Recovery. Replicação prepara uma recuperação; testes e dependências continuam necessários.
- **MGN:** Sigla usada para Application Migration Service. Apoia a migração de servidores compatíveis; não reescreve automaticamente a aplicação.
- **DMS:** Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.

| Categoria oficial | Local de estudo e observação |
|---|---|
| Analytics | [Fichas](../../servicos/README.md): Athena, EMR, Glue, Kinesis, OpenSearch, Quick Sight; Redshift está na pasta de bancos |
| Application Integration | EventBridge, SNS, SQS e Step Functions nas fichas de integração |
| Business Applications | Connect e SES nas fichas de aplicações |
| Cloud Financial Management | Budgets, Cost Explorer, CUR/Data Exports; Marketplace em recursos de ajuda |
| Compute | Batch, EC2, Beanstalk, Lightsail e Outposts em computação |
| Containers | ECR, ECS e EKS em computação |
| Customer Enablement | AWS Support em custos/suporte |
| Database | Aurora, DocumentDB, DynamoDB, ElastiCache, Neptune e RDS em bancos |
| Developer Tools | CLI, CodeBuild, CodePipeline e X-Ray em desenvolvimento |
| End User Computing | WorkSpaces, AppStream e Secure Browser na ficha conjunta |
| Frontend Web and Mobile | Amplify na ficha de aplicações |
| Internet of Things | IoT Core na ficha de IoT; separar Greengrass fora do escopo |
| Machine Learning | APIs prontas, Amazon Q e SageMaker AI em IA/ML |
| Management and Governance | Auto Scaling, CloudFormation, CloudTrail, CloudWatch, Config, Organizations e demais em computação/gerenciamento; Console na ficha de acesso; Well-Architected Tool no tópico 1.4 e ficha de utilitários |
| Migration and Transfer | Discovery, MGN, DMS, Evaluator, Hub e SCT em migração |
| Networking and Content Delivery | API Gateway, CloudFront, Direct Connect, Global Accelerator, PrivateLink, Route 53, Transit Gateway, VPC e modalidades VPN em redes |
| Security, Identity, and Compliance | Identidade, chaves, proteção, detecção e documentos em segurança; RAM em gerenciamento |
| Serverless | Fargate e Lambda em computação |
| Storage | Backup, EBS, EFS, DRS, FSx, S3/Glacier e Storage Gateway em armazenamento |

“Coberto numa ficha conjunta” não significa uma ficha independente para cada nome.

As 105 fichas incluem extras e cinco arquivos de famílias fora do escopo. Não são 105 serviços obrigatórios da prova.

## Correções e limites identificados

**Antes de ler este trecho:**

- **GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.
- **Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.
- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
- **PUT:** Nomes comuns de operações: enviar ou gravar, obter e excluir. O significado preciso e as permissões dependem da API usada.
- **DB:** Abreviação de database, ou banco de dados. Cada mecanismo oferece formas e garantias próprias de armazenamento e consulta.

| Encontrado | Tratamento nesta revisão | Evidência oficial |
|---|---|---|
| “O guia atual cobra os planos novos” | Removida a certeza. Guia consultado cita Developer, Business, Enterprise On-Ramp e Enterprise; página comercial apresenta Business Support+, Enterprise e Unified Operations. Estudar os dois com contexto | [Task 4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html), [planos comerciais](https://aws.amazon.com/premiumsupport/plans/) |
| “700 é cerca de 70%” | Explicada a nota escalonada; meta de acerto em simulado é editorial | [Resultados da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) |
| Escolher alternativa só porque contém um valor atual ou um serviço no escopo | Enfatizada leitura do requisito/contexto; listas não são regra universal de eliminação | [Guia](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html), [lista no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html) |
| “Lambda nunca ultrapassa 15 minutos” e “nada quando não executa” | Delimitado o caso de funções convencionais e cobrança base. Durable Functions/MicroVMs e capacidade provisionada exigem contexto próprio | [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), [Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), [preços](https://aws.amazon.com/lambda/pricing/) |
| Um único máximo do S3 como se toda forma de upload fosse igual | Diferenciados PUT simples, console e multipart; não sugerida memorização descontextualizada | [Uploads S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) |
| Risco de generalizar RDS Multi-AZ | Diferenciado standby de DB instance de modalidades de cluster que podem ter leitores | [Multi-AZ DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html) |
| “Detectar”, “permitir” e “corrigir” misturados | Fichas separam achado, autorização, configuração e ação operacional | [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html), [Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html), [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) |

Os relatórios antigos em `fontes/` permanecem como registros históricos, sem edição.

Quando houver divergência, esta revisão informa a leitura mais recente e suas fontes; um lançamento comercial

não permite deduzir a data em que uma questão de certificação será alterada.

## O que foi acrescentado

**41 aprofundamentos**, cada um com funcionamento, decisão, limite e exercício com resposta comentada.

**105 fichas práticas**, cada uma com recursos, escolhas, sequência, capacidade condicional, limite e caso comentado.

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.

Um [roteiro sem console](estudar-sem-console.md) com modelo de raciocínio e exemplo integrado.

Cobertura obrigatória no gerador: falha se houver tópico/ficha sem aprofundamento ou registro extra sem destino.

**Antes de ler este trecho:**

- **SLA:** Acordo de nível de serviço com condições e medidas próprias. Não é garantia de que a aplicação do cliente nunca falhará.

Os exemplos não acrescentam preços voláteis nem novas promessas de SLA.

As fichas mantêm sua documentação oficial e usam seus fundamentos já descritos; esta revisão fez consultas

diretas adicionais para os pontos corrigidos e comparações centrais. Não é uma revalidação linha a linha de

todas as datas, quotas, preços e anúncios históricos presentes nas fontes.

## Lacunas que ainda exigem estudo externo

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.

| Limite | Consequência prática |
|---|---|
| Um simulado de 65 questões, reutilizado por domínio | Repetir o mesmo banco pode medir memória da resposta; complemente com questões inéditas |
| Novos exercícios discursivos não entram no banco de múltipla escolha | Use-os para explicar decisões; o treino cronometrado continua no simulado existente |
| Sem experiência prática obrigatória | Suficiente para aprender seleção conceitual; não comprova habilidade de operar produção |
| Listas não exaustivas e páginas sujeitas a mudança | Consulte o guia antes da prova; não há garantia de cobertura de todas as questões |
| Preços, disponibilidade e limites variam | Para implantar, verifique a documentação específica da região/modalidade e a página atual de preço |

## Verificação das alterações

**Antes de ler este trecho:**

- **índice:** Estrutura adicional para apoiar consultas. Pode melhorar um padrão de acesso, mas possui condições de atualização, capacidade e custo.

Geração de 41 tópicos, 302 flashcards e índice de 105 fichas concluída.

Geração do simulado de 65 questões concluída.

Cada um dos 41 tópicos e das 105 fichas contém exatamente um bloco de aprofundamento.

**Antes de ler este trecho:**

- **idempotência:** Repetir uma operação sem duplicar seu efeito de negócio. Por exemplo, receber novamente o mesmo pedido não deve gerar uma segunda cobrança indevida.

Repetir o gerador não altera o conteúdo produzido (idempotência verificada por hash).

Anotações e complementos foram preservados em um teste de regeneração, com restauração do arquivo ao final.

Verificador de links relativos terminou sem destinos quebrados; ele não valida conteúdo de URLs externas nem âncoras.

Diff conferido sem erros de whitespace.

## Fontes do escopo

[Guia CLF-C02](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)

[Domínio 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html)

[Domínio 2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html)

[Domínio 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html)

[Domínio 4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html)

[Serviços no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html)

[Serviços fora do escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)

[Voltar ao índice](../../README.md)
