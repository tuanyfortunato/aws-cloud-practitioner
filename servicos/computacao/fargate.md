# AWS Fargate

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
| **Tamanho da task/pod** | Você escolhe vCPU e memória (combinações predefinidas, de 0,25 vCPU até 16 vCPU / 120 GB 🧊). |
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
- Fargate × Lambda: contêiner sem limite de tempo × função até 15 min.
- Fargate × EC2 launch type: menos controle (sem GPU, sem acesso ao host) e menos operação.

## ❓ Perguntas típicas

- "Rodar contêineres sem gerenciar instâncias." → Fargate (com ECS ou EKS).
- "Processar arquivo por 2 horas sem gerenciar servidores." → Fargate (ou AWS Batch).
- "Como o Fargate é cobrado?" → Por vCPU e memória alocadas, por segundo.

## 🔗 Documentação oficial

- [Fargate no ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
