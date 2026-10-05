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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **produtor:** Componente que envia dados ou mensagens. Enviar uma mensagem não significa que o trabalho correspondente já foi realizado.
- **consumidor:** Programa que recebe e processa dados ou tarefas. Ele precisa realizar o trabalho e tratar falhas, não apenas receber a mensagem.


**Passo 1.** O produtor envia uma mensagem descrevendo um trabalho, como emitir um certificado. A fila guarda a mensagem; ela ainda não executou o trabalho.

**Passo 2.** O consumidor recebe a mensagem e realiza a tarefa. Durante o prazo de invisibilidade, a mensagem fica indisponível para novos recebimentos.

**Passo 3.** Após sucesso, o consumidor exclui a mensagem. Se falhar sem excluir, ela pode reaparecer; trate repetições e encaminhamento para uma fila de falhas configurada.

## 2. Recursos e opções, com significado

### Como funciona

1. O produtor envia mensagens para a fila.


2. O consumidor **puxa** (*poll*) as mensagens, processa e **apaga**.

**Antes de ler este trecho:**

- **visibility timeout:** Intervalo em que uma mensagem recebida do SQS fica temporariamente invisível a outros recebimentos. Se ela não for excluída e o prazo terminar, pode voltar a ser recebida.
- **timeout:** Limite de espera ou duração. Ao excedê-lo, uma operação pode falhar ou exigir tratamento; não presuma que nada aconteceu antes da interrupção.


3. Enquanto processa, a mensagem fica invisível (*visibility timeout*); se não for apagada a tempo, volta para a fila.

### Tipos de fila

**Antes de ler este trecho:**

- **throughput:** Quantidade de dados ou de trabalho processada por unidade de tempo. É diferente de latência, que mede quanto uma operação demora.
- **FIFO:** Primeiro a entrar, primeiro a sair. No SQS, a ordenação considera grupos de mensagens; deduplicação no envio não garante ausência de repetição de efeitos no programa.
- **deduplicação:** Identificação e tratamento de entradas repetidas conforme um critério e uma janela. É diferente de garantir toda a execução da aplicação apenas uma vez.
- **message group:** Identificação de grupo usada nas filas FIFO do SQS para a ordenação. Não presuma uma ordem única entre grupos independentes.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| | **Standard** | **FIFO** |
|---|---|---|
| Throughput | Quase ilimitado | Alto, mas limitado (🧊 milhares/s com lote e modo de alto throughput) |
| Entrega | **Pelo menos uma vez** (pode duplicar) | **Deduplicação no envio**; a aplicação ainda precisa tratar recebimento e efeitos repetidos |
| Ordem | Melhor esforço | **Garantida** (por *message group*) |
| Nome | qualquer | termina em `.fifo` |

### Configurações (📌 números)

**Tamanho da mensagem**

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **MiB / KiB:** Unidades em escala binária: cada nível corresponde a 1.024 do anterior. MiB e MB não são a mesma unidade; preserve a unidade indicada pelo serviço.


**Valor:** 🔄 até **1 MiB** (antes **256 KiB** — use o valor que estiver nas alternativas); maiores: guardar no S3 e enviar referência (*extended client*)

**Retenção**

**Antes de ler este trecho:**

- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.


**Valor:** padrão **4 dias**, de 60 s a **14 dias**

**Visibility timeout**


**Valor:** padrão **30 s**, de 0 a **12 h**

**Delay queue / message timer**


**Valor:** até **15 min**

**Long polling**

**Antes de ler este trecho:**

- **long polling / short polling:** Formas de consultar mensagens: a consulta longa pode esperar por disponibilidade, reduzindo consultas vazias; a curta retorna sem essa mesma espera.


**Valor:** espera até **20 s** por mensagens (menos requisições vazias, menor custo) — preferível ao *short polling*

**Dead-letter queue (DLQ)**

**Antes de ler este trecho:**

- **DLQ / dead-letter queue:** Fila separada para mensagens que atingiram condições configuradas de falha. Ajuda a isolar e investigar o problema; não corrige a mensagem automaticamente.
- **redrive:** Reenvio de mensagens de uma fila de falhas para processamento, conforme o recurso. Antes de reenviar, é necessário entender a causa das falhas.


**Valor:** Recebe mensagens que falharam N vezes (`maxReceiveCount`); *redrive* devolve à fila original

**Criptografia**

**Antes de ler este trecho:**

- **TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **SSE-KMS:** Formas de criptografia no servidor do S3, que diferem na origem e administração das chaves e, no último caso, nas camadas. A tabela da seção distingue essas escolhas.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **SSE-SQS:** Criptografia gerenciada pelo SQS para mensagens. É diferente da modalidade que integra uma chave KMS escolhida segundo a configuração.


**Valor:** SSE-SQS (padrão) ou SSE-KMS; TLS em trânsito

**Access policy**

**Antes de ler este trecho:**

- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **policy / política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.
- **Access policy:** Política de acesso. O serviço e o tipo de objeto determinam quem é avaliado, quais ações podem ser permitidas e quais limites se aplicam.


**Valor:** Política de recurso (ex.: permitir que um tópico SNS publique)

### Integrações comuns

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.
- **fan-out:** Publicação de uma mensagem para destinatários inscritos. Distribuir avisos a vários destinos é diferente de manter uma tarefa aguardando um consumidor.


**Lambda** (event source mapping), **Auto Scaling** de workers pelo tamanho da fila (`ApproximateNumberOfMessages`), **SNS fan-out**, notificações do S3, EventBridge.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.


SQS não executa a tarefa nem garante, em toda modalidade, que ela será recebida apenas uma vez. O consumidor deve tratar falhas e as condições de entrega.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Amazon MQ:** Amazon MQ oferece brokers gerenciados compatíveis com tecnologias suportadas, como ActiveMQ e RabbitMQ.
- **MQ:** Intermediário de mensagens entre componentes. Sua interface e seus protocolos precisam ser compatíveis com as aplicações conectadas.
- **pull / push:** Em pull, o consumidor busca dados. Em push, o envio é iniciado para o destinatário. A forma de entrega não executa automaticamente a regra de negócio.


**SQS** (fila, pull, 1 consumidor processa) × **SNS** (pub/sub, push para vários) × **EventBridge** (roteamento de eventos com regras) × **Kinesis** (stream relido por vários consumidores) × **Amazon MQ** (brokers ActiveMQ/RabbitMQ existentes).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **KB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.


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

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Um sistema recebe trabalhos mais rápido do que consegue executá-los. Se depender de tudo acontecer imediatamente, pode perder pedidos ou ficar indisponível.

**2. O que a solução fornece?**

SQS guarda mensagens numa fila até que consumidores as recebam e processem. Isso permite separar o envio de uma tarefa da execução dela.

**3. Que conclusão seria incorreta?**

SQS não executa a tarefa nem garante, em toda modalidade, que ela será recebida apenas uma vez. O consumidor deve tratar falhas e as condições de entrega.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Desacoplar componentes para que um pico não derrube o processamento."

**Resposta curta:** SQS.


**Fundamento explicado no capítulo:** "Desacoplar componentes para que um pico não derrube o processamento." → SQS.

**Pergunta:** "Ordenar mensagens por grupo e evitar envios duplicados dentro das condições de deduplicação."

**Resposta curta:** SQS FIFO; isso não garante sozinho efeitos de negócio apenas uma vez.


**Fundamento explicado no capítulo:** "Ordenar mensagens por grupo e evitar envios duplicados dentro das condições de deduplicação." → SQS FIFO; isso não garante sozinho efeitos de negócio apenas uma vez.

**Pergunta:** "Mensagens que falham repetidamente devem ser isoladas."

**Resposta curta:** Dead-letter queue.


**Fundamento explicado no capítulo:** "Mensagens que falham repetidamente devem ser isoladas." → Dead-letter queue.

**Pergunta:** "Reduzir requisições vazias e custo."

**Resposta curta:** Long polling.


**Fundamento explicado no capítulo:** "Reduzir requisições vazias e custo." → Long polling.

**Pergunta:** "Retenção máxima de uma mensagem?"

**Resposta curta:** 14 dias.


**Fundamento explicado no capítulo:** "Retenção máxima de uma mensagem?" → 14 dias.


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
