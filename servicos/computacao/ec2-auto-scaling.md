# Amazon EC2 Auto Scaling

> **Categoria:** Computação · **Domínio:** 1 (elasticidade) e 3 · **Escopo:** Regional (grupo distribuído entre AZs) · **Tópico do guia:** [3.4 Escalabilidade e balanceamento](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)
>
> **Em uma frase:** aumenta e reduz automaticamente o número de instâncias EC2 conforme a demanda e substitui as que falham.
>
> **Escopo oficial:** ✅ No escopo (AWS Auto Scaling) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é como um **gerente que chama funcionários extras no horário de pico** e dispensa quando o movimento cai — e substitui quem faltar.

- ✅ **Escolha quando:** a carga varia e você quer **aumentar e reduzir instâncias automaticamente**, ou garantir um número mínimo de instâncias saudáveis.
- 🚫 **Não é a resposta quando:** precisa **distribuir o tráfego** entre as instâncias → [Elastic Load Balancing](elastic-load-balancing.md); quer uma instância **maior** (escala vertical) → trocar o tipo da [EC2](ec2.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "elasticidade", "escalar automaticamente", "pico toda sexta", "manter a CPU em 50%", "substituir instâncias com falha".
<!-- didatico:fim -->

## Para que serve

- **Elasticidade:** acompanhar picos e vales de tráfego sem intervenção manual.
- **Alta disponibilidade:** manter um número mínimo de instâncias saudáveis distribuídas em várias AZs.
- **Otimização de custos:** não pagar por capacidade ociosa.

## Conceitos e componentes

| Componente | O que é |
|---|---|
| **Auto Scaling Group (ASG)** | Conjunto lógico de instâncias com capacidade **mínima**, **desejada** e **máxima**. |
| **Launch template** | Configuração das instâncias (AMI, tipo, SG, key pair, user data). Substitui as antigas *launch configurations*. |
| **Health check** | EC2 (status da instância) e/ou **ELB** (health check do load balancer). Instância não saudável é substituída. |
| **Scaling policy** | Regra que muda a capacidade desejada. |
| **Lifecycle hooks** | Pausam a instância ao entrar/sair do grupo para rodar ações (ex.: instalar agente, drenar logs). |
| **Warm pools** | Instâncias pré-inicializadas para escalar mais rápido. |
| **Instance refresh** | Substitui gradualmente as instâncias para aplicar nova AMI/template. |

## Configurações e opções importantes

| Política | Como funciona | Exemplo |
|---|---|---|
| **Target tracking** | Mantém uma métrica num alvo | CPU média em 50% |
| **Step scaling** | Ajustes em degraus conforme o tamanho do desvio do alarme | +2 instâncias se CPU > 70%, +4 se > 90% |
| **Simple scaling** | Um ajuste por alarme, com cooldown | Legado |
| **Scheduled** | Capacidade em horários conhecidos | Pico toda sexta às 18h |
| **Predictive** | ML prevê a demanda com base no histórico e escala antes | Padrões diários/semanais |

- **Mixed instances policy:** combina On-Demand e **Spot** e vários tipos de instância no mesmo grupo.
- **Termination policy:** define qual instância sai primeiro (padrão: equilibra AZs, depois a com template mais antigo…).
- **Rebalanceamento entre AZs:** o ASG tenta manter o mesmo número de instâncias por AZ.

## Limites e números

- 🧊 Quotas de ASGs e templates por região não caem.
- 📌 Monitoramento detalhado (1 min) deixa o escalonamento mais rápido.

## Cobrança

- **Sem custo próprio:** paga-se as instâncias EC2 e alarmes/métricas do CloudWatch usados.

## Segurança e responsabilidade compartilhada

- **AWS:** executa o serviço de escalonamento.
- **Cliente:** define políticas, AMIs atualizadas, IAM, security groups.

## ⚠️ Pegadinhas e não confundir

- **EC2 Auto Scaling** (instâncias) × **AWS Auto Scaling** (planos de escalonamento para vários recursos: EC2, ECS, DynamoDB, Aurora).
- Auto Scaling **não distribui tráfego** — quem faz isso é o [ELB](elastic-load-balancing.md). Juntos dão HA + elasticidade.
- Escalar **horizontalmente** (scale out) é o que o ASG faz; aumentar o tamanho da instância é **vertical** (scale up) e exige parar a instância.

## ❓ Perguntas típicas

- "Ajustar automaticamente o número de instâncias à demanda." → EC2 Auto Scaling.
- "A loja tem pico toda sexta às 18h." → Scheduled scaling.
- "Manter a CPU média em 50%." → Target tracking.
- "Escalar antes do pico com base no histórico." → Predictive scaling.
- "Substituir automaticamente instâncias com falha." → ASG com health checks.
- "O Auto Scaling tem custo?" → Não; paga-se só os recursos.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Grupo, launch template, mínimo, máximo, capacidade desejada e políticas |
| **O que você decide/configura?** | Número de instâncias e critérios de saúde/escala |
| **Em que ordem as coisas acontecem?** | O grupo compara saúde e demanda com a configuração e ajusta instâncias |
| **O que pode fazer, e em que condição?** | Pode recuperar capacidade e distribuir instâncias entre AZs configuradas |
| **O que não pode presumir?** | Não remove gargalos de aplicação/banco nem copia arquivos locais entre instâncias |

**Caso comentado:** Pico previsível: política agendada; demanda variável: política dinâmica com métrica adequada.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
