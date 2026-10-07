<!-- autoral -->

# Amazon SageMaker AI

> **Categoria:** IA e machine learning · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** serviço de machine learning totalmente gerenciado para criar, treinar e implantar modelos próprios, sem montar nem gerenciar os servidores.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

A rede quer prever quais alunos correm risco de abandonar a escola. Nenhum serviço pronto faz isso: a resposta depende das notas, das faltas e do histórico dos alunos da própria rede. É preciso **treinar um modelo próprio**, e montar servidores com GPU, ferramentas e ambiente de produção para isso seria um projeto à parte.

O **SageMaker AI** entrega essa estrutura gerenciada. Cientistas de dados e desenvolvedores preparam os dados, treinam o modelo com algoritmos gerenciados ou com os frameworks que já usam e o **implantam** num ambiente hospedado pronto para produção, onde ele recebe dados novos e devolve previsões. Quem não programa pode usar o **SageMaker Canvas**, que cria modelos sem código.

O limite é de responsabilidade: a AWS cuida da infraestrutura, mas a escola escolhe os dados, treina, avalia o resultado e responde pelo uso do modelo. E, para tarefas comuns como ler documentos ou traduzir, um [serviço de IA pronto](servicos-de-ia-prontos.md) resolve sem treinamento.

## Como funciona

1. A equipe reúne e prepara os dados históricos, por exemplo no SageMaker Studio.
2. Treina o modelo com um algoritmo gerenciado ou o seu próprio, na capacidade que escolher.
3. Avalia o modelo e, se necessário, verifica vieses com o SageMaker Clarify.
4. Implanta o modelo num endpoint, que devolve previsões; o Model Monitor acompanha a qualidade em produção.

## Opções principais

| Recurso | O que faz | Exemplo na escola |
|---|---|---|
| SageMaker Studio | Ambiente web com ferramentas de desenvolvimento para ML | Equipe de dados trabalha nos notebooks |
| SageMaker Canvas | Cria modelos e previsões sem programar | Coordenação testa uma previsão de matrículas |
| JumpStart | Modelos pré-treinados e soluções prontas para implantar ou ajustar | Partir de um modelo pronto |
| Ground Truth | Cria conjuntos de dados rotulados para treino | Rotular redações por nível |
| Clarify | Detecta vieses e explica as previsões | Conferir se o modelo trata turmas de forma justa |
| Model Monitor | Acompanha o modelo em produção | Perceber quando os dados mudam |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| O que faz | Criar, treinar e implantar modelos | 06/10/2026 |
| Nome atual | SageMaker AI (antes Amazon SageMaker, renomeado em 03/12/2024) | 06/10/2026 |
| Formas de pagamento | Sob demanda, sem mínimo, ou Savings Plans do SageMaker | 06/10/2026 |

## Como é cobrado

Paga-se pelo que usa: instâncias de notebook, treinamento e endpoints, armazenamento e recursos usados. Há duas formas: sob demanda, sem taxa mínima nem compromisso, e os Savings Plans do SageMaker, com desconto em troca de um compromisso de uso. O SageMaker AI tem nível gratuito para começar.

## Não confundir com

| Serviço | Diferença para o SageMaker AI | Pista no enunciado |
|---|---|---|
| [Serviços de IA prontos](servicos-de-ia-prontos.md) | Modelos já treinados pela AWS, por API | "Sem conhecimento de ML", "traduzir", "ler documentos" |
| [Amazon Q](amazon-q.md) | Assistente de IA generativa | "Assistente", "perguntas sobre a AWS" |
| [Amazon Bedrock](bedrock.md) | Acesso a modelos de fundação para IA generativa | "Modelos de fundação" |
| [Amazon EMR](../analytics/emr.md) | Processamento de big data com Spark e Hadoop | "Spark", "Hadoop" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [Recursos do SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis-features.html)
- [Preços do Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
