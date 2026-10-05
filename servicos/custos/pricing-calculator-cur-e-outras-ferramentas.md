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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.


**Passo 1.** Antes do uso, estime a capacidade e as condições previstas na calculadora.

**Passo 2.** Depois do uso, analise registros e relatórios para entender o consumo ocorrido.

**Passo 3.** Compare hipóteses e realidade. Estimativa e relatório respondem perguntas diferentes e não são garantias de uma fatura fixa.

## 2. Recursos e opções, com significado

### Tabela de ferramentas

**AWS Pricing Calculator**

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **CSV:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
- **PDF:** Formato de documento. Um serviço de extração analisa conteúdo compatível; guardar um PDF num bucket não executa automaticamente essa análise.


**Para que serve:** **Estimar** custos **antes** de criar recursos

**Detalhes:** Web, **gratuita**, sem conta; estimativas compartilháveis por link e exportáveis (CSV/PDF); versão no console de Billing considera seus descontos

**Billing and Cost Management console**

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.


**Para que serve:** Fatura do mês, pagamentos, créditos, perfis de pagamento

**Detalhes:** Ponto de partida do faturamento; root pode liberar acesso ao Billing para usuários IAM

**Cost and Usage Report (CUR) / Data Exports**

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.
- **QuickSight:** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis.
- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **CUR:** Relatório de custos e uso. Ele ajuda a analisar consumo registrado; é diferente de uma estimativa antes de criar recursos.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.
- **FOCUS:** Especificação de organização de dados de custos e uso. Padronizar dados ajuda a analisá-los, mas não reduz o gasto automaticamente.


**Para que serve:** Dados **mais granulares** possíveis (hora a hora, por recurso, com tags)

**Detalhes:** ✔️ Configurado pelo **AWS Data Exports**: CUR 2.0 (recomendado) e **FOCUS 1.2/1.0**; o CUR legado continua disponível. Entregue no **S3**; analisados com **Athena**, QuickSight, Redshift

**Cost Anomaly Detection**

**Antes de ler este trecho:**

- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **tag:** Par de nome e valor associado a recursos ou objetos compatíveis. Ajuda organização; usos em permissões e cobrança dependem de configuração e suporte.


**Para que serve:** Detecta **gastos anormais** com ML

**Detalhes:** Monitores por serviço/conta/tag; alertas com causa raiz provável; ✔️ **gratuito**

**Cost Optimization Hub**

**Antes de ler este trecho:**

- **rightsizing:** Ajustar capacidade à necessidade observada. Reduzir demais pode prejudicar a aplicação; a recomendação precisa ser avaliada pelo uso real.


**Para que serve:** Consolida recomendações de economia (rightsizing, RIs/SPs, ociosos) num lugar

**Detalhes:** Prioriza por economia estimada

**Cost allocation tags**


**Para que serve:** **Ratear custos** por projeto, time, centro de custo

**Detalhes:** Tags do usuário ou geradas pela AWS; precisam ser **ativadas** no Billing para aparecer nos relatórios

**Cost Categories**

**Antes de ler este trecho:**

- **Cost Explorer:** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.
- **Budgets:** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.


**Para que serve:** Regras que agrupam custos (ex.: "Marketing" = contas X e Y + tag Z)

**Detalhes:** Usadas em Cost Explorer, Budgets, CUR

**Consolidated billing (Organizations)**

**Antes de ler este trecho:**

- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.


**Para que serve:** Fatura única, descontos por volume, compartilhamento de RIs/SPs

**Detalhes:** Sem custo extra

**AWS Billing Conductor ❌ fora do escopo**


**Para que serve:** Faturamento **personalizado** (pro forma)

**Detalhes:** Revendedores e empresas que refaturam clientes/áreas

**Savings Plans / Reservations (console)**

**Antes de ler este trecho:**

- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.


**Para que serve:** Comprar, acompanhar utilização e cobertura

**Detalhes:** Recomendações no Cost Explorer

**Free Tier usage alerts**


**Para que serve:** Avisa quando o uso se aproxima dos limites gratuitos

**Detalhes:** Ativado por padrão

**AWS Customer Carbon Footprint Tool**


**Para que serve:** Estimativa de **emissões de carbono** do seu uso

**Detalhes:** Gratuita, no Billing; pilar Sustentabilidade

**AWS Price List API**

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.


**Para que serve:** Preços via API

**Detalhes:** Automação

**AWS Marketplace**

**Antes de ler este trecho:**

- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.


**Para que serve:** Comprar software de terceiros cobrado na fatura AWS

**Detalhes:** AMIs, SaaS, contêineres, dados, serviços profissionais

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Estimativa não é uma proposta de preço garantido nem a fatura futura. Relatório de gasto real também não escolhe sozinho a arquitetura mais econômica.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

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

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A equipe precisa estimar um projeto antes de criar recursos e, depois, pode precisar entender a cobrança em mais detalhe.

**2. O que a solução fornece?**

Pricing Calculator estima custos com entradas fornecidas por você. Relatórios de custos e uso ajudam a analisar consumo ocorrido; outras ferramentas atendem organização e administração da cobrança.

**3. Que conclusão seria incorreta?**

Estimativa não é uma proposta de preço garantido nem a fatura futura. Relatório de gasto real também não escolhe sozinho a arquitetura mais econômica.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Estimar o custo de uma arquitetura antes de criá-la."

**Resposta curta:** Pricing Calculator.


**Fundamento explicado no capítulo:** "Estimar o custo de uma arquitetura antes de criá-la." → Pricing Calculator.

**Pergunta:** "Relatório mais detalhado de custo e uso, por hora e recurso."

**Resposta curta:** Cost and Usage Report.


**Fundamento explicado no capítulo:** "Relatório mais detalhado de custo e uso, por hora e recurso." → Cost and Usage Report.

**Pergunta:** "Ser avisado de um gasto anormal."

**Resposta curta:** Cost Anomaly Detection.


**Fundamento explicado no capítulo:** "Ser avisado de um gasto anormal." → Cost Anomaly Detection.

**Pergunta:** "Separar custos por projeto ou departamento."

**Resposta curta:** Cost allocation tags (ativadas no Billing).


**Fundamento explicado no capítulo:** "Separar custos por projeto ou departamento." → Cost allocation tags (ativadas no Billing).

**Pergunta:** "Acompanhar a pegada de carbono do uso da AWS."

**Resposta curta:** Customer Carbon Footprint Tool.


**Fundamento explicado no capítulo:** "Acompanhar a pegada de carbono do uso da AWS." → Customer Carbon Footprint Tool.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Pricing Calculator](https://calculator.aws/) · [Data Exports / CUR](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) · [Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
