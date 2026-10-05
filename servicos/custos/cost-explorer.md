# AWS Cost Explorer

> **Categoria:** Gestão de custos · **Domínio:** 4 · **Escopo:** Conta / organização · **Tópico do guia:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)
>
> **Em uma frase:** visualiza, analisa e **prevê** seus custos e uso da AWS ao longo do tempo.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **extrato do cartão com gráficos e previsão**: mostra para onde foi o dinheiro e quanto você ainda deve gastar.

- ✅ **Escolha quando:** precisa **analisar gastos passados** e **prever** os próximos meses.
- 🚫 **Não é a resposta quando:** quer **ser avisado** ao passar de um limite → [Budgets](budgets.md); quer **estimar antes** de criar recursos → [Pricing Calculator](pricing-calculator-cur-e-outras-ferramentas.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "visualizar gastos", "prever custos", "recomendações de Reserved Instances e Savings Plans".
<!-- didatico:fim -->

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
