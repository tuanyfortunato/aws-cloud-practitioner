# Planos de AWS Support

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Quando há uma dúvida ou problema, a empresa precisa saber que tipo de ajuda da AWS pode solicitar e em quais condições.

**Como este serviço ajuda?** Planos de suporte definem acesso a canais, orientação e recursos de atendimento conforme a oferta. A necessidade do negócio deve orientar a escolha.

**Exemplo do dia a dia:** Uma empresa com aplicação importante avalia quais recursos de suporte técnico e acompanhamento são necessários para sua operação.

**O que ele não resolve sozinho?** Ter suporte não transfere toda a operação da aplicação para a AWS. Tempo inicial de resposta não é promessa de tempo de resolução; nomes e condições devem ser conferidos no contexto indicado.

**Primeiras palavras para entender:**

- **Caso de suporte:** solicitação de ajuda.
- **Severidade:** impacto do problema.
- **Tempo de resposta:** prazo para início do atendimento conforme as condições.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Suporte · **Domínio:** 4 · **Escopo:** Conta (ou organização, nos planos novos) · **Tópico do guia:** [4.5 Planos de AWS Support](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)
>
> **Em uma frase:** níveis de suporte técnico da AWS — quanto mais alto, mais rápido o atendimento e mais acompanhamento proativo.
>
> **Escopo oficial:** ✅ No escopo (AWS Support — distinguir exemplos do guia e oferta comercial atual) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> Verificado em fontes oficiais em 04/10/2026 ([relatório](../../fontes/verificacao-fontes-oficiais-2026-10.md)).

> **Divergência entre fontes:** a [task 4.3 consultada](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) ainda cita Developer, Business e Enterprise On-Ramp. A página comercial mostra os planos abaixo. Não há aqui evidência para afirmar que todos os exemplos da prova foram substituídos. [Ver auditoria](../../docs/00-guia-do-exame/auditoria-conteudo-2026-10.md).

## 1. A sequência de funcionamento

**Passo 1.** Identifique a necessidade de ajuda e o impacto real do problema.

**Passo 2.** Confira a oferta aplicável e abra um caso elegível com informações suficientes para o atendimento.

**Passo 3.** Acompanhe investigação e ações. Primeira resposta, resolução e operação cotidiana da aplicação são responsabilidades distintas.

## 2. Recursos e opções, com significado

### 📌 Planos comerciais atuais (distinguir dos exemplos do guia)

> ✔️ Comparação completa verificada em 04/10/2026 nas páginas [plans](https://aws.amazon.com/premiumsupport/plans/) e [pricing](https://aws.amazon.com/premiumsupport/pricing/).

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **Trusted Advisor:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.
- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **workload:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.
- **TAM:** Gerente técnico de conta em ofertas de suporte que incluem esse papel. Atua no acompanhamento e orientação previstos; não substitui toda a equipe do cliente.
- **IEM:** Nome histórico de uma oferta de acompanhamento de eventos de infraestrutura. Leia o contexto e a oferta atual indicados na ficha.

| | **Basic** | **AWS Business Support+** | **AWS Enterprise Support** | **AWS Unified Operations** |
|---|---|---|---|---|
| Preço mínimo | Incluído (grátis) | **US$ 29/mês por conta** ou % do uso (9 → 7 → 5 → 3%), o maior | **US$ 5.000/mês** ou % (10 → 7 → 5 → 3%), o maior | **US$ 50.000/mês** ou % (10 → 6 → 5%), o maior |
| Cobrança | — | **Por conta** | Soma das contas inscritas | Soma das contas inscritas |
| Compromisso mínimo | — | 30 dias | 30 dias | **90 dias** |
| Canais | Customer service 24/7 (conta e faturamento), docs, whitepapers, re:Post | **Telefone, web, chat e e-mail 24/7**, Slack; casos e contatos ilimitados | Igual | Igual |
| **Caso crítico** | — | **< 30 min** | **< 15 min** | **< 5 min** |
| Produção fora do ar / prejudicada | — | < 1 h / < 4 h | < 1 h / < 4 h | < 1 h / < 4 h |
| Sistema prejudicado / orientação geral | — | < 12 h / < 24 h | < 12 h / < 24 h | < 12 h / < 24 h |
| Trusted Advisor | **Core checks** | **Completo** + API | Completo + API + **TA Priority** | Completo + API + **TA Priority** |
| AWS Support API / AWS Health API | ❌ / Health básico | ✅ / ✅ | ✅ / ✅ | ✅ / ✅ |
| TAM | ❌ | ❌ | **Designado** | Designado + especialistas de domínio + Incident Management Engineers |
| Faturamento | — | Billing 24/7 | **Billing concierge** | Especialista de billing designado |
| AWS Countdown (antigo IEM) | — | Countdown Premium pago | Countdown Premium pago | **Incluído** |
| Revisões | — | Orientação contextual | Well-Architected, revisão de segurança, plano estratégico | Contínuas + Critical Workload Review |
| Monitoramento 24/7 pela AWS | — | — | — | ✅ |
| Security Incident Response | — | Pago à parte | **Incluído** | Incluído |
| Incident Detection and Response | — | — | Pago à parte | **Incluído** |
| IA (créditos de DevOps Agent) | — | 30% | 75% | 100% |

⚠️ US$ 29 é o preço de entrada do **Business Support+** (novo) e era o do **Developer** (clássico): confira o nome do plano.

⚠️ 30 min: **Business Support+** (novo) ou **Enterprise On-Ramp** (clássico). 15 min + TAM designado: **Enterprise** (nos dois modelos). 5 min + monitoramento 24/7: **Unified Operations**.

📌 **Menor plano com todas as verificações do Trusted Advisor e acesso à API:** Business Support+. **Menor plano com TA Priority e TAM designado:** Enterprise.

✔️ O **Enterprise** inclui **workshops conduzidos pelo TAM** e **AWS GameDays** (e exercícios de segurança). Assinatura do Skill Builder incluída: não encontrada.

### Modelo clássico (válido até 01/01/2027)

Developer, Business e Enterprise On-Ramp **encerram em 01/01/2027** (clientes On-Ramp migram automaticamente para

Enterprise em 2026; os três seguem no GovCloud). Ainda podem aparecer em questões antigas.

**Antes de ler este trecho:**

- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.

| | **Basic** | **Developer** | **Business** | **Enterprise On-Ramp** | **Enterprise** |
|---|---|---|---|---|---|
| Preço histórico | Grátis | US$ 29/mês | US$ 100/mês | US$ 5.500/mês | US$ 15.000/mês (hoje US$ 5.000) |
| Suporte técnico | ❌ | E-mail em **horário comercial** | **24/7 telefone, chat, e-mail** | 24/7 | 24/7 |
| Orientação geral | — | < 24 h úteis | < 24 h | < 24 h | < 24 h |
| Sistema prejudicado | — | < 12 h úteis | < 12 h | < 12 h | < 12 h |
| Produção prejudicada | — | — | < 4 h | < 4 h | < 4 h |
| **Produção fora do ar** | — | — | **< 1 h** | < 1 h | < 1 h |
| **Sistema crítico fora do ar** | — | — | — | **< 30 min** | **< 15 min** |
| Trusted Advisor | Core checks | Core checks | **Todos** + API | Todos + API | Todos + API + Priority |
| TAM | — | — | — | **Pool de TAMs** | **TAM designado** |
| Concierge (faturamento/conta) | — | — | — | ✅ | ✅ |
| Eventos de grande escala | — | — | Pago à parte | 1 engajamento **AWS Countdown** por ano | ✅ |

Os **tempos de resposta** clássicos estão confirmados nas páginas oficiais; os **preços** de Developer, Business e On-Ramp não aparecem mais (valores históricos).

### Recursos ligados ao suporte (também na task 4.3)

**AWS Trusted Advisor:** verificações completas e API a partir dos planos pagos superiores ([ficha](../gerenciamento/trusted-advisor.md)).

**Antes de ler este trecho:**

- **AWS Health Dashboard / Health Dashboard:** AWS Health apresenta eventos sobre a saúde dos serviços e informações relevantes aos recursos da conta, conforme a visão consultada.

**AWS Health Dashboard** e **AWS Health API** ([ficha](../gerenciamento/health-dashboard.md)).

**TAM (Technical Account Manager):** consultor técnico proativo.

**Concierge Support Team:** especialistas em faturamento e conta.

**AWS Support Center:** onde se abrem e acompanham os casos de suporte (no console). No Basic, só casos de conta e faturamento.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.

**Quem muda o plano de suporte:** 🔄 deixou de ser tarefa exclusiva do root (a lista oficial atual não a inclui); uma identidade IAM com as permissões necessárias pode fazê-lo.

**Antes de ler este trecho:**

- **APN:** Rede de parceiros AWS. Parceiros oferecem serviços e soluções conforme seus próprios contratos e competências.

Demais recursos (Trust and Safety, APN, Marketplace, Professional Services, Prescriptive Guidance, Knowledge Center, re:Post): [recursos de ajuda e parceiros](recursos-de-ajuda-e-parceiros.md).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ter suporte não transfere toda a operação da aplicação para a AWS. Tempo inicial de resposta não é promessa de tempo de resolução; nomes e condições devem ser conferidos no contexto indicado.

## 4. Caso resolvido: ligando as peças

Uma empresa com aplicação importante avalia quais recursos de suporte técnico e acompanhamento são necessários para sua operação.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique a necessidade de ajuda e o impacto real do problema.
**Etapa 2:** Confira a oferta aplicável e abra um caso elegível com informações suficientes para o atendimento.
**Etapa 3:** Acompanhe investigação e ações. Primeira resposta, resolução e operação cotidiana da aplicação são responsabilidades distintas.

**Resultado e responsabilidade:** Planos de suporte definem acesso a canais, orientação e recursos de atendimento conforme a oferta. A necessidade do negócio deve orientar a escolha.

**Recursos envolvidos:** Plano, Support Center, casos, severidade, canais e orientação.

**Decisões que precisam ser tomadas:** Plano aplicável, impacto real e informações do caso.

**Outra situação comentada:** Aprenda ambos: Business clássico não se confunde com Business Support+; escolha pelo nome/contexto do enunciado.

**Por que não concluir mais do que isso:** Primeira resposta não é resolução; guia da prova e página comercial citam modelos diferentes

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Plano gratuito sem suporte técnico."

**Resposta curta:** Basic.

**Pergunta:** "Plano pago de entrada, a partir de US$ 29 por conta, com resposta de 30 min para casos críticos."

**Resposta curta:** Business Support+.

**Fundamento explicado no capítulo:** 📌 **Menor plano com todas as verificações do Trusted Advisor e acesso à API:** Business Support+. **Menor plano com TA Priority e TAM designado:** Enterprise.

**Pergunta:** "TAM designado e resposta em menos de 15 min para sistema crítico."

**Resposta curta:** Enterprise.

**Fundamento explicado no capítulo:** 📌 **Menor plano com todas as verificações do Trusted Advisor e acesso à API:** Business Support+. **Menor plano com TA Priority e TAM designado:** Enterprise.

**Pergunta:** "Resposta em 5 minutos para incidentes críticos."

**Resposta curta:** Unified Operations.

**Pergunta:** (Clássico) "Mais barato com suporte técnico 24/7 por telefone e < 1 h para produção fora do ar."

**Resposta curta:** Business.

**Pergunta:** (Clássico) "Pool de TAMs e 30 min."

**Resposta curta:** Enterprise On-Ramp.

**Pergunta:** (Clássico) "Ambiente de testes, ajuda ocasional por e-mail em horário comercial."

**Resposta curta:** Developer.

**Pergunta:** "Quem pode mudar o plano de suporte?"

**Resposta curta:** Não é mais exclusivo do root (lista oficial de 10/2026).

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Planos de suporte](https://aws.amazon.com/premiumsupport/plans/) · [Preços do suporte](https://aws.amazon.com/premiumsupport/pricing/) · [Anúncio da transformação do suporte (12/2025)](https://aws.amazon.com/about-aws/whats-new/2025/12/aws-support-transformation-ai-powered-operations)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
