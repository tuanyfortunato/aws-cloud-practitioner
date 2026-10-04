# 4.4 Ferramentas de custo e faturamento

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Cost Explorer](../../servicos/custos/cost-explorer.md) · [AWS Budgets](../../servicos/custos/budgets.md) · [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md)

⬅️ [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) · 🏠 [Índice do domínio](README.md) · [4.5 Planos de AWS Support](05-planos-de-suporte.md) ➡️

---

## 📖 Conteúdo

| Ferramenta | Para que serve | Detalhes de prova |
| --- | --- | --- |
| AWS Pricing Calculator | **Estimar** o custo antes de criar recursos | Gratuita, sem precisar de conta; gera estimativas compartilháveis |
| Billing and Cost Management (Bills) | Ver a **fatura** do mês, por serviço e região | Ponto de partida do faturamento |
| AWS Cost Explorer | **Visualizar e analisar** gastos passados e **prever** os próximos meses | Filtra por serviço, conta, região e tag; recomendações de rightsizing, RIs e Savings Plans; relatórios de uso e cobertura de reservas |
| AWS Budgets | Definir orçamentos e receber **alertas** | Orçamentos de custo, uso, RIs e Savings Plans; alerta pelo valor real ou previsto; **Budget Actions** podem aplicar políticas ou parar recursos |
| AWS Cost and Usage Report (CUR) / Data Exports | Relatório **mais detalhado** possível, hora a hora, por recurso | Entregue num bucket S3; analisado com Athena, QuickSight ou Redshift |
| AWS Cost Anomaly Detection | Detectar **gastos fora do padrão** com ML | Envia alertas com a causa provável |
| Cost allocation tags | **Separar custos** por projeto, time, ambiente ou centro de custo | Tags definidas pelo usuário ou geradas pela AWS; precisam ser **ativadas** no console de Billing para aparecer nos relatórios |
| AWS Organizations (consolidated billing) | **Fatura única** para várias contas | Soma o uso para descontos por volume; compartilha RIs e Savings Plans entre contas; sem custo extra |
| AWS Billing Conductor | Faturamento personalizado | Para revendedores e grandes empresas que refaturam clientes ou áreas internas |
| AWS Marketplace | Comprar **software de terceiros** | Cobrado na fatura AWS; AMIs, SaaS, contêineres, dados; licença por uso ou BYOL |
| CloudWatch billing alarm | Alarme de custo baseado na métrica de cobrança | Alternativa simples ao Budgets |

- **Outras fontes de economia:** Trusted Advisor (recursos ociosos), Compute Optimizer (rightsizing) e Savings Plans recommendations no Cost Explorer.
- **Cai na prova:** "estimar antes de migrar" = Pricing Calculator; "ver tendência e prever gasto" = Cost Explorer; "alerta quando passar de US$ 500" = Budgets; "dados mais granulares para análise" = CUR; "ratear custos por departamento" = cost allocation tags; "várias contas, uma fatura e desconto por volume" = consolidated billing.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).

- "Estimar o custo de uma arquitetura antes de criá-la." → Pricing Calculator.
- "Visualizar gastos dos últimos meses e prever o próximo." → Cost Explorer.
- "Receber alerta quando o gasto previsto passar do orçamento." → Budgets.
- "Relatório mais detalhado de custo e uso, por hora e recurso." → Cost and Usage Report.
- "Ser avisado de um gasto anormal." → Cost Anomaly Detection.
- "Separar custos por projeto ou departamento." → Cost allocation tags (ativadas no Billing).
- "Uma fatura para várias contas, com desconto por volume." → Consolidated billing no Organizations.
- "Comprar software de terceiros pago na fatura AWS." → AWS Marketplace.
- "Onde ver recomendações de Savings Plans?" → Cost Explorer.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) · 🏠 [Índice do domínio](README.md) · [4.5 Planos de AWS Support](05-planos-de-suporte.md) ➡️
