# Amazon ECS (Elastic Container Service)

> **Categoria:** Computação / Contêineres · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** orquestrador de contêineres próprio da AWS, totalmente gerenciado e integrado aos demais serviços.

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

## 🔗 Documentação oficial

- [Guia do ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
