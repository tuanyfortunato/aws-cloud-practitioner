# AWS Budgets

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa quer acompanhar um limite planejado de custo ou uso e receber avisos antes de perder o controle do orçamento.

**Como este serviço ajuda?** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.

**Exemplo do dia a dia:** A escola configura um orçamento mensal e um aviso para determinados níveis de gasto observado ou previsto.

**O que ele não resolve sozinho?** Um orçamento não é, por padrão, um teto rígido que interrompe todo consumo. Alertas e ações não substituem controle de acesso e acompanhamento dos recursos.

**Primeiras palavras para entender:**

- **Orçamento:** meta de gasto ou uso.
- **Limite de aviso:** condição para notificação.
- **Ação:** operação configurada para determinada condição.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gestão de custos · **Domínio:** 4 · **Escopo:** Conta / organização · **Tópico do guia:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)
>
> **Em uma frase:** define orçamentos de custo e uso e **alerta** (ou **age**) quando o valor real ou **previsto** ultrapassa o limite.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Orçamento, thresholds, notificações e actions opcionais |
| **O que você decide/configura?** | Valor/meta, período, destinatários e permissões de ação |
| **Em que ordem as coisas acontecem?** | Compara consumo/previsão com meta e notifica ou aplica ação configurada |
| **O que pode fazer, e em que condição?** | Ajuda acompanhamento e resposta a custos/uso |
| **O que não pode presumir?** | Não garante teto rígido da conta: atualização e ações têm latência e alcance limitado |

**Caso comentado:** Alertar em 80% do orçamento: Budgets; desligar qualquer recurso não é comportamento automático universal.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
