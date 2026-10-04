# AWS Batch

> **Categoria:** Computação / processamento em lote · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)
>
> **Em uma frase:** executa grandes volumes de jobs em lote, escolhendo e provisionando automaticamente a computação ideal.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Milhares de jobs de processamento: renderização, simulações, genômica, análise financeira, ETL pesado.
- Jobs que **duram mais de 15 min** (ao contrário do Lambda).

## Conceitos e componentes

| Componente | O que é |
|---|---|
| **Job definition** | Imagem de contêiner, vCPU, memória, comando, retentativas, timeout. |
| **Job queue** | Fila com prioridade onde os jobs aguardam. |
| **Compute environment** | Onde os jobs rodam: **EC2 On-Demand, EC2 Spot, Fargate, Fargate Spot** ou EKS; gerenciado (a AWS escala) ou não gerenciado. |
| **Array jobs / dependências** | Milhares de jobs paralelos e encadeamento (job B após job A). |
| **Scheduling policies** | Fair-share entre usuários/times. |

## Cobrança

- **Sem custo próprio:** paga-se os recursos (EC2, Spot, Fargate). Combinar com **Spot** reduz muito o custo.

## ⚠️ Pegadinhas e não confundir

- Batch × Lambda: jobs longos e pesados × funções curtas por evento.
- Batch × EMR: jobs genéricos em contêiner × frameworks de big data (Spark/Hadoop).

## ❓ Perguntas típicas

- "Processar milhares de jobs em lote com a capacidade ideal." → AWS Batch.
- "Reduzir o custo de jobs em lote tolerantes a interrupção." → Batch com instâncias Spot.

## 🔗 Documentação oficial

- [Guia do AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
