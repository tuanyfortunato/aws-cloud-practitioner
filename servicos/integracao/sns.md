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

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **MiB / KiB:** Unidades em escala binária: cada nível corresponde a 1.024 do anterior. MiB e MB não são a mesma unidade; preserve a unidade indicada pelo serviço.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **HTTPS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **policy:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.
- **FIFO:** Primeiro a entrar, primeiro a sair. No SQS, a ordenação considera grupos de mensagens; deduplicação no envio não garante ausência de repetição de efeitos no programa.
- **DLQ / dead-letter queue:** Fila separada para mensagens que atingiram condições configuradas de falha. Ajuda a isolar e investigar o problema; não corrige a mensagem automaticamente.
- **deduplicação:** Identificação e tratamento de entradas repetidas conforme um critério e uma janela. É diferente de garantir toda a execução da aplicação apenas uma vez.
- **fan-out:** Publicação de uma mensagem para destinatários inscritos. Distribuir avisos a vários destinos é diferente de manter uma tarefa aguardando um consumidor.
- **push:** Em pull, o consumidor busca dados. Em push, o envio é iniciado para o destinatário. A forma de entrega não executa automaticamente a regra de negócio.
- **atributo:** Informação nomeada dentro de um registro, como nome ou data. Consultas usam os campos conforme a estrutura e o modelo do banco.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **SMS:** Mensagem de texto para dispositivos móveis. Integrações e condições de envio são diferentes de e-mail e de entrega a uma fila.
- **SSE:** Criptografia do lado do servidor. O serviço realiza proteção segundo a modalidade escolhida; administração de chaves e autorizações varia.
- **A2A:** Comunicação de agente para agente no contexto de sistemas de IA. O significado e a compatibilidade dependem da integração citada.
- **A2P:** Mensagem de aplicação para pessoa, como envio automatizado de texto. Condições de entrega e cobrança dependem do canal e do serviço.
- **FCM:** Firebase Cloud Messaging: canal/ecossistema de mensagens a aplicações compatíveis. Integrações exigem configuração e credenciais próprias.

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

**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.

Alarmes do CloudWatch → e-mail/SMS do time; eventos de pedidos para vários sistemas; notificações push em apps.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **consumidor:** Programa que recebe e processa dados ou tarefas. Ele precisa realizar o trabalho e tratar falhas, não apenas receber a mensagem.

Publicar para vários assinantes é diferente de guardar trabalhos numa fila para um consumidor. Entrega, conteúdo e destinatários precisam de configuração apropriada.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.

**SNS × SQS:** push para vários × fila puxada.

**Antes de ler este trecho:**

- **SES:** SES oferece envio de e-mail para aplicações, com recursos de identidade, acompanhamento e controle de envio.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.

**SNS × SES:** notificações simples (inclusive e-mail texto) × e-mails formatados em volume (marketing/transacionais).

**Antes de ler este trecho:**

- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.

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
