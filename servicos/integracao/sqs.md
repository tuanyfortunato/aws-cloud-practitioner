<!-- autoral -->

# Amazon SQS (Simple Queue Service)

> **Categoria:** Integração de aplicações · **Domínio:** 1 (acoplamento fraco) e 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** fila de mensagens gerenciada que **desacopla** quem pede um trabalho de quem o executa e absorve picos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) · base em [0.4 Como programas conversam](../../docs/fundamentos/04-api-e-filas.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

Um sistema recebe pedidos mais rápido do que consegue atendê-los. No primeiro dia de matrículas, o site da escola recebe milhares de formulários, e cada um exige gerar um PDF e avisar o financeiro. Se o site esperar esses trabalhos terminarem, ele trava; se o gerador de PDF cair, os pedidos se perdem.

O SQS resolve isso com uma fila hospedada pela AWS. O site deixa uma mensagem na fila e responde ao usuário na hora; os programas que geram os PDFs buscam as mensagens no ritmo deles. Um pico só aumenta a fila, e uma falha do consumidor não apaga o pedido. Esse desenho, em que as partes não precisam estar no ar ao mesmo tempo, é o **acoplamento fraco** da [aula 1.3](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md).

O limite: o SQS guarda e entrega mensagens, mas não executa o trabalho. Quem gera o PDF é o programa consumidor, e é ele que precisa tratar falhas e mensagens repetidas. A explicação completa, com a figura do fluxo, está na [aula 3.13](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md).

## Como funciona

1. O **produtor** envia a mensagem para a fila. O SQS guarda a mensagem de forma redundante; na fila padrão, em várias zonas de disponibilidade antes de confirmar o envio.
2. O **consumidor** pede mensagens à fila. O SQS não empurra a mensagem: é o consumidor que busca (*polling*).
3. A mensagem recebida continua na fila, mas fica invisível para os outros consumidores durante o **visibility timeout** (prazo de invisibilidade).
4. Se o trabalho der certo, o consumidor **apaga** a mensagem. Se não apagar dentro do prazo, ela volta a ficar visível e pode ser recebida de novo.
5. Depois de um número configurado de recebimentos sem exclusão (`maxReceiveCount`), a mensagem vai para a **fila de mensagens mortas** (*dead-letter queue*, DLQ), se houver uma configurada. O **redrive** devolve essas mensagens à fila de origem depois que o problema for resolvido.

## Opções principais

| | Fila padrão (Standard) | Fila FIFO |
|---|---|---|
| Vazão | Quase ilimitada | 300 chamadas por segundo por ação, ou 3.000 mensagens por segundo com lotes de 10; mais no modo de alta vazão |
| Entrega | **Pelo menos uma vez**: uma mensagem pode chegar repetida | **Processamento exato uma vez**: envios repetidos dentro de 5 minutos não duplicam a mensagem |
| Ordem | Melhor esforço: pode chegar fora de ordem | **Primeiro a entrar, primeiro a sair** dentro de cada grupo de mensagens |
| Nome | Livre | Termina em `.fifo` |
| Quando usar | A vazão importa mais e a aplicação tolera repetição | A ordem importa: comandos do usuário, mudanças de preço, matrícula só depois do cadastro |

| Opção | O que faz | Quando lembrar |
|---|---|---|
| Long polling | O consumidor espera até 20 segundos por uma mensagem antes de receber resposta vazia | Menos respostas vazias e menor custo; o padrão é o short polling, que responde na hora |
| Fila de mensagens mortas (DLQ) | Separa as mensagens que falharam várias vezes | Uma mensagem com defeito não pode travar a fila principal |
| Atraso (delay queue ou message timer) | Esconde a mensagem nova por até 15 minutos antes da entrega | Dar tempo antes do processamento; para agendar além disso, use o EventBridge Scheduler ([aula 3.13](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)) |
| Criptografia no servidor | SSE-SQS, com chaves do próprio SQS, ou SSE-KMS, com chaves do AWS KMS | A SSE-SQS vem ativada por padrão nas filas novas criadas pelo console ou por endpoint HTTPS |
| Mensagem grande | A Extended Client Library guarda o conteúdo no S3 e manda só a referência pela fila | Mensagens acima de 1 MiB |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Retenção da mensagem | 4 dias por padrão; de 60 segundos a 14 dias | 06/10/2026 |
| Visibility timeout | 30 segundos por padrão; de 0 a 12 horas | 06/10/2026 |
| Tamanho máximo da mensagem | 1 MiB; material antigo cita 256 KiB, o limite anterior | 06/10/2026 |
| Espera máxima do long polling | 20 segundos | 06/10/2026 |
| Atraso de entrega | De 0 a 15 minutos | 06/10/2026 |
| Mensagens por lote | Até 10 por requisição | 06/10/2026 |
| Intervalo de deduplicação da FIFO | 5 minutos | 06/10/2026 |
| Mensagens guardadas na fila | Sem limite | 06/10/2026 |

## Como é cobrado

Você paga por requisição, sem taxa mínima: cada ação na API do SQS conta como uma requisição, e o preço é dado por milhão de requisições. As ações de enviar, receber, apagar e mudar a visibilidade de mensagens em filas FIFO têm tarifa própria. Todos os clientes têm **1 milhão de requisições grátis por mês**, somadas em todas as Regiões.

Cada pedaço de 64 KB da carga conta como uma requisição: enviar 1 MiB de uma vez custa 16 requisições. Uma requisição leva de 1 a 10 mensagens, então agrupar mensagens em lotes e usar long polling reduzem a conta.

A transferência de dados entre o SQS e recursos da mesma Região não é cobrada; entre Regiões e para a internet vale a tarifa padrão de transferência ([aula 4.3](../../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md)). Guardar mensagens grandes no S3 gera a cobrança do S3, e usar chaves do KMS gera a cobrança das chamadas ao KMS.

## Não confundir com

| Serviço | Diferença para o SQS | Pista no enunciado |
|---|---|---|
| [Amazon SNS](sns.md) | Empurra a mensagem na hora para todos os assinantes de um tópico; o SQS guarda até um consumidor buscar | "Notificar vários sistemas", "alerta por e-mail ou SMS" |
| SNS + SQS (fan-out) | O tópico copia cada mensagem para várias filas, e cada fila alimenta um sistema | "Vários sistemas processam a mesma mensagem, cada um no seu ritmo" |
| [Amazon EventBridge](eventbridge.md) | Roteia eventos por regras entre serviços da AWS, aplicações próprias e softwares de terceiros | "Reagir quando algo acontece", "agendar uma tarefa" |
| [AWS Step Functions](step-functions.md) | Coordena um fluxo de etapas em ordem, com decisões e novas tentativas | "Processo de várias etapas", "esperar aprovação" |
| [Amazon Kinesis Data Streams](../analytics/kinesis.md) | Fluxo ordenado de dados em tempo real que vários aplicativos leem ao mesmo tempo; no SQS, cada mensagem é processada e apagada | "Tempo real", "vários consumidores leem os mesmos dados" |
| [Amazon MQ](amazon-mq.md) | Broker gerenciado para Apache ActiveMQ e RabbitMQ, com protocolos como JMS, AMQP e MQTT | "Migrar uma aplicação que já usa um broker", "sem reescrever" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [Tipos de fila](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html)
- [Fila padrão](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html)
- [Processamento exato uma vez na FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html)
- [Cotas de mensagens](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html)
- [Cotas da fila padrão](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-queues.html) e [da fila FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-fifo.html)
- [Visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)
- [Short e long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html)
- [Filas de mensagens mortas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
- [Filas com atraso](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html)
- [Criptografia no servidor](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html) e [configuração da SSE-SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html)
- [Mensagens grandes com o S3](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-s3-messages.html)
- [Preços do Amazon SQS](https://aws.amazon.com/sqs/pricing/)
- [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
