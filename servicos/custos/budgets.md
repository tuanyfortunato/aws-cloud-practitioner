# AWS Budgets

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa quer acompanhar um limite planejado de custo ou uso e receber avisos antes de perder o controle do orçamento.

**Como este serviço ajuda?** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.

**Exemplo do dia a dia:** A escola configura um orçamento mensal e um aviso para determinados níveis de gasto observado ou previsto.

**O que ele não resolve sozinho?** Um orçamento não é, por padrão, um teto rígido que interrompe todo consumo. Alertas e ações não substituem controle de acesso e acompanhamento dos recursos.

**Primeiras palavras para entender:**

- **Orçamento:** meta de gasto ou uso.
- **Limite de aviso:** condição para notificação.
- **Ação:** operação configurada para determinada condição.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gestão de custos · **Domínio:** 4 · **Escopo:** Conta / organização · **Tópico do guia:** [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)
>
> **Em uma frase:** define orçamentos de custo e uso e **alerta** (ou **age**) quando o valor real ou **previsto** ultrapassa o limite.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina a meta e quais condições devem gerar um aviso ou ação compatível.

**Passo 2.** Configure destinatários e acompanhe valores observados ou previstos conforme a ferramenta.

**Passo 3.** Ao receber um aviso, investigue e realize a ação pertinente. Um orçamento não é, por padrão, interrupção rígida de todo consumo.

## 2. Recursos e opções, com significado

### Tipos de orçamento

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.

| Tipo | Monitora |
|---|---|
| **Cost budget** | Valor gasto (US$) |
| **Usage budget** | Quantidade de uso (horas de EC2, GB de S3) |
| **Savings Plans budget** | Utilização ou cobertura dos Savings Plans |
| **Reservation budget** | Utilização ou cobertura das RIs |

### Configurações

**Antes de ler este trecho:**

- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **Budgets:** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.
- **SCP:** Política de controle de serviços usada na organização para limitar permissões disponíveis em contas às quais se aplica. Ela não concede acesso ao usuário sozinha.
- **tag:** Par de nome e valor associado a recursos ou objetos compatíveis. Ajuda organização; usos em permissões e cobrança dependem de configuração e suporte.

| Item | Detalhe |
|---|---|
| **Período** | Diário, mensal, trimestral, anual; valor fixo ou planejado mês a mês. |
| **Filtros** | Serviço, conta, região, tag, cost category… |
| **Alertas** | Por limite **real** ou **previsto** (forecasted), em % ou valor; via **e-mail**, **SNS** ou Amazon Q Developer em chat (Slack/Teams). |
| **Budget Actions** | Ações automáticas ao atingir o limite: aplicar **política IAM**, aplicar **SCP**, **parar instâncias EC2/RDS** — com ou sem aprovação. |
| **Templates** | Orçamento de "gasto zero" e mensal fixo para começar (útil para quem estuda no Free Tier). |
| **Budgets reports** | Relatórios periódicos por e-mail. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Um orçamento não é, por padrão, um teto rígido que interrompe todo consumo. Alertas e ações não substituem controle de acesso e acompanhamento dos recursos.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **Cost Explorer:** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.
- **alarme:** Condição acompanhada sobre dados de monitoramento. Uma mudança de estado pode gerar ações configuradas; o alarme não diagnostica todo problema sozinho.

**Budgets** (alerta/ação) × **Cost Explorer** (análise) × **Cost Anomaly Detection** (gasto **fora do padrão**, sem limite definido) × **CloudWatch billing alarm** (alarme simples sobre a cobrança estimada).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Orçamentos de monitoramento são gratuitos; os **dois primeiros** orçamentos com **actions** são grátis por mês e os demais custam **US$ 0,10/dia**; cada relatório do Budgets Reports custa US$ 0,01 (🧊).

## 5. Caso resolvido: ligando as peças

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

A escola quer acompanhar sua meta mensal de custo. O objetivo é receber sinal de desvio e agir a tempo, não presumir que a AWS nunca cobrará acima de um valor informado.

A equipe define o orçamento, condições de notificação e destinatários. Quando recebe um aviso, investiga a parte do consumo que aumentou e decide quais mudanças atendem à aplicação. Ações compatíveis podem ser configuradas conforme requisitos e permissões.

O orçamento, por padrão, não funciona como um corte universal e instantâneo de todos os serviços. Cost Explorer ajuda a analisar gastos; a calculadora estima antes do uso. Meta, análise e estimativa respondem perguntas diferentes.

**Recursos envolvidos:** Orçamento, thresholds, notificações e actions opcionais.

**Decisões que precisam ser tomadas:** Valor/meta, período, destinatários e permissões de ação.

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.

**Outra situação comentada:** Alertar em 80% do orçamento: Budgets; desligar qualquer recurso não é comportamento automático universal.

**Por que não concluir mais do que isso:** Não garante teto rígido da conta: atualização e ações têm latência e alcance limitado

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Receber alerta quando o gasto previsto passar do orçamento."

**Resposta curta:** Budgets.

**Pergunta:** "Parar instâncias automaticamente se o orçamento estourar."

**Resposta curta:** Budget Actions.

**Pergunta:** "Alerta quando as RIs forem subutilizadas."

**Resposta curta:** Reservation budget.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
