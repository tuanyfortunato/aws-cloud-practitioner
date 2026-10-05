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

**Ao terminar este tópico, você deve saber:**

- [ ] Saber que a **Customer Carbon Footprint Tool** mostra a estimativa de emissões de carbono (pilar Sustentabilidade).
- [ ] Reconhecer a função dos serviços da tabela (ex.: STS → credenciais temporárias; Amazon MQ → RabbitMQ/ActiveMQ).
- [ ] Lembrar as categorias **fora do escopo** (games, mídia, robótica, satélite, blockchain).

<details>
<summary>Uma analogia para revisar a ideia</summary>

é como **conhecer os figurantes de um filme**: você não precisa saber a história deles, só reconhecer quem é quem quando aparecem — e perceber quando alguém **nem é do elenco** (serviço fora do escopo).

</details>

> 🎯 **Como não errar na prova:** Se uma alternativa cita serviço de **games, mídia, robótica, satélite ou blockchain**, ou um serviço marcado fora do escopo, ela provavelmente é **distrator**.

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](../../servicos/analytics/lake-formation-msk-e-outros.md) · [Amazon MQ](../../servicos/integracao/amazon-mq.md) · [AWS Firewall Manager e AWS Network Firewall](../../servicos/seguranca/firewall-manager-e-network-firewall.md) · [Amazon Keyspaces, Timestream e outros bancos especializados](../../servicos/banco-de-dados/keyspaces-timestream-e-outros.md) · [Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate, Textract, Kendra, Personalize…)](../../servicos/ia-ml/servicos-de-ia-prontos.md) · [Serviços de mídia e jogos (Elemental, IVS, Elastic Transcoder, GameLift, Lumberyard)](../../servicos/fora-do-escopo/midia-e-jogos.md) · [IoT, robótica, satélite e visão computacional na borda (Device Defender, Monitron, Panorama, RoboMaker, Ground Station)](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) · [Desenvolvimento e aplicações (AppConfig, Infrastructure Composer, CodeGuru, Copilot, Refactor Spaces, AppFabric, SWF, WorkDocs)](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) · [Rede e diretório (Cloud Map, VPC Lattice, Network Access Analyzer, Cloud Directory)](../../servicos/fora-do-escopo/rede-e-diretorio.md) · [Gerenciamento e custos (Data Lifecycle Manager, Chatbot, Launch Wizard, Application Cost Profiler, DevPay)](../../servicos/fora-do-escopo/gerenciamento-e-custos.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** Vários serviços desta seção estão **fora do escopo** oficial (MSK, AppFlow, Data Exchange, Keyspaces, MemoryDB, Personalize, Device Farm, Network Firewall, AWS IQ). Use-os para reconhecer distratores. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.17 Migração e transferência](17-migracao-e-transferencia.md) · 🏠 [Índice do domínio](README.md)

---

## 📖 Conteúdo

A AWS avisa que a lista de serviços no escopo não é exaustiva, e quem já fez a prova relata questões sobre serviços pouco divulgados. Esta seção reúne os mais citados. Basta saber para que cada um serve.

## Sustentabilidade

- **AWS Customer Carbon Footprint Tool:** ferramenta **gratuita** no console de Billing and Cost Management que mostra a **estimativa de emissões de carbono** do uso da AWS da conta, em toneladas métricas de CO₂ equivalente, com histórico e divisão por serviço e por região. Serve para acompanhar metas de sustentabilidade e se liga ao pilar **Sustentabilidade** do Well-Architected.
- Outras práticas sustentáveis que a prova associa a esse pilar: usar processadores Graviton, serviços gerenciados e serverless, rightsizing, desligar recursos ociosos e escolher classes de armazenamento adequadas.

## Ajuda, parceiros e soluções prontas

- **AWS IQ:** 🔄 hoje está declarado **fora do escopo** da prova (verificação de 10/2026). Era um marketplace para contratar **especialistas freelancers certificados em AWS** para projetos sob demanda, pagos na própria fatura AWS. A AWS **encerrou o serviço em 28/05/2026** (a alternativa indicada é o AWS Marketplace Professional Services), mas ele ainda pode aparecer em questões.
- **AWS Solutions Library e AWS Prescriptive Guidance:** arquiteturas de referência e soluções prontas para implantar, validadas pela AWS.

## Outros serviços citados por quem fez a prova

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

## O que está fora do escopo

O exam guide lista categorias que **não caem** na prova. Se uma alternativa citar um serviço delas, provavelmente é distrator:

- **Game Tech** (ex.: Amazon GameLift).
- **Serviços de mídia** (ex.: AWS Elemental).
- **Robótica** (ex.: AWS RoboMaker).
- **Satélite** (ex.: AWS Ground Station).
- **Blockchain** (ex.: Amazon Managed Blockchain).

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Como acompanhar a pegada de carbono do uso da AWS?" → AWS Customer Carbon Footprint Tool.
- "Onde contratar especialistas certificados sob demanda para um projeto pequeno?" → AWS IQ (descontinuado; hoje, AWS Marketplace Professional Services ou um parceiro da APN).
- "Qual serviço emite as credenciais temporárias usadas pelas roles?" → AWS STS.
- "A aplicação usa RabbitMQ e deve migrar sem mudar o código." → Amazon MQ.
- "Testar a resiliência injetando falhas de propósito." → AWS Fault Injection Service.
- "Testar um app mobile em centenas de dispositivos reais." → AWS Device Farm.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** Serviços especializados resolvem necessidades específicas, como grafo, Kafka ou compartilhamento de dados. A lista oficial separa os explicitamente incluídos, excluídos e não citados.

**Como escolher:** Priorize tasks e serviços incluídos; fichas mistas devem ser lidas por serviço, não por categoria inteira. Use extras para entender diferenças, sem substituir os fundamentos.

**O que não concluir:** Ausência na lista não prova que nunca será cobrado. Estar fora do escopo não prova que o produto é ruim nem justifica responder sem ler o cenário.

### Exercício de decisão

Você reconhece Kafka em uma alternativa, mas a questão só pede streaming gerenciado no escopo. Basta escolher por popularidade?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Não. Compare requisito e opções, e priorize o serviço adequado ao escopo, como Kinesis. Fora do escopo reduz prioridade de estudo; não é uma regra universal de eliminação por nome.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.17 Migração e transferência](17-migracao-e-transferencia.md) · 🏠 [Índice do domínio](README.md)
