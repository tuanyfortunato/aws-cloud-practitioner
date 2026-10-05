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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Banco compatível com APIs Redis/Valkey conforme oferta, shards e réplicas |
| **O que você decide/configura?** | Motor, capacidade, acesso e disponibilidade |
| **Em que ordem as coisas acontecem?** | Aplicação acessa dados em memória com mecanismos de durabilidade do serviço |
| **O que pode fazer, e em que condição?** | Pode servir como banco principal para workloads compatíveis |
| **O que não pode presumir?** | Está fora do escopo consultado; cache e banco durável não têm o mesmo objetivo |

**Caso comentado:** Necessidade de banco durável de baixa latência difere de cache descartável; preserve essa diferença sem priorizar na CLF-C02.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html)
