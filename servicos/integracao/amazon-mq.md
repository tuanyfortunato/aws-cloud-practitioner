# Amazon MQ

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação existente já usa um intermediário de mensagens específico, e trocar seu protocolo ou reescrever sua integração seria trabalhoso.

**Como este serviço ajuda?** Amazon MQ oferece brokers gerenciados compatíveis com tecnologias suportadas, como ActiveMQ e RabbitMQ.

**Exemplo do dia a dia:** Uma empresa avalia mover seu broker compatível para Amazon MQ preservando a interface usada por suas aplicações.

**O que ele não resolve sozinho?** Ele não é intercambiável com SQS ou SNS em todas as interfaces. Migração e compatibilidade precisam ser avaliadas; o nome não consta da lista de escopo indicada nesta ficha.

**Primeiras palavras para entender:**

- **Broker:** intermediário de mensagens.
- **Protocolo:** regras da comunicação.
- **Compatibilidade:** suporte às interfaces usadas pela aplicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Integração de aplicações / message broker · **Domínio:** 3 · **Escopo:** Regional (Multi-AZ opcional) · **Tópico do guia:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** brokers de mensagens gerenciados **Apache ActiveMQ** e **RabbitMQ**, compatíveis com protocolos padrão.
>
> **Escopo oficial:** ⚪ Não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **broker:** Intermediário de mensagens entre componentes. Sua interface e seus protocolos precisam ser compatíveis com as aplicações conectadas.


**Passo 1.** Avalie a tecnologia e os protocolos de mensagens usados pela aplicação existente.

**Passo 2.** Prepare um broker compatível e conecte produtores e consumidores autorizados.

**Passo 3.** Teste comportamento, falhas e disponibilidade. Preservar interface não dispensa validar a migração do sistema.

## 2. Recursos e opções, com significado

### Quando usar

**Antes de ler este trecho:**

- **WebSocket:** Comunicação que mantém uma conexão para troca de mensagens entre cliente e servidor. É diferente de uma sequência de pedidos web independentes.
- **MQTT:** Protocolo de mensagens comum em dispositivos conectados. Aplicação, tópicos e permissões precisam ser definidos para a comunicação desejada.
- **AMQP / STOMP / JMS:** Protocolos ou interfaces de mensageria. AMQP e STOMP definem comunicação; JMS é uma interface Java. A aplicação e o broker precisam de suporte compatível.


**Migrar aplicações existentes** que já usam ActiveMQ/RabbitMQ e protocolos padrão (**JMS, AMQP, MQTT, STOMP, OpenWire, WebSocket**) **sem reescrever o código**.

**Antes de ler este trecho:**

- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


Para aplicações novas na nuvem, a AWS recomenda SQS/SNS (mais escaláveis e simples).

### Destaques

**Antes de ler este trecho:**

- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.


Instância única ou ativo/standby Multi-AZ (ActiveMQ) / cluster (RabbitMQ); a AWS cuida de patch e manutenção.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não é intercambiável com SQS ou SNS em todas as interfaces. Migração e compatibilidade precisam ser avaliadas; o nome não consta da lista de escopo indicada nesta ficha.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Uma empresa avalia mover seu broker compatível para Amazon MQ preservando a interface usada por suas aplicações.

**Aplicando a sequência à situação:**

**Etapa 1:** Avalie a tecnologia e os protocolos de mensagens usados pela aplicação existente.
**Etapa 2:** Prepare um broker compatível e conecte produtores e consumidores autorizados.
**Etapa 3:** Teste comportamento, falhas e disponibilidade. Preservar interface não dispensa validar a migração do sistema.

**Resultado e responsabilidade:** Amazon MQ oferece brokers gerenciados compatíveis com tecnologias suportadas, como ActiveMQ e RabbitMQ.

**Recursos envolvidos:** Broker, filas/tópicos e engines/protocolos compatíveis.

**Decisões que precisam ser tomadas:** ActiveMQ/RabbitMQ, capacidade, rede e acesso.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.


**Outra situação comentada:** Aplicação exige protocolo de broker existente: avalie MQ; nova fila AWS simples: SQS.

**Por que não concluir mais do que isso:** Não listado não é exclusão formal; escolha por compatibilidade, sem igualar a API SQS

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma aplicação existente já usa um intermediário de mensagens específico, e trocar seu protocolo ou reescrever sua integração seria trabalhoso.

**2. O que a solução fornece?**

Amazon MQ oferece brokers gerenciados compatíveis com tecnologias suportadas, como ActiveMQ e RabbitMQ.

**3. Que conclusão seria incorreta?**

Ele não é intercambiável com SQS ou SNS em todas as interfaces. Migração e compatibilidade precisam ser avaliadas; o nome não consta da lista de escopo indicada nesta ficha.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Aplicação usa RabbitMQ e deve migrar sem mudar o código."

**Resposta curta:** Amazon MQ (SQS exigiria reescrever).

**Antes de ler este trecho:**

- **Amazon MQ:** Amazon MQ oferece brokers gerenciados compatíveis com tecnologias suportadas, como ActiveMQ e RabbitMQ.


**Fundamento explicado no capítulo:** "Aplicação usa RabbitMQ e deve migrar sem mudar o código." → Amazon MQ (SQS exigiria reescrever).


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
