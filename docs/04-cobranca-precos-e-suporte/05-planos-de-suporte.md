# 4.5 Planos de AWS Support

## 🧠 Antes de começar

**Qual é a dificuldade?** Quando o sistema tem um problema, a empresa precisa saber como pedir ajuda e quais recursos de atendimento estão incluídos em sua oferta.

**A ideia em palavras simples:** Planos de suporte definem canais e condições de auxílio. A escolha deve considerar a necessidade de orientação e o impacto dos incidentes.

**Exemplo do dia a dia:** Uma empresa avalia o acesso a suporte técnico necessário para sua aplicação e confere as condições da oferta aplicável.

**O que não concluir?** Tempo de primeira resposta não é prazo garantido de correção. Os nomes comerciais e os exemplos do guia podem diferir; leia os avisos e o contexto.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **TAM** | Technical Account Manager: consultor técnico que acompanha a conta. |
| **Concierge** | time de especialistas em faturamento e conta. |
| **Caso crítico** | sistema crítico de negócio fora do ar. |

---

> **Domínio 4 — Cobrança, Preços e Suporte (12%)**

> 🔎 **Fichas detalhadas:** [Planos de AWS Support](../../servicos/custos/planos-de-suporte.md) · [AWS Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** A task 4.3 consultada cita **Developer, Business, Enterprise On-Ramp e Enterprise**; a página comercial apresenta **Business Support+, Enterprise e Unified Operations**. Estude os dois modelos, distinguindo contexto do guia e oferta comercial. Veja a [auditoria](../00-guia-do-exame/auditoria-conteudo-2026-10.md) e a [ficha de suporte](../../servicos/custos/planos-de-suporte.md). [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [4.4 Ferramentas de custo e faturamento](04-ferramentas-de-custo.md) · 🏠 [Índice do domínio](README.md) · [4.6 Outros recursos de ajuda](06-outros-recursos-de-ajuda.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.

Suporte é uma relação de assistência com cobertura definida. A organização informa o problema, seu impacto e o contexto; o atendimento responde e acompanha conforme a oferta. A equipe continua operando as partes que não foram contratadas para administração externa.

Separe resposta inicial de resolução. Uma primeira resposta rápida pode iniciar uma investigação longa. Também diferencie exemplos do guia do exame de nomes comerciais atuais: a pergunta deve ser interpretada dentro do contexto descrito.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como **planos de assistência técnica**: o básico só tem o manual e o FAQ; os planos maiores dão atendimento 24 h, resposta mais rápida e, no topo, um **consultor dedicado** (TAM) que acompanha você de perto.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **Trusted Advisor:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.
- **Health Dashboard:** AWS Health apresenta eventos sobre a saúde dos serviços e informações relevantes aos recursos da conta, conforme a visão consultada.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.
- **TAM:** Gerente técnico de conta em ofertas de suporte que incluem esse papel. Atua no acompanhamento e orientação previstos; não substitui toda a equipe do cliente.

| Plano (modelo clássico; preços históricos, não cotação atual) | Preço mínimo histórico | Canais de suporte técnico | Tempo de primeira resposta | Recursos principais |
| --- | --- | --- | --- | --- |
| Basic | Gratuito | Atendimento ao cliente 24/7 só para conta e faturamento | Sem suporte técnico | Documentação, whitepapers, re:Post, Health Dashboard, verificações principais do Trusted Advisor |
| Developer | A partir de US$ 29/mês | E-mail em horário comercial | Orientação geral: menos de 24 h úteis; sistema prejudicado: menos de 12 h úteis | Para testes e desenvolvimento; orientação de arquitetura geral |
| Business | A partir de US$ 100/mês | Telefone, chat e e-mail 24/7 | Sistema de produção prejudicado: menos de 4 h; **produção fora do ar: menos de 1 h** | **Todas as verificações do Trusted Advisor**; Health API; suporte a software de terceiros comum; Infrastructure Event Management pago à parte |
| Enterprise On-Ramp | A partir de US$ 5.500/mês | Telefone, chat e e-mail 24/7 | **Sistema crítico de negócio fora do ar: menos de 30 min** | **Pool de TAMs**; Concierge Support Team (faturamento e conta); revisões consultivas |
| Enterprise | A partir de US$ 15.000/mês | Telefone, chat e e-mail 24/7 | **Sistema crítico de negócio fora do ar: menos de 15 min** | **TAM dedicado**; Concierge; Infrastructure Event Management; revisões Well-Architected e de operações; treinamentos |

**TAM (Technical Account Manager):** consultor técnico que acompanha a conta de forma proativa. Dedicado só no Enterprise; compartilhado (pool) no Enterprise On-Ramp.

**Concierge Support Team:** especialistas em faturamento e gestão de conta (Enterprise On-Ramp e Enterprise).

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **IEM:** Nome histórico de uma oferta de acompanhamento de eventos de infraestrutura. Leia o contexto e a oferta atual indicados na ficha.

**Infrastructure Event Management (IEM):** apoio da AWS para planejar eventos de grande escala (lançamentos, Black Friday).

**Cai na prova:** 🔄 *oferta comercial atual (sem confirmação de substituição no banco da prova):* "plano pago de entrada, US$ 29 por conta, 30 min" = Business Support+; "TAM designado e 15 min" = Enterprise; "5 min" = Unified Operations. *Modelo clássico (até 01/01/2027):* "menor plano com suporte 24/7 por telefone" = Business; "menor plano com todas as verificações do Trusted Advisor" = Business; "TAM dedicado" = Enterprise; "resposta em 15 minutos" = Enterprise; "só precisa de ajuda com a fatura" = Basic (atendimento ao cliente é grátis). Preços e tempos mudam com frequência: confira a página oficial de planos antes da prova.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **SLA:** Acordo de nível de serviço com condições e medidas próprias. Não é garantia de que a aplicação do cliente nunca falhará.

**Primeiro, identifique o funcionamento:** Support Center organiza casos de suporte; planos determinam canais, recursos e objetivos de resposta. TAM oferece orientação técnica proativa; cobrança/conta é uma necessidade distinta de incidente técnico.

**Depois, compare as escolhas:** Leia o nome e o contexto: o guia consultado cita modelos clássicos; a página comercial oferece planos novos. Preserve as duas tabelas com fonte e data, sem tratar lançamento comercial como confirmação de questão.

**Por fim, verifique o limite:** Tempo de primeira resposta não é prazo de resolução nem SLA da aplicação. Basic não inclui atendimento técnico individual como os planos pagos.

## 4. Caso resolvido

Um plano promete primeira resposta para incidente crítico em quinze minutos. Isso garante que a aplicação será restaurada nesse prazo?

**Raciocínio e resposta:** Não. O objetivo se refere ao contato inicial do suporte, sujeito aos termos; restaurar depende do diagnóstico, contexto e ações necessárias.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar os **planos novos** (Basic, Business Support+, Enterprise, Unified Operations) dos **clássicos**.
- [ ] Ligar os tempos de resposta a cada plano (30 min, 15 min, 5 min no modelo novo).
- [ ] Saber o que é **TAM**, **Concierge** e quem tem **todas as verificações do Trusted Advisor**.

**Dica de revisão para a prova:** Distinga os exemplos clássicos do guia da oferta comercial atual (veja o aviso no topo). "TAM designado + 15 min" → **Enterprise**. "5 min" → **Unified Operations**. "Plano pago de entrada, 30 min" → **Business Support+**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).
**Pergunta:** "Qual o plano mais barato com suporte técnico 24/7 por telefone?"

**Resposta curta:** Business Support+ (no modelo clássico, Business).

**Pergunta:** "Qual o plano mais barato com todas as verificações do Trusted Advisor?"

**Resposta curta:** Business Support+ (no modelo clássico, Business).

**Pergunta:** "Qual plano inclui TAM dedicado?"

**Resposta curta:** Enterprise.

**Pergunta:** "Qual plano dá acesso a um pool de TAMs?"

**Resposta curta:** Enterprise On-Ramp (plano clássico, encerra em 01/01/2027).

**Pergunta:** "Qual plano responde em menos de 15 minutos a um sistema crítico fora do ar?"

**Resposta curta:** Enterprise.

**Pergunta:** "Qual plano responde em menos de 1 hora a produção fora do ar?"

**Resposta curta:** Business Support+ ou superior (no modelo clássico, Business).

**Pergunta:** "Ambiente de testes que só precisa de ajuda técnica ocasional por e-mail."

**Resposta curta:** Developer (plano clássico, encerra em 01/01/2027; no modelo atual, o plano pago de entrada é o Business Support+).

**Pergunta:** "O plano Basic oferece suporte técnico?"

**Resposta curta:** Não; só atendimento de conta e faturamento, documentação e re:Post.

**Pergunta:** "Quem ajuda com dúvidas de faturamento em planos Enterprise?"

**Resposta curta:** Concierge Support Team.

**Pergunta:** "Quem pode mudar o plano de suporte?"

**Resposta curta:** 🔄 Não é mais tarefa exclusiva do root (saiu da lista oficial em 10/2026): uma identidade IAM com as permissões necessárias.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.

<!-- extra:inicio -->
## 🔄 Planos comerciais novos (distinguir dos exemplos do guia)

> Verificado em fontes oficiais em 04/10/2026 ([relatório](../../fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md)). Comparação completa na [ficha de planos de suporte](../../servicos/custos/planos-de-suporte.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

| Plano (📌) | Preço mínimo | Resposta para caso crítico | Destaques |
|---|---|---|---|
| **Basic** | Grátis | — (sem suporte técnico) | Conta e faturamento, documentação, re:Post, Health Dashboard, verificações principais do Trusted Advisor |
| **AWS Business Support+** | **US$ 29/mês por conta** | **30 min** | Plano pago de entrada: 24/7 por telefone, chat e e-mail; Trusted Advisor completo + API; Support API e Health API |
| **AWS Enterprise Support** | **US$ 5.000/mês** (antes US$ 15.000) | **15 min** | **TAM designado**, Trusted Advisor Priority, billing concierge, Security Incident Response incluído |
| **AWS Unified Operations** | **US$ 50.000/mês**, compromisso mínimo de 90 dias | **5 min** | Monitoramento 24/7, AWS Countdown incluído, TAM + especialistas |

- Nos três planos pagos (✔️ confirmado): produção fora do ar < 1 h · produção prejudicada < 4 h · sistema prejudicado < 12 h · orientação geral < 24 h.
- 📌 **Menor plano com Trusted Advisor completo e API:** Business Support+. **Menor plano com TAM designado e TA Priority:** Enterprise.
- Lançados em 02/12/2025. **Developer, Business e Enterprise On-Ramp encerram em 01/01/2027** (On-Ramp migrando automaticamente para Enterprise em 2026; os legados seguem no GovCloud).
- ⚠️ **Pegadinha de preço:** o Business Support+ começa em US$ 29 — o mesmo valor que se cita para o antigo Developer. Confira o **nome** do plano na questão.
- ⚠️ **30 minutos** aparece nos dois modelos: Enterprise On-Ramp (clássico) e Business Support+ (novo). **15 minutos + TAM designado** → Enterprise nos dois modelos. **5 minutos** → Unified Operations.
- A task 4.3 também cita **Trusted Advisor**, **AWS Health Dashboard** e **AWS Health API**.
- Os preços clássicos de Developer (US$ 29), Business (US$ 100) e On-Ramp (US$ 5.500) não aparecem mais nas páginas oficiais; os **tempos de resposta** clássicos continuam confirmados até 01/01/2027.
- A página do Enterprise On-Ramp cita **1 engajamento AWS Countdown por ano** (não usa o termo "IEM").
- Shield Advanced (US$ 3.000/mês) e Enterprise (US$ 5.000/mês) são "custo fixo alto": raramente são a resposta "mais barata".
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [4.4 Ferramentas de custo e faturamento](04-ferramentas-de-custo.md) · 🏠 [Índice do domínio](README.md) · [4.6 Outros recursos de ajuda](06-outros-recursos-de-ajuda.md) ➡️
