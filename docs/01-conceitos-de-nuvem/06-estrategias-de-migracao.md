# 1.6 Estratégias de migração (os 7 Rs)

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma empresa quer levar um sistema para a AWS, mas não sabe se deve copiá-lo, adaptá-lo, reescrevê-lo ou até encerrá-lo.

**A ideia em palavras simples:** Estratégias de migração descrevem essas escolhas. O esforço e o resultado mudam conforme a decisão sobre cada aplicação.

**Exemplo do dia a dia:** Um sistema antigo pode ser movido com poucas mudanças; outro pode ser substituído por um software pronto. Não é necessário escolher a mesma estratégia para tudo.

**O que não concluir?** Migrar não significa modernizar automaticamente. Antes de escolher, considere dependências, riscos e a necessidade de manter ou mudar o sistema.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Lift-and-shift** | "levantar e mover": migrar sem alterar nada (Rehost). |
| **Cloud-native** | feito para aproveitar a nuvem (serverless, microsserviços). |

**Ao terminar este tópico, você deve saber:**

- [ ] Citar os **7 Rs** e um exemplo de cada.
- [ ] Diferenciar **Rehost** (sem mudanças) de **Replatform** (pequena mudança, ex.: banco para RDS).
- [ ] Saber que **Rehost** é o mais rápido e **Refactor** traz mais benefício de longo prazo.

<details>
<summary>Uma analogia para revisar a ideia</summary>

é como **mudar de casa** e decidir o destino de cada móvel: jogar fora (Retire), deixar na casa antiga (Retain), levar como está (Rehost), levar o cômodo inteiro de uma vez (Relocate), levar e trocar o estofado (Replatform), comprar um novo (Repurchase) ou mandar fazer um sob medida (Refactor).

</details>

> 🎯 **Como não errar na prova:** Procure o **quanto muda**: nada → Rehost; um pouco → Replatform; tudo → Refactor; troca por SaaS → Repurchase; "ninguém usa" → Retire; "ainda não pode sair" → Retain.

---

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Application Migration Service (AWS MGN)](../../servicos/migracao/application-migration-service.md) · [AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)](../../servicos/migracao/dms-e-sct.md)

⬅️ [1.5 AWS Cloud Adoption Framework (CAF)](05-cloud-adoption-framework.md) · 🏠 [Índice do domínio](README.md) · [1.7 Economia da nuvem](07-economia-da-nuvem.md) ➡️

---

## 📖 Conteúdo

| Estratégia | O que é | Exemplo |
| --- | --- | --- |
| Retire | Desligar o que não é mais usado | Aplicação legada sem usuários |
| Retain | Manter on-premises por enquanto | Sistema que ainda não pode migrar por regulação ou dependências |
| Rehost | Lift-and-shift, sem mudanças | Mover VMs para EC2 com Application Migration Service |
| Relocate | Mover em bloco no nível do hipervisor | VMware Cloud on AWS |
| Replatform | Lift-tinker-and-shift: pequenas otimizações | Banco em servidor próprio para Amazon RDS |
| Repurchase | Trocar por outro produto, normalmente SaaS | CRM próprio para Salesforce |
| Refactor / Re-architect | Reescrever para cloud-native | Monolito para microsserviços com Lambda e ECS |

- **Cai na prova:** Rehost (sem mudar nada) vs Replatform (pequena mudança para serviço gerenciado). Refactor é o que tem mais custo e mais benefício de longo prazo.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).

- "Migrar servidores para EC2 sem mudar nada." → Rehost.
- "Migrar o banco para RDS para reduzir administração, sem mudar a aplicação." → Replatform.
- "Trocar o sistema próprio por um produto SaaS." → Repurchase.
- "Reescrever a aplicação para usar Lambda e microsserviços." → Refactor.
- "Desligar aplicações que ninguém usa." → Retire.
- "Manter a aplicação no datacenter por exigência regulatória." → Retain.
- "Qual estratégia é a mais rápida?" → Rehost. "Qual traz mais benefícios de nuvem a longo prazo?" → Refactor.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** Avalie cada aplicação e suas dependências antes de escolher um dos 7 Rs. A estratégia orienta ferramentas, esforço e testes; aplicações da mesma empresa podem ter destinos distintos.

**Como escolher:** Sem mudar aplicação: Rehost. Pequeno ajuste: Replatform. Redesenho: Refactor. Troca por SaaS: Repurchase. Desligar: Retire. Manter: Retain. Mover a plataforma: Relocate.

**O que não concluir:** Rehost não moderniza automaticamente a aplicação. Refactor demanda mudanças e não é sempre a opção mais rápida. Uma ferramenta de migração não decide a estratégia de negócio.

### Exercício de decisão

Um banco instalado em servidor próprio vai para RDS, mantendo a aplicação com poucos ajustes. Qual estratégia?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Replatform: há mudança da plataforma operacional. Levar o mesmo servidor e banco para EC2 sem ajustes seria Rehost.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.5 AWS Cloud Adoption Framework (CAF)](05-cloud-adoption-framework.md) · 🏠 [Índice do domínio](README.md) · [1.7 Economia da nuvem](07-economia-da-nuvem.md) ➡️
