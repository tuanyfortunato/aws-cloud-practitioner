# Amazon EventBridge

> **Categoria:** Integração de aplicações / eventos · **Domínio:** 3 · **Escopo:** Regional (cross-account e cross-region) · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** **barramento de eventos** serverless que recebe eventos de serviços AWS, das suas aplicações e de parceiros SaaS e os roteia por **regras**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **central de eventos com regras**: "quando acontecer X, avise Y" — vale para serviços AWS, seus apps e apps SaaS.

- ✅ **Escolha quando:** precisa **reagir a eventos** com regras ou **agendar tarefas** (cron) sem servidor.
- 🚫 **Não é a resposta quando:** precisa **orquestrar várias etapas** com estado → [Step Functions](step-functions.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "reagir a eventos", "regras", "eventos de SaaS", "agendar tarefa".
<!-- didatico:fim -->

## Componentes

| Componente | Detalhe |
|---|---|
| **Event bus** | **Default** (eventos de serviços AWS), **custom** (suas aplicações) e **partner** (SaaS: Zendesk, Datadog, Shopify…). |
| **Rules** | *Event pattern* (filtra por conteúdo do evento) → **targets** (Lambda, SQS, SNS, Step Functions, ECS task, Kinesis, API Gateway, outro bus…). |
| **EventBridge Scheduler** | Agendamentos **cron/rate ou únicos**, com fuso horário, para milhões de tarefas (substitui as *scheduled rules*). |
| **Pipes** | Conexões ponto-a-ponto origem → filtro → enriquecimento → destino (ex.: SQS → Step Functions). |
| **Archive & replay** | Guardar e reprocessar eventos. |
| **Schema registry** | Descobre e documenta o formato dos eventos. |
| **API destinations** | Envia eventos para APIs HTTP externas. |

## Exemplos

- "Quando uma instância EC2 mudar para `stopped`, notificar no Slack."
- Achado do GuardDuty → Lambda que isola a instância.
- Evento de um SaaS (novo ticket) → workflow interno.

## Cobrança

- Por milhão de eventos publicados (eventos de serviços AWS no bus default são gratuitos); Scheduler por invocação; Pipes por requisição.

## ⚠️ Não confundir

- **EventBridge** (roteia e reage a eventos, inclusive de SaaS) × **SNS** (notificação pub/sub) × **Step Functions** (orquestra fluxos com estado) × **CloudWatch Events** (nome antigo do EventBridge).

## ❓ Perguntas típicas

- "Reagir a eventos de serviços AWS e de aplicações SaaS com regras." → EventBridge.
- "Executar uma tarefa todo dia às 2h sem servidor." → EventBridge Scheduler + Lambda.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Event buses, rules, targets; Scheduler e Pipes conforme necessidade |
| **O que você decide/configura?** | Padrão de evento, destinos, role e falhas |
| **Em que ordem as coisas acontecem?** | Evento entra no bus, regra filtra e destino recebe |
| **O que pode fazer, e em que condição?** | Integra eventos AWS, apps e fontes compatíveis |
| **O que não pode presumir?** | Não executa lógica de negócio por si; evento exige consumidor/destino |

**Caso comentado:** Mudança de estado dispara automação: regra EventBridge com destino autorizado.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
