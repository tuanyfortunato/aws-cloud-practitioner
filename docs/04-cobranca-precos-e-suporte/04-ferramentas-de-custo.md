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

---

> **Domínio 4 — Cobrança, Preços e Suporte (12%)**

> 🔎 **Fichas detalhadas:** [AWS Cost Explorer](../../servicos/custos/cost-explorer.md) · [AWS Budgets](../../servicos/custos/budgets.md) · [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md)

⬅️ [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) · 🏠 [Índice do domínio](README.md) · [4.5 Planos de AWS Support](05-planos-de-suporte.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

O momento da pergunta muda a ferramenta: antes do uso, há hipóteses de consumo; depois do uso, há registros; durante o acompanhamento, há metas e avisos. Estimativa, análise e orçamento se complementam, mas não entregam o mesmo resultado.

Uma previsão não é garantia, e um alerta não é um teto rígido universal. Para agir, identifique o recurso que gera custo, suas condições e o impacto de mudar. Relatórios mais detalhados ajudam a investigar, mas não escolhem sozinhos a arquitetura.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

a **Pricing Calculator** é o **orçamento da obra**; o **Cost Explorer** é o **extrato com gráficos**; o **Budgets** é o **aviso do cartão** quando passa do limite; o **CUR** é a **nota fiscal detalhada**, item por item; as **tags** são **etiquetas** para separar a conta por departamento.

</details>

## 2. Conceitos e opções explicados

**AWS Pricing Calculator**

**Para que serve:** **Estimar** o custo antes de criar recursos

**Detalhes de prova:** Gratuita, sem precisar de conta; gera estimativas compartilháveis

**Billing and Cost Management (Bills)**

**Para que serve:** Ver a **fatura** do mês, por serviço e região

**Detalhes de prova:** Ponto de partida do faturamento

**AWS Cost Explorer**

**Para que serve:** **Visualizar e analisar** gastos passados e **prever** os próximos meses

**Detalhes de prova:** Filtra por serviço, conta, região e tag; recomendações de rightsizing, RIs e Savings Plans; relatórios de uso e cobertura de reservas

**AWS Budgets**

**Para que serve:** Definir orçamentos e receber **alertas**

**Detalhes de prova:** Orçamentos de custo, uso, RIs e Savings Plans; alerta pelo valor real ou previsto; **Budget Actions** podem aplicar políticas ou parar recursos

**AWS Cost and Usage Report (CUR) / Data Exports**

**Para que serve:** Relatório **mais detalhado** possível, hora a hora, por recurso

**Detalhes de prova:** Entregue num bucket S3; analisado com Athena, QuickSight ou Redshift

**AWS Cost Anomaly Detection**

**Para que serve:** Detectar **gastos fora do padrão** com ML

**Detalhes de prova:** Envia alertas com a causa provável

**Cost allocation tags**

**Para que serve:** **Separar custos** por projeto, time, ambiente ou centro de custo

**Detalhes de prova:** Tags definidas pelo usuário ou geradas pela AWS; precisam ser **ativadas** no console de Billing para aparecer nos relatórios

**AWS Organizations (consolidated billing)**

**Para que serve:** **Fatura única** para várias contas

**Detalhes de prova:** Soma o uso para descontos por volume; compartilha RIs e Savings Plans entre contas; sem custo extra

**AWS Billing Conductor (❌ fora do escopo)**

**Para que serve:** Faturamento personalizado

**Detalhes de prova:** Para revendedores e grandes empresas que refaturam clientes ou áreas internas

**AWS Marketplace**

**Para que serve:** Comprar **software de terceiros**

**Detalhes de prova:** Cobrado na fatura AWS; AMIs, SaaS, contêineres, dados; licença por uso ou BYOL

**CloudWatch billing alarm**

**Para que serve:** Alarme de custo baseado na métrica de cobrança

**Detalhes de prova:** Alternativa simples ao Budgets

**Outras fontes de economia:** Trusted Advisor (recursos ociosos), Compute Optimizer (rightsizing) e Savings Plans recommendations no Cost Explorer.

**Cai na prova:** "estimar antes de migrar" = Pricing Calculator; "ver tendência e prever gasto" = Cost Explorer; "alerta quando passar de US$ 500" = Budgets; "dados mais granulares para análise" = CUR; "ratear custos por departamento" = cost allocation tags; "várias contas, uma fatura e desconto por volume" = consolidated billing.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** Calculator estima antes do uso; Cost Explorer investiga custo e consumo; Budgets acompanha limites e previsão; CUR/Data Exports fornece registros detalhados para análise.

**Depois, compare as escolhas:** Antes de implantar: Calculator. Onde gastou: Explorer. Avisar quando ultrapassar meta: Budgets. Dados detalhados: exportação. Tags de custo precisam ser ativadas conforme sua categoria.

**Por fim, verifique o limite:** Budgets não é um teto rígido de cobrança. Atualização de dados e ações têm latência. Colocar tag num recurso não a torna automaticamente coluna ativa dos relatórios de custo.

## 4. Caso resolvido

A empresa quer avisar ao atingir 80% do orçamento e explicar quais serviços gastaram mais. Qual combinação?

**Raciocínio e resposta:** Budgets para alerta e Cost Explorer para análise. Calculator projeta uma solução; não substitui os gastos já registrados.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Ligar cada pergunta à ferramenta certa (estimar, analisar/prever, alertar, detalhar).
- [ ] Saber que as **cost allocation tags** precisam ser **ativadas** no Billing.
- [ ] Saber que o **consolidated billing** dá fatura única e desconto por volume.

**Dica de revisão para a prova:** "Estimar **antes**" → **Pricing Calculator**. "Tendência e **previsão**" → **Cost Explorer**. "**Alerta** ao passar de US$ X" → **Budgets**. "Mais **granular**" → **CUR**. "Ratear por departamento" → **cost allocation tags**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).
**Pergunta:** "Estimar o custo de uma arquitetura antes de criá-la."

**Resposta curta:** Pricing Calculator.

**Pergunta:** "Visualizar gastos dos últimos meses e prever o próximo."

**Resposta curta:** Cost Explorer.

**Pergunta:** "Receber alerta quando o gasto previsto passar do orçamento."

**Resposta curta:** Budgets.

**Pergunta:** "Relatório mais detalhado de custo e uso, por hora e recurso."

**Resposta curta:** Cost and Usage Report.

**Pergunta:** "Ser avisado de um gasto anormal."

**Resposta curta:** Cost Anomaly Detection.

**Pergunta:** "Separar custos por projeto ou departamento."

**Resposta curta:** Cost allocation tags (ativadas no Billing).

**Pergunta:** "Uma fatura para várias contas, com desconto por volume."

**Resposta curta:** Consolidated billing no Organizations.

**Pergunta:** "Comprar software de terceiros pago na fatura AWS."

**Resposta curta:** AWS Marketplace.

**Pergunta:** "Onde ver recomendações de Savings Plans?"

**Resposta curta:** Cost Explorer.

**Fundamento explicado no capítulo:** **Outras fontes de economia:** Trusted Advisor (recursos ociosos), Compute Optimizer (rightsizing) e Savings Plans recommendations no Cost Explorer.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) · 🏠 [Índice do domínio](README.md) · [4.5 Planos de AWS Support](05-planos-de-suporte.md) ➡️
