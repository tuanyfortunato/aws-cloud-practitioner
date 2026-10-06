# 3.13 Integração de aplicações

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma ação pode gerar tarefas para outros sistemas. Se cada parte depender de todas as outras responderem na hora, a aplicação fica mais difícil de operar.

**A ideia em palavras simples:** Integração permite separar tarefas e coordenar comunicação. Filas guardam trabalho; notificações distribuem avisos; eventos orientam ações; fluxos coordenam etapas.

**Exemplo do dia a dia:** A matrícula confirmada gera um aviso e uma tarefa de emitir certificado. Uma fila pode guardar a tarefa; um fluxo pode acompanhar etapas do processo.

**O que não concluir?** Uma fila não executa o trabalho, e uma notificação não coordena por si só todo o processo. Entenda qual parte da comunicação precisa ser resolvida.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Desacoplar** | fazer componentes funcionarem sem depender um do outro estar disponível. |
| **Pub/sub** | publicar uma vez e todos os assinantes recebem. |
| **Fan-out** | uma mensagem do SNS copiada para várias filas SQS. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [Amazon SQS (Simple Queue Service)](../../servicos/integracao/sqs.md) · [Amazon SNS (Simple Notification Service)](../../servicos/integracao/sns.md) · [Amazon EventBridge](../../servicos/integracao/eventbridge.md) · [AWS Step Functions](../../servicos/integracao/step-functions.md) · [Amazon MQ](../../servicos/integracao/amazon-mq.md)

⬅️ [3.12 IA e machine learning](12-ia-e-machine-learning.md) · 🏠 [Índice do domínio](README.md) · [3.14 Aplicações de negócio, usuário final, front-end e IoT](14-aplicacoes-de-negocio-e-iot.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Enviar uma solicitação e executar seu trabalho não precisam acontecer no mesmo instante. Uma fila conserva trabalho; uma notificação avisa interessados; um evento descreve algo ocorrido; um fluxo coordena tarefas. Essa separação reduz dependências imediatas.

Pense num certificado: o site confirma que recebeu o pedido, a fila guarda a tarefa e um consumidor gera o arquivo depois. Se o processamento falhar, receber de novo pode ser necessário. A aplicação precisa evitar que repetição crie efeitos indevidos.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **SQS** é uma **fila de pedidos** (cada um é atendido no seu ritmo); o **SNS** é um **alto-falante** (todos ouvem ao mesmo tempo); o **EventBridge** é uma **central de regras** ("quando acontecer X, avise Y"); o **Step Functions** é um **fluxograma** que se executa sozinho.

</details>

## 2. Conceitos e opções explicados

**Amazon SQS:** Pontos de prova:

  - Fila gerenciada que **desacopla** componentes; o consumidor **puxa** (poll) as mensagens.

  - **Standard:** throughput quase ilimitado, entrega pelo menos uma vez, ordem não garantida. **FIFO:** ordenação por grupo e deduplicação no envio dentro das condições do serviço; o consumidor ainda precisa tratar recebimentos repetidos e efeitos de negócio.

  - Retenção padrão de 4 dias, configurável até 14 dias; **visibility timeout**; **dead-letter queue** para mensagens com falha.

**Amazon SNS:** **pub/sub**. Um produtor publica num **tópico** e a mensagem é **empurrada** (push) para todos os assinantes: e-mail, SMS, HTTP, Lambda, filas SQS e push mobile.

  - **Fan-out:** SNS publica e várias filas SQS recebem a mesma mensagem para processamento paralelo.

**Amazon EventBridge:** **barramento de eventos** serverless. Recebe eventos de serviços AWS, de aplicações e de parceiros SaaS e os roteia com **regras** para destinos. **EventBridge Scheduler** agenda tarefas (estilo cron).

**AWS Step Functions:** **orquestra fluxos de trabalho** com várias etapas em máquinas de estado visuais, com tratamento de erros e novas tentativas (ex.: várias Lambdas em sequência, com aprovação humana no meio).

**Cai na prova:** "desacoplar e absorver picos" = SQS; "notificar vários sistemas ao mesmo tempo" = SNS; "reagir a eventos de um SaaS" = EventBridge; "coordenar várias etapas de um processo" = Step Functions.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** SQS mantém mensagens para consumidores; SNS publica para assinantes; EventBridge filtra e roteia eventos; Step Functions controla etapas, escolhas e retentativas do fluxo.

**Depois, compare as escolhas:** Fila de trabalho: SQS. Aviso para vários destinos: SNS. Eventos com regras: EventBridge. Sequência com estado: Step Functions. As combinações podem ser necessárias.

**Por fim, verifique o limite:** Ler da fila não é o mesmo que excluir. Consumidores devem tratar repetição. SNS sozinho não dá a cada assinante uma fila persistente para consumo posterior.

## 4. Caso resolvido

Cada pedido precisa acionar faturamento e estoque, e cada equipe deve processar no próprio ritmo. Como combinar?

**Raciocínio e resposta:** SNS com uma fila SQS para cada consumidor permite fan-out e desacoplamento. Uma só fila com dois consumidores normalmente distribui trabalho entre eles, em vez de entregar uma cópia para cada equipe.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **SQS** (fila, o consumidor puxa) de **SNS** (pub/sub, empurra para todos).
- [ ] Diferenciar fila **Standard** de **FIFO**.
- [ ] Saber quando usar **EventBridge** (reagir a eventos, inclusive de SaaS) e **Step Functions** (orquestrar etapas).

**Dica de revisão para a prova:** "Desacoplar/absorver picos" → **SQS**. "Notificar vários" → **SNS**. "Ordem garantida" → **SQS FIFO**. "Evento de SaaS" → **EventBridge**. "Várias etapas com aprovação" → **Step Functions**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Desacoplar componentes para que um pico não derrube o processamento."

**Resposta curta:** SQS.

**Pergunta:** "Ordenar mensagens por grupo e tratar duplicações no envio."

**Resposta curta:** Fila SQS FIFO; o programa ainda precisa evitar efeitos repetidos.

**Pergunta:** "Enviar a mesma mensagem para vários sistemas e para e-mail."

**Resposta curta:** SNS.

**Pergunta:** "Um evento precisa ser processado por várias filas em paralelo."

**Resposta curta:** Fan-out com SNS + SQS.

**Pergunta:** "Reagir a eventos de serviços AWS e de aplicações SaaS com regras."

**Resposta curta:** EventBridge.

**Pergunta:** "Executar uma tarefa todo dia às 2h sem servidor."

**Resposta curta:** EventBridge Scheduler (disparando Lambda).

**Pergunta:** "Orquestrar um processo com várias etapas e tratamento de erro."

**Resposta curta:** Step Functions.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **SQS — números (📌):**

| Item | Valor |
|---|---|
| Tamanho máximo de mensagem | 🔄 **1 MiB** desde 04/08/2025 (antes **256 KiB**) (✔️ confirmado) — escolha pelo contexto e pelas condições pedidas |
| Retenção | padrão **4 dias**, mínimo 60 s, máximo **14 dias** |
| Visibility timeout | padrão **30 s**, mínimo 0, máximo **12 h** |
| Delay queue | até **15 min** |

- **Standard × FIFO:** Standard = throughput quase ilimitado, entrega "pelo menos uma vez", ordem por melhor esforço. FIFO = ordem garantida e processamento exatamente uma vez.
- 🔄 **SNS:** o padrão continua **256 KiB**; dá para aceitar até **1 MiB** configurando `MaximumMessageSize` no tópico (desde 18/09/2026, ✔️ confirmado).
- **SQS × SNS × EventBridge:** fila (pull, buffer) × pub/sub (push, fan-out) × barramento de eventos com regras, eventos AWS/SaaS e agendamento (Scheduler). **Step Functions** = orquestração; **SWF** é legado.
- 🧊 Não decorar: mensagens in-flight, cobrança por blocos de 64 KB, throughput exato do FIFO.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.12 IA e machine learning](12-ia-e-machine-learning.md) · 🏠 [Índice do domínio](README.md) · [3.14 Aplicações de negócio, usuário final, front-end e IoT](14-aplicacoes-de-negocio-e-iot.md) ➡️
