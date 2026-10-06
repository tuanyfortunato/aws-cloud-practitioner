<!-- autoral -->

# AWS Fargate

> **Categoria:** Computação serverless (containers) · **Domínio:** 1 (serverless) e 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** mecanismo de computação serverless que roda containers do ECS ou do EKS sem que você provisione ou gerencie servidores.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

O orquestrador decide quais containers rodam, mas eles precisam de máquinas para rodar. Em instâncias do EC2, a empresa escolhe o tipo, decide quantas instâncias manter, aplica patches e paga por capacidade sobrando quando a carga cai.

O Fargate tira esse trabalho: você empacota a aplicação, diz quanto de processador e memória ela precisa, configura rede e permissões, e o Fargate roda o container. Não há servidores para escolher, escalar ou atualizar. Ele funciona com o [ECS](ecs.md) e com o [EKS](eks.md).

O limite: o Fargate não é orquestrador; quem decide o que rodar é o ECS ou o EKS. E ele roda containers, não funções: para código curto disparado por eventos, o [Lambda](lambda.md) é mais direto. O Fargate também serve para tarefas longas, como a conversão de vídeos de duas horas da [aula 3.5](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md), que passa dos 15 minutos do Lambda.

## Como funciona

1. A imagem do container fica num registro, como o Amazon ECR.
2. Na definição da tarefa do ECS (ou do pod do EKS), você pede processador, memória e armazenamento e escolhe o Fargate como capacidade.
3. O Fargate baixa a imagem e roda o container numa capacidade que a AWS gerencia.
4. A cobrança corre do início do download da imagem até a tarefa terminar.

## Opções principais

| Opção | O que faz | Quando lembrar |
|---|---|---|
| Fargate | Capacidade serverless pelo preço normal | Aplicações que precisam ficar no ar |
| Fargate Spot (ECS) | Roda tarefas em capacidade sobrando, com até 70% de desconto, e pode interrompê-las com aviso de dois minutos | Tarefas que toleram interrupção |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Arredondamento da cobrança | Por segundo, com mínimo de 1 minuto | 06/10/2026 |
| Desconto do Fargate Spot | Até 70% | 06/10/2026 |

## Como é cobrado

Você paga pelo processador (vCPU), pela memória e pelo armazenamento que a tarefa ou o pod **pede**, do início do download da imagem até o fim da execução, arredondado para o segundo, com mínimo de um minuto. Não há custo antecipado. O Compute Savings Plans dá desconto no Fargate ([aula 4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)).

## Não confundir com

| Serviço | Diferença para o Fargate | Pista no enunciado |
|---|---|---|
| [Amazon ECS](ecs.md) e [Amazon EKS](eks.md) | Orquestram os containers; o Fargate é onde eles rodam | "Orquestrar containers" |
| [Amazon EC2](ec2.md) | Instâncias que você escolhe e administra | "Controle das instâncias" |
| [AWS Lambda](lambda.md) | Roda funções disparadas por eventos, por até 15 minutos por execução | "Código curto quando algo acontece" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [AWS Fargate para o Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
- [Preços do AWS Fargate](https://aws.amazon.com/fargate/pricing/)
- [Preços do Amazon ECS](https://aws.amazon.com/ecs/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
