# Planos de AWS Support

> **Categoria:** Suporte · **Domínio:** 4 · **Escopo:** Conta (ou organização, nos planos novos) · **Tópico do guia:** [4.5 Planos de AWS Support](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)
>
> **Em uma frase:** níveis de suporte técnico da AWS — quanto mais alto, mais rápido o atendimento e mais acompanhamento proativo.
>
> **Escopo oficial:** ✅ No escopo (AWS Support — task 4.3 cobra os planos novos) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> Verificado em fontes oficiais em 04/10/2026 ([relatório](../../fontes/verificacao-fontes-oficiais-2026-10.md)).

## 📌 Planos atuais (o que o exam guide cobra — task 4.3)

> ✔️ Comparação completa verificada em 04/10/2026 nas páginas [plans](https://aws.amazon.com/premiumsupport/plans/) e [pricing](https://aws.amazon.com/premiumsupport/pricing/).

| | **Basic** | **AWS Business Support+** | **AWS Enterprise Support** | **AWS Unified Operations** |
|---|---|---|---|---|
| Preço mínimo | Incluído (grátis) | **US$ 29/mês por conta** ou % do uso (9 → 7 → 5 → 3%), o maior | **US$ 5.000/mês** ou % (10 → 7 → 5 → 3%), o maior | **US$ 50.000/mês** ou % (10 → 6 → 5%), o maior |
| Cobrança | — | **Por conta** | Soma das contas inscritas | Soma das contas inscritas |
| Compromisso mínimo | — | 30 dias | 30 dias | **90 dias** |
| Canais | Customer service 24/7 (conta e faturamento), docs, whitepapers, re:Post | **Telefone, web, chat e e-mail 24/7**, Slack; casos e contatos ilimitados | Igual | Igual |
| **Caso crítico** | — | **< 30 min** | **< 15 min** | **< 5 min** |
| Produção fora do ar / prejudicada | — | < 1 h / < 4 h | < 1 h / < 4 h | < 1 h / < 4 h |
| Sistema prejudicado / orientação geral | — | < 12 h / < 24 h | < 12 h / < 24 h | < 12 h / < 24 h |
| Trusted Advisor | **Core checks** | **Completo** + API | Completo + API + **TA Priority** | Completo + API + **TA Priority** |
| AWS Support API / AWS Health API | ❌ / Health básico | ✅ / ✅ | ✅ / ✅ | ✅ / ✅ |
| TAM | ❌ | ❌ | **Designado** | Designado + especialistas de domínio + Incident Management Engineers |
| Faturamento | — | Billing 24/7 | **Billing concierge** | Especialista de billing designado |
| AWS Countdown (antigo IEM) | — | Countdown Premium pago | Countdown Premium pago | **Incluído** |
| Revisões | — | Orientação contextual | Well-Architected, revisão de segurança, plano estratégico | Contínuas + Critical Workload Review |
| Monitoramento 24/7 pela AWS | — | — | — | ✅ |
| Security Incident Response | — | Pago à parte | **Incluído** | Incluído |
| Incident Detection and Response | — | — | Pago à parte | **Incluído** |
| IA (créditos de DevOps Agent) | — | 30% | 75% | 100% |

- ⚠️ US$ 29 é o preço de entrada do **Business Support+** (novo) e era o do **Developer** (clássico): confira o nome do plano.
- ⚠️ 30 min: **Business Support+** (novo) ou **Enterprise On-Ramp** (clássico). 15 min + TAM designado: **Enterprise** (nos dois modelos). 5 min + monitoramento 24/7: **Unified Operations**.
- 📌 **Menor plano com todas as verificações do Trusted Advisor e acesso à API:** Business Support+. **Menor plano com TA Priority e TAM designado:** Enterprise.
- ✔️ O **Enterprise** inclui **workshops conduzidos pelo TAM** e **AWS GameDays** (e exercícios de segurança). Assinatura do Skill Builder incluída: não encontrada.

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
- **AWS Support Center:** onde se abrem e acompanham os casos de suporte (no console). No Basic, só casos de conta e faturamento.
- **Quem muda o plano de suporte:** 🔄 deixou de ser tarefa exclusiva do root (a lista oficial atual não a inclui); uma identidade IAM com as permissões necessárias pode fazê-lo.
- Demais recursos (Trust and Safety, APN, Marketplace, Professional Services, Prescriptive Guidance, Knowledge Center, re:Post): [recursos de ajuda e parceiros](recursos-de-ajuda-e-parceiros.md).

## ❓ Perguntas típicas

- "Plano gratuito sem suporte técnico." → Basic.
- "Plano pago de entrada, a partir de US$ 29 por conta, com resposta de 30 min para casos críticos." → Business Support+.
- "TAM designado e resposta em menos de 15 min para sistema crítico." → Enterprise.
- "Resposta em 5 minutos para incidentes críticos." → Unified Operations.
- (Clássico) "Mais barato com suporte técnico 24/7 por telefone e < 1 h para produção fora do ar." → Business.
- (Clássico) "Pool de TAMs e 30 min." → Enterprise On-Ramp.
- (Clássico) "Ambiente de testes, ajuda ocasional por e-mail em horário comercial." → Developer.
- "Quem pode mudar o plano de suporte?" → Não é mais exclusivo do root (lista oficial de 10/2026).

## 🔗 Documentação oficial

- [Planos de suporte](https://aws.amazon.com/premiumsupport/plans/) · [Preços do suporte](https://aws.amazon.com/premiumsupport/pricing/) · [Anúncio da transformação do suporte (12/2025)](https://aws.amazon.com/about-aws/whats-new/2025/12/aws-support-transformation-ai-powered-operations)
