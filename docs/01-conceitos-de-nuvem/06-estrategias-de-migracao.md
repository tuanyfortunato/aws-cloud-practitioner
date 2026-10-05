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

---

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Application Migration Service (AWS MGN)](../../servicos/migracao/application-migration-service.md) · [AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)](../../servicos/migracao/dms-e-sct.md)

⬅️ [1.5 AWS Cloud Adoption Framework (CAF)](05-cloud-adoption-framework.md) · 🏠 [Índice do domínio](README.md) · [1.7 Economia da nuvem](07-economia-da-nuvem.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


Primeiro conheça a aplicação e suas dependências. Depois decida o que preservar e o que mudar. Mover o mesmo programa, mudar a plataforma de banco e reescrever partes importantes são decisões diferentes, mesmo que o destino seja AWS nos três casos.

A estratégia descreve o tipo de mudança; a ferramenta executa parte do trabalho. Uma ferramenta não decide sozinha se vale manter ou substituir o sistema. Testes e transição dos dados continuam necessários em cada caminho.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como **mudar de casa** e decidir o destino de cada móvel: jogar fora (Retire), deixar na casa antiga (Retain), levar como está (Rehost), levar o cômodo inteiro de uma vez (Relocate), levar e trocar o estofado (Replatform), comprar um novo (Repurchase) ou mandar fazer um sob medida (Refactor).

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **Amazon RDS / RDS:** O RDS oferece bancos relacionais gerenciados.
- **Application Migration Service:** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.
- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **rehost / lift-and-shift:** Mover um sistema com poucas mudanças iniciais. A infraestrutura muda, mas isso não moderniza automaticamente o software.
- **replatform:** Mudar parte da plataforma mantendo boa parte da aplicação. Por exemplo, trocar a operação do banco sem reescrever todas as regras do programa.
- **refactor:** Redesenhar partes da aplicação para atender novos objetivos. Pode trazer vantagens, mas demanda mudanças, testes e esforço.
- **hipervisor:** Camada que permite executar máquinas virtuais sobre equipamentos físicos. No EC2, ela não é administrada pelo cliente como o sistema dentro de sua máquina.
- **repurchase / retain / retire / relocate:** Estratégias de migração: trocar por outra oferta, manter onde está, desativar ou mover a plataforma, respectivamente. A decisão vem do objetivo da aplicação e do negócio.
- **CRM:** CRM trata relacionamento com clientes; CAD, projeto assistido por computador; EDI, troca eletrônica estruturada de dados. São necessidades de aplicação distintas.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Estratégia | O que é | Exemplo |
| --- | --- | --- |
| Retire | Desligar o que não é mais usado | Aplicação legada sem usuários |
| Retain | Manter on-premises por enquanto | Sistema que ainda não pode migrar por regulação ou dependências |
| Rehost | Lift-and-shift, sem mudanças | Mover VMs para EC2 com Application Migration Service |
| Relocate | Mover em bloco no nível do hipervisor | VMware Cloud on AWS |
| Replatform | Lift-tinker-and-shift: pequenas otimizações | Banco em servidor próprio para Amazon RDS |
| Repurchase | Trocar por outro produto, normalmente SaaS | CRM próprio para Salesforce |
| Refactor / Re-architect | Reescrever para cloud-native | Monolito para microsserviços com Lambda e ECS |


**Antes de ler este trecho:**

- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.


**Cai na prova:** Rehost (sem mudar nada) vs Replatform (pequena mudança para serviço gerenciado). Refactor é o que tem mais custo e mais benefício de longo prazo.

## 3. Como analisar uma situação


**Primeiro, identifique o funcionamento:** Avalie cada aplicação e suas dependências antes de escolher um dos 7 Rs. A estratégia orienta ferramentas, esforço e testes; aplicações da mesma empresa podem ter destinos distintos.

**Depois, compare as escolhas:** Sem mudar aplicação: Rehost. Pequeno ajuste: Replatform. Redesenho: Refactor. Troca por SaaS: Repurchase. Desligar: Retire. Manter: Retain. Mover a plataforma: Relocate.

**Por fim, verifique o limite:** Rehost não moderniza automaticamente a aplicação. Refactor demanda mudanças e não é sempre a opção mais rápida. Uma ferramenta de migração não decide a estratégia de negócio.

## 4. Caso resolvido

Um banco instalado em servidor próprio vai para RDS, mantendo a aplicação com poucos ajustes. Qual estratégia?

**Raciocínio e resposta:** Replatform: há mudança da plataforma operacional. Levar o mesmo servidor e banco para EC2 sem ajustes seria Rehost.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma empresa quer levar um sistema para a AWS, mas não sabe se deve copiá-lo, adaptá-lo, reescrevê-lo ou até encerrá-lo.

**2. O que a solução fornece?**

Estratégias de migração descrevem essas escolhas. O esforço e o resultado mudam conforme a decisão sobre cada aplicação.

**3. Que conclusão seria incorreta?**

Migrar não significa modernizar automaticamente. Antes de escolher, considere dependências, riscos e a necessidade de manter ou mudar o sistema.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Citar os **7 Rs** e um exemplo de cada.
- [ ] Diferenciar **Rehost** (sem mudanças) de **Replatform** (pequena mudança, ex.: banco para RDS).
- [ ] Saber que **Rehost** é o mais rápido e **Refactor** traz mais benefício de longo prazo.

**Dica de revisão para a prova:** Procure o **quanto muda**: nada → Rehost; um pouco → Replatform; tudo → Refactor; troca por SaaS → Repurchase; "ninguém usa" → Retire; "ainda não pode sair" → Retain.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).
**Pergunta:** "Migrar servidores para EC2 sem mudar nada."

**Resposta curta:** Rehost.


**Fundamento explicado no capítulo:** "Migrar servidores para EC2 sem mudar nada." → Rehost.

**Pergunta:** "Migrar o banco para RDS para reduzir administração, sem mudar a aplicação."

**Resposta curta:** Replatform.


**Fundamento explicado no capítulo:** "Migrar o banco para RDS para reduzir administração, sem mudar a aplicação." → Replatform.

**Pergunta:** "Trocar o sistema próprio por um produto SaaS."

**Resposta curta:** Repurchase.


**Fundamento explicado no capítulo:** "Trocar o sistema próprio por um produto SaaS." → Repurchase.

**Pergunta:** "Reescrever a aplicação para usar Lambda e microsserviços."

**Resposta curta:** Refactor.


**Fundamento explicado no capítulo:** "Reescrever a aplicação para usar Lambda e microsserviços." → Refactor.

**Pergunta:** "Desligar aplicações que ninguém usa."

**Resposta curta:** Retire.


**Fundamento explicado no capítulo:** "Desligar aplicações que ninguém usa." → Retire.

**Pergunta:** "Manter a aplicação no datacenter por exigência regulatória."

**Resposta curta:** Retain.

**Antes de ler este trecho:**

- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.


**Fundamento explicado no capítulo:** "Manter a aplicação no datacenter por exigência regulatória." → Retain.

**Pergunta:** "Qual estratégia é a mais rápida?"

**Resposta curta:** Rehost. "Qual traz mais benefícios de nuvem a longo prazo?" → Refactor.


**Fundamento explicado no capítulo:** "Qual estratégia é a mais rápida?" → Rehost. "Qual traz mais benefícios de nuvem a longo prazo?" → Refactor.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.5 AWS Cloud Adoption Framework (CAF)](05-cloud-adoption-framework.md) · 🏠 [Índice do domínio](README.md) · [1.7 Economia da nuvem](07-economia-da-nuvem.md) ➡️
