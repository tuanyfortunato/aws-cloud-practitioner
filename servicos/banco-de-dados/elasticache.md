# Amazon ElastiCache

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A aplicação consulta repetidamente dados parecidos e o banco principal demora mais do que o desejado.

**Como este serviço ajuda?** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.

**Exemplo do dia a dia:** Uma loja guarda temporariamente o resultado de uma consulta popular num cache. Nas próximas consultas, a aplicação pode usar esse resultado sem consultar o banco de novo.

**O que ele não resolve sozinho?** A aplicação precisa decidir quando atualizar ou invalidar o cache. Ele não acelera qualquer consulta automaticamente nem deve ser tratado sem planejamento como a única cópia de dados essenciais.

**Primeiras palavras para entender:**

- **Memória:** armazenamento de acesso rápido usado durante a execução.
- **Cache:** dados mantidos para reutilização.
- **Invalidar:** deixar de usar uma cópia desatualizada.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Cache em memória · **Domínio:** 3 · **Escopo:** Regional (nós em AZs) · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** cache em memória gerenciado (Valkey, Redis OSS, Memcached) com latência de microssegundos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Cache, motores suportados, endpoints e política de expiração |
| **O que você decide/configura?** | Motor, capacidade, rede e estratégia de cache |
| **Em que ordem as coisas acontecem?** | Aplicação consulta cache; no miss, busca origem e preenche conforme estratégia |
| **O que pode fazer, e em que condição?** | Reduz latência e consultas repetitivas ao banco principal |
| **O que não pode presumir?** | Não acelera automaticamente código que nunca usa o cache; não trate toda modalidade como armazenamento definitivo |

**Caso comentado:** Resultado muito consultado: cache com TTL; aplicação deve tratar expiração e indisponibilidade.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)
