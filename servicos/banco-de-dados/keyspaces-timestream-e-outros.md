# Amazon Keyspaces, Timestream e outros bancos especializados

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Nem todos os dados têm a mesma estrutura: leituras de sensores ao longo do tempo e registros de uma aplicação Cassandra pedem soluções diferentes.

**Como este serviço ajuda?** A ficha compara bancos especializados. Keyspaces atende aplicações compatíveis com Cassandra; a família Timestream é voltada a séries temporais, isto é, valores associados a momentos.

**Exemplo do dia a dia:** Para entender a diferença, compare guardar a temperatura de uma máquina a cada minuto com migrar registros de uma aplicação Cassandra. São problemas distintos.

**O que ele não resolve sozinho?** Não existe um único banco desta ficha que resolva todos esses casos. Algumas ofertas têm restrições comerciais ou estão encerradas; confira as observações e o escopo antes de escolher.

**Primeiras palavras para entender:**

- **Série temporal:** valores com data e hora.
- **Cassandra:** tecnologia de banco com modelo e interface próprios.
- **Modelo de dados:** forma de organizar registros.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Bancos de propósito específico · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** a AWS tem um banco "sob medida" para cada modelo de dados — saiba associar o modelo ao serviço.
>
> **Escopo oficial:** 🔀 Keyspaces e MemoryDB ❌ fora do escopo · Timestream ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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
