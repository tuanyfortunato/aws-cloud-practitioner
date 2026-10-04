# Amazon MemoryDB

> **Categoria:** Banco em memória durável · **Domínio:** 3 · **Escopo:** Regional (multi-AZ) · **Tópico do guia:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** banco de dados **primário** em memória, compatível com Valkey/Redis, com durabilidade multi-AZ.

## Diferencial

- Grava as alterações num **log transacional distribuído em várias AZs** → não perde dados se um nó falhar (ao contrário de um cache).
- Leituras em microssegundos, escritas em milissegundos de um dígito.
- Uso: microsserviços que usam estruturas Redis como banco principal, sessões críticas, placares, feeds, busca vetorial.

## Cobrança

- Por nó-hora + dados gravados + snapshots.

## ⚠️ Não confundir

- ElastiCache = **cache** (pode ser reconstruído). MemoryDB = **banco durável**.

## ❓ Perguntas típicas

- "Banco principal com latência de microssegundos e durabilidade, compatível com Redis." → MemoryDB.

## 🔗 Documentação oficial

- [MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html)
