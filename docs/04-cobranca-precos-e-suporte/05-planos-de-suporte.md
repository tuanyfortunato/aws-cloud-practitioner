# 4.5 Planos de AWS Support

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Planos de AWS Support](../../servicos/custos/planos-de-suporte.md) · [AWS Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md)

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
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- 🔄 **Planos reestruturados (dezembro/2025):**

| Novo plano | Preço de referência | Resposta crítica |
|---|---|---|
| Basic | Grátis | — |
| **Business Support+** | a partir de **US$ 29/mês por conta** (ou % do uso começando em 9%) | **30 min** |
| **Enterprise** | mínimo **US$ 5.000/mês** (antes US$ 15.000); TAM designado | **15 min** |
| **Unified Operations** | a partir de **US$ 50.000/mês** | **5 min** |

- Tempos comuns aos pagos: general guidance < 24 h · system impaired < 12 h · production system impaired < 4 h · production system down < 1 h.
- **Developer, Business e Enterprise On-Ramp encerram em 01/01/2027** (Enterprise On-Ramp migrando automaticamente para Enterprise em 2026; os legados seguem no GovCloud).
- ⚠️ **Na prova** continue estudando os **5 planos clássicos** (Basic, Developer, Business, Enterprise On-Ramp, Enterprise). "Menor plano com TAM designado e 15 min" → **Enterprise** (válido nos dois modelos). "Menor custo com < 1 h para produção fora do ar" → **Business** (clássico) / Business Support+ (novo).
- Shield Advanced (US$ 3.000/mês) e Enterprise (US$ 5.000 mínimo) são "custo fixo alto": raramente são a resposta "mais barata".
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [4.4 Ferramentas de custo e faturamento](04-ferramentas-de-custo.md) · 🏠 [Índice do domínio](README.md) · [4.6 Outros recursos de ajuda](06-outros-recursos-de-ajuda.md) ➡️
