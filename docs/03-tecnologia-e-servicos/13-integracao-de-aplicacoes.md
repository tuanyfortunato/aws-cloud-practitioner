# 3.13 Integração de aplicações

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon SQS (Simple Queue Service)](../../servicos/integracao/sqs.md) · [Amazon SNS (Simple Notification Service)](../../servicos/integracao/sns.md) · [Amazon EventBridge](../../servicos/integracao/eventbridge.md) · [AWS Step Functions](../../servicos/integracao/step-functions.md) · [Amazon MQ](../../servicos/integracao/amazon-mq.md)

⬅️ [3.12 IA e machine learning](12-ia-e-machine-learning.md) · 🏠 [Índice do domínio](README.md) · [3.14 Aplicações de negócio, usuário final, front-end e IoT](14-aplicacoes-de-negocio-e-iot.md) ➡️

---

## 📖 Conteúdo

- **Amazon SQS:** Pontos de prova:
  - Fila gerenciada que **desacopla** componentes; o consumidor **puxa** (poll) as mensagens.
  - **Standard:** throughput quase ilimitado, entrega pelo menos uma vez, ordem não garantida. **FIFO:** ordem garantida e entrega exatamente uma vez.
  - Retenção padrão de 4 dias, configurável até 14 dias; **visibility timeout**; **dead-letter queue** para mensagens com falha.
- **Amazon SNS:** **pub/sub**. Um produtor publica num **tópico** e a mensagem é **empurrada** (push) para todos os assinantes: e-mail, SMS, HTTP, Lambda, filas SQS e push mobile.
  - **Fan-out:** SNS publica e várias filas SQS recebem a mesma mensagem para processamento paralelo.
- **Amazon EventBridge:** **barramento de eventos** serverless. Recebe eventos de serviços AWS, de aplicações e de parceiros SaaS e os roteia com **regras** para destinos. **EventBridge Scheduler** agenda tarefas (estilo cron).
- **AWS Step Functions:** **orquestra fluxos de trabalho** com várias etapas em máquinas de estado visuais, com tratamento de erros e novas tentativas (ex.: várias Lambdas em sequência, com aprovação humana no meio).
- **Cai na prova:** "desacoplar e absorver picos" = SQS; "notificar vários sistemas ao mesmo tempo" = SNS; "reagir a eventos de um SaaS" = EventBridge; "coordenar várias etapas de um processo" = Step Functions.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Desacoplar componentes para que um pico não derrube o processamento." → SQS.
- "Garantir ordem e processamento exatamente uma vez." → Fila SQS FIFO.
- "Enviar a mesma mensagem para vários sistemas e para e-mail." → SNS.
- "Um evento precisa ser processado por várias filas em paralelo." → Fan-out com SNS + SQS.
- "Reagir a eventos de serviços AWS e de aplicações SaaS com regras." → EventBridge.
- "Executar uma tarefa todo dia às 2h sem servidor." → EventBridge Scheduler (disparando Lambda).
- "Orquestrar um processo com várias etapas e tratamento de erro." → Step Functions.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **SQS — números (📌):**

| Item | Valor |
|---|---|
| Tamanho máximo de mensagem | 🔄 **1 MiB** desde 04/08/2025 (antes **256 KiB**) — ⚠️ se só houver 256 KB como opção, marque 256 KB |
| Retenção | padrão **4 dias**, mínimo 60 s, máximo **14 dias** |
| Visibility timeout | padrão **30 s**, mínimo 0, máximo **12 h** |
| Delay queue | até **15 min** |

- **Standard × FIFO:** Standard = throughput quase ilimitado, entrega "pelo menos uma vez", ordem por melhor esforço. FIFO = ordem garantida e processamento exatamente uma vez.
- 🔄 Segundo a pesquisa, o **SNS** também passou a aceitar mensagens de 1 MiB.
- **SQS × SNS × EventBridge:** fila (pull, buffer) × pub/sub (push, fan-out) × barramento de eventos com regras, eventos AWS/SaaS e agendamento (Scheduler). **Step Functions** = orquestração; **SWF** é legado.
- 🧊 Não decorar: mensagens in-flight, cobrança por blocos de 64 KB, throughput exato do FIFO.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.12 IA e machine learning](12-ia-e-machine-learning.md) · 🏠 [Índice do domínio](README.md) · [3.14 Aplicações de negócio, usuário final, front-end e IoT](14-aplicacoes-de-negocio-e-iot.md) ➡️
