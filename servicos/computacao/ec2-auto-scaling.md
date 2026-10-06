# Amazon EC2 Auto Scaling

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma loja tem poucos visitantes de madrugada e muitos durante uma promoção. Manter sempre a mesma quantidade de máquinas pode desperdiçar dinheiro ou deixar o site lento.

**Como este serviço ajuda?** O EC2 Auto Scaling aumenta ou diminui a quantidade de máquinas EC2 seguindo regras que você configura. Ele também pode substituir máquinas consideradas sem saúde pelo grupo.

**Exemplo do dia a dia:** A loja configura um grupo que adiciona máquinas quando a demanda aumenta e reduz a quantidade depois da promoção. O programa precisa estar preparado para funcionar em várias máquinas.

**O que ele não resolve sozinho?** Ele gerencia a quantidade de máquinas; não distribui sozinho cada pedido dos visitantes entre elas. Essa distribuição costuma ser feita por um balanceador.

**Primeiras palavras para entender:**

- **Escalar:** ajustar capacidade.
- **Grupo:** conjunto de máquinas administrado em conjunto.
- **Política:** regra para decidir quando ajustar esse conjunto.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação · **Domínio:** 1 (elasticidade) e 3 · **Escopo:** Regional (grupo distribuído entre AZs) · **Tópico do guia:** [3.4 Escalabilidade e balanceamento](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)
>
> **Em uma frase:** aumenta e reduz automaticamente o número de instâncias EC2 conforme a demanda e substitui as que falham.
>
> **Escopo oficial:** ✅ No escopo (AWS Auto Scaling) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina a configuração das máquinas e a quantidade mínima, desejada e máxima do grupo.

**Passo 2.** Escolha condições que ajustam a quantidade, como uma métrica de utilização. O grupo cria ou remove máquinas dentro desses limites.

**Passo 3.** Observe se a capacidade acompanha a demanda. A aplicação deve funcionar com cópias que podem ser substituídas.

## 2. Recursos e opções, com significado

### Para que serve

**Elasticidade:** acompanhar picos e vales de tráfego sem intervenção manual.

**Alta disponibilidade:** manter um número mínimo de instâncias saudáveis distribuídas em várias AZs.

**Otimização de custos:** não pagar por capacidade ociosa.

### Conceitos e componentes

**Auto Scaling Group (ASG)**

**O que é:** Conjunto lógico de instâncias com capacidade **mínima**, **desejada** e **máxima**.

**Launch template**

**O que é:** Configuração das instâncias (AMI, tipo, SG, key pair, user data). Substitui as antigas *launch configurations*.

**Health check**

**O que é:** EC2 (status da instância) e/ou **ELB** (health check do load balancer). Instância não saudável é substituída.

**Scaling policy**

**O que é:** Regra que muda a capacidade desejada.

**Lifecycle hooks**

**O que é:** Pausam a instância ao entrar/sair do grupo para rodar ações (ex.: instalar agente, drenar logs).

**Warm pools**

**O que é:** Instâncias pré-inicializadas para escalar mais rápido.

**Instance refresh**

**O que é:** Substitui gradualmente as instâncias para aplicar nova AMI/template.

### Configurações e opções importantes

| Política | Como funciona | Exemplo |
|---|---|---|
| **Target tracking** | Mantém uma métrica num alvo | CPU média em 50% |
| **Step scaling** | Ajustes em degraus conforme o tamanho do desvio do alarme | +2 instâncias se CPU > 70%, +4 se > 90% |
| **Simple scaling** | Um ajuste por alarme, com cooldown | Legado |
| **Scheduled** | Capacidade em horários conhecidos | Pico toda sexta às 18h |
| **Predictive** | ML prevê a demanda com base no histórico e escala antes | Padrões diários/semanais |

**Mixed instances policy:** combina On-Demand e **Spot** e vários tipos de instância no mesmo grupo.

**Termination policy:** define qual instância sai primeiro (padrão: equilibra AZs, depois a com template mais antigo…).

**Rebalanceamento entre AZs:** o ASG tenta manter o mesmo número de instâncias por AZ.

### Limites e números

🧊 Quotas de ASGs e templates por região não caem.

📌 Monitoramento detalhado (1 min) deixa o escalonamento mais rápido.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele gerencia a quantidade de máquinas; não distribui sozinho cada pedido dos visitantes entre elas. Essa distribuição costuma ser feita por um balanceador.

### ⚠️ Pegadinhas e não confundir

**EC2 Auto Scaling** (instâncias) × **AWS Auto Scaling** (planos de escalonamento para vários recursos: EC2, ECS, DynamoDB, Aurora).

Auto Scaling **não distribui tráfego** — quem faz isso é o [ELB](elastic-load-balancing.md). Juntos dão HA + elasticidade.

Escalar **horizontalmente** (scale out) é o que o ASG faz; aumentar o tamanho da instância é **vertical** (scale up) e exige parar a instância.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Sem custo próprio:** paga-se as instâncias EC2 e alarmes/métricas do CloudWatch usados.

### Segurança e responsabilidade compartilhada

**AWS:** executa o serviço de escalonamento.

**Cliente:** define políticas, AMIs atualizadas, IAM, security groups.

## 5. Caso resolvido: ligando as peças

A loja configura um grupo que adiciona máquinas quando a demanda aumenta e reduz a quantidade depois da promoção. O programa precisa estar preparado para funcionar em várias máquinas.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina a configuração das máquinas e a quantidade mínima, desejada e máxima do grupo.
**Etapa 2:** Escolha condições que ajustam a quantidade, como uma métrica de utilização. O grupo cria ou remove máquinas dentro desses limites.
**Etapa 3:** Observe se a capacidade acompanha a demanda. A aplicação deve funcionar com cópias que podem ser substituídas.

**Resultado e responsabilidade:** O EC2 Auto Scaling aumenta ou diminui a quantidade de máquinas EC2 seguindo regras que você configura. Ele também pode substituir máquinas consideradas sem saúde pelo grupo.

**Recursos envolvidos:** Grupo, launch template, mínimo, máximo, capacidade desejada e políticas.

**Decisões que precisam ser tomadas:** Número de instâncias e critérios de saúde/escala.

**Outra situação comentada:** Pico previsível: política agendada; demanda variável: política dinâmica com métrica adequada.

**Por que não concluir mais do que isso:** Não remove gargalos de aplicação/banco nem copia arquivos locais entre instâncias

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Ajustar automaticamente o número de instâncias à demanda."

**Resposta curta:** EC2 Auto Scaling.

**Pergunta:** "A loja tem pico toda sexta às 18h."

**Resposta curta:** Scheduled scaling.

**Pergunta:** "Manter a CPU média em 50%."

**Resposta curta:** Target tracking.

**Pergunta:** "Escalar antes do pico com base no histórico."

**Resposta curta:** Predictive scaling.

**Pergunta:** "Substituir automaticamente instâncias com falha."

**Resposta curta:** ASG com health checks.

**Pergunta:** "O Auto Scaling tem custo?"

**Resposta curta:** Não; paga-se só os recursos.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
