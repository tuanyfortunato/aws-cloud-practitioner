# AWS Cost Explorer

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A fatura aumentou, mas a equipe não sabe qual serviço, conta ou período explica esse crescimento.

**Como este serviço ajuda?** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.

**Exemplo do dia a dia:** A escola compara dois meses e separa custos por serviço para investigar onde o gasto mudou.

**O que ele não resolve sozinho?** Ele analisa gastos; não bloqueia automaticamente a criação de recursos. Os dados não devem ser tratados como medição instantânea nem a previsão como garantia.

**Primeiras palavras para entender:**

- **Filtro:** seleção de uma parte dos dados.
- **Agrupamento:** divisão por critério, como serviço.
- **Previsão:** estimativa baseada em dados e método.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gestão de custos · **Domínio:** 4 · **Escopo:** Conta / organização · **Tópico do guia:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)
>
> **Em uma frase:** visualiza, analisa e **prevê** seus custos e uso da AWS ao longo do tempo.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Recursos

| Recurso | Detalhe |
|---|---|
| **Gráficos e filtros** | Por serviço, conta, região, tipo de instância, **tag**, cost category, tipo de cobrança; granularidade mensal, diária (e horária, paga). |
| **Previsão (forecast)** | ✔️ Até **3 meses** em granularidade diária e até **12 meses** em mensal, com intervalo de predição de 80%; sem histórico suficiente (conta nova), não gera previsão. |
| **Histórico** | ✔️ **13 meses** + o mês corrente. |
| **Relatórios salvos** | Modelos prontos (custo mensal por serviço, uso de RIs…) e customizados. |
| **Recomendações** | **Rightsizing** de EC2, **compra de RIs e Savings Plans** (com estimativa de economia). |
| **Relatórios de RI/SP** | **Utilização** (quanto do compromisso foi usado) e **cobertura** (quanto do uso está coberto). |
| **API** | ✔️ Interface gráfica gratuita; a **API** custa **US$ 0,01 por requisição paginada**. |
| **Ativação** | Precisa ser **habilitado** no console (dados levam até 24 h para aparecer). |

## ⚠️ Não confundir

- **Cost Explorer** (analisa o passado e prevê) × **Budgets** (alerta e age) × **Pricing Calculator** (estima **antes** de usar) × **CUR** (dados brutos mais detalhados).

## ❓ Perguntas típicas

- "Visualizar gastos dos últimos meses e prever o próximo." → Cost Explorer.
- "Onde ver recomendações de Savings Plans e RIs?" → Cost Explorer.
- "Verificar se as Reserved Instances estão sendo usadas." → Relatório de utilização de RI no Cost Explorer.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Relatórios, filtros, dimensões, grupos e previsões |
| **O que você decide/configura?** | Período, granularidade e visão autorizada |
| **Em que ordem as coisas acontecem?** | Consulte custos processados e compare distribuição/tendências |
| **O que pode fazer, e em que condição?** | Ajuda a explicar onde e como se gasta |
| **O que não pode presumir?** | Não é medidor instantâneo nem bloqueio de consumo; previsão não garante valor final |

**Caso comentado:** Descobrir serviço responsável pelo aumento: agrupar por serviço e investigar conta/região/tags.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
