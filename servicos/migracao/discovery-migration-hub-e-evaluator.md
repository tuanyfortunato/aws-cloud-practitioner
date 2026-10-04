# Migration Evaluator, Application Discovery Service e Migration Hub

> **Categoria:** Migração / avaliação e planejamento · **Domínio:** 1 (migração) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) · [1.6 Estratégias de migração](../../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)
>
> **Em uma frase:** as ferramentas das fases **avaliar → planejar → acompanhar** de uma migração.
>
> **Escopo oficial:** ✅ No escopo (Migration Hub e Application Discovery Service fechados a novos clientes) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é a **preparação da mudança**: medir os móveis (Discovery), fazer o orçamento (Migration Evaluator) e acompanhar a obra (Migration Hub).

- ✅ **Escolha quando:** precisa **planejar e acompanhar** uma migração.
- 🚫 **Não é a resposta quando:** precisa **migrar de fato** → [Application Migration Service](application-migration-service.md) ou [DMS](dms-e-sct.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "dependências entre servidores" → Application Discovery Service; "custo da migração (TCO)" → Migration Evaluator; "painel central" → Migration Hub.
<!-- didatico:fim -->

## Comparação

| Serviço | Fase | O que faz | Detalhes |
|---|---|---|---|
| **Migration Evaluator** (antigo TSO Logic) | Avaliar | Monta o **caso de negócio (TCO)**: quanto custaria o ambiente atual na AWS | Coletor sem agente ou importação de inventário; recomendações de *rightsizing* e licenças; **gratuito** |
| **AWS Application Discovery Service** | Avaliar | Levanta **inventário**, **uso** e **dependências** entre servidores on-premises | **Agentless Collector** (VMware) ou **Discovery Agent** (físicos/VMs, mais detalhado: processos e conexões de rede); dados vão para o Migration Hub |
| **AWS Migration Hub** | Acompanhar | **Painel único** do progresso de migrações feitas com várias ferramentas (MGN, DMS, parceiros) | Agrupamento em aplicações, *Strategy Recommendations* (sugere o "R" de cada aplicação), *Orchestrator* (modelos de workflow) |

## 🔄 Atualizações 2025-2026

- **AWS Migration Hub** e **AWS Application Discovery Service** estão **fechados a novos clientes desde 07/11/2025**, mas continuam na lista oficial da prova — estude a função de cada um.
- **Migration Evaluator** entrou explicitamente na lista de serviços no escopo.
- A AWS lançou o **AWS Transform**, que usa agentes de IA generativa para acelerar migrações e modernizações (VMware, mainframe, .NET, Java) — 🧊 fora da prova.

## Sequência típica de migração

1. **Avaliar:** Migration Evaluator (custo) + Application Discovery Service (inventário e dependências).
2. **Mobilizar/planejar:** Migration Hub, escolha dos 7 Rs, landing zone (Control Tower).
3. **Migrar:** [Application Migration Service](application-migration-service.md), [DMS/SCT](dms-e-sct.md), [DataSync/Snow](datasync-e-transfer-family.md).
4. **Acompanhar:** Migration Hub.

## ❓ Perguntas típicas

- "Estimar quanto a empresa vai economizar ao migrar." → Migration Evaluator.
- "Levantar servidores e dependências antes de migrar." → Application Discovery Service.
- "Acompanhar todas as migrações num painel central." → Migration Hub.

## 🔗 Documentação oficial

- [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) · [Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html) · [Migration Hub](https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html)
