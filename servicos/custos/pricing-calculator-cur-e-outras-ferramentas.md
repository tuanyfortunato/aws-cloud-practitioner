# Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento

> **Categoria:** Gestão de custos e faturamento · **Domínio:** 4 · **Escopo:** Conta / organização · **Tópico do guia:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)
>
> **Em uma frase:** ferramentas para estimar, detalhar, ratear, otimizar e acompanhar os custos da AWS.
>
> **Escopo oficial:** ✅ No escopo (Billing Conductor ❌ fora do escopo) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **orçamento antes da obra** (Pricing Calculator) e a **nota fiscal detalhada depois** (Cost and Usage Report).

- ✅ **Escolha quando:** precisa **estimar custos antes** de criar recursos, ou obter os **dados mais detalhados** de cobrança.
- 🚫 **Não é a resposta quando:** quer **gráficos do gasto** → [Cost Explorer](cost-explorer.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "estimar antes" → Pricing Calculator; "relatório mais detalhado" → Cost and Usage Report; "separar custos por projeto" → cost allocation tags.
<!-- didatico:fim -->

## Tabela de ferramentas

| Ferramenta | Para que serve | Detalhes |
|---|---|---|
| **AWS Pricing Calculator** | **Estimar** custos **antes** de criar recursos | Web, **gratuita**, sem conta; estimativas compartilháveis por link e exportáveis (CSV/PDF); versão no console de Billing considera seus descontos |
| **Billing and Cost Management console** | Fatura do mês, pagamentos, créditos, perfis de pagamento | Ponto de partida do faturamento; root pode liberar acesso ao Billing para usuários IAM |
| **Cost and Usage Report (CUR) / Data Exports** | Dados **mais granulares** possíveis (hora a hora, por recurso, com tags) | ✔️ Configurado pelo **AWS Data Exports**: CUR 2.0 (recomendado) e **FOCUS 1.2/1.0**; o CUR legado continua disponível. Entregue no **S3**; analisados com **Athena**, QuickSight, Redshift |
| **Cost Anomaly Detection** | Detecta **gastos anormais** com ML | Monitores por serviço/conta/tag; alertas com causa raiz provável; ✔️ **gratuito** |
| **Cost Optimization Hub** | Consolida recomendações de economia (rightsizing, RIs/SPs, ociosos) num lugar | Prioriza por economia estimada |
| **Cost allocation tags** | **Ratear custos** por projeto, time, centro de custo | Tags do usuário ou geradas pela AWS; precisam ser **ativadas** no Billing para aparecer nos relatórios |
| **Cost Categories** | Regras que agrupam custos (ex.: "Marketing" = contas X e Y + tag Z) | Usadas em Cost Explorer, Budgets, CUR |
| **Consolidated billing** (Organizations) | Fatura única, descontos por volume, compartilhamento de RIs/SPs | Sem custo extra |
| **AWS Billing Conductor** ❌ *fora do escopo* | Faturamento **personalizado** (pro forma) | Revendedores e empresas que refaturam clientes/áreas |
| **Savings Plans / Reservations** (console) | Comprar, acompanhar utilização e cobertura | Recomendações no Cost Explorer |
| **Free Tier usage alerts** | Avisa quando o uso se aproxima dos limites gratuitos | Ativado por padrão |
| **AWS Customer Carbon Footprint Tool** | Estimativa de **emissões de carbono** do seu uso | Gratuita, no Billing; pilar Sustentabilidade |
| **AWS Price List API** | Preços via API | Automação |
| **AWS Marketplace** | Comprar software de terceiros cobrado na fatura AWS | AMIs, SaaS, contêineres, dados, serviços profissionais |

## ❓ Perguntas típicas

- "Estimar o custo de uma arquitetura antes de criá-la." → Pricing Calculator.
- "Relatório mais detalhado de custo e uso, por hora e recurso." → Cost and Usage Report.
- "Ser avisado de um gasto anormal." → Cost Anomaly Detection.
- "Separar custos por projeto ou departamento." → Cost allocation tags (ativadas no Billing).
- "Acompanhar a pegada de carbono do uso da AWS." → Customer Carbon Footprint Tool.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Estimativas, exports detalhados, tags de custo e detecção de anomalia |
| **O que você decide/configura?** | Premissas, dados exportados, destino e acesso |
| **Em que ordem as coisas acontecem?** | Estime antes; após uso, analise registros e desvios |
| **O que pode fazer, e em que condição?** | Calculator projeta; CUR/Data Exports detalha consumo |
| **O que não pode presumir?** | Estimativa não é fatura garantida; tag precisa ativação como tag de custo quando aplicável |

**Caso comentado:** Planejar nova aplicação: Calculator; auditoria detalhada do gasto real: exportação de custos.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Pricing Calculator](https://calculator.aws/) · [Data Exports / CUR](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) · [Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)
