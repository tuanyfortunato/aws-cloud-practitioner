<!-- autoral -->

# Amazon Keyspaces e Amazon Timestream

> **Categoria:** Bancos de propósito específico · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** referência
>
> **Em uma frase:** dois bancos especializados fora da prova: o Keyspaces para aplicações Apache Cassandra e o Timestream para séries temporais.
>
> **Escopo oficial:** 🔀 Keyspaces e MemoryDB ❌ fora do escopo · Timestream ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Alguns dados pedem um banco feito para eles. Uma aplicação escrita para o **Apache Cassandra** (banco de código aberto de colunas largas) e as leituras de temperatura de um sensor a cada minuto, que são uma **série temporal** (valores ligados a momentos), são dois casos.

1. **Amazon Keyspaces (for Apache Cassandra):** banco gerenciado e sem servidor para cargas Cassandra, com o mesmo código e as mesmas ferramentas; escala as tabelas sozinho e cobra pelo uso. Está fora do escopo.
2. **Amazon Timestream for LiveAnalytics:** banco de séries temporais que guarda os dados recentes em memória e move os antigos para um armazenamento mais barato; não aceita novos clientes desde 20/06/2025.
3. **Amazon Timestream for InfluxDB:** a alternativa que a AWS indica para novos clientes. O Timestream não aparece na lista do exame.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon DynamoDB](dynamodb.md) | NoSQL chave-valor sem servidor, no escopo | "NoSQL", "sem servidor" |
| [Amazon MemoryDB](memorydb.md) | Banco em memória durável | "Redis", "Valkey" |
| [Amazon Neptune](neptune.md) | Banco de grafos, no escopo | "Relações" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html)
- [O que é o Timestream for LiveAnalytics](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html)
- [Mudança de disponibilidade do Timestream for LiveAnalytics](https://docs.aws.amazon.com/timestream/latest/developerguide/AmazonTimestreamForLiveAnalytics-availability-change.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
