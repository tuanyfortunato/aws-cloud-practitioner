<!-- autoral -->

# AWS Budgets

> **Categoria:** Gestão de custos · **Domínio:** 4 · **Abrangência:** Global (console de Billing and Cost Management) · **Ficha:** núcleo
>
> **Em uma frase:** acompanha custos e uso contra um valor definido, avisa quando o real ou o previsto se aproxima ou passa dele e pode agir automaticamente.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A rede de escolas tem US$ 2.000 por mês para a AWS. No ano passado, um laboratório esquecido ligado só apareceu na fatura do mês seguinte, quando o dinheiro já tinha sido gasto. A diretora quer saber antes.

O **AWS Budgets** acompanha custos e uso contra o valor definido e **avisa** por e-mail ou por um tópico do Amazon SNS quando o custo **real** ou o **previsto** se aproxima ou passa do limite. A escola cria um orçamento de custo de US$ 2.000 por mês, com aviso quando a previsão passar de 80%. Além de avisar, o Budgets pode **agir**, de forma automática ou depois de uma aprovação: aplicar uma política do IAM ou uma SCP que impeça criar novos recursos, ou agir sobre instâncias específicas do EC2 e do RDS.

O limite: o Budgets compara com um valor fixo. Um gasto que dobrou sem passar do orçamento é trabalho do Cost Anomaly Detection, e entender de onde veio o gasto é trabalho do [Cost Explorer](cost-explorer.md).

## Como funciona

1. Escolhe-se o tipo de orçamento e o período, como custo mensal.
2. Define-se o valor e os limites de aviso, pelo real ou pelo previsto.
3. Indicam-se os destinatários: e-mails ou um tópico do SNS.
4. Opcionalmente, configura-se uma ação que roda ao atingir o limite.

## Opções principais

| Tipo | O que acompanha | Na escola |
|---|---|---|
| Orçamento de custo | Gasto real ou previsto contra um valor | US$ 2.000 por mês |
| Orçamento de uso | Uso de um ou mais serviços | Horas de instância do laboratório |
| Utilização e cobertura de RIs e Savings Plans | Se os descontos comprados estão sendo usados | Reservas da sede pouco aproveitadas |
| Ações | Política do IAM, SCP ou ação em instâncias do EC2 e do RDS | Bloquear novos recursos ao estourar |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Acompanhar e receber avisos | Gratuito | 06/10/2026 |
| Orçamentos com ações | Os dois primeiros grátis por mês; depois US$ 0,10 por dia cada | 06/10/2026 |
| Relatórios do Budgets por e-mail | US$ 0,01 por relatório entregue | 06/10/2026 |

## Como é cobrado

Criar orçamentos, acompanhá-los e receber avisos é gratuito. Paga-se só pelos orçamentos com ações além dos dois primeiros e por cada relatório entregue.

## Não confundir com

| Serviço | Diferença para o Budgets | Pista no enunciado |
|---|---|---|
| [AWS Cost Explorer](cost-explorer.md) | Analisa gastos passados e prevê | "Visualizar", "tendência" |
| Alarme de cobrança do CloudWatch | Dispara pela cobrança atual estimada, sem previsão | "Métrica de cobranças estimadas" |
| Cost Anomaly Detection | Usa machine learning para gastos fora do padrão | "Gasto incomum" |
| [AWS Organizations (SCP)](../gerenciamento/organizations.md) | Define limites de permissão; o Budgets pode aplicá-los | "Impedir em todas as contas" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Gerenciar custos com o AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Ações do Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html)
- [Preços do AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
