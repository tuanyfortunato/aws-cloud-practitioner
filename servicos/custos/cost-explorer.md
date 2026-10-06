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

## 1. A sequência de funcionamento

**Passo 1.** Selecione o período e a pergunta sobre custo ou uso que precisa responder.

**Passo 2.** Agrupe ou filtre dados para identificar a parte do gasto relacionada à pergunta.

**Passo 3.** Investigue a mudança nos recursos. Um aumento pode ter várias causas; a ferramenta mostra dados, não decide a ação sozinha.

## 2. Recursos e opções, com significado

### Recursos

**Gráficos e filtros**

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **tag:** Par de nome e valor associado a recursos ou objetos compatíveis. Ajuda organização; usos em permissões e cobrança dependem de configuração e suporte.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.

**Detalhe:** Por serviço, conta, região, tipo de instância, **tag**, cost category, tipo de cobrança; granularidade mensal, diária (e horária, paga).

**Previsão (forecast)**

**Detalhe:** ✔️ Até **3 meses** em granularidade diária e até **12 meses** em mensal, com intervalo de predição de 80%; sem histórico suficiente (conta nova), não gera previsão.

**Histórico**

**Detalhe:** ✔️ **13 meses** + o mês corrente.

**Relatórios salvos**

**Detalhe:** Modelos prontos (custo mensal por serviço, uso de RIs…) e customizados.

**Recomendações**

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
- **rightsizing:** Ajustar capacidade à necessidade observada. Reduzir demais pode prejudicar a aplicação; a recomendação precisa ser avaliada pelo uso real.

**Detalhe:** **Rightsizing** de EC2, **compra de RIs e Savings Plans** (com estimativa de economia).

**Relatórios de RI/SP**

**Antes de ler este trecho:**

- **RI:** Benefício e condições de reserva para configurações compatíveis. Não confunda desconto com qualquer garantia universal de capacidade.

**Detalhe:** **Utilização** (quanto do compromisso foi usado) e **cobertura** (quanto do uso está coberto).

**API**

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.

**Detalhe:** ✔️ Interface gráfica gratuita; a **API** custa **US$ 0,01 por requisição paginada**.

**Ativação**

**Detalhe:** Precisa ser **habilitado** no console (dados levam até 24 h para aparecer).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele analisa gastos; não bloqueia automaticamente a criação de recursos. Os dados não devem ser tratados como medição instantânea nem a previsão como garantia.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Cost Explorer:** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.
- **Budgets:** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.
- **CUR:** Relatório de custos e uso. Ele ajuda a analisar consumo registrado; é diferente de uma estimativa antes de criar recursos.

**Cost Explorer** (analisa o passado e prevê) × **Budgets** (alerta e age) × **Pricing Calculator** (estima **antes** de usar) × **CUR** (dados brutos mais detalhados).

## 4. Caso resolvido: ligando as peças

A escola compara dois meses e separa custos por serviço para investigar onde o gasto mudou.

**Aplicando a sequência à situação:**

**Etapa 1:** Selecione o período e a pergunta sobre custo ou uso que precisa responder.
**Etapa 2:** Agrupe ou filtre dados para identificar a parte do gasto relacionada à pergunta.
**Etapa 3:** Investigue a mudança nos recursos. Um aumento pode ter várias causas; a ferramenta mostra dados, não decide a ação sozinha.

**Resultado e responsabilidade:** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.

**Recursos envolvidos:** Relatórios, filtros, dimensões, grupos e previsões.

**Decisões que precisam ser tomadas:** Período, granularidade e visão autorizada.

**Outra situação comentada:** Descobrir serviço responsável pelo aumento: agrupar por serviço e investigar conta/região/tags.

**Por que não concluir mais do que isso:** Não é medidor instantâneo nem bloqueio de consumo; previsão não garante valor final

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Visualizar gastos dos últimos meses e prever o próximo."

**Resposta curta:** Cost Explorer.

**Pergunta:** "Onde ver recomendações de Savings Plans e RIs?"

**Resposta curta:** Cost Explorer.

**Pergunta:** "Verificar se as Reserved Instances estão sendo usadas."

**Resposta curta:** Relatório de utilização de RI no Cost Explorer.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
