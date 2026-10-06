# 3.7 Bancos de dados

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma aplicação precisa guardar dados, mas um cadastro, uma rede de relações e um relatório sobre milhões de vendas têm formas de consulta diferentes.

**A ideia em palavras simples:** Bancos de dados organizam registros para armazenar e consultar. A AWS oferece modelos relacionais, chave-valor, documentos, grafos e análise, entre outros.

**Exemplo do dia a dia:** A escola usa tabelas relacionadas para matrículas. Um jogo pode buscar perfis por identificador; uma análise histórica pode usar um ambiente voltado a relatórios.

**O que não concluir?** Não há um banco melhor para qualquer dado. Primeiro identifique a estrutura e as perguntas que a aplicação precisa fazer; depois avalie o serviço.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Relacional** | dados em tabelas ligadas entre si, consultadas com SQL. |
| **NoSQL** | bancos que não usam o modelo de tabelas relacionais (chave-valor, documentos, grafos). |
| **OLTP** | muitas transações pequenas do dia a dia (vendas, cadastros). |
| **OLAP** | análises grandes sobre o histórico (relatórios, BI). |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [Amazon RDS (Relational Database Service)](../../servicos/banco-de-dados/rds.md) · [Amazon Aurora](../../servicos/banco-de-dados/aurora.md) · [Amazon DynamoDB](../../servicos/banco-de-dados/dynamodb.md) · [Amazon ElastiCache](../../servicos/banco-de-dados/elasticache.md) · [Amazon MemoryDB](../../servicos/banco-de-dados/memorydb.md) · [Amazon Redshift](../../servicos/banco-de-dados/redshift.md) · [Amazon DocumentDB (compatível com MongoDB)](../../servicos/banco-de-dados/documentdb.md) · [Amazon Neptune](../../servicos/banco-de-dados/neptune.md) · [Amazon Keyspaces, Timestream e outros bancos especializados](../../servicos/banco-de-dados/keyspaces-timestream-e-outros.md)

⬅️ [3.6 Outros serviços de computação](06-outros-servicos-de-computacao.md) · 🏠 [Índice do domínio](README.md) · [3.8 Amazon S3 — armazenamento de objetos](08-s3.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.

Comece pelas perguntas que a aplicação fará aos dados. Relacionar alunos e matrículas pede um modelo; buscar um perfil pelo identificador pede outro; explorar vínculos entre contas pede relações; comparar meses de vendas pede análise.

O modelo do banco e os acessos precisam combinar. Um serviço gerenciado reduz parte da operação, mas você ainda define estruturas, consultas e permissões. Trocar de produto sem avaliar interfaces e padrões de consulta pode não atender à aplicação.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **RDS** é uma **planilha organizada com zelador**; o **DynamoDB** é um **fichário gigante** que acha qualquer ficha pela etiqueta na hora; o **ElastiCache** é um **post-it** com as respostas mais pedidas; o **Neptune** é um **mapa de quem conhece quem**; o **Redshift** é o **arquivo histórico** usado para relatórios.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **schema:** Estrutura e tipos dos dados. Em migração, adaptar a estrutura é uma tarefa diferente de copiar os registros.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.

**Banco no EC2 vs gerenciado:** no EC2 você cuida de SO, instalação, patch, backup e alta disponibilidade. Nos serviços gerenciados, a AWS cuida disso e você foca no schema, nas consultas e no acesso.

**Antes de ler este trecho:**

- **Amazon RDS / RDS:** O RDS oferece bancos relacionais gerenciados.

**Amazon RDS:** Banco relacional gerenciado.

**Antes de ler este trecho:**

- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.

  - Motores: **MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 e Aurora**.
**Antes de ler este trecho:**

- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **failover:** Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.

  - **Multi-AZ:** réplica de espera síncrona em outra AZ, com **failover automático**. Objetivo: **disponibilidade**, não performance.
**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.

  - **Read Replicas:** cópias assíncronas só de leitura (inclusive em outra região) para **escalar leitura**.
**Antes de ler este trecho:**

- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.

  - **Backups automáticos** com restauração para um ponto no tempo (retenção de até 35 dias) e **snapshots** manuais.
**Antes de ler este trecho:**

- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.

  - Sem acesso ao SO da instância de banco (a AWS gerencia).

**Amazon Aurora:** Relacional da AWS compatível com **MySQL e PostgreSQL**.

  - Mais performático que o MySQL e PostgreSQL padrão (a AWS cita até 5x e 3x, respectivamente).

  - Armazenamento cresce sozinho e mantém **6 cópias dos dados em 3 AZs**.
**Antes de ler este trecho:**

- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.

  - **Aurora Serverless:** capacidade ajustada automaticamente. **Aurora Global Database:** replicação entre regiões.
**Antes de ler este trecho:**

- **Amazon DynamoDB / DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **NoSQL:** Família de modelos de banco que não se limita à estrutura relacional tradicional. Não significa ausência de estrutura ou que todo produto NoSQL faz o mesmo trabalho.

**Amazon DynamoDB:** NoSQL **chave-valor e documentos**, serverless, latência de milissegundos de um dígito em qualquer escala.

**Antes de ler este trecho:**

- **provisionado:** Recurso ou capacidade já disponibilizado para uso. Em algumas cobranças, a disponibilidade mantida importa mesmo sem execução de trabalho de negócio.

  - Modos de capacidade: **sob demanda** (paga por requisição) ou **provisionado** (com Auto Scaling).

  - **Global Tables:** replicação multi-região ativa-ativa.
**Antes de ler este trecho:**

- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **DAX:** Cache compatível com DynamoDB para determinados acessos. É uma camada de aceleração, não uma cópia independente de qualquer banco.

  - **DAX:** cache em memória para leituras em microssegundos.
**Antes de ler este trecho:**

- **TTL:** Tempo de vida de uma informação. Em DNS pode orientar cache; em um banco pode indicar expiração de itens. O efeito concreto depende do serviço.

  - Streams, TTL (expiração automática de itens) e backup point-in-time.
**Antes de ler este trecho:**

- **Amazon ElastiCache / ElastiCache:** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.
- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.
- **Redis / Redis OSS / Valkey / Memcached:** Tecnologias de dados em memória com comportamentos e funções diferentes. A modalidade gerenciada deve ser escolhida segundo compatibilidade e necessidade, não apenas pela palavra cache.

**Amazon ElastiCache:** Cache em memória gerenciado, compatível com **Redis OSS/Valkey e Memcached**. Latência em microssegundos; reduz a carga do banco e guarda sessões.

**Amazon Keyspaces:** Cassandra gerenciado e serverless. Não aparece na lista oficial de serviços da prova, então dificilmente cai.

**Antes de ler este trecho:**

- **Amazon Neptune / Neptune:** Neptune é um banco de grafos: representa entidades e as conexões entre elas para consultar relações.

**Amazon Neptune:** banco de **grafos**. Para redes sociais, motores de recomendação, detecção de fraude e grafos de conhecimento.

**Antes de ler este trecho:**

- **Amazon DocumentDB / DocumentDB:** DocumentDB armazena e consulta documentos, como registros estruturados de produtos.

**Amazon DocumentDB:** banco de **documentos** compatível com **MongoDB**.

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **Amazon Redshift / Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **OLAP:** Análise de conjuntos de dados, como comparar vendas de vários meses. Prioriza perguntas e agregações, não apenas registrar uma operação individual.
- **data warehouse:** Ambiente de dados organizado para análise de grandes conjuntos. O modelo e as consultas são orientados a perguntas analíticas.
- **BI:** Análise e apresentação de dados para apoiar decisões. Um painel depende de dados adequados e de uma interpretação correta dos indicadores.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.

**Amazon Redshift:** **data warehouse** em colunas, para análise (OLAP) de grandes volumes com SQL e BI. Redshift Serverless dispensa gerenciar cluster; Redshift Spectrum consulta dados direto no S3.

**Antes de ler este trecho:**

- **SCT:** Ferramenta de conversão de estrutura de banco em migrações compatíveis. Nem toda estrutura ou regra da aplicação é convertida automaticamente.
- **DMS:** Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.

**Migração de bancos:** DMS e SCT (ver [3.17](17-migracao-e-transferencia.md)).

**Antes de ler este trecho:**

- **JSON:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
- **OLTP:** Processamento de operações individuais do negócio, como registrar uma compra. É diferente de analisar grandes conjuntos históricos de registros.

| Tipo de dado ou necessidade | Serviço |
| --- | --- |
| Relacional, transações (OLTP), SQL tradicional | RDS ou Aurora |
| Relacional com máxima performance e alta disponibilidade gerenciada | Aurora |
| Chave-valor, escala massiva, latência baixa, serverless | DynamoDB |
| Cache em memória | ElastiCache (ou DAX para DynamoDB) |
| Relacionamentos entre entidades (grafos) | Neptune |
| Documentos JSON compatíveis com MongoDB | DocumentDB |
| Análise de grandes volumes, BI, data warehouse (OLAP) | Redshift |

**Antes de ler este trecho:**

- **segundo:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **read replica:** Cópia de banco que pode atender consultas em cenários suportados. Ela não deve ser confundida com toda modalidade de standby para recuperação.

**Cai na prova:** Multi-AZ = disponibilidade; Read Replica = performance de leitura. "Banco para carrinho de compras com milhões de acessos por segundo" = DynamoDB. "Recomendações tipo amigos de amigos" = Neptune.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.

**Primeiro, identifique o funcionamento:** Relacionais organizam tabelas e relações; NoSQL atende modelos como chave-valor/documentos; cache guarda dados de acesso rápido; warehouse prioriza análises agregadas.

**Depois, compare as escolhas:** RDS/Aurora para relacional; DynamoDB para chave-valor/documentos; ElastiCache para cache; DocumentDB para documentos compatíveis; Neptune para grafos; Redshift para analytics.

**Por fim, verifique o limite:** Gerenciado não elimina desenho de esquema, índices e consultas. Compatibilidade não significa identidade completa de APIs. Cache não deve ser confundido automaticamente com banco principal durável.

## 4. Caso resolvido

Um sistema transacional usa SQL e quer tolerar falha de AZ; outro faz relatórios agregados de grandes conjuntos. Mesmo banco por palavra-chave SQL?

**Raciocínio e resposta:** Não. RDS/Aurora atendem o transacional; Redshift atende o warehouse. O padrão de uso pesa mais que a presença de SQL.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **banco no EC2** (você cuida de tudo) de **banco gerenciado** (a AWS cuida).
- [ ] Diferenciar **Multi-AZ** (disponibilidade) de **Read Replica** (performance de leitura).
- [ ] Escolher o banco pelo tipo de dado (use a tabela "tipo de dado → serviço" do conteúdo).
- [ ] Diferenciar **OLTP** (RDS/Aurora) de **OLAP** (Redshift).

**Dica de revisão para a prova:** "Multi-AZ" → **disponibilidade**; "Read Replica" → **leitura**. "Milhões de acessos, chave-valor, serverless" → **DynamoDB**. "BI/data warehouse" → **Redshift**. "Amigos de amigos" → **Neptune**. "MongoDB" → **DocumentDB**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Qual a vantagem do RDS sobre instalar o banco no EC2?"

**Resposta curta:** A AWS cuida de patch, backups, hardware e failover.

**Pergunta:** "Como garantir failover automático do banco para outra AZ?"

**Resposta curta:** RDS Multi-AZ.

**Pergunta:** "Como aliviar consultas de leitura pesadas?"

**Resposta curta:** Read Replicas (ou cache com ElastiCache).

**Pergunta:** "Qual banco relacional compatível com MySQL e PostgreSQL oferece mais performance?"

**Resposta curta:** Aurora.

**Pergunta:** "Qual banco NoSQL serverless com latência de milissegundos?"

**Resposta curta:** DynamoDB.

**Pergunta:** "Replicação multi-região ativa-ativa no DynamoDB."

**Resposta curta:** Global Tables.

**Pergunta:** "Cache de microssegundos para DynamoDB."

**Resposta curta:** DAX.

**Pergunta:** "Banco para relacionamentos complexos (redes sociais, fraude)."

**Resposta curta:** Neptune.

**Pergunta:** "Migrar banco MongoDB para serviço gerenciado."

**Resposta curta:** DocumentDB.

**Pergunta:** "Data warehouse para relatórios de BI sobre petabytes."

**Resposta curta:** Redshift.

**Pergunta:** "Quais motores o RDS suporta?"

**Resposta curta:** MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 e Aurora.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **DynamoDB:** item de no máximo **400 KB** (📌, incluindo nomes e valores de atributos). ⚠️ "Guardar vídeos/imagens no DynamoDB" → guarde no **S3** e mantenha só a referência na tabela.
- **Aurora:** até **15 Aurora Replicas** por cluster (📌), além da primária. Um cluster secundário de Global Database pode ter até 16.
- **RDS Read Replicas:** até **15** por origem para MySQL, MariaDB e PostgreSQL (até 5 cross-region). Oracle e SQL Server: até **5**; Db2: até **3** (✔️ confirmado na API do RDS, 04/10/2026).
- ⚠️ **Read Replica × Multi-AZ:** read replica = **escalar leitura** (assíncrona, pode ser cross-region). Multi-AZ = **alta disponibilidade/failover** (standby síncrono que, no modelo clássico, não atende leitura).
- **Diferenças sutis:**
  - Redshift (OLAP, SQL analítico em petabytes) × RDS/Aurora (OLTP) × Athena (SQL serverless direto no S3, paga por dado escaneado).
  - ElastiCache (cache em memória: Valkey/Redis OSS/Memcached) × MemoryDB (banco em memória **durável**) × DAX (cache **exclusivo** do DynamoDB, microssegundos).
  - Neptune = grafos · DocumentDB = MongoDB · Keyspaces = Cassandra · Timestream = séries temporais.
- 🔄 **Timestream for LiveAnalytics** fechado para novos clientes (20/06/2025). Na prova, "séries temporais/IoT" ainda → Timestream.
- 🧊 Não decorar: RCU/WCU por tamanho de item, limites de armazenamento por motor, versões.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.6 Outros serviços de computação](06-outros-servicos-de-computacao.md) · 🏠 [Índice do domínio](README.md) · [3.8 Amazon S3 — armazenamento de objetos](08-s3.md) ➡️
