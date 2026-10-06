<!-- autoral -->

# AWS Cost Explorer

> **Categoria:** Gestão de custos · **Domínio:** 4 · **Abrangência:** Global (console de Billing and Cost Management) · **Ficha:** núcleo
>
> **Em uma frase:** mostra os custos e o uso da conta em gráficos e relatórios, com filtros e agrupamentos, até 13 meses para trás e previsão para os próximos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A conta da rede de escolas subiu nos últimos três meses, e a diretora financeira quer saber o porquê e quanto vai gastar até dezembro. A fatura mostra os totais por serviço, mas não conta a história do gasto ao longo do tempo.

O **Cost Explorer** permite **ver e analisar** custos e uso com gráficos e relatórios. A diretora filtra e agrupa por serviço, conta, Região ou tag e descobre que o aumento veio da transferência de dados de uma escola. Ele mostra até os **últimos 13 meses**, faz a **previsão** dos próximos 18 e traz recomendações de compra de instâncias reservadas e de Savings Plans.

O limite: o Cost Explorer olha e prevê, mas não avisa nem age quando o gasto passa de um valor; isso é do [Budgets](budgets.md). Para os dados linha a linha, por recurso e por hora, numa análise própria, o caminho é o [Cost and Usage Report](pricing-calculator-cur-e-outras-ferramentas.md).

## Como funciona

1. Abre-se o Cost Explorer no console de Billing and Cost Management.
2. Escolhe-se o período, a granularidade (mês, dia ou hora) e a métrica.
3. Filtra-se e agrupa-se por serviço, conta, Região ou tag de alocação de custos ativada.
4. Lê-se o gráfico, a previsão e as recomendações; a visão pode ser salva como relatório.

## Opções principais

| Recurso | O que mostra | Na escola |
|---|---|---|
| Gráficos de custo e uso | Gasto ao longo do tempo, com filtros | De onde veio o aumento |
| Previsão | Estimativa dos próximos meses | Quanto a rede gasta até dezembro |
| Agrupar por tag | Custo de cada projeto ou unidade | Gasto de cada escola |
| Recomendações | Compras de instâncias reservadas e Savings Plans | Economizar nos servidores sempre ligados |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Histórico | Até os últimos 13 meses | 06/10/2026 |
| Previsão | Próximos 18 meses | 06/10/2026 |
| Granularidade por hora | Últimos 14 dias, recurso cobrado à parte | 06/10/2026 |
| Uso pelo console | Gratuito | 06/10/2026 |
| Uso pela API | US$ 0,01 por requisição | 06/10/2026 |

## Como é cobrado

Usar o Cost Explorer pelo console não tem custo. O acesso programático pela API é cobrado por requisição, e a granularidade por hora, quando ativada, é cobrada pelo número de registros de uso.

## Não confundir com

| Serviço | Diferença para o Cost Explorer | Pista no enunciado |
|---|---|---|
| [AWS Budgets](budgets.md) | Avisa e age ao passar de um limite | "Alerta", "orçamento" |
| [AWS Pricing Calculator](pricing-calculator-cur-e-outras-ferramentas.md) | Estima o custo antes de criar os recursos | "Antes de migrar", "estimar" |
| [Cost and Usage Report](pricing-calculator-cur-e-outras-ferramentas.md) | Dados mais detalhados, entregues no S3 | "Por recurso e por hora", "planilha" |
| Cost Anomaly Detection | Detecta gastos fora do padrão com machine learning | "Gasto incomum" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Análise de custos com o AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Filtros do Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html)
- [Preços do AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
