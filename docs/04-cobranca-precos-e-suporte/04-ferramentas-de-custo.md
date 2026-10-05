# 4.4 Ferramentas de custo e faturamento

## 🧠 Antes de começar

**Qual é a dificuldade?** A equipe quer planejar um projeto, entender uma fatura e acompanhar um orçamento. São três perguntas diferentes sobre dinheiro.

**A ideia em palavras simples:** Calculadora estima; análise de custos explica gastos; orçamento acompanha metas; relatórios fornecem detalhe. A ferramenta depende da pergunta.

**Exemplo do dia a dia:** Antes de criar o sistema, a escola estima o custo. Depois, analisa o consumo e configura avisos para acompanhar o orçamento.

**O que não concluir?** Estimar não garante a fatura, e um aviso não é um bloqueio automático de todo gasto. Não confunda planejamento, análise e controle.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Forecast** | previsão de gasto futuro. |
| **Tag** | etiqueta chave-valor colocada num recurso (ex.: projeto=site). |
| **Anomalia** | gasto fora do padrão. |

**Ao terminar este tópico, você deve saber:**

- [ ] Ligar cada pergunta à ferramenta certa (estimar, analisar/prever, alertar, detalhar).
- [ ] Saber que as **cost allocation tags** precisam ser **ativadas** no Billing.
- [ ] Saber que o **consolidated billing** dá fatura única e desconto por volume.

<details>
<summary>Uma analogia para revisar a ideia</summary>

a **Pricing Calculator** é o **orçamento da obra**; o **Cost Explorer** é o **extrato com gráficos**; o **Budgets** é o **aviso do cartão** quando passa do limite; o **CUR** é a **nota fiscal detalhada**, item por item; as **tags** são **etiquetas** para separar a conta por departamento.

</details>

> 🎯 **Como não errar na prova:** "Estimar **antes**" → **Pricing Calculator**. "Tendência e **previsão**" → **Cost Explorer**. "**Alerta** ao passar de US$ X" → **Budgets**. "Mais **granular**" → **CUR**. "Ratear por departamento" → **cost allocation tags**.

---

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
| AWS Billing Conductor (❌ fora do escopo) | Faturamento personalizado | Para revendedores e grandes empresas que refaturam clientes ou áreas internas |
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

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** Calculator estima antes do uso; Cost Explorer investiga custo e consumo; Budgets acompanha limites e previsão; CUR/Data Exports fornece registros detalhados para análise.

**Como escolher:** Antes de implantar: Calculator. Onde gastou: Explorer. Avisar quando ultrapassar meta: Budgets. Dados detalhados: exportação. Tags de custo precisam ser ativadas conforme sua categoria.

**O que não concluir:** Budgets não é um teto rígido de cobrança. Atualização de dados e ações têm latência. Colocar tag num recurso não a torna automaticamente coluna ativa dos relatórios de custo.

### Exercício de decisão

A empresa quer avisar ao atingir 80% do orçamento e explicar quais serviços gastaram mais. Qual combinação?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Budgets para alerta e Cost Explorer para análise. Calculator projeta uma solução; não substitui os gastos já registrados.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) · 🏠 [Índice do domínio](README.md) · [4.5 Planos de AWS Support](05-planos-de-suporte.md) ➡️
