# Amazon Keyspaces, Timestream e outros bancos especializados

> **Categoria:** Bancos de propósito específico · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** a AWS tem um banco "sob medida" para cada modelo de dados — saiba associar o modelo ao serviço.
>
> **Escopo oficial:** 🔀 Keyspaces e MemoryDB ❌ fora do escopo · Timestream ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é a **prateleira certa para cada tipo de dado**: Cassandra, séries temporais, ledger e outros modelos especializados.

- ✅ **Escolha quando:** o enunciado cita um **modelo de dados específico**. (Keyspaces e MemoryDB estão fora da prova.)
- 🚫 **Não é a resposta quando:** na dúvida entre bancos, use a tabela "qual banco para qual dado" desta ficha.
- 🎯 **Palavras do enunciado que apontam para ele:** "Cassandra" → Keyspaces; "séries temporais" ou "leituras de sensores ao longo do tempo" → Timestream.
<!-- didatico:fim -->

## Tabela de decisão

| Serviço | Modelo | Uso | Observação |
|---|---|---|---|
| **Amazon Keyspaces** ❌ *fora do escopo* | Colunar largo (**Apache Cassandra**, CQL) | Migrar Cassandra para serverless | Fora da lista oficial; raramente cai |
| **Amazon Timestream** | **Séries temporais** | Leituras de sensores IoT, métricas, telemetria | 🔄 *Timestream for LiveAnalytics* fechado a novos clientes (20/06/2025); segue o *Timestream for InfluxDB*. Na prova: "séries temporais" → Timestream |
| **Amazon MemoryDB** ❌ *fora do escopo* | Chave-valor em memória **durável** | Banco primário estilo Redis | [Ficha](memorydb.md) |
| **Amazon DocumentDB** | Documentos (MongoDB) | Catálogos, conteúdo | [Ficha](documentdb.md) |
| **Amazon Neptune** | Grafos | Redes sociais, fraude | [Ficha](neptune.md) |
| **Amazon QLDB** | Ledger imutável | — | 🔄 Encerrado em 31/07/2025 (confirmado) — se aparecer em questão antiga: "registro imutável e verificável criptograficamente" |

## Visão geral: qual banco para qual dado

| Necessidade | Serviço |
|---|---|
| Relacional OLTP | [RDS](rds.md) / [Aurora](aurora.md) |
| Chave-valor em escala, serverless | [DynamoDB](dynamodb.md) |
| Cache em memória | [ElastiCache](elasticache.md) / DAX |
| Data warehouse OLAP | [Redshift](redshift.md) |
| Grafos | [Neptune](neptune.md) |
| Documentos | [DocumentDB](documentdb.md) |
| Séries temporais | Timestream |
| Cassandra | Keyspaces |

## ❓ Perguntas típicas

- "Guardar leituras de sensores IoT ao longo do tempo." → Timestream.
- "Migrar Cassandra sem gerenciar servidores." → Keyspaces.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Bancos especializados por API/modelo, como Cassandra e séries temporais |
| **O que você decide/configura?** | Tipo de dado, API compatível e oferta disponível |
| **Em que ordem as coisas acontecem?** | Escolha banco pelo modelo de acesso antes de migrar dados |
| **O que pode fazer, e em que condição?** | Serviços especializados podem reduzir gestão de infraestrutura |
| **O que não pode presumir?** | Keyspaces está fora do escopo; Timestream não citado não deve ser tratado como exclusão formal |

**Caso comentado:** Dados de sensores com tempo como dimensão pedem modelo temporal; popularidade não substitui requisito.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Bancos de dados na AWS](https://aws.amazon.com/products/databases/)
