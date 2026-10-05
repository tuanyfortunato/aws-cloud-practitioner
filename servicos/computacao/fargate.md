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

## Para que serve

- Rodar contêineres sem cuidar de instâncias, patch de SO ou escalonamento do cluster.
- Jobs longos que **excedem os 15 min do Lambda** (sem limite de duração).
- Cargas variáveis em que o *bin packing* de instâncias não compensa.

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Tamanho da task/pod** | Você escolhe vCPU e memória (combinações predefinidas, de 0,25 vCPU até **32 vCPU / 244 GB** 🧊). |
| **Isolamento** | Cada task roda em seu próprio ambiente isolado (micro-VM). |
| **Armazenamento** | Efêmero (20 GB padrão, ampliável) + volumes **EFS** e **EBS** persistentes. |
| **Arquitetura** | x86_64 ou ARM (Graviton). |
| **Fargate Spot** | Até ~70% mais barato, pode ser interrompido (aviso de 2 min) — só no ECS. |
| **Rede** | Modo `awsvpc`: cada task recebe sua ENI e security group. |

## Cobrança

- Por **vCPU e memória alocadas**, por segundo (mínimo de 1 minuto), + armazenamento efêmero extra.
- Coberto pelo **Compute Savings Plans**.

## Segurança e responsabilidade compartilhada

- **AWS:** hosts, SO, runtime de contêiner, isolamento, patch da infraestrutura.
- **Cliente:** imagem do contêiner e suas dependências, task role, rede, dados.

## ⚠️ Pegadinhas e não confundir

- Fargate **não é orquestrador**: é usado **com** ECS ou EKS.
- Fargate × Lambda: contêiner sem limite de tempo × função Lambda convencional até 15 min por invocação; workflows e outras modalidades têm modelos próprios.
- Fargate × EC2 launch type: menos controle (sem GPU, sem acesso ao host) e menos operação.

## ❓ Perguntas típicas

- "Rodar contêineres sem gerenciar instâncias." → Fargate (com ECS ou EKS).
- "Processar arquivo por 2 horas sem gerenciar servidores." → Fargate (ou AWS Batch).
- "Como o Fargate é cobrado?" → Por vCPU e memória alocadas, por segundo.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Tasks ECS ou workloads EKS compatíveis e interfaces de rede |
| **O que você decide/configura?** | Recursos de CPU/memória suportados, imagem, roles e rede |
| **Em que ordem as coisas acontecem?** | Orquestrador solicita capacidade; Fargate executa container sem você manter o host |
| **O que pode fazer, e em que condição?** | Reduz administração dos servidores de containers |
| **O que não pode presumir?** | Não armazena imagens nem substitui ECS/EKS; aplicações ainda exigem segurança e dados persistentes adequados |

**Caso comentado:** Container de worker: ECR guarda imagem, ECS organiza, Fargate executa.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Fargate no ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
