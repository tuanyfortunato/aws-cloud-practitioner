# Amazon EKS (Elastic Kubernetes Service)

> **Categoria:** Computação / Contêineres · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** Kubernetes gerenciado — a AWS opera o plano de controle e você roda seus pods.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Empresas que **já usam Kubernetes** (on-premises ou outra nuvem) e querem migrar sem reescrever manifestos.
- Portabilidade entre ambientes; ecossistema open source (Helm, operadores).

## Conceitos e componentes

| Componente | O que é |
|---|---|
| **Control plane** | API server e etcd gerenciados, multi-AZ, pela AWS. |
| **Nós (data plane)** | **Managed node groups** (EC2 gerenciadas), **self-managed nodes**, **Fargate** (pods serverless) ou **EKS Auto Mode** (AWS gerencia os nós). |
| **Add-ons** | VPC CNI, CoreDNS, kube-proxy, EBS CSI driver… |
| **IAM ↔ Kubernetes** | *EKS Pod Identity* / IRSA dão IAM roles a pods; *access entries* mapeiam usuários IAM para RBAC. |
| **EKS Anywhere / EKS Hybrid Nodes** | Rodar ou anexar nós fora da AWS (on-premises). |

## Cobrança

- **Taxa por cluster por hora** (plano de controle) + nós (EC2/Fargate). Versões do Kubernetes em *extended support* custam mais.

## Segurança e responsabilidade compartilhada

- **AWS:** plano de controle (disponibilidade, patch, escalonamento).
- **Cliente:** nós (patch de AMIs, salvo Auto Mode/Fargate), pods, imagens, RBAC, network policies, atualização de versão do cluster.

## ⚠️ Pegadinhas e não confundir

- "Já usa Kubernetes" / "padrão open source portátil" → **EKS**. "Mais simples, nativo AWS" → **ECS**.
- EKS tem custo do plano de controle; ECS não.

## ❓ Perguntas típicas

- "A empresa usa Kubernetes on-premises e quer um serviço gerenciado na AWS." → EKS.
- "Rodar pods sem gerenciar nós." → EKS com Fargate (ou Auto Mode).

## 🔗 Documentação oficial

- [Guia do EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
