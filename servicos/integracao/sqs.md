# Amazon SQS (Simple Queue Service)

> **Categoria:** Integração de aplicações / filas · **Domínio:** 1 (acoplamento fraco) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** fila de mensagens totalmente gerenciada que **desacopla** produtores e consumidores e absorve picos.

## Como funciona

1. O produtor envia mensagens para a fila.
2. O consumidor **puxa** (*poll*) as mensagens, processa e **apaga**.
3. Enquanto processa, a mensagem fica invisível (*visibility timeout*); se não for apagada a tempo, volta para a fila.

## Tipos de fila

| | **Standard** | **FIFO** |
|---|---|---|
| Throughput | Quase ilimitado | Alto, mas limitado (🧊 milhares/s com lote e modo de alto throughput) |
| Entrega | **Pelo menos uma vez** (pode duplicar) | **Exatamente uma vez** (deduplicação) |
| Ordem | Melhor esforço | **Garantida** (por *message group*) |
| Nome | qualquer | termina em `.fifo` |

## Configurações (📌 números)

| Opção | Valor |
|---|---|
| Tamanho da mensagem | 🔄 até **1 MiB** (antes **256 KiB** — use o valor que estiver nas alternativas); maiores: guardar no S3 e enviar referência (*extended client*) |
| **Retenção** | padrão **4 dias**, de 60 s a **14 dias** |
| **Visibility timeout** | padrão **30 s**, de 0 a **12 h** |
| **Delay queue / message timer** | até **15 min** |
| **Long polling** | espera até **20 s** por mensagens (menos requisições vazias, menor custo) — preferível ao *short polling* |
| **Dead-letter queue (DLQ)** | Recebe mensagens que falharam N vezes (`maxReceiveCount`); *redrive* devolve à fila original |
| **Criptografia** | SSE-SQS (padrão) ou SSE-KMS; TLS em trânsito |
| **Access policy** | Política de recurso (ex.: permitir que um tópico SNS publique) |

## Integrações comuns

- **Lambda** (event source mapping), **Auto Scaling** de workers pelo tamanho da fila (`ApproximateNumberOfMessages`), **SNS fan-out**, notificações do S3, EventBridge.

## Cobrança

- Por milhão de requisições (cada 64 KB = 1 requisição 🧊) + transferência. **1 milhão de requisições grátis/mês** (sempre gratuito).

## ⚠️ Não confundir

- **SQS** (fila, pull, 1 consumidor processa) × **SNS** (pub/sub, push para vários) × **EventBridge** (roteamento de eventos com regras) × **Kinesis** (stream relido por vários consumidores) × **Amazon MQ** (brokers ActiveMQ/RabbitMQ existentes).

## ❓ Perguntas típicas

- "Desacoplar componentes para que um pico não derrube o processamento." → SQS.
- "Garantir ordem e processamento exatamente uma vez." → SQS FIFO.
- "Mensagens que falham repetidamente devem ser isoladas." → Dead-letter queue.
- "Reduzir requisições vazias e custo." → Long polling.
- "Retenção máxima de uma mensagem?" → 14 dias.

## 🔗 Documentação oficial

- [Guia do SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
