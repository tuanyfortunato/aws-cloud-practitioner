# 4.5 Planos de AWS Support

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Planos de AWS Support](../../servicos/custos/planos-de-suporte.md) · [AWS Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** O exam guide atual (task 4.3) cobra os **planos novos: Basic, Business Support+, Enterprise e Unified Operations**. O conteúdo abaixo descreve o modelo clássico (válido até 01/01/2027). Estude primeiro a tabela de planos novos na seção de atualizações e na [ficha de planos de suporte](../../servicos/custos/planos-de-suporte.md). [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [4.4 Ferramentas de custo e faturamento](04-ferramentas-de-custo.md) · 🏠 [Índice do domínio](README.md) · [4.6 Outros recursos de ajuda](06-outros-recursos-de-ajuda.md) ➡️

---

## 📖 Conteúdo

| Plano | Preço de referência | Canais | Tempos de resposta | Destaques |
| --- | --- | --- | --- | --- |
| Basic | Gratuito | Atendimento ao cliente 24/7 só para conta e faturamento | Sem suporte técnico | Documentação, whitepapers, re:Post, Health Dashboard, verificações principais do Trusted Advisor |
| Developer | A partir de US$ 29/mês | E-mail em horário comercial | Orientação geral: menos de 24 h úteis; sistema prejudicado: menos de 12 h úteis | Para testes e desenvolvimento; orientação de arquitetura geral |
| Business | A partir de US$ 100/mês | Telefone, chat e e-mail 24/7 | Sistema de produção prejudicado: menos de 4 h; **produção fora do ar: menos de 1 h** | **Todas as verificações do Trusted Advisor**; Health API; suporte a software de terceiros comum; Infrastructure Event Management pago à parte |
| Enterprise On-Ramp | A partir de US$ 5.500/mês | Telefone, chat e e-mail 24/7 | **Sistema crítico de negócio fora do ar: menos de 30 min** | **Pool de TAMs**; Concierge Support Team (faturamento e conta); revisões consultivas |
| Enterprise | A partir de US$ 15.000/mês | Telefone, chat e e-mail 24/7 | **Sistema crítico de negócio fora do ar: menos de 15 min** | **TAM dedicado**; Concierge; Infrastructure Event Management; revisões Well-Architected e de operações; treinamentos |

- **TAM (Technical Account Manager):** consultor técnico que acompanha a conta de forma proativa. Dedicado só no Enterprise; compartilhado (pool) no Enterprise On-Ramp.
- **Concierge Support Team:** especialistas em faturamento e gestão de conta (Enterprise On-Ramp e Enterprise).
- **Infrastructure Event Management (IEM):** apoio da AWS para planejar eventos de grande escala (lançamentos, Black Friday).
- **Cai na prova:** "menor plano com suporte 24/7 por telefone" = Business; "menor plano com todas as verificações do Trusted Advisor" = Business; "TAM dedicado" = Enterprise; "resposta em 15 minutos" = Enterprise; "só precisa de ajuda com a fatura" = Basic (atendimento ao cliente é grátis). Preços e tempos mudam com frequência: confira a página oficial de planos antes da prova.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).

- "Qual o plano mais barato com suporte técnico 24/7 por telefone?" → Business.
- "Qual o plano mais barato com todas as verificações do Trusted Advisor?" → Business.
- "Qual plano inclui TAM dedicado?" → Enterprise.
- "Qual plano dá acesso a um pool de TAMs?" → Enterprise On-Ramp.
- "Qual plano responde em menos de 15 minutos a um sistema crítico fora do ar?" → Enterprise.
- "Qual plano responde em menos de 1 hora a produção fora do ar?" → Business.
- "Ambiente de testes que só precisa de ajuda técnica ocasional por e-mail." → Developer.
- "O plano Basic oferece suporte técnico?" → Não; só atendimento de conta e faturamento, documentação e re:Post.
- "Quem ajuda com dúvidas de faturamento em planos Enterprise?" → Concierge Support Team.
- "Quem pode mudar o plano de suporte?" → O usuário root.

<!-- extra:inicio -->
## 🔄 Planos novos (o que o exam guide atual cobra)

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
