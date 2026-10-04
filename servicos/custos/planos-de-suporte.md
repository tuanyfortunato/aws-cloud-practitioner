# Planos de AWS Support

> **Categoria:** Suporte · **Domínio:** 4 · **Escopo:** Conta (ou organização, nos planos novos) · **Tópico do guia:** [4.5 Planos de AWS Support](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)
>
> **Em uma frase:** níveis de suporte técnico da AWS — quanto mais alto, mais rápido o atendimento e mais acompanhamento proativo.
>
> **Escopo oficial:** ✅ No escopo (AWS Support — task 4.3 cobra os planos novos) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> Verificado em fontes oficiais em 04/10/2026 ([relatório](../../fontes/verificacao-fontes-oficiais-2026-10.md)).

## 📌 Planos atuais (o que o exam guide cobra — task 4.3)

| | **Basic** | **AWS Business Support+** | **AWS Enterprise Support** | **AWS Unified Operations** |
|---|---|---|---|---|
| Preço mínimo | Grátis | **US$ 29/mês por conta** | **US$ 5.000/mês** | **US$ 50.000/mês** (compromisso de 90 dias) |
| Suporte técnico | ❌ (só conta e faturamento) | ✅ | ✅ | ✅ |
| **Resposta para caso crítico** | — | **30 min** | **15 min** | **5 min** |
| TAM | — | — | **Designado** | ✅ |
| Lançamento | — | 02/12/2025 | Preço reduzido em 02/12/2025 (antes US$ 15.000) | 02/12/2025 |

- ⚠️ US$ 29 é o preço de entrada do **Business Support+** (novo) e era o do **Developer** (clássico): confira o nome do plano.
- ⚠️ 30 min: **Business Support+** (novo) ou **Enterprise On-Ramp** (clássico). 15 min + TAM designado: **Enterprise** (nos dois modelos). 5 min: **Unified Operations**.

## Modelo clássico (válido até 01/01/2027)

Developer, Business e Enterprise On-Ramp **encerram em 01/01/2027** (clientes On-Ramp migram automaticamente para
Enterprise em 2026; os três seguem no GovCloud). Ainda podem aparecer em questões antigas.

| | **Basic** | **Developer** | **Business** | **Enterprise On-Ramp** | **Enterprise** |
|---|---|---|---|---|---|
| Preço histórico | Grátis | US$ 29/mês | US$ 100/mês | US$ 5.500/mês | US$ 15.000/mês (hoje US$ 5.000) |
| Suporte técnico | ❌ | E-mail em **horário comercial** | **24/7 telefone, chat, e-mail** | 24/7 | 24/7 |
| Orientação geral | — | < 24 h úteis | < 24 h | < 24 h | < 24 h |
| Sistema prejudicado | — | < 12 h úteis | < 12 h | < 12 h | < 12 h |
| Produção prejudicada | — | — | < 4 h | < 4 h | < 4 h |
| **Produção fora do ar** | — | — | **< 1 h** | < 1 h | < 1 h |
| **Sistema crítico fora do ar** | — | — | — | **< 30 min** | **< 15 min** |
| Trusted Advisor | Core checks | Core checks | **Todos** + API | Todos + API | Todos + API + Priority |
| TAM | — | — | — | **Pool de TAMs** | **TAM designado** |
| Concierge (faturamento/conta) | — | — | — | ✅ | ✅ |
| Eventos de grande escala | — | — | Pago à parte | 1 engajamento **AWS Countdown** por ano | ✅ |

- Os **tempos de resposta** clássicos estão confirmados nas páginas oficiais; os **preços** de Developer, Business e On-Ramp não aparecem mais (valores históricos).

## Recursos ligados ao suporte (também na task 4.3)

- **AWS Trusted Advisor:** verificações completas e API a partir dos planos pagos superiores ([ficha](../gerenciamento/trusted-advisor.md)).
- **AWS Health Dashboard** e **AWS Health API** ([ficha](../gerenciamento/health-dashboard.md)).
- **TAM (Technical Account Manager):** consultor técnico proativo.
- **Concierge Support Team:** especialistas em faturamento e conta.
- **Quem muda o plano de suporte:** o **usuário root**.
- Demais recursos (Trust and Safety, APN, Marketplace, Professional Services, Prescriptive Guidance, Knowledge Center, re:Post): [recursos de ajuda e parceiros](recursos-de-ajuda-e-parceiros.md).

## ❓ Perguntas típicas

- "Plano gratuito sem suporte técnico." → Basic.
- "Plano pago de entrada, a partir de US$ 29 por conta, com resposta de 30 min para casos críticos." → Business Support+.
- "TAM designado e resposta em menos de 15 min para sistema crítico." → Enterprise.
- "Resposta em 5 minutos para incidentes críticos." → Unified Operations.
- (Clássico) "Mais barato com suporte técnico 24/7 por telefone e < 1 h para produção fora do ar." → Business.
- (Clássico) "Pool de TAMs e 30 min." → Enterprise On-Ramp.
- (Clássico) "Ambiente de testes, ajuda ocasional por e-mail em horário comercial." → Developer.
- "Quem pode mudar o plano de suporte?" → O usuário root.

## 🔗 Documentação oficial

- [Planos de suporte](https://aws.amazon.com/premiumsupport/plans/) · [Preços do suporte](https://aws.amazon.com/premiumsupport/pricing/) · [Anúncio da transformação do suporte (12/2025)](https://aws.amazon.com/about-aws/whats-new/2025/12/aws-support-transformation-ai-powered-operations)
