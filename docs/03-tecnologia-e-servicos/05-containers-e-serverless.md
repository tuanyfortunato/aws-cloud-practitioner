# 3.5 Containers e serverless

## 🧠 Antes de começar

**Qual é a dificuldade?** Sua aplicação pode precisar rodar como um pacote completo ou executar apenas uma tarefa quando algo acontece. A equipe precisa escolher a forma de execução e quem administra os servidores.

**A ideia em palavras simples:** Containers empacotam aplicações e dependências. Serviços como ECS e EKS coordenam sua execução; Fargate fornece capacidade sem administração direta das máquinas. Lambda executa funções acionadas por chamadas ou eventos.

**Exemplo do dia a dia:** Um serviço de pedidos executa em containers. Uma tarefa de gerar miniatura pode ser uma função acionada quando chega uma foto.

**O que não concluir?** Serverless não significa ausência de servidores, custo zero ou execução ilimitada. Empacotar, coordenar e fornecer capacidade são funções distintas.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Contêiner** | pacote leve com a aplicação e suas dependências, que roda igual em qualquer lugar. |
| **Orquestrador** | sistema que decide onde e quantos contêineres rodam. |
| **Serverless** | você não gerencia servidores e paga só pelo uso. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon ECS (Elastic Container Service)](../../servicos/computacao/ecs.md) · [Amazon EKS (Elastic Kubernetes Service)](../../servicos/computacao/eks.md) · [AWS Fargate](../../servicos/computacao/fargate.md) · [Amazon ECR (Elastic Container Registry)](../../servicos/computacao/ecr.md) · [AWS Lambda](../../servicos/computacao/lambda.md)

⬅️ [3.4 Escalabilidade e balanceamento de carga](04-escalabilidade-e-balanceamento.md) · 🏠 [Índice do domínio](README.md) · [3.6 Outros serviços de computação](06-outros-servicos-de-computacao.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **EKS:** O EKS oferece Kubernetes gerenciado.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **ECR:** O ECR é um repositório de imagens de containers.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **evento:** Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.
- **container:** Ambiente que executa uma aplicação a partir de uma imagem com software e dependências. É diferente de criar uma máquina virtual completa para cada pacote.
- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.
- **longa duração:** Trabalho que precisa de execução continuada ou por mais tempo que determinado limite de uma modalidade. Os limites do serviço e o tratamento de falhas devem combinar com o trabalho.


Uma imagem de container empacota software; um container executa esse pacote; um coordenador mantém unidades de execução; uma opção de capacidade fornece o lugar onde elas rodam. Separar essas funções evita confundir ECR, ECS, EKS e Fargate.

Uma função acionada por evento é outra forma de execução: recebe entrada, realiza uma tarefa e devolve ou grava resultado. Não precisa ser a melhor opção para todo programa de longa duração. ‘Sem administrar servidores’ não significa ‘sem configuração’.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

um **contêiner** é como uma **marmita pronta**: leva a comida e os talheres e funciona em qualquer micro-ondas. O **ECS/EKS** é o **gerente da cozinha** que distribui as marmitas; o **Fargate** é **não ter cozinha** (alguém esquenta para você); o **Lambda** é um **garçom que só aparece quando chamado** e cobra por minuto de atendimento.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.


**Amazon ECS:** Orquestrador de containers da AWS. Dois tipos de execução: **EC2** (você gerencia as instâncias do cluster) ou **Fargate** (serverless).

**Antes de ler este trecho:**

- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.


**AWS Fargate:** Computação **serverless para containers**, usada com ECS ou EKS; você define CPU e memória da task e não gerencia servidores.

**Antes de ler este trecho:**

- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **Kubernetes:** Sistema que coordena containers e mantém o estado de execução desejado. Sua operação exige conceitos e configurações próprios.


**Amazon EKS:** **Kubernetes** gerenciado. Escolha quando a empresa já usa Kubernetes ou quer portabilidade.

**Antes de ler este trecho:**

- **Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.


**Amazon ECR:** registro privado de imagens de container, com varredura de vulnerabilidades (integrado ao Inspector).

**Antes de ler este trecho:**

- **AWS Lambda / Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.


**AWS Lambda**

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.


  - Executa código em resposta a **eventos** (upload no S3, requisição no API Gateway, mensagem no SQS, regra do EventBridge, alteração no DynamoDB).
**Antes de ler este trecho:**

- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.


  - Sem servidores, escala automática, alta disponibilidade embutida.

  - **Limite de 15 minutos** por execução; memória configurável (a CPU acompanha a memória).

  - **Cobrança por número de requisições e por duração** (GB-segundo). Nada é cobrado quando não executa. Tem camada gratuita mensal.

  - Linguagens: Python, Node.js, Java, .NET, Go, Ruby e runtimes customizados.
**Antes de ler este trecho:**

- **Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.


**Cai na prova:** "processar imagem assim que chega ao S3" = Lambda; "tarefa que roda por 2 horas" = não é Lambda (ECS/Fargate, Batch ou EC2); "containers sem gerenciar servidores" = Fargate; "já usa Kubernetes" = EKS.

### ➕ Complemento

**Antes de ler este trecho:**

- **segundo:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.


**Cobrança do Fargate:** por vCPU e memória alocadas à task, por segundo.


**Cobrança do Lambda:** por número de requisições e duração (arredondada ao milissegundo), proporcional à memória configurada.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **orquestração:** Coordenação de onde e como tarefas ou componentes executam. O coordenador não escreve o conteúdo do trabalho por si só.


**Primeiro, identifique o funcionamento:** ECR armazena imagens; ECS/EKS organizam execução; Fargate fornece capacidade sem administrar hosts. Uma função Lambda executa código em resposta a uma invocação.

**Depois, compare as escolhas:** Kubernetes necessário: EKS. Orquestração AWS: ECS. Containers sem hosts: Fargate. Função convencional por evento: Lambda. Separe orquestrador, imagem e capacidade.

**Por fim, verifique o limite:** Serverless significa servidores administrados pelo provedor. A função convencional tem limite de execução por invocação; não generalize esse limite a todo recurso novo do Lambda.

## 4. Caso resolvido

Você guardou uma imagem no ECR. Sua API já está rodando?

**Raciocínio e resposta:** Não: ECR é registro. É preciso executar a imagem em capacidade adequada, como ECS com Fargate, configurar rede, acesso e exposição da API.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Sua aplicação pode precisar rodar como um pacote completo ou executar apenas uma tarefa quando algo acontece. A equipe precisa escolher a forma de execução e quem administra os servidores.

**2. O que a solução fornece?**

Containers empacotam aplicações e dependências. Serviços como ECS e EKS coordenam sua execução; Fargate fornece capacidade sem administração direta das máquinas. Lambda executa funções acionadas por chamadas ou eventos.

**3. Que conclusão seria incorreta?**

Serverless não significa ausência de servidores, custo zero ou execução ilimitada. Empacotar, coordenar e fornecer capacidade são funções distintas.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Diferenciar **ECS** (nativo da AWS) de **EKS** (Kubernetes).
- [ ] Saber que o **Fargate** roda contêineres **sem servidores** e o **ECR** guarda as imagens.
- [ ] Lembrar que a **função Lambda convencional** roda por **até 15 minutos por invocação**, é disparado por eventos e cobra por requisição e duração.

**Dica de revisão para a prova:** "Processar quando o arquivo chega ao S3" → **Lambda**. "Roda por **2 horas**" → **não** é Lambda (Fargate, Batch ou EC2). "Já usa **Kubernetes**" → **EKS**. "Contêineres sem gerenciar servidores" → **Fargate**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Qual serviço executa código sem servidores, em resposta a eventos?"

**Resposta curta:** Lambda.


**Fundamento explicado no capítulo:** "Qual serviço executa código sem servidores, em resposta a eventos?" → Lambda.

**Pergunta:** "Qual é o tempo máximo de execução do Lambda?"

**Resposta curta:** 15 minutos.


**Fundamento explicado no capítulo:** "Qual é o tempo máximo de execução do Lambda?" → 15 minutos.

**Pergunta:** "Como o Lambda é cobrado?"

**Resposta curta:** No modelo base, requisições e duração; extras como concorrência provisionada podem cobrar sem invocação.

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.


**Fundamento explicado no capítulo:** "Como o Lambda é cobrado?" → No modelo base, requisições e duração; extras como concorrência provisionada podem cobrar sem invocação.

**Pergunta:** "Rodar containers sem gerenciar instâncias."

**Resposta curta:** Fargate (com ECS ou EKS).


**Fundamento explicado no capítulo:** "Rodar containers sem gerenciar instâncias." → Fargate (com ECS ou EKS).

**Pergunta:** "Empresa já usa Kubernetes on-premises e quer migrar."

**Resposta curta:** EKS.

**Antes de ler este trecho:**

- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.


**Fundamento explicado no capítulo:** "Empresa já usa Kubernetes on-premises e quer migrar." → EKS.

**Pergunta:** "Onde guardar imagens Docker privadas?"

**Resposta curta:** ECR.


**Fundamento explicado no capítulo:** "Onde guardar imagens Docker privadas?" → ECR.

**Pergunta:** "Qual serviço orquestra containers e é nativo da AWS?"

**Resposta curta:** ECS.


**Fundamento explicado no capítulo:** "Qual serviço orquestra containers e é nativo da AWS?" → ECS.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **Lambda — números confirmados (📌):**

| Item | Valor |
|---|---|
| Memória | 128 MB (mínimo e padrão) a **10.240 MB**, em incrementos de 1 MB |
| CPU | **Proporcional à memória** — ⚠️ não existe configuração separada de vCPU |
| Timeout | até **900 s (15 min)** |
| `/tmp` (efêmero) | **512 MB a 10.240 MB** (512 MB sem custo extra) |
| Imagem de contêiner | até 10 GB (🧊) |
| Layers | até 5 por função (🧊) |
| Cobrança | nº de requisições + duração em ms × memória (GB-s) |

- Contas novas têm quotas reduzidas de concorrência/memória que a AWS aumenta automaticamente com o uso (explica relatos de "limite de 3.008 MB").
- *Questão-modelo:* "processar um arquivo por até **2 horas** sem gerenciar servidores" → **não** é Lambda; resposta: **Fargate/ECS ou AWS Batch**.
- 🧊 Não decorar: escalonamento de concorrência (1.000 ambientes a cada 10 s), detalhes de rede da Lambda.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.4 Escalabilidade e balanceamento de carga](04-escalabilidade-e-balanceamento.md) · 🏠 [Índice do domínio](README.md) · [3.6 Outros serviços de computação](06-outros-servicos-de-computacao.md) ➡️
