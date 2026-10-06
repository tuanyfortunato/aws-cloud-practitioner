# 3.18 Serviços menos conhecidos que podem aparecer

## 🧠 Antes de começar

**Qual é a dificuldade?** Alguns nomes AWS aparecem em listas antigas ou em problemas muito específicos. Tentar decorar todos sem entender a função dificulta o estudo.

**A ideia em palavras simples:** Esta seção organiza serviços adicionais por finalidade e identifica seu status no escopo. O objetivo é reconhecer o tipo de problema e saber quando aprofundar.

**Exemplo do dia a dia:** Ao encontrar um nome novo, descubra primeiro se ele atende armazenamento, integração, rede ou outra necessidade e confira se está na lista atual da prova.

**O que não concluir?** Estar nesta seção não significa que o serviço continua disponível ou que é prioritário para o exame. Use as marcações de escopo e as observações de cada ficha.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Distrator** | alternativa errada colocada para confundir. |
| **Engenharia do caos** | provocar falhas de propósito para testar se o sistema se recupera. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](../../servicos/analytics/lake-formation-msk-e-outros.md) · [Amazon MQ](../../servicos/integracao/amazon-mq.md) · [AWS Firewall Manager e AWS Network Firewall](../../servicos/seguranca/firewall-manager-e-network-firewall.md) · [Amazon Keyspaces, Timestream e outros bancos especializados](../../servicos/banco-de-dados/keyspaces-timestream-e-outros.md) · [Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate, Textract, Kendra, Personalize…)](../../servicos/ia-ml/servicos-de-ia-prontos.md) · [Serviços de mídia e jogos (Elemental, IVS, Elastic Transcoder, GameLift, Lumberyard)](../../servicos/fora-do-escopo/midia-e-jogos.md) · [IoT, robótica, satélite e visão computacional na borda (Device Defender, Monitron, Panorama, RoboMaker, Ground Station)](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) · [Desenvolvimento e aplicações (AppConfig, Infrastructure Composer, CodeGuru, Copilot, Refactor Spaces, AppFabric, SWF, WorkDocs)](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) · [Rede e diretório (Cloud Map, VPC Lattice, Network Access Analyzer, Cloud Directory)](../../servicos/fora-do-escopo/rede-e-diretorio.md) · [Gerenciamento e custos (Data Lifecycle Manager, Chatbot, Launch Wizard, Application Cost Profiler, DevPay)](../../servicos/fora-do-escopo/gerenciamento-e-custos.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** Vários serviços desta seção estão **fora do escopo** oficial (MSK, AppFlow, Data Exchange, Keyspaces, MemoryDB, Personalize, Device Farm, Network Firewall, AWS IQ). Use-os para reconhecer distratores. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.17 Migração e transferência](17-migracao-e-transferencia.md) · 🏠 [Índice do domínio](README.md)

---

## 1. Entenda as peças e a relação entre elas

Um nome pouco conhecido precisa ser lido pelo trabalho que realiza. A categoria reúne funções distintas e também referências históricas. Aprender a classificar o problema ajuda mais que decorar todos os nomes sem contexto.

Examine função, compatibilidade e status. Fora do escopo do exame não significa que um produto é recomendável ou está disponível hoje; não listado também não significa uma garantia sobre futuras questões. Priorize o guia oficial e use o restante como referência.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como **conhecer os figurantes de um filme**: você não precisa saber a história deles, só reconhecer quem é quem quando aparecem — e perceber quando alguém **nem é do elenco** (serviço fora do escopo).

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

A AWS avisa que a lista de serviços no escopo não é exaustiva, e quem já fez a prova relata questões sobre serviços pouco divulgados. Esta seção reúne os mais citados. Basta saber para que cada um serve.

### Sustentabilidade

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.

**AWS Customer Carbon Footprint Tool:** ferramenta **gratuita** no console de Billing and Cost Management que mostra a **estimativa de emissões de carbono** do uso da AWS da conta, em toneladas métricas de CO₂ equivalente, com histórico e divisão por serviço e por região. Serve para acompanhar metas de sustentabilidade e se liga ao pilar **Sustentabilidade** do Well-Architected.

**Antes de ler este trecho:**

- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **rightsizing:** Ajustar capacidade à necessidade observada. Reduzir demais pode prejudicar a aplicação; a recomendação precisa ser avaliada pelo uso real.
- **Graviton:** Família de processadores AWS baseada em arquitetura ARM. A aplicação e sua imagem precisam ser compatíveis com essa arquitetura.

Outras práticas sustentáveis que a prova associa a esse pilar: usar processadores Graviton, serviços gerenciados e serverless, rightsizing, desligar recursos ociosos e escolher classes de armazenamento adequadas.

### Ajuda, parceiros e soluções prontas

**AWS IQ:** 🔄 hoje está declarado **fora do escopo** da prova (verificação de 10/2026). Era um marketplace para contratar **especialistas freelancers certificados em AWS** para projetos sob demanda, pagos na própria fatura AWS. A AWS **encerrou o serviço em 28/05/2026** (a alternativa indicada é o AWS Marketplace Professional Services), mas ele ainda pode aparecer em questões.

**AWS Solutions Library e AWS Prescriptive Guidance:** arquiteturas de referência e soluções prontas para implantar, validadas pela AWS.

### Outros serviços citados por quem fez a prova

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **Amazon MemoryDB / MemoryDB:** MemoryDB oferece um banco em memória com mecanismos de durabilidade.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **MSK / Kafka:** Kafka é uma plataforma de fluxo de eventos; MSK é a oferta gerenciada compatível da AWS. A aplicação ainda precisa produzir e consumir os registros.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **Amazon MQ:** Amazon MQ oferece brokers gerenciados compatíveis com tecnologias suportadas, como ActiveMQ e RabbitMQ.
- **MQ / broker:** Intermediário de mensagens entre componentes. Sua interface e seus protocolos precisam ser compatíveis com as aplicações conectadas.
- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.
- **resiliência:** Capacidade de resistir e recuperar-se de falhas. Requer escolher quais falhas serão tratadas e como a operação continuará.
- **RTO:** Objetivo de tempo de recuperação: quanto tempo a organização aceita ficar sem o sistema após uma interrupção.
- **RPO:** Objetivo de ponto de recuperação: quanto histórico de dados a organização aceita perder, medido como intervalo de tempo.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **STS:** Serviço que fornece credenciais temporárias AWS. Essas credenciais permitem uma sessão autorizada dentro das permissões aplicáveis.
- **data lake:** Conjunto de dados mantido para usos diversos, frequentemente em armazenamento de objetos. Organização, catálogo e permissões continuam necessários.
- **streaming:** Fluxo contínuo de dados ou mídia. É diferente de esperar um arquivo completo antes de iniciar o trabalho.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.
- **durabilidade:** Capacidade de preservar os dados armazenados. É diferente de disponibilidade, que trata de conseguir acessá-los quando necessário.
- **Redis / Valkey:** Tecnologias de dados em memória com comportamentos e funções diferentes. A modalidade gerenciada deve ser escolhida segundo compatibilidade e necessidade, não apenas pela palavra cache.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.
- **SAP:** Tecnologias e aplicações empresariais do ecossistema SAP. Podem exigir requisitos específicos de memória, licenciamento e operação.

| Serviço | O que faz | Exemplo de cenário |
| --- | --- | --- |
| AWS Security Token Service (STS) | Emite **credenciais temporárias**; é o que está por trás das IAM roles | "Qual serviço gera credenciais temporárias?" |
| AWS Network Firewall | Firewall de rede gerenciado para a VPC, com inspeção de tráfego e prevenção de intrusão | "Inspecionar e filtrar todo o tráfego que entra na VPC" |
| AWS Private Certificate Authority | Emite **certificados privados** para uso interno | "Certificados para serviços internos, não públicos" |
| Amazon MQ | Message broker gerenciado para **Apache ActiveMQ e RabbitMQ** | "Migrar aplicação que usa RabbitMQ sem reescrever" (SQS exigiria mudar o código) |
| Amazon MSK | **Apache Kafka** gerenciado | "Streaming com Kafka sem gerenciar cluster" |
| Amazon AppFlow | Transfere dados entre aplicações **SaaS** (Salesforce, SAP, Zendesk) e a AWS sem código | "Levar dados do Salesforce para o S3" |
| AWS Data Exchange | Encontrar e assinar **conjuntos de dados de terceiros** | "Comprar dados de mercado para análise" |
| AWS Lake Formation | Montar e proteger um **data lake** no S3 | "Criar data lake com controle de acesso centralizado" |
| Amazon Timestream | Banco de **séries temporais** | "Guardar leituras de sensores IoT ao longo do tempo" |
| Amazon MemoryDB | Banco **em memória durável**, compatível com Redis/Valkey | "Banco principal com latência de microssegundos e durabilidade" |
| Amazon Personalize | **Recomendações personalizadas** com ML | "Recomendar produtos como na Amazon.com" |
| AWS Device Farm | Testa apps web e mobile em **dispositivos reais** na nuvem | "Testar o app em vários modelos de celular" |
| AWS Fault Injection Service | **Engenharia do caos**: injeta falhas controladas para testar resiliência | "Simular falhas para validar a recuperação" (pilar Confiabilidade) |
| AWS Resilience Hub | Avalia e acompanha a **resiliência** das aplicações contra metas de RTO e RPO | "Verificar se a aplicação atende ao RTO definido" |
| EC2 Image Builder | Automatiza a criação e atualização de **AMIs** | "Manter imagens de servidor atualizadas e com patches" |
| Amazon Managed Grafana / Managed Service for Prometheus | Visualização e monitoramento de métricas com ferramentas open source gerenciadas | "Usar Grafana sem gerenciar servidores" |
| Amazon WorkMail | **E-mail corporativo** e calendário gerenciados | "E-mail empresarial compatível com Outlook" |

### O que está fora do escopo

O exam guide lista categorias que **não caem** na prova. Se uma alternativa citar um serviço delas, provavelmente é distrator:

**Game Tech** (ex.: Amazon GameLift).

**Serviços de mídia** (ex.: AWS Elemental).

**Robótica** (ex.: AWS RoboMaker).

**Satélite** (ex.: AWS Ground Station).

**Blockchain** (ex.: Amazon Managed Blockchain).

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** Serviços especializados resolvem necessidades específicas, como grafo, Kafka ou compartilhamento de dados. A lista oficial separa os explicitamente incluídos, excluídos e não citados.

**Depois, compare as escolhas:** Priorize tasks e serviços incluídos; fichas mistas devem ser lidas por serviço, não por categoria inteira. Use extras para entender diferenças, sem substituir os fundamentos.

**Por fim, verifique o limite:** Ausência na lista não prova que nunca será cobrado. Estar fora do escopo não prova que o produto é ruim nem justifica responder sem ler o cenário.

## 4. Caso resolvido

Você reconhece Kafka em uma alternativa, mas a questão só pede streaming gerenciado no escopo. Basta escolher por popularidade?

**Raciocínio e resposta:** Não. Compare requisito e opções, e priorize o serviço adequado ao escopo, como Kinesis. Fora do escopo reduz prioridade de estudo; não é uma regra universal de eliminação por nome.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Saber que a **Customer Carbon Footprint Tool** mostra a estimativa de emissões de carbono (pilar Sustentabilidade).
- [ ] Reconhecer a função dos serviços da tabela (ex.: STS → credenciais temporárias; Amazon MQ → RabbitMQ/ActiveMQ).
- [ ] Lembrar as categorias **fora do escopo** (games, mídia, robótica, satélite, blockchain).

**Dica de revisão para a prova:** Se uma alternativa cita serviço de **games, mídia, robótica, satélite ou blockchain**, ou um serviço marcado fora do escopo, ela provavelmente é **distrator**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Como acompanhar a pegada de carbono do uso da AWS?"

**Resposta curta:** AWS Customer Carbon Footprint Tool.

**Pergunta:** "Onde contratar especialistas certificados sob demanda para um projeto pequeno?"

**Resposta curta:** AWS IQ (descontinuado; hoje, AWS Marketplace Professional Services ou um parceiro da APN).

**Antes de ler este trecho:**

- **APN:** Rede de parceiros AWS. Parceiros oferecem serviços e soluções conforme seus próprios contratos e competências.

**Pergunta:** "Qual serviço emite as credenciais temporárias usadas pelas roles?"

**Resposta curta:** AWS STS.

**Pergunta:** "A aplicação usa RabbitMQ e deve migrar sem mudar o código."

**Resposta curta:** Amazon MQ.

**Pergunta:** "Testar a resiliência injetando falhas de propósito."

**Resposta curta:** AWS Fault Injection Service.

**Pergunta:** "Testar um app mobile em centenas de dispositivos reais."

**Resposta curta:** AWS Device Farm.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.17 Migração e transferência](17-migracao-e-transferencia.md) · 🏠 [Índice do domínio](README.md)
