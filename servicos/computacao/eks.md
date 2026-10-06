<!-- autoral -->

# Amazon EKS (Elastic Kubernetes Service)

> **Categoria:** Computação (containers) · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** Kubernetes gerenciado: a AWS opera o plano de controle do cluster, e você roda suas aplicações em containers.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Uma empresa que já roda seus containers com **Kubernetes**, um orquestrador de código aberto, quer levá-los para a AWS sem trocar de ferramenta. Operar o Kubernetes por conta própria dá trabalho: a parte central do cluster, que agenda os containers e guarda o estado, precisa ficar sempre no ar e atualizada.

O EKS entrega o Kubernetes gerenciado. A AWS opera o **plano de controle** (a parte central do Kubernetes), e a empresa continua usando as mesmas ferramentas e configurações. O EKS roda na nuvem da AWS e também em datacenters do cliente.

O limite: o EKS faz sentido quando há um motivo para Kubernetes. Para orquestrar containers sem esse requisito, o [ECS](ecs.md) é mais simples. A regra da prova: "já usa Kubernetes" aponta para o EKS.

## Como funciona

1. Você cria um **cluster** do EKS; a AWS cria e mantém o plano de controle do Kubernetes.
2. Os containers rodam em **nós**: instâncias do EC2, o Fargate ou servidores do próprio cliente.
3. Você publica as aplicações com as ferramentas de sempre do Kubernetes.
4. No **EKS Auto Mode**, a AWS também gerencia os nós: cria a infraestrutura, escolhe as instâncias e escala.

## Opções principais

| Opção | O que faz | Quando lembrar |
|---|---|---|
| EKS padrão | A AWS gerencia o plano de controle; você gerencia os nós | Controle dos nós |
| EKS Auto Mode | A AWS gerencia também os nós | Menos trabalho de operação |
| Fargate | Roda os pods sem servidores para gerenciar | Containers serverless com Kubernetes |
| EKS Anywhere e Hybrid Nodes | Kubernetes do EKS em datacenters do cliente | Ambiente híbrido |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Suporte padrão de uma versão do Kubernetes no EKS | 14 meses após o lançamento no EKS | 06/10/2026 |
| Suporte estendido, com custo adicional | Mais 12 meses | 06/10/2026 |

## Como é cobrado

Todo cluster do EKS paga uma taxa **por hora**, que depende da versão do Kubernetes: a taxa é maior quando a versão já saiu do suporte padrão e está no suporte estendido. Além disso, você paga a capacidade onde os containers rodam, como as instâncias do EC2 ou o Fargate. Diferente do ECS, que não cobra pela orquestração, o EKS cobra pelo cluster.

## Não confundir com

| Serviço | Diferença para o EKS | Pista no enunciado |
|---|---|---|
| [Amazon ECS](ecs.md) | Orquestrador próprio da AWS, sem Kubernetes e sem taxa pela orquestração | "Orquestrar containers" sem citar Kubernetes |
| [AWS Fargate](fargate.md) | Capacidade serverless onde o EKS pode rodar os pods | "Sem gerenciar servidores" |
| [AWS Elastic Beanstalk](elastic-beanstalk.md) | Recebe o código e monta o ambiente; no modo Cluster, usa o EKS por baixo | "Só enviar o código" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- [Preços do Amazon EKS](https://aws.amazon.com/eks/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
