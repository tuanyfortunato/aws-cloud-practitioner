<!-- autoral -->

# Amazon ECS (Elastic Container Service)

> **Categoria:** Computação (containers) · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** orquestrador de containers totalmente gerenciado da própria AWS, que decide onde e quantos containers rodam.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A empresa que mantém o sistema de matrícula empacotou a aplicação em **containers**, para que ela rode igual no computador do desenvolvedor e no servidor. Agora alguém precisa decidir em que máquinas cada container roda, quantas cópias manter, reiniciar as que falham e distribuir tudo entre as máquinas.

Esse trabalho é do **orquestrador**, e o ECS é o orquestrador da própria AWS, com as boas práticas da AWS embutidas e integração com o Amazon ECR (onde ficam as imagens) e com ferramentas como o Docker. A empresa descreve a aplicação, e o ECS mantém os containers rodando.

O limite: o ECS decide o que rodar, mas os containers precisam de capacidade para rodar, em instâncias do EC2 que você gerencia ou no Fargate, sem servidores. E se a empresa já usa Kubernetes, a resposta é o [EKS](eks.md).

## Como funciona

1. A imagem do container fica num registro, como o [Amazon ECR](ecr.md).
2. Uma **definição de tarefa** (*task definition*) descreve a aplicação: imagem, processador, memória, rede e permissões.
3. O ECS roda **tarefas** (trabalhos que terminam, como um lote) ou **serviços** (aplicações que ficam no ar, com um número de cópias mantido).
4. As tarefas rodam num **cluster**, na capacidade escolhida: Fargate, instâncias do EC2 ou servidores do próprio cliente.
5. O ECS reinicia tarefas que falham e mantém a quantidade pedida.

## Opções principais

| Capacidade | O que é | Quando usar |
|---|---|---|
| AWS Fargate | Serverless: sem servidores para escolher, escalar ou atualizar | Rodar containers sem cuidar de instâncias |
| Instâncias do EC2 | Você escolhe o tipo e o número de instâncias e gerencia a capacidade | Controle das instâncias, como tipos específicos |
| ECS Managed Instances | Instâncias do EC2 cujo gerenciamento fica com a AWS | Precisar de recursos específicos, como GPU, sem administrar as instâncias |
| ECS Anywhere | Registra servidores ou máquinas virtuais do próprio cliente no cluster | Containers no datacenter da empresa |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Cobrança pela orquestração do ECS | Nenhuma (paga-se a capacidade) | 06/10/2026 |

## Como é cobrado

A orquestração do ECS não tem cobrança adicional: você paga a capacidade em que os containers rodam. No Fargate, paga pelo processador, pela memória e pelo armazenamento que as tarefas pedem; no EC2, pelas instâncias. O ECS Managed Instances acrescenta uma taxa de gerenciamento por instância.

## Não confundir com

| Serviço | Diferença para o ECS | Pista no enunciado |
|---|---|---|
| [Amazon EKS](eks.md) | Kubernetes gerenciado, um orquestrador de código aberto | "Já usa Kubernetes", "mesmas ferramentas em vários ambientes" |
| [AWS Fargate](fargate.md) | Não orquestra: é a capacidade serverless onde o ECS ou o EKS rodam os containers | "Sem gerenciar servidores" |
| [Amazon ECR](ecr.md) | Guarda as imagens; não põe nada no ar | "Registro de imagens" |
| [AWS Lambda](lambda.md) | Roda funções curtas disparadas por eventos, sem containers para orquestrar | "Código que roda quando algo acontece" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [Preços do Amazon ECS](https://aws.amazon.com/ecs/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
