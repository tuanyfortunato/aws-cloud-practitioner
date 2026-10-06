<!-- autoral -->

# AWS Batch

> **Categoria:** Computação / processamento em lote · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** serviço totalmente gerenciado para cargas em lote de qualquer escala: recebe as tarefas, provisiona a capacidade e a libera quando o trabalho acaba.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

No fim do bimestre, a secretaria gera milhares de boletins em PDF. O trabalho não precisa de resposta imediata, mas precisa de muita capacidade por algumas horas. O **AWS Batch** recebe as tarefas, sobe a capacidade necessária e distribui o trabalho, sem que a escola instale ou gerencie software de processamento em lote.

1. A equipe define o ambiente de computação: instâncias do EC2, Fargate ou ECS Managed Instances.
2. Cria uma fila e envia as tarefas (*jobs*), cada uma num container.
3. O Batch provisiona a capacidade de acordo com a quantidade e o tamanho das tarefas e as executa sobre o ECS ou o EKS.
4. Quando a fila esvazia, a capacidade é liberada.

O limite: o Batch é para trabalho que pode esperar na fila. Para reagir a um evento em segundos, a resposta costuma ser o [Lambda](lambda.md); o Batch também serve para tarefas longas demais para uma função Lambda.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Lambda](lambda.md) | Funções curtas disparadas por eventos | "Ao enviar um arquivo, execute" |
| [AWS Step Functions](../integracao/step-functions.md) | Coordena as etapas de um fluxo | "Fluxo com etapas" |
| [Amazon EMR](../analytics/emr.md) | Big data com Spark e Hadoop | "Spark", "Hadoop" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
