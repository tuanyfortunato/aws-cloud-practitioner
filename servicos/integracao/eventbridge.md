# Amazon EventBridge

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Aplicações produzem acontecimentos diferentes e a empresa precisa encaminhar cada tipo para a ação correta, sem ligar manualmente todos os sistemas entre si.

**Como este serviço ajuda?** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis. O conteúdo do evento ajuda a decidir o caminho.

**Exemplo do dia a dia:** Um evento de matrícula confirmada aciona o processo de boas-vindas; um evento de cancelamento segue para outro destino.

**O que ele não resolve sozinho?** EventBridge encaminha acontecimentos, mas não realiza toda a tarefa de negócio por si só. Regras, destinos, permissões e tratamento de falhas precisam ser definidos.

**Primeiras palavras para entender:**

- **Evento:** informação sobre algo que aconteceu.
- **Barramento:** canal que recebe eventos.
- **Regra:** critério para encaminhá-los.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Integração de aplicações / eventos · **Domínio:** 3 · **Escopo:** Regional (cross-account e cross-region) · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** **barramento de eventos** serverless que recebe eventos de serviços AWS, das suas aplicações e de parceiros SaaS e os roteia por **regras**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina a origem dos eventos e o critério que distingue cada situação.

**Passo 2.** Configure regras e destinos compatíveis. Um evento que corresponde à regra é encaminhado ao destino apropriado.

**Passo 3.** Observe entrega e ação do destino. Encaminhar o acontecimento e concluir o trabalho de negócio são etapas diferentes.

## 2. Recursos e opções, com significado

### Componentes

**Event bus**

**Detalhe:** **Default** (eventos de serviços AWS), **custom** (suas aplicações) e **partner** (SaaS: Zendesk, Datadog, Shopify…).

**Rules**

**Detalhe:** *Event pattern* (filtra por conteúdo do evento) → **targets** (Lambda, SQS, SNS, Step Functions, ECS task, Kinesis, API Gateway, outro bus…).

**EventBridge Scheduler**

**Detalhe:** Agendamentos **cron/rate ou únicos**, com fuso horário, para milhões de tarefas (substitui as *scheduled rules*).

**Pipes**

**Detalhe:** Conexões ponto-a-ponto origem → filtro → enriquecimento → destino (ex.: SQS → Step Functions).

**Archive & replay**

**Detalhe:** Guardar e reprocessar eventos.

**Schema registry**

**Detalhe:** Descobre e documenta o formato dos eventos.

**API destinations**

**Detalhe:** Envia eventos para APIs HTTP externas.

### Exemplos

"Quando uma instância EC2 mudar para `stopped`, notificar no Slack."

Achado do GuardDuty → Lambda que isola a instância.

Evento de um SaaS (novo ticket) → workflow interno.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

EventBridge encaminha acontecimentos, mas não realiza toda a tarefa de negócio por si só. Regras, destinos, permissões e tratamento de falhas precisam ser definidos.

### ⚠️ Não confundir

**EventBridge** (roteia e reage a eventos, inclusive de SaaS) × **SNS** (notificação pub/sub) × **Step Functions** (orquestra fluxos com estado) × **CloudWatch Events** (nome antigo do EventBridge).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por milhão de eventos publicados (eventos de serviços AWS no bus default são gratuitos); Scheduler por invocação; Pipes por requisição.

## 5. Caso resolvido: ligando as peças

Um evento de matrícula confirmada aciona o processo de boas-vindas; um evento de cancelamento segue para outro destino.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina a origem dos eventos e o critério que distingue cada situação.
**Etapa 2:** Configure regras e destinos compatíveis. Um evento que corresponde à regra é encaminhado ao destino apropriado.
**Etapa 3:** Observe entrega e ação do destino. Encaminhar o acontecimento e concluir o trabalho de negócio são etapas diferentes.

**Resultado e responsabilidade:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis. O conteúdo do evento ajuda a decidir o caminho.

**Recursos envolvidos:** Event buses, rules, targets; Scheduler e Pipes conforme necessidade.

**Decisões que precisam ser tomadas:** Padrão de evento, destinos, role e falhas.

**Outra situação comentada:** Mudança de estado dispara automação: regra EventBridge com destino autorizado.

**Por que não concluir mais do que isso:** Não executa lógica de negócio por si; evento exige consumidor/destino

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Reagir a eventos de serviços AWS e de aplicações SaaS com regras."

**Resposta curta:** EventBridge.

**Pergunta:** "Executar uma tarefa todo dia às 2h sem servidor."

**Resposta curta:** EventBridge Scheduler + Lambda.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
