# AWS Fargate

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Você quer executar containers, mas não quer escolher, atualizar e manter as máquinas que ficam por baixo deles.

**Como este serviço ajuda?** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução. Você define, entre outras coisas, os recursos necessários ao container.

**Exemplo do dia a dia:** A equipe informa que seu serviço de pedidos precisa de determinada capacidade e o executa pelo ECS com Fargate, sem criar um grupo próprio de máquinas EC2.

**O que ele não resolve sozinho?** Fargate não substitui a aplicação nem o coordenador ECS/EKS. Configuração, permissões, rede e custo continuam exigindo decisões.

**Primeiras palavras para entender:**

- **Container:** pacote em execução com a aplicação.
- **Capacidade:** recursos como processamento e memória.
- **Gerenciado:** parte do trabalho operacional fica com a AWS.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação serverless para contêineres · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** motor serverless que executa contêineres do ECS ou EKS sem você provisionar ou gerenciar servidores.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **EKS:** O EKS oferece Kubernetes gerenciado.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.

**Passo 1.** Descreva os containers pelo ECS ou EKS e selecione uma modalidade de execução compatível com Fargate.

**Passo 2.** Defina capacidade, comunicação e permissões. Fargate fornece a infraestrutura de execução sem você administrar diretamente as máquinas.

**Passo 3.** Observe os containers e seus resultados. A AWS administrar servidores não elimina a responsabilidade pelo código e pelos acessos.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.

Rodar contêineres sem cuidar de instâncias, patch de SO ou escalonamento do cluster.

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.

Jobs longos que **excedem os 15 min do Lambda** (sem limite de duração).

Cargas variáveis em que o *bin packing* de instâncias não compensa.

### Conceitos e configurações

**Antes de ler este trecho:**

- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **EFS:** O EFS oferece um sistema de arquivos compartilhado.
- **vCPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **ARM:** Família de arquitetura de processadores. O software precisa ser compatível com a arquitetura escolhida; não basta comparar a quantidade de processadores.
- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **security group:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **pod:** Unidade de execução do Kubernetes que reúne um ou mais containers. Recursos e disponibilidade dependem do ambiente e das configurações.
- **ENI:** Interface de rede virtual. Ela associa endereços e configurações de comunicação a recursos compatíveis.
- **Graviton:** Família de processadores AWS baseada em arquitetura ARM. A aplicação e sua imagem precisam ser compatíveis com essa arquitetura.

| Item | Detalhe |
|---|---|
| **Tamanho da task/pod** | Você escolhe vCPU e memória (combinações predefinidas, de 0,25 vCPU até **32 vCPU / 244 GB** 🧊). |
| **Isolamento** | Cada task roda em seu próprio ambiente isolado (micro-VM). |
| **Armazenamento** | Efêmero (20 GB padrão, ampliável) + volumes **EFS** e **EBS** persistentes. |
| **Arquitetura** | x86_64 ou ARM (Graviton). |
| **Fargate Spot** | Até ~70% mais barato, pode ser interrompido (aviso de 2 min) — só no ECS. |
| **Rede** | Modo `awsvpc`: cada task recebe sua ENI e security group. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Fargate não substitui a aplicação nem o coordenador ECS/EKS. Configuração, permissões, rede e custo continuam exigindo decisões.

### ⚠️ Pegadinhas e não confundir

Fargate **não é orquestrador**: é usado **com** ECS ou EKS.

Fargate × Lambda: contêiner sem limite de tempo × função Lambda convencional até 15 min por invocação; workflows e outras modalidades têm modelos próprios.

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **GPU:** Processador especializado em executar muitos cálculos em paralelo. Pode atender gráficos e determinadas tarefas de aprendizado de máquina; não é necessário para todo programa.

Fargate × EC2 launch type: menos controle (sem GPU, sem acesso ao host) e menos operação.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **segundo / minuto:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.

Por **vCPU e memória alocadas**, por segundo (mínimo de 1 minuto), + armazenamento efêmero extra.

**Antes de ler este trecho:**

- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.

Coberto pelo **Compute Savings Plans**.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **runtime:** Ambiente que executa código de uma linguagem ou plataforma. Compatibilidade de bibliotecas e versões deve ser avaliada.

**AWS:** hosts, SO, runtime de contêiner, isolamento, patch da infraestrutura.

**Antes de ler este trecho:**

- **role:** Papel que fornece permissões a uma sessão que o assume. O termo função IAM não significa um trecho de código como uma função Lambda.
- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.

**Cliente:** imagem do contêiner e suas dependências, task role, rede, dados.

## 5. Caso resolvido: ligando as peças

A equipe informa que seu serviço de pedidos precisa de determinada capacidade e o executa pelo ECS com Fargate, sem criar um grupo próprio de máquinas EC2.

**Aplicando a sequência à situação:**

**Etapa 1:** Descreva os containers pelo ECS ou EKS e selecione uma modalidade de execução compatível com Fargate.
**Etapa 2:** Defina capacidade, comunicação e permissões. Fargate fornece a infraestrutura de execução sem você administrar diretamente as máquinas.
**Etapa 3:** Observe os containers e seus resultados. A AWS administrar servidores não elimina a responsabilidade pelo código e pelos acessos.

**Resultado e responsabilidade:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução. Você define, entre outras coisas, os recursos necessários ao container.

**Recursos envolvidos:** Tasks ECS ou workloads EKS compatíveis e interfaces de rede.

**Decisões que precisam ser tomadas:** Recursos de CPU/memória suportados, imagem, roles e rede.

**Antes de ler este trecho:**

- **ECR:** O ECR é um repositório de imagens de containers.
- **worker:** Programa que recebe e processa dados ou tarefas. Ele precisa realizar o trabalho e tratar falhas, não apenas receber a mensagem.
- **container:** Ambiente que executa uma aplicação a partir de uma imagem com software e dependências. É diferente de criar uma máquina virtual completa para cada pacote.

**Outra situação comentada:** Container de worker: ECR guarda imagem, ECS organiza, Fargate executa.

**Por que não concluir mais do que isso:** Não armazena imagens nem substitui ECS/EKS; aplicações ainda exigem segurança e dados persistentes adequados

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Rodar contêineres sem gerenciar instâncias."

**Resposta curta:** Fargate (com ECS ou EKS).

**Pergunta:** "Processar arquivo por 2 horas sem gerenciar servidores."

**Resposta curta:** Fargate (ou AWS Batch).

**Antes de ler este trecho:**

- **AWS Batch / Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.

**Pergunta:** "Como o Fargate é cobrado?"

**Resposta curta:** Por vCPU e memória alocadas, por segundo.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Fargate no ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
