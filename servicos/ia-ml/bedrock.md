<!-- autoral -->

# Amazon Bedrock

> **Categoria:** IA generativa · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** referência
>
> **Em uma frase:** serviço totalmente gerenciado que dá acesso a modelos de fundação de várias empresas de IA para criar aplicações de IA generativa; não está na lista do exame.
>
> **Escopo oficial:** ⚪ Não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

A escola quer um assistente que responda dúvidas dos pais com base no regulamento escolar. Treinar um modelo de linguagem do zero está fora de alcance. Um **modelo de fundação** é um modelo grande, já treinado, que serve de base para muitas tarefas. O **Amazon Bedrock** dá acesso a modelos de várias empresas de IA por uma API, sem gerenciar servidores.

1. A equipe escolhe um modelo de fundação no Bedrock.
2. A aplicação envia o pedido pela API e recebe a resposta gerada.
3. Se precisar, a equipe personaliza o modelo, por exemplo com ajuste fino (*fine-tuning*).
4. A aplicação vai para produção sem que a escola gerencie a infraestrutura dos modelos.

O Bedrock aparece muito em materiais sobre a AWS, mas não está na lista de serviços do exame CLF-C02. O Amazon Q Developer, que está no escopo, roda sobre ele.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon Q](amazon-q.md) | Assistente de IA pronto para trabalhar com a AWS, no escopo | "Assistente", "perguntas sobre a AWS" |
| [Amazon SageMaker AI](sagemaker-ai.md) | Treinar e implantar modelos próprios, no escopo | "Treinar um modelo" |
| [Serviços de IA prontos](servicos-de-ia-prontos.md) | Tarefas definidas por API, no escopo | "Traduzir", "transcrever" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Serviços no escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
