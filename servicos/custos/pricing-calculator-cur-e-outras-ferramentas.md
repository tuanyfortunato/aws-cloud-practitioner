<!-- autoral -->

# Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento

> **Categoria:** Gestão de custos e faturamento · **Domínio:** 4 · **Abrangência:** Conta e organização · **Ficha:** núcleo
>
> **Em uma frase:** as demais ferramentas de custo da prova: a Pricing Calculator estima antes, as tags e o faturamento consolidado separam e juntam os custos, o Cost Anomaly Detection pega gastos fora do padrão e o Cost and Usage Report entrega os dados completos.
>
> **Escopo oficial:** ✅ No escopo (Billing Conductor ❌ fora do escopo) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A diretora financeira da rede tem quatro pedidos além dos gráficos e dos avisos: saber quanto o sistema da biblioteca vai custar antes de criá-lo, ver o gasto de cada escola, receber uma fatura só para todas as contas e entregar à contabilidade os dados detalhados para as planilhas.

Cada pedido tem uma ferramenta. A **AWS Pricing Calculator** é uma ferramenta web **gratuita** para **estimar** o custo antes de criar os recursos; a estimativa mostra os custos adiantados, mensais e anuais, pode ser compartilhada por link e exportada em CSV ou PDF. As **tags de alocação de custos**, depois de **ativadas**, separam o gasto por escola nos relatórios. O **faturamento consolidado** do AWS Organizations junta as contas numa **fatura única** e soma o uso, o que compartilha descontos por volume, de instâncias reservadas e de Savings Plans. O **AWS Cost and Usage Report** (CUR) tem o conjunto **mais completo** de dados de custo e uso e os publica num **bucket do S3**; hoje a forma recomendada é o **CUR 2.0**, criado pelo **AWS Data Exports**. E o **Cost Anomaly Detection** usa machine learning para avisar sobre gastos fora do padrão.

O limite: a estimativa da calculadora não inclui impostos e não é um preço garantido; ela depende das hipóteses que a pessoa informa. E nenhuma dessas ferramentas escolhe sozinha a arquitetura mais barata.

## Como funciona

1. Antes de criar, a equipe monta a solução na Pricing Calculator e compartilha a estimativa.
2. Ao criar os recursos, aplica tags como `escola` e as ativa no console de Billing and Cost Management.
3. Durante o mês, o Cost Anomaly Detection monitora os gastos; no fim, a conta de gerenciamento paga a fatura consolidada.
4. O Data Exports entrega o CUR 2.0 no S3, onde pode ser analisado com Athena, Redshift ou Quick Sight.

## Opções principais

| Ferramenta | Para que serve | Na escola |
|---|---|---|
| AWS Pricing Calculator | Estimar antes de criar | Custo do sistema da biblioteca |
| Página Bills (Billing and Cost Management) | Fatura do mês e as anteriores | Conferir a fatura de setembro |
| Tags de alocação de custos | Separar custos por projeto, time ou unidade | Gasto de cada escola |
| Faturamento consolidado | Uma fatura para várias contas, com uso somado | Sede paga por todas as escolas |
| Cost Anomaly Detection | Avisar sobre gasto fora do padrão | Gasto que dobrou sem estourar o orçamento |
| Cost and Usage Report (Data Exports) | Dados mais detalhados, no S3 | Planilhas da contabilidade |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Pricing Calculator | Gratuita; exporta CSV ou PDF; sem impostos | 06/10/2026 |
| Faturamento consolidado | Sem custo adicional | 06/10/2026 |
| Prefixos das tags | `user:` (usuário) e `aws:` (geradas pela AWS) | 06/10/2026 |
| Cost Anomaly Detection | Roda cerca de três vezes por dia | 06/10/2026 |
| AWS Billing Conductor | Fora do escopo | 06/10/2026 |

## Como é cobrado

A Pricing Calculator é gratuita, e o faturamento consolidado não tem custo adicional. O CUR é gravado num bucket do S3 da própria conta.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Cost Explorer](cost-explorer.md) | Analisa e prevê o gasto que já existe | "Visualizar gastos passados" |
| [AWS Budgets](budgets.md) | Avisa e age ao passar de um valor fixo | "Alerta ao passar de US$ X" |
| [AWS Organizations](../gerenciamento/organizations.md) | Agrupa as contas; o faturamento consolidado é um recurso dele | "Várias contas", "SCP" |
| [AWS Marketplace](recursos-de-ajuda-e-parceiros.md) | Software de terceiros, cobrado na fatura da AWS | "Comprar software pronto" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é a AWS Pricing Calculator](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html)
- [Entender a fatura](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/getting-viewing-bill.html)
- [Tags de alocação de custos](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
- [Faturamento consolidado](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)
- [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)
- [O que é o AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
