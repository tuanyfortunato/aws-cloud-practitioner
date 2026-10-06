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

**Antes de ler este trecho:**

- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.

**Passo 1.** Guarde a imagem da aplicação num repositório acessível e descreva como executar seus containers.

**Passo 2.** Escolha a capacidade de execução e configure o serviço quando precisar manter uma quantidade de tarefas funcionando.

**Passo 3.** ECS acompanha o estado desejado. A aplicação, a conexão e as permissões ainda precisam estar corretas.

## 2. Recursos e opções, com significado

### Para que serve

Rodar microsserviços, APIs, workers e jobs em contêineres Docker.

**Antes de ler este trecho:**

- **Kubernetes:** Sistema que coordena containers e mantém o estado de execução desejado. Sua operação exige conceitos e configurações próprios.
- **replatform:** Mudar parte da plataforma mantendo boa parte da aplicação. Por exemplo, trocar a operação do banco sem reescrever todas as regras do programa.
- **refactor:** Redesenhar partes da aplicação para atender novos objetivos. Pode trazer vantagens, mas demanda mudanças, testes e esforço.

Modernizar aplicações (Refactor/Replatform) sem adotar Kubernetes.

### Conceitos e componentes

**Cluster**

**Antes de ler este trecho:**

- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.

**O que é:** Agrupamento lógico de capacidade.

**Task definition**

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **JSON:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
- **role:** Papel que fornece permissões a uma sessão que o assume. O termo função IAM não significa um trecho de código como uma função Lambda.

**O que é:** "Receita" JSON: imagem, CPU, memória, portas, variáveis, IAM role, logs.

**Task**

**Antes de ler este trecho:**

- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.

**O que é:** Instância em execução de uma task definition (um ou mais contêineres).

**Service**

**Antes de ler este trecho:**

- **ELB:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.

**O que é:** Mantém N tasks rodando, substitui as que falham, integra com ELB e Auto Scaling.

**Capacity provider / launch type**

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.

**O que é:** **Fargate** (serverless), **EC2** (você gerencia as instâncias) ou **ECS Anywhere** (on-premises).

**Task role × execution role**

**Antes de ler este trecho:**

- **ECR:** O ECR é um repositório de imagens de containers.

**O que é:** Task role = permissões da aplicação; execution role = permissões do agente (puxar imagem do ECR, enviar logs).

### Configurações e opções importantes

**Fargate**

**Antes de ler este trecho:**

- **segundo:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.

**Detalhe:** Sem servidores; paga vCPU e memória da task por segundo. Suporta Fargate Spot.

**EC2 launch type**

**Antes de ler este trecho:**

- **GPU:** Processador especializado em executar muitos cálculos em paralelo. Pode atender gráficos e determinadas tarefas de aprendizado de máquina; não é necessário para todo programa.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.

**Detalhe:** Mais controle (GPU, tipos específicos, instâncias reservadas/Spot); você faz patch e escala o cluster.

**Service Auto Scaling**

**Antes de ler este trecho:**

- **ALB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
- **métrica:** Medida observada ao longo do tempo, como utilização ou número de erros. O número precisa de unidade, período e contexto para ter significado.

**Detalhe:** Escala o número de tasks por métrica (CPU, memória, requisições do ALB).

**Deploy**

**Antes de ler este trecho:**

- **deploy:** Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.

**Detalhe:** Rolling update (padrão) ou blue/green (com CodeDeploy ou nativo).

**Service Connect / Cloud Map**

**Antes de ler este trecho:**

- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.

**Detalhe:** Descoberta de serviços entre tasks.

**ECS Express Mode**

**Detalhe:** Forma simplificada de publicar uma aplicação web em contêiner — 🧊 fora da prova.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

ECS coordena containers; ele não escreve a aplicação. Usar ECS com EC2 ainda exige administrar as máquinas. Fargate muda essa parte da responsabilidade.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **EKS:** O EKS oferece Kubernetes gerenciado.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.

**ECS × EKS:** orquestrador nativo da AWS × Kubernetes gerenciado. "Já usa Kubernetes" → EKS.

**ECS × Fargate:** ECS é o orquestrador; Fargate é o *modo de execução* serverless (também usado pelo EKS).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Sem custo pelo ECS em si:** paga-se Fargate (vCPU/memória por segundo) ou as instâncias EC2, além de ELB, logs etc.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.

**AWS:** plano de controle do ECS; com Fargate, também a infraestrutura e o SO do host.

**Antes de ler este trecho:**

- **Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.

**Cliente:** imagens (vulnerabilidades — use ECR scan/Inspector), task roles, segredos, rede (SGs), dados; com EC2, também patch das instâncias.

## 5. Caso resolvido: ligando as peças

**Antes de ler este trecho:**

- **container:** Ambiente que executa uma aplicação a partir de uma imagem com software e dependências. É diferente de criar uma máquina virtual completa para cada pacote.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.

O serviço de pedidos da escola foi empacotado em uma imagem de container. A equipe precisa executar várias cópias e manter a quantidade desejada, sem iniciar cada cópia manualmente.

A imagem fica num repositório acessível. Uma definição de tarefa descreve a execução e seus recursos. Um serviço ECS mantém tarefas conforme a configuração. Com EC2, a equipe também administra as máquinas; com uma modalidade Fargate compatível, muda a responsabilidade pela capacidade subjacente.

ECR guarda a imagem, mas não mantém sozinho as cópias em execução. Fargate fornece capacidade, mas não substitui a definição de serviço ou a aplicação. Se visitantes precisam de distribuição de tráfego, isso é outra integração a preparar, não consequência automática de guardar a imagem.

**Recursos envolvidos:** Cluster, task definition, task, service e capacidade.

**Decisões que precisam ser tomadas:** Imagem, CPU/memória, role, rede, número de tasks e capacidade EC2/Fargate.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.

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
