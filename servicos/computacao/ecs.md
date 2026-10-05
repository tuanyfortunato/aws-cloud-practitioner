# Amazon ECS (Elastic Container Service)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação empacotada precisa funcionar em várias máquinas, reiniciar quando falha e manter a quantidade desejada de cópias. Fazer isso manualmente é trabalhoso.

**Como este serviço ajuda?** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências. Você descreve como rodar o pacote e escolhe a infraestrutura que vai executá-lo.

**Exemplo do dia a dia:** Uma loja empacota seu serviço de pedidos e pede ao ECS que mantenha várias cópias funcionando. Elas podem executar em máquinas EC2 ou com Fargate, conforme a configuração.

**O que ele não resolve sozinho?** ECS coordena containers; ele não escreve a aplicação. Usar ECS com EC2 ainda exige administrar as máquinas. Fargate muda essa parte da responsabilidade.

**Primeiras palavras para entender:**

- **Container:** ambiente de execução baseado num pacote de software.
- **Imagem:** pacote usado para criar o container.
- **Tarefa:** unidade de execução no ECS.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação / Contêineres · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** orquestrador de contêineres próprio da AWS, totalmente gerenciado e integrado aos demais serviços.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Rodar microsserviços, APIs, workers e jobs em contêineres Docker.
- Modernizar aplicações (Refactor/Replatform) sem adotar Kubernetes.

## Conceitos e componentes

| Componente | O que é |
|---|---|
| **Cluster** | Agrupamento lógico de capacidade. |
| **Task definition** | "Receita" JSON: imagem, CPU, memória, portas, variáveis, IAM role, logs. |
| **Task** | Instância em execução de uma task definition (um ou mais contêineres). |
| **Service** | Mantém N tasks rodando, substitui as que falham, integra com ELB e Auto Scaling. |
| **Capacity provider / launch type** | **Fargate** (serverless), **EC2** (você gerencia as instâncias) ou **ECS Anywhere** (on-premises). |
| **Task role × execution role** | Task role = permissões da aplicação; execution role = permissões do agente (puxar imagem do ECR, enviar logs). |

## Configurações e opções importantes

| Opção | Detalhe |
|---|---|
| **Fargate** | Sem servidores; paga vCPU e memória da task por segundo. Suporta Fargate Spot. |
| **EC2 launch type** | Mais controle (GPU, tipos específicos, instâncias reservadas/Spot); você faz patch e escala o cluster. |
| **Service Auto Scaling** | Escala o número de tasks por métrica (CPU, memória, requisições do ALB). |
| **Deploy** | Rolling update (padrão) ou blue/green (com CodeDeploy ou nativo). |
| **Service Connect / Cloud Map** | Descoberta de serviços entre tasks. |
| **ECS Express Mode** | Forma simplificada de publicar uma aplicação web em contêiner — 🧊 fora da prova. |

## Cobrança

- **Sem custo pelo ECS em si:** paga-se Fargate (vCPU/memória por segundo) ou as instâncias EC2, além de ELB, logs etc.

## Segurança e responsabilidade compartilhada

- **AWS:** plano de controle do ECS; com Fargate, também a infraestrutura e o SO do host.
- **Cliente:** imagens (vulnerabilidades — use ECR scan/Inspector), task roles, segredos, rede (SGs), dados; com EC2, também patch das instâncias.

## ⚠️ Pegadinhas e não confundir

- **ECS × EKS:** orquestrador nativo da AWS × Kubernetes gerenciado. "Já usa Kubernetes" → EKS.
- **ECS × Fargate:** ECS é o orquestrador; Fargate é o *modo de execução* serverless (também usado pelo EKS).

## ❓ Perguntas típicas

- "Orquestrar contêineres de forma nativa na AWS." → ECS.
- "Rodar contêineres sem gerenciar servidores." → ECS com Fargate.
- "Contêineres que precisam de GPU específica." → ECS com launch type EC2.
- "Rodar contêineres no datacenter com o mesmo painel." → ECS Anywhere.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Cluster, task definition, task, service e capacidade |
| **O que você decide/configura?** | Imagem, CPU/memória, role, rede, número de tasks e capacidade EC2/Fargate |
| **Em que ordem as coisas acontecem?** | A definição descreve containers; o service mantém tasks; capacidade executa |
| **O que pode fazer, e em que condição?** | Pode operar containers de longa duração ou tarefas pontuais |
| **O que não pode presumir?** | ECS não é registro de imagens; criar cluster não publica uma API automaticamente |

**Caso comentado:** Web containerizada sem administrar hosts: ECS com Fargate, com rede e exposição configuradas.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
