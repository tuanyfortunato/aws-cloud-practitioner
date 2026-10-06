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

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [Amazon ECS (Elastic Container Service)](../../servicos/computacao/ecs.md) · [Amazon EKS (Elastic Kubernetes Service)](../../servicos/computacao/eks.md) · [AWS Fargate](../../servicos/computacao/fargate.md) · [Amazon ECR (Elastic Container Registry)](../../servicos/computacao/ecr.md) · [AWS Lambda](../../servicos/computacao/lambda.md)

⬅️ [3.4 Escalabilidade e balanceamento de carga](04-escalabilidade-e-balanceamento.md) · 🏠 [Índice do domínio](README.md) · [3.6 Outros serviços de computação](06-outros-servicos-de-computacao.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Uma imagem de container empacota software; um container executa esse pacote; um coordenador mantém unidades de execução; uma opção de capacidade fornece o lugar onde elas rodam. Separar essas funções evita confundir ECR, ECS, EKS e Fargate.

Uma função acionada por evento é outra forma de execução: recebe entrada, realiza uma tarefa e devolve ou grava resultado. Não precisa ser a melhor opção para todo programa de longa duração. ‘Sem administrar servidores’ não significa ‘sem configuração’.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

um **contêiner** é como uma **marmita pronta**: leva a comida e os talheres e funciona em qualquer micro-ondas. O **ECS/EKS** é o **gerente da cozinha** que distribui as marmitas; o **Fargate** é **não ter cozinha** (alguém esquenta para você); o **Lambda** é um **garçom que só aparece quando chamado** e cobra por minuto de atendimento.

</details>

## 2. Conceitos e opções explicados

**Amazon ECS:** Orquestrador de containers da AWS. Dois tipos de execução: **EC2** (você gerencia as instâncias do cluster) ou **Fargate** (serverless).

**AWS Fargate:** Computação **serverless para containers**, usada com ECS ou EKS; você define CPU e memória da task e não gerencia servidores.

**Amazon EKS:** **Kubernetes** gerenciado. Escolha quando a empresa já usa Kubernetes ou quer portabilidade.

**Amazon ECR:** registro privado de imagens de container, com varredura de vulnerabilidades (integrado ao Inspector).

**AWS Lambda**

  - Executa código em resposta a **eventos** (upload no S3, requisição no API Gateway, mensagem no SQS, regra do EventBridge, alteração no DynamoDB).

  - Sem servidores, escala automática, alta disponibilidade embutida.

  - **Limite de 15 minutos** por execução; memória configurável (a CPU acompanha a memória).

  - **Cobrança por número de requisições e por duração** (GB-segundo). Nada é cobrado quando não executa. Tem camada gratuita mensal.

  - Linguagens: Python, Node.js, Java, .NET, Go, Ruby e runtimes customizados.

**Cai na prova:** "processar imagem assim que chega ao S3" = Lambda; "tarefa que roda por 2 horas" = não é Lambda (ECS/Fargate, Batch ou EC2); "containers sem gerenciar servidores" = Fargate; "já usa Kubernetes" = EKS.

### ➕ Complemento

**Cobrança do Fargate:** por vCPU e memória alocadas à task, por segundo.

**Cobrança do Lambda:** por número de requisições e duração (arredondada ao milissegundo), proporcional à memória configurada.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** ECR armazena imagens; ECS/EKS organizam execução; Fargate fornece capacidade sem administrar hosts. Uma função Lambda executa código em resposta a uma invocação.

**Depois, compare as escolhas:** Kubernetes necessário: EKS. Orquestração AWS: ECS. Containers sem hosts: Fargate. Função convencional por evento: Lambda. Separe orquestrador, imagem e capacidade.

**Por fim, verifique o limite:** Serverless significa servidores administrados pelo provedor. A função convencional tem limite de execução por invocação; não generalize esse limite a todo recurso novo do Lambda.

## 4. Caso resolvido

Você guardou uma imagem no ECR. Sua API já está rodando?

**Raciocínio e resposta:** Não: ECR é registro. É preciso executar a imagem em capacidade adequada, como ECS com Fargate, configurar rede, acesso e exposição da API.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **ECS** (nativo da AWS) de **EKS** (Kubernetes).
- [ ] Saber que o **Fargate** roda contêineres **sem servidores** e o **ECR** guarda as imagens.
- [ ] Lembrar que a **função Lambda convencional** roda por **até 15 minutos por invocação**, é disparado por eventos e cobra por requisição e duração.

**Dica de revisão para a prova:** "Processar quando o arquivo chega ao S3" → **Lambda**. "Roda por **2 horas**" → **não** é Lambda (Fargate, Batch ou EC2). "Já usa **Kubernetes**" → **EKS**. "Contêineres sem gerenciar servidores" → **Fargate**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Qual serviço executa código sem servidores, em resposta a eventos?"

**Resposta curta:** Lambda.

**Pergunta:** "Qual é o tempo máximo de execução do Lambda?"

**Resposta curta:** 15 minutos.

**Pergunta:** "Como o Lambda é cobrado?"

**Resposta curta:** No modelo base, requisições e duração; extras como concorrência provisionada podem cobrar sem invocação.

**Pergunta:** "Rodar containers sem gerenciar instâncias."

**Resposta curta:** Fargate (com ECS ou EKS).

**Pergunta:** "Empresa já usa Kubernetes on-premises e quer migrar."

**Resposta curta:** EKS.

**Pergunta:** "Onde guardar imagens Docker privadas?"

**Resposta curta:** ECR.

**Pergunta:** "Qual serviço orquestra containers e é nativo da AWS?"

**Resposta curta:** ECS.

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
