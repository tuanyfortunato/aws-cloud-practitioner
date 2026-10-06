# Amazon SNS (Simple Notification Service)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um acontecimento precisa avisar vários interessados, e o sistema não quer enviar manualmente uma mensagem diferente para cada um.

**Como este serviço ajuda?** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis. Cada assinante recebe a notificação pelo mecanismo configurado.

**Exemplo do dia a dia:** Quando um pedido é confirmado, um tópico avisa sistemas de faturamento e acompanhamento por assinaturas compatíveis.

**O que ele não resolve sozinho?** Publicar para vários assinantes é diferente de guardar trabalhos numa fila para um consumidor. Entrega, conteúdo e destinatários precisam de configuração apropriada.

**Primeiras palavras para entender:**

- **Tópico:** canal de publicação.
- **Assinante:** destino inscrito nesse canal.
- **Pub/sub:** padrão de publicar mensagens e recebê-las por assinaturas.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Integração de aplicações / pub-sub · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** serviço **pub/sub**: um produtor publica num **tópico** e a mensagem é **empurrada** para todos os assinantes.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina um tópico e os destinos que devem receber notificações compatíveis.

**Passo 2.** Publique uma mensagem. O serviço encaminha a notificação conforme assinaturas e filtros configurados.

**Passo 3.** Cada destinatário realiza seu próprio trabalho e precisa tratar falhas. Publicar uma mensagem não comprova sucesso em todos os sistemas interessados.

## 2. Recursos e opções, com significado

### Conceitos

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

### Usos

Alarmes do CloudWatch → e-mail/SMS do time; eventos de pedidos para vários sistemas; notificações push em apps.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Publicar para vários assinantes é diferente de guardar trabalhos numa fila para um consumidor. Entrega, conteúdo e destinatários precisam de configuração apropriada.

### ⚠️ Não confundir

**SNS × SQS:** push para vários × fila puxada.

**SNS × SES:** notificações simples (inclusive e-mail texto) × e-mails formatados em volume (marketing/transacionais).

**SNS × EventBridge:** notificações em alta escala × roteamento por regras com eventos de AWS/SaaS.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por milhão de publicações + entregas por tipo (SMS e e-mail têm preços próprios).

## 5. Caso resolvido: ligando as peças

Quando um pedido é confirmado, um tópico avisa sistemas de faturamento e acompanhamento por assinaturas compatíveis.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina um tópico e os destinos que devem receber notificações compatíveis.
**Etapa 2:** Publique uma mensagem. O serviço encaminha a notificação conforme assinaturas e filtros configurados.
**Etapa 3:** Cada destinatário realiza seu próprio trabalho e precisa tratar falhas. Publicar uma mensagem não comprova sucesso em todos os sistemas interessados.

**Resultado e responsabilidade:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis. Cada assinante recebe a notificação pelo mecanismo configurado.

**Recursos envolvidos:** Topic, publishers, subscriptions e filtros.

**Decisões que precisam ser tomadas:** Destinos, acesso, filtros e tratamento de falha.

**Outra situação comentada:** Pedido notifica estoque e cobrança: topic com filas independentes permite cada equipe consumir no próprio ritmo.

**Por que não concluir mais do que isso:** Não é fila persistente individual de cada consumidor; use SQS quando necessário

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Enviar a mesma mensagem para vários sistemas e para e-mail."

**Resposta curta:** SNS.

**Pergunta:** "Um evento processado por várias filas em paralelo."

**Resposta curta:** Fan-out SNS + SQS.

**Pergunta:** "Notificar o time por SMS quando um alarme disparar."

**Resposta curta:** CloudWatch alarm → SNS.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
