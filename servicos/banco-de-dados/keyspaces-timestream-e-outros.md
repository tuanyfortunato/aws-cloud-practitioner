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

## 1. A sequência de funcionamento

**Passo 1.** Identifique se os dados são registros Cassandra, valores com horários ou outro modelo especializado.

**Passo 2.** Compare compatibilidade e disponibilidade da oferta apropriada; a ficha não descreve um único banco para todos os casos.

**Passo 3.** Modele e consulte os dados conforme a interface escolhida. Confira as observações sobre serviços restritos ou encerrados.

## 2. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Não existe um único banco desta ficha que resolva todos esses casos. Algumas ofertas têm restrições comerciais ou estão encerradas; confira as observações e o escopo antes de escolher.

### Tabela de decisão

| Serviço | Modelo | Uso | Observação |
|---|---|---|---|
| **Amazon Keyspaces** ❌ *fora do escopo* | Colunar largo (**Apache Cassandra**, CQL) | Migrar Cassandra para serverless | Fora da lista oficial; raramente cai |
| **Amazon Timestream** | **Séries temporais** | Leituras de sensores IoT, métricas, telemetria | 🔄 *Timestream for LiveAnalytics* fechado a novos clientes (20/06/2025); segue o *Timestream for InfluxDB*. Na prova: "séries temporais" → Timestream |
| **Amazon MemoryDB** ❌ *fora do escopo* | Chave-valor em memória **durável** | Banco primário estilo Redis | [Ficha](memorydb.md) |
| **Amazon DocumentDB** | Documentos (MongoDB) | Catálogos, conteúdo | [Ficha](documentdb.md) |
| **Amazon Neptune** | Grafos | Redes sociais, fraude | [Ficha](neptune.md) |
| **Amazon QLDB** | Ledger imutável | — | 🔄 Encerrado em 31/07/2025 (confirmado) — se aparecer em questão antiga: "registro imutável e verificável criptograficamente" |

### Visão geral: qual banco para qual dado

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

## 3. Caso resolvido: ligando as peças

Para entender a diferença, compare guardar a temperatura de uma máquina a cada minuto com migrar registros de uma aplicação Cassandra. São problemas distintos.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique se os dados são registros Cassandra, valores com horários ou outro modelo especializado.
**Etapa 2:** Compare compatibilidade e disponibilidade da oferta apropriada; a ficha não descreve um único banco para todos os casos.
**Etapa 3:** Modele e consulte os dados conforme a interface escolhida. Confira as observações sobre serviços restritos ou encerrados.

**Resultado e responsabilidade:** A ficha compara bancos especializados. Keyspaces atende aplicações compatíveis com Cassandra; a família Timestream é voltada a séries temporais, isto é, valores associados a momentos.

**Recursos envolvidos:** Bancos especializados por API/modelo, como Cassandra e séries temporais.

**Decisões que precisam ser tomadas:** Tipo de dado, API compatível e oferta disponível.

**Outra situação comentada:** Dados de sensores com tempo como dimensão pedem modelo temporal; popularidade não substitui requisito.

**Por que não concluir mais do que isso:** Keyspaces está fora do escopo; Timestream não citado não deve ser tratado como exclusão formal

## 4. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Guardar leituras de sensores IoT ao longo do tempo."

**Resposta curta:** Timestream.

**Pergunta:** "Migrar Cassandra sem gerenciar servidores."

**Resposta curta:** Keyspaces.

## 5. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Bancos de dados na AWS](https://aws.amazon.com/products/databases/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
