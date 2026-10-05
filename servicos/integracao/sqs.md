# Amazon SQS (Simple Queue Service)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um sistema recebe trabalhos mais rápido do que consegue executá-los. Se depender de tudo acontecer imediatamente, pode perder pedidos ou ficar indisponível.

**Como este serviço ajuda?** SQS guarda mensagens numa fila até que consumidores as recebam e processem. Isso permite separar o envio de uma tarefa da execução dela.

**Exemplo do dia a dia:** O site recebe pedidos de geração de certificados e coloca mensagens na fila. Um programa processa os pedidos no ritmo que consegue atender.

**O que ele não resolve sozinho?** SQS não executa a tarefa nem garante, em toda modalidade, que ela será recebida apenas uma vez. O consumidor deve tratar falhas e as condições de entrega.

**Primeiras palavras para entender:**

- **Mensagem:** informação sobre uma tarefa.
- **Fila:** lugar de espera.
- **Consumidor:** programa que recebe e processa mensagens.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Integração de aplicações / filas · **Domínio:** 1 (acoplamento fraco) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** fila de mensagens totalmente gerenciada que **desacopla** produtores e consumidores e absorve picos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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

- Por milhão de requisições (cada 64 KB = 1 requisição 🧊) + transferência. **1 milhão de requisições grátis/mês** para todos os clientes (✔️ Always Free nos planos Free e Paid).

## ⚠️ Não confundir

- **SQS** (fila, pull, 1 consumidor processa) × **SNS** (pub/sub, push para vários) × **EventBridge** (roteamento de eventos com regras) × **Kinesis** (stream relido por vários consumidores) × **Amazon MQ** (brokers ActiveMQ/RabbitMQ existentes).

## ❓ Perguntas típicas

- "Desacoplar componentes para que um pico não derrube o processamento." → SQS.
- "Garantir ordem e processamento exatamente uma vez." → SQS FIFO.
- "Mensagens que falham repetidamente devem ser isoladas." → Dead-letter queue.
- "Reduzir requisições vazias e custo." → Long polling.
- "Retenção máxima de uma mensagem?" → 14 dias.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Fila, mensagens, produtores, consumidores e DLQ |
| **O que você decide/configura?** | Standard/FIFO, retenção, visibility timeout e redrive |
| **Em que ordem as coisas acontecem?** | Envie, receba, processe e exclua após sucesso |
| **O que pode fazer, e em que condição?** | Amortece picos e desacopla execução |
| **O que não pode presumir?** | Receber não exclui; falha/timeout pode tornar mensagem visível novamente; efeitos de negócio precisam ser idempotentes |

**Caso comentado:** Worker falha após leitura: mensagem pode reaparecer; trate repetição e DLQ configurada.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
