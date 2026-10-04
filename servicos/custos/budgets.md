# AWS Budgets

> **Categoria:** Gestão de custos · **Domínio:** 4 · **Escopo:** Conta / organização · **Tópico do guia:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)
>
> **Em uma frase:** define orçamentos de custo e uso e **alerta** (ou **age**) quando o valor real ou **previsto** ultrapassa o limite.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **limite do cartão com aviso no celular**: avisa (ou age) quando o gasto real ou previsto passa do combinado.

- ✅ **Escolha quando:** precisa **definir orçamentos** e **receber alertas**.
- 🚫 **Não é a resposta quando:** quer **analisar o histórico** de gastos → [Cost Explorer](cost-explorer.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "alertar quando o gasto passar de", "orçamento", "gasto previsto".
<!-- didatico:fim -->

## Tipos de orçamento

| Tipo | Monitora |
|---|---|
| **Cost budget** | Valor gasto (US$) |
| **Usage budget** | Quantidade de uso (horas de EC2, GB de S3) |
| **Savings Plans budget** | Utilização ou cobertura dos Savings Plans |
| **Reservation budget** | Utilização ou cobertura das RIs |

## Configurações

| Item | Detalhe |
|---|---|
| **Período** | Diário, mensal, trimestral, anual; valor fixo ou planejado mês a mês. |
| **Filtros** | Serviço, conta, região, tag, cost category… |
| **Alertas** | Por limite **real** ou **previsto** (forecasted), em % ou valor; via **e-mail**, **SNS** ou Amazon Q Developer em chat (Slack/Teams). |
| **Budget Actions** | Ações automáticas ao atingir o limite: aplicar **política IAM**, aplicar **SCP**, **parar instâncias EC2/RDS** — com ou sem aprovação. |
| **Templates** | Orçamento de "gasto zero" e mensal fixo para começar (útil para quem estuda no Free Tier). |
| **Budgets reports** | Relatórios periódicos por e-mail. |

## Cobrança

- Orçamentos de monitoramento são gratuitos; os **dois primeiros** orçamentos com **actions** são grátis por mês e os demais custam **US$ 0,10/dia**; cada relatório do Budgets Reports custa US$ 0,01 (🧊).

## ⚠️ Não confundir

- **Budgets** (alerta/ação) × **Cost Explorer** (análise) × **Cost Anomaly Detection** (gasto **fora do padrão**, sem limite definido) × **CloudWatch billing alarm** (alarme simples sobre a cobrança estimada).

## ❓ Perguntas típicas

- "Receber alerta quando o gasto previsto passar do orçamento." → Budgets.
- "Parar instâncias automaticamente se o orçamento estourar." → Budget Actions.
- "Alerta quando as RIs forem subutilizadas." → Reservation budget.

## 🔗 Documentação oficial

- [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
