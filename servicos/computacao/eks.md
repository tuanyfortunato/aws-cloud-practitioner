# Amazon EKS (Elastic Kubernetes Service)

> **Categoria:** Computação / Contêineres · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** Kubernetes gerenciado — a AWS opera o plano de controle e você roda seus pods.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **mesmo Kubernetes** que você usaria em qualquer lugar, mas com a AWS cuidando do "cérebro" (o plano de controle).

- ✅ **Escolha quando:** a empresa **já usa Kubernetes** ou quer portabilidade entre nuvens e datacenter.
- 🚫 **Não é a resposta quando:** quer o orquestrador **mais simples e nativo** da AWS → [ECS](ecs.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "Kubernetes", "já usa Kubernetes on-premises", "portabilidade", "open source".
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Cluster Kubernetes, control plane, pods, services e capacidade |
| **O que você decide/configura?** | Versão, acesso, rede e modalidade de execução dos workloads |
| **Em que ordem as coisas acontecem?** | Envie manifests; Kubernetes agenda workloads na capacidade configurada |
| **O que pode fazer, e em que condição?** | Fornece Kubernetes gerenciado e integrações AWS |
| **O que não pode presumir?** | Gerenciar control plane não elimina configuração dos workloads e responsabilidades da modalidade escolhida |

**Caso comentado:** Equipe exige APIs Kubernetes: EKS, em vez de escolher ECS apenas porque ambos executam containers.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
