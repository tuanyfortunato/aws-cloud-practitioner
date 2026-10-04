# 3.7 Bancos de dados

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon RDS (Relational Database Service)](../../servicos/banco-de-dados/rds.md) · [Amazon Aurora](../../servicos/banco-de-dados/aurora.md) · [Amazon DynamoDB](../../servicos/banco-de-dados/dynamodb.md) · [Amazon ElastiCache](../../servicos/banco-de-dados/elasticache.md) · [Amazon MemoryDB](../../servicos/banco-de-dados/memorydb.md) · [Amazon Redshift](../../servicos/banco-de-dados/redshift.md) · [Amazon DocumentDB (compatível com MongoDB)](../../servicos/banco-de-dados/documentdb.md) · [Amazon Neptune](../../servicos/banco-de-dados/neptune.md) · [Amazon Keyspaces, Timestream e outros bancos especializados](../../servicos/banco-de-dados/keyspaces-timestream-e-outros.md)

⬅️ [3.6 Outros serviços de computação](06-outros-servicos-de-computacao.md) · 🏠 [Índice do domínio](README.md) · [3.8 Amazon S3 — armazenamento de objetos](08-s3.md) ➡️

---

## 📖 Conteúdo

- **Banco no EC2 vs gerenciado:** no EC2 você cuida de SO, instalação, patch, backup e alta disponibilidade. Nos serviços gerenciados, a AWS cuida disso e você foca no schema, nas consultas e no acesso.
- **Amazon RDS:** Banco relacional gerenciado.
  - Motores: **MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 e Aurora**.
  - **Multi-AZ:** réplica de espera síncrona em outra AZ, com **failover automático**. Objetivo: **disponibilidade**, não performance.
  - **Read Replicas:** cópias assíncronas só de leitura (inclusive em outra região) para **escalar leitura**.
  - **Backups automáticos** com restauração para um ponto no tempo (retenção de até 35 dias) e **snapshots** manuais.
  - Sem acesso ao SO da instância de banco (a AWS gerencia).
- **Amazon Aurora:** Relacional da AWS compatível com **MySQL e PostgreSQL**.
  - Mais performático que o MySQL e PostgreSQL padrão (a AWS cita até 5x e 3x, respectivamente).
  - Armazenamento cresce sozinho e mantém **6 cópias dos dados em 3 AZs**.
  - **Aurora Serverless:** capacidade ajustada automaticamente. **Aurora Global Database:** replicação entre regiões.
- **Amazon DynamoDB:** NoSQL **chave-valor e documentos**, serverless, latência de milissegundos de um dígito em qualquer escala.
  - Modos de capacidade: **sob demanda** (paga por requisição) ou **provisionado** (com Auto Scaling).
  - **Global Tables:** replicação multi-região ativa-ativa.
  - **DAX:** cache em memória para leituras em microssegundos.
  - Streams, TTL (expiração automática de itens) e backup point-in-time.
- **Amazon ElastiCache:** Cache em memória gerenciado, compatível com **Redis OSS/Valkey e Memcached**. Latência em microssegundos; reduz a carga do banco e guarda sessões.
- **Amazon Keyspaces:** Cassandra gerenciado e serverless. Não aparece na lista oficial de serviços da prova, então dificilmente cai.
- **Amazon Neptune:** banco de **grafos**. Para redes sociais, motores de recomendação, detecção de fraude e grafos de conhecimento.
- **Amazon DocumentDB:** banco de **documentos** compatível com **MongoDB**.
- **Amazon Redshift:** **data warehouse** em colunas, para análise (OLAP) de grandes volumes com SQL e BI. Redshift Serverless dispensa gerenciar cluster; Redshift Spectrum consulta dados direto no S3.
- **Migração de bancos:** DMS e SCT (ver [3.17](17-migracao-e-transferencia.md)).

| Tipo de dado ou necessidade | Serviço |
| --- | --- |
| Relacional, transações (OLTP), SQL tradicional | RDS ou Aurora |
| Relacional com máxima performance e alta disponibilidade gerenciada | Aurora |
| Chave-valor, escala massiva, latência baixa, serverless | DynamoDB |
| Cache em memória | ElastiCache (ou DAX para DynamoDB) |
| Relacionamentos entre entidades (grafos) | Neptune |
| Documentos JSON compatíveis com MongoDB | DocumentDB |
| Análise de grandes volumes, BI, data warehouse (OLAP) | Redshift |

- **Cai na prova:** Multi-AZ = disponibilidade; Read Replica = performance de leitura. "Banco para carrinho de compras com milhões de acessos por segundo" = DynamoDB. "Recomendações tipo amigos de amigos" = Neptune.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Qual a vantagem do RDS sobre instalar o banco no EC2?" → A AWS cuida de patch, backups, hardware e failover.
- "Como garantir failover automático do banco para outra AZ?" → RDS Multi-AZ.
- "Como aliviar consultas de leitura pesadas?" → Read Replicas (ou cache com ElastiCache).
- "Qual banco relacional compatível com MySQL e PostgreSQL oferece mais performance?" → Aurora.
- "Qual banco NoSQL serverless com latência de milissegundos?" → DynamoDB.
- "Replicação multi-região ativa-ativa no DynamoDB." → Global Tables.
- "Cache de microssegundos para DynamoDB." → DAX.
- "Banco para relacionamentos complexos (redes sociais, fraude)." → Neptune.
- "Migrar banco MongoDB para serviço gerenciado." → DocumentDB.
- "Data warehouse para relatórios de BI sobre petabytes." → Redshift.
- "Quais motores o RDS suporta?" → MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 e Aurora.

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
