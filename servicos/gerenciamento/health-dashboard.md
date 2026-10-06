# AWS Health Dashboard

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um problema da AWS ou uma manutenção pode afetar recursos. A equipe precisa distinguir isso de um erro exclusivo de sua aplicação.

**Como este serviço ajuda?** AWS Health apresenta eventos sobre a saúde dos serviços e informações relevantes aos recursos da conta, conforme a visão consultada.

**Exemplo do dia a dia:** A equipe consulta um evento de manutenção que afeta seu ambiente e planeja a ação indicada para os recursos envolvidos.

**O que ele não resolve sozinho?** A visão pública não mostra todos os detalhes específicos de uma conta. AWS Health também não substitui métricas e logs da aplicação.

**Primeiras palavras para entender:**

- **Evento de saúde:** aviso sobre condição ou mudança operacional.
- **Visão pública:** estado geral dos serviços.
- **Visão da conta:** informações associadas ao ambiente do cliente.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / operações · **Domínio:** 2 e 3 · **Escopo:** Global · **Gratuito** · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)
>
> **Em uma frase:** mostra o status dos serviços AWS e, principalmente, os eventos que afetam **os seus** recursos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Consulte a visão geral ou específica da conta conforme a investigação.

**Passo 2.** Leia os eventos e identifique os recursos e prazos relevantes.

**Passo 3.** Execute as ações pertinentes e acompanhe a aplicação com suas próprias ferramentas de observação.

## 2. Recursos e opções, com significado

### Duas visões

| Visão | O que mostra | Acesso |
|---|---|---|
| **Service health** | Status **público** de todos os serviços em todas as regiões | Sem login |
| **Your account health** | Eventos **personalizados**: manutenções programadas (ex.: reinício de instância por hardware), problemas que afetam seus recursos, avisos (fim de versões, certificados) — com **orientação de correção** | Console, para todos os clientes |

### Integrações

**AWS Health API:** acesso programático — exige plano **Business ou superior**.

**EventBridge:** automatizar respostas a eventos (ex.: notificar no Slack, mover cargas).

**Organizational view:** eventos de todas as contas da organização.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

A visão pública não mostra todos os detalhes específicos de uma conta. AWS Health também não substitui métricas e logs da aplicação.

### ⚠️ Não confundir

Health Dashboard (eventos **da AWS** que afetam você) × CloudWatch (métricas **dos seus** recursos) × Trusted Advisor (recomendações).

## 4. Caso resolvido: ligando as peças

A equipe consulta um evento de manutenção que afeta seu ambiente e planeja a ação indicada para os recursos envolvidos.

**Aplicando a sequência à situação:**

**Etapa 1:** Consulte a visão geral ou específica da conta conforme a investigação.
**Etapa 2:** Leia os eventos e identifique os recursos e prazos relevantes.
**Etapa 3:** Execute as ações pertinentes e acompanhe a aplicação com suas próprias ferramentas de observação.

**Resultado e responsabilidade:** AWS Health apresenta eventos sobre a saúde dos serviços e informações relevantes aos recursos da conta, conforme a visão consultada.

**Recursos envolvidos:** Eventos públicos e eventos específicos da conta.

**Decisões que precisam ser tomadas:** Conta, região, serviço e integrações de evento.

**Outra situação comentada:** Manutenção de recurso específico: Health; erro interno do app: logs/métricas da aplicação.

**Por que não concluir mais do que isso:** Ausência de evento AWS não prova que o código da aplicação está saudável

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Ver eventos de manutenção da AWS que afetam minhas instâncias."

**Resposta curta:** AWS Health Dashboard.

**Pergunta:** "Automatizar reação a um evento de manutenção programada."

**Resposta curta:** Health + EventBridge.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
