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

| Tipo | Monitora |
|---|---|
| **Cost budget** | Valor gasto (US$) |
| **Usage budget** | Quantidade de uso (horas de EC2, GB de S3) |
| **Savings Plans budget** | Utilização ou cobertura dos Savings Plans |
| **Reservation budget** | Utilização ou cobertura das RIs |

### Configurações

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

**Budgets** (alerta/ação) × **Cost Explorer** (análise) × **Cost Anomaly Detection** (gasto **fora do padrão**, sem limite definido) × **CloudWatch billing alarm** (alarme simples sobre a cobrança estimada).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Orçamentos de monitoramento são gratuitos; os **dois primeiros** orçamentos com **actions** são grátis por mês e os demais custam **US$ 0,10/dia**; cada relatório do Budgets Reports custa US$ 0,01 (🧊).

## 5. Caso resolvido: ligando as peças

A escola quer acompanhar sua meta mensal de custo. O objetivo é receber sinal de desvio e agir a tempo, não presumir que a AWS nunca cobrará acima de um valor informado.

A equipe define o orçamento, condições de notificação e destinatários. Quando recebe um aviso, investiga a parte do consumo que aumentou e decide quais mudanças atendem à aplicação. Ações compatíveis podem ser configuradas conforme requisitos e permissões.

O orçamento, por padrão, não funciona como um corte universal e instantâneo de todos os serviços. Cost Explorer ajuda a analisar gastos; a calculadora estima antes do uso. Meta, análise e estimativa respondem perguntas diferentes.

**Recursos envolvidos:** Orçamento, thresholds, notificações e actions opcionais.

**Decisões que precisam ser tomadas:** Valor/meta, período, destinatários e permissões de ação.

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
