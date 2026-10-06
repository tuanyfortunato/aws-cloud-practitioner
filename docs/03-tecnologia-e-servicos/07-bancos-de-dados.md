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

Comece pelas perguntas que a aplicação fará aos dados. Relacionar alunos e matrículas pede um modelo; buscar um perfil pelo identificador pede outro; explorar vínculos entre contas pede relações; comparar meses de vendas pede análise.

O modelo do banco e os acessos precisam combinar. Um serviço gerenciado reduz parte da operação, mas você ainda define estruturas, consultas e permissões. Trocar de produto sem avaliar interfaces e padrões de consulta pode não atender à aplicação.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **RDS** é uma **planilha organizada com zelador**; o **DynamoDB** é um **fichário gigante** que acha qualquer ficha pela etiqueta na hora; o **ElastiCache** é um **post-it** com as respostas mais pedidas; o **Neptune** é um **mapa de quem conhece quem**; o **Redshift** é o **arquivo histórico** usado para relatórios.

</details>

## 2. Conceitos e opções explicados

**Banco no EC2 vs gerenciado:** no EC2 você cuida de SO, instalação, patch, backup e alta disponibilidade. Nos serviços gerenciados, a AWS cuida disso e você foca no schema, nas consultas e no acesso.

**Amazon RDS:** Banco relacional gerenciado.

  - Motores: **MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 e Aurora**.

  - **Multi-AZ:** réplica de espera síncrona em outra AZ, com **failover automático**. Objetivo: **disponibilidade**, não performance.

  - **Read Replicas:** cópias assíncronas só de leitura (inclusive em outra região) para **escalar leitura**.

  - **Backups automáticos** com restauração para um ponto no tempo (retenção de até 35 dias) e **snapshots** manuais.

  - Sem acesso ao SO da instância de banco (a AWS gerencia).

**Amazon Aurora:** Relacional da AWS compatível com **MySQL e PostgreSQL**.

  - Mais performático que o MySQL e PostgreSQL padrão (a AWS cita até 5x e 3x, respectivamente).

  - Armazenamento cresce sozinho e mantém **6 cópias dos dados em 3 AZs**.

  - **Aurora Serverless:** capacidade ajustada automaticamente. **Aurora Global Database:** replicação entre regiões.

**Amazon DynamoDB:** NoSQL **chave-valor e documentos**, serverless, latência de milissegundos de um dígito em qualquer escala.

  - Modos de capacidade: **sob demanda** (paga por requisição) ou **provisionado** (com Auto Scaling).

  - **Global Tables:** replicação multi-região ativa-ativa.

  - **DAX:** cache em memória para leituras em microssegundos.

  - Streams, TTL (expiração automática de itens) e backup point-in-time.

**Amazon ElastiCache:** Cache em memória gerenciado, compatível com **Redis OSS/Valkey e Memcached**. Latência em microssegundos; reduz a carga do banco e guarda sessões.

**Amazon Keyspaces:** Cassandra gerenciado e serverless. Não aparece na lista oficial de serviços da prova, então dificilmente cai.

**Amazon Neptune:** banco de **grafos**. Para redes sociais, motores de recomendação, detecção de fraude e grafos de conhecimento.

**Amazon DocumentDB:** banco de **documentos** compatível com **MongoDB**.

**Amazon Redshift:** **data warehouse** em colunas, para análise (OLAP) de grandes volumes com SQL e BI. Redshift Serverless dispensa gerenciar cluster; Redshift Spectrum consulta dados direto no S3.

**Migração de bancos:** DMS e SCT (ver [3.17](17-migracao-e-transferencia.md)).

| Tipo de dado ou necessidade | Serviço |
| --- | --- |
| Relacional, transações (OLTP), SQL tradicional | RDS ou Aurora |
| Relacional com máxima performance e alta disponibilidade gerenciada | Aurora |
| Chave-valor, escala massiva, latência baixa, serverless | DynamoDB |
| Cache em memória | ElastiCache (ou DAX para DynamoDB) |
| Relacionamentos entre entidades (grafos) | Neptune |
| Documentos JSON compatíveis com MongoDB | DocumentDB |
| Análise de grandes volumes, BI, data warehouse (OLAP) | Redshift |

**Cai na prova:** Multi-AZ = disponibilidade; Read Replica = performance de leitura. "Banco para carrinho de compras com milhões de acessos por segundo" = DynamoDB. "Recomendações tipo amigos de amigos" = Neptune.

## 3. Como analisar uma situação

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
