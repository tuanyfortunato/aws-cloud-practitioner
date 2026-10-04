# Planos de AWS Support

> **Categoria:** Suporte · **Domínio:** 4 · **Escopo:** Conta (ou organização, nos planos novos) · **Tópico do guia:** [4.5 Planos de AWS Support](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)
>
> **Em uma frase:** níveis de suporte técnico da AWS — quanto mais alto, mais rápido o atendimento e mais acompanhamento proativo.

## 📌 Modelo clássico (o que o exam guide cobra)

| | **Basic** | **Developer** | **Business** | **Enterprise On-Ramp** | **Enterprise** |
|---|---|---|---|---|---|
| Preço de referência | Grátis | A partir de US$ 29/mês | A partir de US$ 100/mês | A partir de US$ 5.500/mês | A partir de US$ 15.000/mês |
| Suporte técnico | ❌ (só conta e faturamento 24/7) | E-mail em **horário comercial** | **24/7 telefone, chat, e-mail** | 24/7 | 24/7 |
| Orientação geral | — | < 24 h úteis | < 24 h | < 24 h | < 24 h |
| Sistema prejudicado | — | < 12 h úteis | < 12 h | < 12 h | < 12 h |
| Produção prejudicada | — | — | < 4 h | < 4 h | < 4 h |
| **Produção fora do ar** | — | — | **< 1 h** | < 1 h | < 1 h |
| **Sistema crítico fora do ar** | — | — | — | **< 30 min** | **< 15 min** |
| Trusted Advisor | Core checks | Core checks | **Todos** + API | Todos + API | Todos + API + Priority |
| AWS Health API | — | — | ✅ | ✅ | ✅ |
| TAM | — | — | — | **Pool de TAMs** | **TAM designado** |
| Concierge (faturamento/conta) | — | — | — | ✅ | ✅ |
| Infrastructure Event Management | — | — | Pago à parte | ✅ (1/ano) | ✅ |
| Revisões Well-Architected/operações | — | — | — | ✅ | ✅ |
| Suporte a software de terceiros | — | — | ✅ | ✅ | ✅ |
| Treinamentos/workshops | — | — | — | — | ✅ |

## 🔄 Modelo novo (desde dezembro/2025)

| Plano | Preço | Resposta crítica |
|---|---|---|
| Basic | Grátis | — |
| **Business Support+** | A partir de US$ 29/mês por conta (ou % do uso) | 30 min |
| **Enterprise** | Mínimo US$ 5.000/mês (TAM designado) | 15 min |
| **Unified Operations** | A partir de US$ 50.000/mês | 5 min |

- Developer, Business e Enterprise On-Ramp **encerram em 01/01/2027**. Na prova, estude o modelo clássico.

## Recursos do suporte

- **TAM (Technical Account Manager):** consultor técnico proativo.
- **Concierge Support Team:** especialistas em faturamento e conta.
- **IEM:** apoio para eventos de grande escala (lançamentos, Black Friday).
- **AWS Support App** (Slack), **AWS Support API** (Business+), **AWS Incident Detection and Response** (add-on Enterprise).
- **Quem muda o plano:** o **usuário root**.

## ❓ Perguntas típicas

- "Mais barato com suporte técnico 24/7 por telefone." → Business.
- "Mais barato com todas as verificações do Trusted Advisor." → Business.
- "TAM dedicado." → Enterprise. "Pool de TAMs." → Enterprise On-Ramp.
- "< 15 min para sistema crítico." → Enterprise. "< 1 h para produção fora do ar." → Business.
- "Ambiente de testes, ajuda ocasional por e-mail." → Developer.
- "O Basic tem suporte técnico?" → Não.

## 🔗 Documentação oficial

- [Comparação de planos](https://aws.amazon.com/premiumsupport/plans/) · [AWS Support User Guide](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html)
