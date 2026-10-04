# Amazon SNS (Simple Notification Service)

> **Categoria:** Integração de aplicações / pub-sub · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** serviço **pub/sub**: um produtor publica num **tópico** e a mensagem é **empurrada** para todos os assinantes.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Conceitos

| Item | Detalhe |
|---|---|
| **Tópico** | Canal lógico; **Standard** ou **FIFO** (ordem e deduplicação, só para assinantes SQS/Lambda…). |
| **Assinantes (A2A)** | **SQS**, **Lambda**, **HTTP/HTTPS**, Data Firehose. |
| **Assinantes (A2P)** | **E-mail**, **SMS**, **push mobile** (APNs, FCM). |
| **Fan-out** | Um tópico entrega a mesma mensagem a **várias filas SQS** para processamento paralelo e independente. |
| **Message filtering** | *Filter policies* por atributo/corpo: cada assinante recebe só o que interessa. |
| **Retentativas e DLQ** | Políticas de entrega e dead-letter queue (SQS) para falhas. |
| **Criptografia e acesso** | SSE com KMS; *topic policy*. |
| **Tamanho da mensagem** | 🔄 Padrão **256 KiB**; até **1 MiB** configurando o atributo `MaximumMessageSize` do tópico (Standard e FIFO, desde 18/09/2026). |

## Usos

- Alarmes do CloudWatch → e-mail/SMS do time; eventos de pedidos para vários sistemas; notificações push em apps.

## Cobrança

- Por milhão de publicações + entregas por tipo (SMS e e-mail têm preços próprios).

## ⚠️ Não confundir

- **SNS × SQS:** push para vários × fila puxada.
- **SNS × SES:** notificações simples (inclusive e-mail texto) × e-mails formatados em volume (marketing/transacionais).
- **SNS × EventBridge:** notificações em alta escala × roteamento por regras com eventos de AWS/SaaS.

## ❓ Perguntas típicas

- "Enviar a mesma mensagem para vários sistemas e para e-mail." → SNS.
- "Um evento processado por várias filas em paralelo." → Fan-out SNS + SQS.
- "Notificar o time por SMS quando um alarme disparar." → CloudWatch alarm → SNS.

## 🔗 Documentação oficial

- [Guia do SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
