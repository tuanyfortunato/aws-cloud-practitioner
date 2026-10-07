<!-- autoral -->

# Amazon ECR (Elastic Container Registry)

> **Categoria:** Computação / Contêineres · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** registro gerenciado da AWS para guardar e distribuir imagens de container, com repositórios privados controlados pelo IAM e também repositórios públicos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Como funciona

A equipe da escola empacota o sistema de matrícula numa **imagem de container**: o programa com tudo o que ele precisa para rodar. O **Amazon ECR** é o lugar onde essa imagem fica guardada, para que o ECS, o EKS ou o Fargate a busquem na hora de executar.

1. A equipe cria um repositório privado no ECR e define pelo IAM quem pode enviar e baixar imagens.
2. Com a CLI, envia (*push*) a imagem do container para o repositório.
3. Opcionalmente, o ECR examina cada imagem enviada em busca de vulnerabilidades de software.
4. O orquestrador (ECS ou EKS) baixa (*pull*) a imagem e executa os containers; regras de ciclo de vida apagam as imagens antigas.

O limite: guardar a imagem no ECR não põe nada no ar. Quem executa é o [ECS](ecs.md), o [EKS](eks.md) ou o [Fargate](fargate.md).

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon ECS](ecs.md) | Executa e orquestra os containers | "Rodar containers" |
| [AWS Fargate](fargate.md) | Executa containers sem gerenciar servidores | "Sem gerenciar servidores" |
| [Amazon S3](../armazenamento/s3.md) | Guarda objetos de qualquer tipo, não é registro de imagens | "Arquivos", "objetos" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
- [O que é o Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/what-is-ecr.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
