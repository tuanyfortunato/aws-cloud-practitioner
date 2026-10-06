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

## 1. A sequência de funcionamento

**Passo 1.** Avalie a tecnologia e os protocolos de mensagens usados pela aplicação existente.

**Passo 2.** Prepare um broker compatível e conecte produtores e consumidores autorizados.

**Passo 3.** Teste comportamento, falhas e disponibilidade. Preservar interface não dispensa validar a migração do sistema.

## 2. Recursos e opções, com significado

### Quando usar

**Migrar aplicações existentes** que já usam ActiveMQ/RabbitMQ e protocolos padrão (**JMS, AMQP, MQTT, STOMP, OpenWire, WebSocket**) **sem reescrever o código**.

Para aplicações novas na nuvem, a AWS recomenda SQS/SNS (mais escaláveis e simples).

### Destaques

Instância única ou ativo/standby Multi-AZ (ActiveMQ) / cluster (RabbitMQ); a AWS cuida de patch e manutenção.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não é intercambiável com SQS ou SNS em todas as interfaces. Migração e compatibilidade precisam ser avaliadas; o nome não consta da lista de escopo indicada nesta ficha.

## 4. Caso resolvido: ligando as peças

Uma empresa avalia mover seu broker compatível para Amazon MQ preservando a interface usada por suas aplicações.

**Aplicando a sequência à situação:**

**Etapa 1:** Avalie a tecnologia e os protocolos de mensagens usados pela aplicação existente.
**Etapa 2:** Prepare um broker compatível e conecte produtores e consumidores autorizados.
**Etapa 3:** Teste comportamento, falhas e disponibilidade. Preservar interface não dispensa validar a migração do sistema.

**Resultado e responsabilidade:** Amazon MQ oferece brokers gerenciados compatíveis com tecnologias suportadas, como ActiveMQ e RabbitMQ.

**Recursos envolvidos:** Broker, filas/tópicos e engines/protocolos compatíveis.

**Decisões que precisam ser tomadas:** ActiveMQ/RabbitMQ, capacidade, rede e acesso.

**Outra situação comentada:** Aplicação exige protocolo de broker existente: avalie MQ; nova fila AWS simples: SQS.

**Por que não concluir mais do que isso:** Não listado não é exclusão formal; escolha por compatibilidade, sem igualar a API SQS

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Aplicação usa RabbitMQ e deve migrar sem mudar o código."

**Resposta curta:** Amazon MQ (SQS exigiria reescrever).

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
