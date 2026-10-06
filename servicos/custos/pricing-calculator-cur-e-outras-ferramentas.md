# Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe precisa estimar um projeto antes de criar recursos e, depois, pode precisar entender a cobrança em mais detalhe.

**Como este serviço ajuda?** Pricing Calculator estima custos com entradas fornecidas por você. Relatórios de custos e uso ajudam a analisar consumo ocorrido; outras ferramentas atendem organização e administração da cobrança.

**Exemplo do dia a dia:** A escola descreve a capacidade planejada para estimar um sistema. Depois de usá-lo, consulta dados de cobrança para comparar a estimativa com o consumo real.

**O que ele não resolve sozinho?** Estimativa não é uma proposta de preço garantido nem a fatura futura. Relatório de gasto real também não escolhe sozinho a arquitetura mais econômica.

**Primeiras palavras para entender:**

- **Estimativa:** cálculo com hipóteses.
- **Uso:** consumo efetivo de recursos.
- **CUR:** relatório detalhado de custos e uso.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gestão de custos e faturamento · **Domínio:** 4 · **Escopo:** Conta / organização · **Tópico do guia:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)
>
> **Em uma frase:** ferramentas para estimar, detalhar, ratear, otimizar e acompanhar os custos da AWS.
>
> **Escopo oficial:** ✅ No escopo (Billing Conductor ❌ fora do escopo) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Antes do uso, estime a capacidade e as condições previstas na calculadora.

**Passo 2.** Depois do uso, analise registros e relatórios para entender o consumo ocorrido.

**Passo 3.** Compare hipóteses e realidade. Estimativa e relatório respondem perguntas diferentes e não são garantias de uma fatura fixa.

## 2. Recursos e opções, com significado

### Tabela de ferramentas

**AWS Pricing Calculator**

**Para que serve:** **Estimar** custos **antes** de criar recursos

**Detalhes:** Web, **gratuita**, sem conta; estimativas compartilháveis por link e exportáveis (CSV/PDF); versão no console de Billing considera seus descontos

**Billing and Cost Management console**

**Para que serve:** Fatura do mês, pagamentos, créditos, perfis de pagamento

**Detalhes:** Ponto de partida do faturamento; root pode liberar acesso ao Billing para usuários IAM

**Cost and Usage Report (CUR) / Data Exports**

**Para que serve:** Dados **mais granulares** possíveis (hora a hora, por recurso, com tags)

**Detalhes:** ✔️ Configurado pelo **AWS Data Exports**: CUR 2.0 (recomendado) e **FOCUS 1.2/1.0**; o CUR legado continua disponível. Entregue no **S3**; analisados com **Athena**, QuickSight, Redshift

**Cost Anomaly Detection**

**Para que serve:** Detecta **gastos anormais** com ML

**Detalhes:** Monitores por serviço/conta/tag; alertas com causa raiz provável; ✔️ **gratuito**

**Cost Optimization Hub**

**Para que serve:** Consolida recomendações de economia (rightsizing, RIs/SPs, ociosos) num lugar

**Detalhes:** Prioriza por economia estimada

**Cost allocation tags**

**Para que serve:** **Ratear custos** por projeto, time, centro de custo

**Detalhes:** Tags do usuário ou geradas pela AWS; precisam ser **ativadas** no Billing para aparecer nos relatórios

**Cost Categories**

**Para que serve:** Regras que agrupam custos (ex.: "Marketing" = contas X e Y + tag Z)

**Detalhes:** Usadas em Cost Explorer, Budgets, CUR

**Consolidated billing (Organizations)**

**Para que serve:** Fatura única, descontos por volume, compartilhamento de RIs/SPs

**Detalhes:** Sem custo extra

**AWS Billing Conductor ❌ fora do escopo**

**Para que serve:** Faturamento **personalizado** (pro forma)

**Detalhes:** Revendedores e empresas que refaturam clientes/áreas

**Savings Plans / Reservations (console)**

**Para que serve:** Comprar, acompanhar utilização e cobertura

**Detalhes:** Recomendações no Cost Explorer

**Free Tier usage alerts**

**Para que serve:** Avisa quando o uso se aproxima dos limites gratuitos

**Detalhes:** Ativado por padrão

**AWS Customer Carbon Footprint Tool**

**Para que serve:** Estimativa de **emissões de carbono** do seu uso

**Detalhes:** Gratuita, no Billing; pilar Sustentabilidade

**AWS Price List API**

**Para que serve:** Preços via API

**Detalhes:** Automação

**AWS Marketplace**

**Para que serve:** Comprar software de terceiros cobrado na fatura AWS

**Detalhes:** AMIs, SaaS, contêineres, dados, serviços profissionais

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Estimativa não é uma proposta de preço garantido nem a fatura futura. Relatório de gasto real também não escolhe sozinho a arquitetura mais econômica.

## 4. Caso resolvido: ligando as peças

A escola descreve a capacidade planejada para estimar um sistema. Depois de usá-lo, consulta dados de cobrança para comparar a estimativa com o consumo real.

**Aplicando a sequência à situação:**

**Etapa 1:** Antes do uso, estime a capacidade e as condições previstas na calculadora.
**Etapa 2:** Depois do uso, analise registros e relatórios para entender o consumo ocorrido.
**Etapa 3:** Compare hipóteses e realidade. Estimativa e relatório respondem perguntas diferentes e não são garantias de uma fatura fixa.

**Resultado e responsabilidade:** Pricing Calculator estima custos com entradas fornecidas por você. Relatórios de custos e uso ajudam a analisar consumo ocorrido; outras ferramentas atendem organização e administração da cobrança.

**Recursos envolvidos:** Estimativas, exports detalhados, tags de custo e detecção de anomalia.

**Decisões que precisam ser tomadas:** Premissas, dados exportados, destino e acesso.

**Outra situação comentada:** Planejar nova aplicação: Calculator; auditoria detalhada do gasto real: exportação de custos.

**Por que não concluir mais do que isso:** Estimativa não é fatura garantida; tag precisa ativação como tag de custo quando aplicável

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Estimar o custo de uma arquitetura antes de criá-la."

**Resposta curta:** Pricing Calculator.

**Pergunta:** "Relatório mais detalhado de custo e uso, por hora e recurso."

**Resposta curta:** Cost and Usage Report.

**Pergunta:** "Ser avisado de um gasto anormal."

**Resposta curta:** Cost Anomaly Detection.

**Pergunta:** "Separar custos por projeto ou departamento."

**Resposta curta:** Cost allocation tags (ativadas no Billing).

**Pergunta:** "Acompanhar a pegada de carbono do uso da AWS."

**Resposta curta:** Customer Carbon Footprint Tool.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Pricing Calculator](https://calculator.aws/) · [Data Exports / CUR](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) · [Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
