# Amazon MemoryDB

> **Categoria:** Banco em memória durável · **Domínio:** 3 · **Escopo:** Regional (multi-AZ) · **Tópico do guia:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** banco de dados **primário** em memória, compatível com Valkey/Redis, com durabilidade multi-AZ.
>
> **Escopo oficial:** ❌ Fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência. Na prova, "cache em memória" → **ElastiCache** (no escopo).

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** parece um cache em memória, mas **não esquece**: grava tudo de forma durável em várias AZs.

- ✅ **Escolha quando:** precisa de um **banco principal em memória**, compatível com Redis/Valkey, sem perder dados. Só para referência — **não cai na prova**. Se aparecer como alternativa, provavelmente é distrator.
- 🚫 **Não é a resposta quando:** na prova, "cache em memória" é o [ElastiCache](elasticache.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "banco em memória durável", "compatível com Redis".
<!-- didatico:fim -->

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
