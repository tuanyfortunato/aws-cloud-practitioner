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

## 1. A sequência de funcionamento

**Passo 1.** O produtor envia uma mensagem descrevendo um trabalho, como emitir um certificado. A fila guarda a mensagem; ela ainda não executou o trabalho.

**Passo 2.** O consumidor recebe a mensagem e realiza a tarefa. Durante o prazo de invisibilidade, a mensagem fica indisponível para novos recebimentos.

**Passo 3.** Após sucesso, o consumidor exclui a mensagem. Se falhar sem excluir, ela pode reaparecer; trate repetições e encaminhamento para uma fila de falhas configurada.

## 2. Recursos e opções, com significado

### Como funciona

1. O produtor envia mensagens para a fila.

2. O consumidor **puxa** (*poll*) as mensagens, processa e **apaga**.

3. Enquanto processa, a mensagem fica invisível (*visibility timeout*); se não for apagada a tempo, volta para a fila.

### Tipos de fila

| | **Standard** | **FIFO** |
|---|---|---|
| Throughput | Quase ilimitado | Alto, mas limitado (🧊 milhares/s com lote e modo de alto throughput) |
| Entrega | **Pelo menos uma vez** (pode duplicar) | **Deduplicação no envio**; a aplicação ainda precisa tratar recebimento e efeitos repetidos |
| Ordem | Melhor esforço | **Garantida** (por *message group*) |
| Nome | qualquer | termina em `.fifo` |

### Configurações (📌 números)

**Tamanho da mensagem**

**Valor:** 🔄 até **1 MiB** (antes **256 KiB** — use o valor que estiver nas alternativas); maiores: guardar no S3 e enviar referência (*extended client*)

**Retenção**

**Valor:** padrão **4 dias**, de 60 s a **14 dias**

**Visibility timeout**

**Valor:** padrão **30 s**, de 0 a **12 h**

**Delay queue / message timer**

**Valor:** até **15 min**

**Long polling**

**Valor:** espera até **20 s** por mensagens (menos requisições vazias, menor custo) — preferível ao *short polling*

**Dead-letter queue (DLQ)**

**Valor:** Recebe mensagens que falharam N vezes (`maxReceiveCount`); *redrive* devolve à fila original

**Criptografia**

**Valor:** SSE-SQS (padrão) ou SSE-KMS; TLS em trânsito

**Access policy**

**Valor:** Política de recurso (ex.: permitir que um tópico SNS publique)

### Integrações comuns

**Lambda** (event source mapping), **Auto Scaling** de workers pelo tamanho da fila (`ApproximateNumberOfMessages`), **SNS fan-out**, notificações do S3, EventBridge.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

SQS não executa a tarefa nem garante, em toda modalidade, que ela será recebida apenas uma vez. O consumidor deve tratar falhas e as condições de entrega.

### ⚠️ Não confundir

**SQS** (fila, pull, 1 consumidor processa) × **SNS** (pub/sub, push para vários) × **EventBridge** (roteamento de eventos com regras) × **Kinesis** (stream relido por vários consumidores) × **Amazon MQ** (brokers ActiveMQ/RabbitMQ existentes).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por milhão de requisições (cada 64 KB = 1 requisição 🧊) + transferência. **1 milhão de requisições grátis/mês** para todos os clientes (✔️ Always Free nos planos Free e Paid).

## 5. Caso resolvido: ligando as peças

A secretaria recebe muitos pedidos de certificado ao fim de um curso. Gerar todos durante a mesma conexão do aluno pode tornar o site lento. A escola separa recebimento do pedido e execução do trabalho.

O site envia uma mensagem com a identificação do pedido. Um consumidor recebe a mensagem, verifica os dados e gera o certificado. O SQS não gera o arquivo: o programa consumidor faz isso. Depois de confirmar sucesso, o programa exclui a mensagem. Durante o processamento, o prazo de invisibilidade reduz novos recebimentos daquela mensagem.

Se o consumidor falhar antes de excluir, a mensagem pode reaparecer. O programa precisa reconhecer pedidos já concluídos para não duplicar efeitos. FIFO trata ordenação por grupo e deduplicação no envio sob condições; não elimina todo risco de efeitos repetidos. SNS atenderia avisos a vários destinos, mas não substitui sozinho esse trabalho em espera.

**Recursos envolvidos:** Fila, mensagens, produtores, consumidores e DLQ.

**Decisões que precisam ser tomadas:** Standard/FIFO, retenção, visibility timeout e redrive.

**Outra situação comentada:** Worker falha após leitura: mensagem pode reaparecer; trate repetição e DLQ configurada.

**Por que não concluir mais do que isso:** Receber não exclui; falha/timeout pode tornar mensagem visível novamente; efeitos de negócio precisam ser idempotentes

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Desacoplar componentes para que um pico não derrube o processamento."

**Resposta curta:** SQS.

**Pergunta:** "Ordenar mensagens por grupo e evitar envios duplicados dentro das condições de deduplicação."

**Resposta curta:** SQS FIFO; isso não garante sozinho efeitos de negócio apenas uma vez.

**Pergunta:** "Mensagens que falham repetidamente devem ser isoladas."

**Resposta curta:** Dead-letter queue.

**Pergunta:** "Reduzir requisições vazias e custo."

**Resposta curta:** Long polling.

**Pergunta:** "Retenção máxima de uma mensagem?"

**Resposta curta:** 14 dias.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Deduplicação FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html)
- [Risco de processamento repetido](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/avoding-processing-duplicates-in-multiple-producer-consumer-system.html)
- [Guia do SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
