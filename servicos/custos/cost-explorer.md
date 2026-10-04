# AWS Cost Explorer

> **Categoria:** Gestão de custos · **Domínio:** 4 · **Escopo:** Conta / organização · **Tópico do guia:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)
>
> **Em uma frase:** visualiza, analisa e **prevê** seus custos e uso da AWS ao longo do tempo.

## Recursos

| Recurso | Detalhe |
|---|---|
| **Gráficos e filtros** | Por serviço, conta, região, tipo de instância, **tag**, cost category, tipo de cobrança; granularidade mensal, diária (e horária, paga). |
| **Previsão (forecast)** | Estima o gasto dos próximos meses com base no histórico. |
| **Relatórios salvos** | Modelos prontos (custo mensal por serviço, uso de RIs…) e customizados. |
| **Recomendações** | **Rightsizing** de EC2, **compra de RIs e Savings Plans** (com estimativa de economia). |
| **Relatórios de RI/SP** | **Utilização** (quanto do compromisso foi usado) e **cobertura** (quanto do uso está coberto). |
| **API** | Consultas programáticas (pagas por requisição). |
| **Ativação** | Precisa ser **habilitado** no console (dados levam até 24 h para aparecer). |

## ⚠️ Não confundir

- **Cost Explorer** (analisa o passado e prevê) × **Budgets** (alerta e age) × **Pricing Calculator** (estima **antes** de usar) × **CUR** (dados brutos mais detalhados).

## ❓ Perguntas típicas

- "Visualizar gastos dos últimos meses e prever o próximo." → Cost Explorer.
- "Onde ver recomendações de Savings Plans e RIs?" → Cost Explorer.
- "Verificar se as Reserved Instances estão sendo usadas." → Relatório de utilização de RI no Cost Explorer.

## 🔗 Documentação oficial

- [Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
