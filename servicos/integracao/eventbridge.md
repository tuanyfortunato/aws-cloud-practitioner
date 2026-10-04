# Amazon EventBridge

> **Categoria:** Integração de aplicações / eventos · **Domínio:** 3 · **Escopo:** Regional (cross-account e cross-region) · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** **barramento de eventos** serverless que recebe eventos de serviços AWS, das suas aplicações e de parceiros SaaS e os roteia por **regras**.

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

## 🔗 Documentação oficial

- [Guia do EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
