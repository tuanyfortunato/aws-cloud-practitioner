# Amazon ElastiCache

> **Categoria:** Cache em memória · **Domínio:** 3 · **Escopo:** Regional (nós em AZs) · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** cache em memória gerenciado (Valkey, Redis OSS, Memcached) com latência de microssegundos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **memória de curto prazo na frente do banco**: guarda as respostas mais pedidas para responder em microssegundos.

- ✅ **Escolha quando:** quer **reduzir a carga e a latência do banco** ou guardar **sessões de usuário**.
- 🚫 **Não é a resposta quando:** o cache é **só para DynamoDB** → DAX, na ficha do [DynamoDB](dynamodb.md); precisa de **banco em memória durável** → [MemoryDB](memorydb.md) (fora da prova).
- 🎯 **Palavras do enunciado que apontam para ele:** "cache em memória", "Redis, Valkey, Memcached", "reduzir leituras no banco", "armazenar sessões".
<!-- didatico:fim -->

## Para que serve

- Reduzir carga e latência do banco (cache de consultas), **armazenar sessões** (aplicação stateless), placares, filas simples, pub/sub, rate limiting.

## Motores

| Motor | Destaques |
|---|---|
| **Valkey** | Fork open source do Redis, recomendado pela AWS, mais barato. |
| **Redis OSS** | Estruturas de dados ricas, **replicação, Multi-AZ com failover, persistência/backup**, pub/sub. |
| **Memcached** | Simples, multithread, **sem persistência nem replicação**; escala horizontal por sharding. |

## Configurações

- **Serverless** (sem planejar nós; paga por dados armazenados e ECPUs) ou **clusters de nós** (tipo de nó, shards, réplicas).
- Criptografia em repouso e em trânsito, autenticação (RBAC/AUTH), backups (Valkey/Redis), *Global Datastore* (replicação entre regiões).

## Cobrança

- Por nó-hora (ou nós reservados) ou, no serverless, por GB-hora armazenado + ECPUs. 🔄 Coberto por Database Savings Plans.

## ⚠️ Pegadinhas e não confundir

- **ElastiCache** (cache, dados podem ser recriados) × **MemoryDB** (banco primário durável) × **DAX** (cache só do DynamoDB).
- "Guardar sessão fora do servidor para escalar horizontalmente" → ElastiCache (ou DynamoDB).

## ❓ Perguntas típicas

- "Reduzir a carga de leitura do RDS com cache em memória." → ElastiCache.
- "Armazenar sessões de usuário para aplicação stateless." → ElastiCache.

## 🔗 Documentação oficial

- [ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)
