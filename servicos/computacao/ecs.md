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

## 1. A sequência de funcionamento

**Passo 1.** Guarde a imagem da aplicação num repositório acessível e descreva como executar seus containers.

**Passo 2.** Escolha a capacidade de execução e configure o serviço quando precisar manter uma quantidade de tarefas funcionando.

**Passo 3.** ECS acompanha o estado desejado. A aplicação, a conexão e as permissões ainda precisam estar corretas.

## 2. Recursos e opções, com significado

### Para que serve

Rodar microsserviços, APIs, workers e jobs em contêineres Docker.

Modernizar aplicações (Refactor/Replatform) sem adotar Kubernetes.

### Conceitos e componentes

**Cluster**

**O que é:** Agrupamento lógico de capacidade.

**Task definition**

**O que é:** "Receita" JSON: imagem, CPU, memória, portas, variáveis, IAM role, logs.

**Task**

**O que é:** Instância em execução de uma task definition (um ou mais contêineres).

**Service**

**O que é:** Mantém N tasks rodando, substitui as que falham, integra com ELB e Auto Scaling.

**Capacity provider / launch type**

**O que é:** **Fargate** (serverless), **EC2** (você gerencia as instâncias) ou **ECS Anywhere** (on-premises).

**Task role × execution role**

**O que é:** Task role = permissões da aplicação; execution role = permissões do agente (puxar imagem do ECR, enviar logs).

### Configurações e opções importantes

**Fargate**

**Detalhe:** Sem servidores; paga vCPU e memória da task por segundo. Suporta Fargate Spot.

**EC2 launch type**

**Detalhe:** Mais controle (GPU, tipos específicos, instâncias reservadas/Spot); você faz patch e escala o cluster.

**Service Auto Scaling**

**Detalhe:** Escala o número de tasks por métrica (CPU, memória, requisições do ALB).

**Deploy**

**Detalhe:** Rolling update (padrão) ou blue/green (com CodeDeploy ou nativo).

**Service Connect / Cloud Map**

**Detalhe:** Descoberta de serviços entre tasks.

**ECS Express Mode**

**Detalhe:** Forma simplificada de publicar uma aplicação web em contêiner — 🧊 fora da prova.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

ECS coordena containers; ele não escreve a aplicação. Usar ECS com EC2 ainda exige administrar as máquinas. Fargate muda essa parte da responsabilidade.

### ⚠️ Pegadinhas e não confundir

**ECS × EKS:** orquestrador nativo da AWS × Kubernetes gerenciado. "Já usa Kubernetes" → EKS.

**ECS × Fargate:** ECS é o orquestrador; Fargate é o *modo de execução* serverless (também usado pelo EKS).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Sem custo pelo ECS em si:** paga-se Fargate (vCPU/memória por segundo) ou as instâncias EC2, além de ELB, logs etc.

### Segurança e responsabilidade compartilhada

**AWS:** plano de controle do ECS; com Fargate, também a infraestrutura e o SO do host.

**Cliente:** imagens (vulnerabilidades — use ECR scan/Inspector), task roles, segredos, rede (SGs), dados; com EC2, também patch das instâncias.

## 5. Caso resolvido: ligando as peças

O serviço de pedidos da escola foi empacotado em uma imagem de container. A equipe precisa executar várias cópias e manter a quantidade desejada, sem iniciar cada cópia manualmente.

A imagem fica num repositório acessível. Uma definição de tarefa descreve a execução e seus recursos. Um serviço ECS mantém tarefas conforme a configuração. Com EC2, a equipe também administra as máquinas; com uma modalidade Fargate compatível, muda a responsabilidade pela capacidade subjacente.

ECR guarda a imagem, mas não mantém sozinho as cópias em execução. Fargate fornece capacidade, mas não substitui a definição de serviço ou a aplicação. Se visitantes precisam de distribuição de tráfego, isso é outra integração a preparar, não consequência automática de guardar a imagem.

**Recursos envolvidos:** Cluster, task definition, task, service e capacidade.

**Decisões que precisam ser tomadas:** Imagem, CPU/memória, role, rede, número de tasks e capacidade EC2/Fargate.

**Outra situação comentada:** Web containerizada sem administrar hosts: ECS com Fargate, com rede e exposição configuradas.

**Por que não concluir mais do que isso:** ECS não é registro de imagens; criar cluster não publica uma API automaticamente

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Orquestrar contêineres de forma nativa na AWS."

**Resposta curta:** ECS.

**Pergunta:** "Rodar contêineres sem gerenciar servidores."

**Resposta curta:** ECS com Fargate.

**Pergunta:** "Contêineres que precisam de GPU específica."

**Resposta curta:** ECS com launch type EC2.

**Pergunta:** "Rodar contêineres no datacenter com o mesmo painel."

**Resposta curta:** ECS Anywhere.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
