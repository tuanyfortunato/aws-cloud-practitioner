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

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Cost Explorer](../../servicos/custos/cost-explorer.md) · [AWS Budgets](../../servicos/custos/budgets.md) · [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md)

⬅️ [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) · 🏠 [Índice do domínio](README.md) · [4.5 Planos de AWS Support](05-planos-de-suporte.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.


O momento da pergunta muda a ferramenta: antes do uso, há hipóteses de consumo; depois do uso, há registros; durante o acompanhamento, há metas e avisos. Estimativa, análise e orçamento se complementam, mas não entregam o mesmo resultado.

Uma previsão não é garantia, e um alerta não é um teto rígido universal. Para agir, identifique o recurso que gera custo, suas condições e o impacto de mudar. Relatórios mais detalhados ajudam a investigar, mas não escolhem sozinhos a arquitetura.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

a **Pricing Calculator** é o **orçamento da obra**; o **Cost Explorer** é o **extrato com gráficos**; o **Budgets** é o **aviso do cartão** quando passa do limite; o **CUR** é a **nota fiscal detalhada**, item por item; as **tags** são **etiquetas** para separar a conta por departamento.

</details>

## 2. Conceitos e opções explicados

**AWS Pricing Calculator**

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**Para que serve:** **Estimar** o custo antes de criar recursos

**Detalhes de prova:** Gratuita, sem precisar de conta; gera estimativas compartilháveis

**Billing and Cost Management (Bills)**

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.


**Para que serve:** Ver a **fatura** do mês, por serviço e região

**Detalhes de prova:** Ponto de partida do faturamento

**AWS Cost Explorer**

**Antes de ler este trecho:**

- **AWS Cost Explorer / Cost Explorer:** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
- **rightsizing:** Ajustar capacidade à necessidade observada. Reduzir demais pode prejudicar a aplicação; a recomendação precisa ser avaliada pelo uso real.
- **tag:** Par de nome e valor associado a recursos ou objetos compatíveis. Ajuda organização; usos em permissões e cobrança dependem de configuração e suporte.


**Para que serve:** **Visualizar e analisar** gastos passados e **prever** os próximos meses

**Detalhes de prova:** Filtra por serviço, conta, região e tag; recomendações de rightsizing, RIs e Savings Plans; relatórios de uso e cobertura de reservas

**AWS Budgets**

**Antes de ler este trecho:**

- **AWS Budgets / Budgets:** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.


**Para que serve:** Definir orçamentos e receber **alertas**

**Detalhes de prova:** Orçamentos de custo, uso, RIs e Savings Plans; alerta pelo valor real ou previsto; **Budget Actions** podem aplicar políticas ou parar recursos

**AWS Cost and Usage Report (CUR) / Data Exports**

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.
- **QuickSight:** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis.
- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **CUR:** Relatório de custos e uso. Ele ajuda a analisar consumo registrado; é diferente de uma estimativa antes de criar recursos.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.


**Para que serve:** Relatório **mais detalhado** possível, hora a hora, por recurso

**Detalhes de prova:** Entregue num bucket S3; analisado com Athena, QuickSight ou Redshift

**AWS Cost Anomaly Detection**

**Antes de ler este trecho:**

- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.


**Para que serve:** Detectar **gastos fora do padrão** com ML

**Detalhes de prova:** Envia alertas com a causa provável

**Cost allocation tags**


**Para que serve:** **Separar custos** por projeto, time, ambiente ou centro de custo

**Detalhes de prova:** Tags definidas pelo usuário ou geradas pela AWS; precisam ser **ativadas** no console de Billing para aparecer nos relatórios

**AWS Organizations (consolidated billing)**

**Antes de ler este trecho:**

- **AWS Organizations / Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.


**Para que serve:** **Fatura única** para várias contas

**Detalhes de prova:** Soma o uso para descontos por volume; compartilha RIs e Savings Plans entre contas; sem custo extra

**AWS Billing Conductor (❌ fora do escopo)**


**Para que serve:** Faturamento personalizado

**Detalhes de prova:** Para revendedores e grandes empresas que refaturam clientes ou áreas internas

**AWS Marketplace**

**Antes de ler este trecho:**

- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.
- **BYOL:** Trazer licença própria elegível. É necessário verificar o direito de uso e as condições do software; a AWS não cria automaticamente essa licença.
- **licença:** Direito de usar um software sob condições. Instalar o programa ou inventariá-lo não concede automaticamente esse direito.


**Para que serve:** Comprar **software de terceiros**

**Detalhes de prova:** Cobrado na fatura AWS; AMIs, SaaS, contêineres, dados; licença por uso ou BYOL

**CloudWatch billing alarm**

**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **métrica:** Medida observada ao longo do tempo, como utilização ou número de erros. O número precisa de unidade, período e contexto para ter significado.
- **alarme:** Condição acompanhada sobre dados de monitoramento. Uma mudança de estado pode gerar ações configuradas; o alarme não diagnostica todo problema sozinho.


**Para que serve:** Alarme de custo baseado na métrica de cobrança

**Detalhes de prova:** Alternativa simples ao Budgets


**Antes de ler este trecho:**

- **Trusted Advisor:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.


**Outras fontes de economia:** Trusted Advisor (recursos ociosos), Compute Optimizer (rightsizing) e Savings Plans recommendations no Cost Explorer.


**Cai na prova:** "estimar antes de migrar" = Pricing Calculator; "ver tendência e prever gasto" = Cost Explorer; "alerta quando passar de US$ 500" = Budgets; "dados mais granulares para análise" = CUR; "ratear custos por departamento" = cost allocation tags; "várias contas, uma fatura e desconto por volume" = consolidated billing.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.


**Primeiro, identifique o funcionamento:** Calculator estima antes do uso; Cost Explorer investiga custo e consumo; Budgets acompanha limites e previsão; CUR/Data Exports fornece registros detalhados para análise.

**Depois, compare as escolhas:** Antes de implantar: Calculator. Onde gastou: Explorer. Avisar quando ultrapassar meta: Budgets. Dados detalhados: exportação. Tags de custo precisam ser ativadas conforme sua categoria.

**Por fim, verifique o limite:** Budgets não é um teto rígido de cobrança. Atualização de dados e ações têm latência. Colocar tag num recurso não a torna automaticamente coluna ativa dos relatórios de custo.

## 4. Caso resolvido

A empresa quer avisar ao atingir 80% do orçamento e explicar quais serviços gastaram mais. Qual combinação?

**Raciocínio e resposta:** Budgets para alerta e Cost Explorer para análise. Calculator projeta uma solução; não substitui os gastos já registrados.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A equipe quer planejar um projeto, entender uma fatura e acompanhar um orçamento. São três perguntas diferentes sobre dinheiro.

**2. O que a solução fornece?**

Calculadora estima; análise de custos explica gastos; orçamento acompanha metas; relatórios fornecem detalhe. A ferramenta depende da pergunta.

**3. Que conclusão seria incorreta?**

Estimar não garante a fatura, e um aviso não é um bloqueio automático de todo gasto. Não confunda planejamento, análise e controle.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Ligar cada pergunta à ferramenta certa (estimar, analisar/prever, alertar, detalhar).
- [ ] Saber que as **cost allocation tags** precisam ser **ativadas** no Billing.
- [ ] Saber que o **consolidated billing** dá fatura única e desconto por volume.

**Dica de revisão para a prova:** "Estimar **antes**" → **Pricing Calculator**. "Tendência e **previsão**" → **Cost Explorer**. "**Alerta** ao passar de US$ X" → **Budgets**. "Mais **granular**" → **CUR**. "Ratear por departamento" → **cost allocation tags**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).
**Pergunta:** "Estimar o custo de uma arquitetura antes de criá-la."

**Resposta curta:** Pricing Calculator.


**Fundamento explicado no capítulo:** "Estimar o custo de uma arquitetura antes de criá-la." → Pricing Calculator.

**Pergunta:** "Visualizar gastos dos últimos meses e prever o próximo."

**Resposta curta:** Cost Explorer.


**Fundamento explicado no capítulo:** "Visualizar gastos dos últimos meses e prever o próximo." → Cost Explorer.

**Pergunta:** "Receber alerta quando o gasto previsto passar do orçamento."

**Resposta curta:** Budgets.


**Fundamento explicado no capítulo:** "Receber alerta quando o gasto previsto passar do orçamento." → Budgets.

**Pergunta:** "Relatório mais detalhado de custo e uso, por hora e recurso."

**Resposta curta:** Cost and Usage Report.


**Fundamento explicado no capítulo:** "Relatório mais detalhado de custo e uso, por hora e recurso." → Cost and Usage Report.

**Pergunta:** "Ser avisado de um gasto anormal."

**Resposta curta:** Cost Anomaly Detection.


**Fundamento explicado no capítulo:** "Ser avisado de um gasto anormal." → Cost Anomaly Detection.

**Pergunta:** "Separar custos por projeto ou departamento."

**Resposta curta:** Cost allocation tags (ativadas no Billing).


**Fundamento explicado no capítulo:** "Separar custos por projeto ou departamento." → Cost allocation tags (ativadas no Billing).

**Pergunta:** "Uma fatura para várias contas, com desconto por volume."

**Resposta curta:** Consolidated billing no Organizations.


**Fundamento explicado no capítulo:** "Uma fatura para várias contas, com desconto por volume." → Consolidated billing no Organizations.

**Pergunta:** "Comprar software de terceiros pago na fatura AWS."

**Resposta curta:** AWS Marketplace.


**Fundamento explicado no capítulo:** "Comprar software de terceiros pago na fatura AWS." → AWS Marketplace.

**Pergunta:** "Onde ver recomendações de Savings Plans?"

**Resposta curta:** Cost Explorer.


**Fundamento explicado no capítulo:** "Onde ver recomendações de Savings Plans?" → Cost Explorer.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) · 🏠 [Índice do domínio](README.md) · [4.5 Planos de AWS Support](05-planos-de-suporte.md) ➡️
