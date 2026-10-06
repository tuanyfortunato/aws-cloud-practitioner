# Amazon EKS (Elastic Kubernetes Service)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma empresa já usa Kubernetes para coordenar seus containers e quer continuar usando essa ferramenta na AWS, sem manter sozinha sua camada central de controle.

**Como este serviço ajuda?** O EKS oferece Kubernetes gerenciado. Kubernetes é o sistema que organiza onde os containers executam e mantém o estado desejado da aplicação.

**Exemplo do dia a dia:** Uma equipe leva uma aplicação que já usa Kubernetes para um ambiente EKS. Ela mantém suas definições de aplicação e escolhe como fornecer a capacidade de execução.

**O que ele não resolve sozinho?** A AWS gerenciar a camada de controle não significa que toda a aplicação, as permissões e todas as máquinas estão administradas para você. Isso depende das opções usadas.

**Primeiras palavras para entender:**

- **Kubernetes:** ferramenta para coordenar containers.
- **Cluster:** conjunto de recursos que trabalham juntos.
- **Camada de controle:** parte que coordena esse conjunto.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação / Contêineres · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** Kubernetes gerenciado — a AWS opera o plano de controle e você roda seus pods.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina um ambiente Kubernetes e a forma de fornecer capacidade para os containers.

**Passo 2.** Publique as descrições da aplicação e suas necessidades. Kubernetes coordena o posicionamento e a quantidade de unidades de execução.

**Passo 3.** Acompanhe aplicação e recursos. A divisão do trabalho de administração depende da modalidade escolhida.

## 2. Recursos e opções, com significado

### Para que serve

Empresas que **já usam Kubernetes** (on-premises ou outra nuvem) e querem migrar sem reescrever manifestos.

Portabilidade entre ambientes; ecossistema open source (Helm, operadores).

### Conceitos e componentes

**Control plane**

**O que é:** API server e etcd gerenciados, multi-AZ, pela AWS.

**Nós (data plane)**

**O que é:** **Managed node groups** (EC2 gerenciadas), **self-managed nodes**, **Fargate** (pods serverless) ou **EKS Auto Mode** (AWS gerencia os nós).

**Add-ons**

**O que é:** VPC CNI, CoreDNS, kube-proxy, EBS CSI driver…

**IAM ↔ Kubernetes**

**O que é:** *EKS Pod Identity* / IRSA dão IAM roles a pods; *access entries* mapeiam usuários IAM para RBAC.

**EKS Anywhere / EKS Hybrid Nodes**

**O que é:** Rodar ou anexar nós fora da AWS (on-premises).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

A AWS gerenciar a camada de controle não significa que toda a aplicação, as permissões e todas as máquinas estão administradas para você. Isso depende das opções usadas.

### ⚠️ Pegadinhas e não confundir

"Já usa Kubernetes" / "padrão open source portátil" → **EKS**. "Mais simples, nativo AWS" → **ECS**.

EKS tem custo do plano de controle; ECS não.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Taxa por cluster por hora** (plano de controle) + nós (EC2/Fargate). Versões do Kubernetes em *extended support* custam mais.

### Segurança e responsabilidade compartilhada

**AWS:** plano de controle (disponibilidade, patch, escalonamento).

**Cliente:** nós (patch de AMIs, salvo Auto Mode/Fargate), pods, imagens, RBAC, network policies, atualização de versão do cluster.

## 5. Caso resolvido: ligando as peças

Uma equipe leva uma aplicação que já usa Kubernetes para um ambiente EKS. Ela mantém suas definições de aplicação e escolhe como fornecer a capacidade de execução.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina um ambiente Kubernetes e a forma de fornecer capacidade para os containers.
**Etapa 2:** Publique as descrições da aplicação e suas necessidades. Kubernetes coordena o posicionamento e a quantidade de unidades de execução.
**Etapa 3:** Acompanhe aplicação e recursos. A divisão do trabalho de administração depende da modalidade escolhida.

**Resultado e responsabilidade:** O EKS oferece Kubernetes gerenciado. Kubernetes é o sistema que organiza onde os containers executam e mantém o estado desejado da aplicação.

**Recursos envolvidos:** Cluster Kubernetes, control plane, pods, services e capacidade.

**Decisões que precisam ser tomadas:** Versão, acesso, rede e modalidade de execução dos workloads.

**Outra situação comentada:** Equipe exige APIs Kubernetes: EKS, em vez de escolher ECS apenas porque ambos executam containers.

**Por que não concluir mais do que isso:** Gerenciar control plane não elimina configuração dos workloads e responsabilidades da modalidade escolhida

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "A empresa usa Kubernetes on-premises e quer um serviço gerenciado na AWS."

**Resposta curta:** EKS.

**Pergunta:** "Rodar pods sem gerenciar nós."

**Resposta curta:** EKS com Fargate (ou Auto Mode).

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
