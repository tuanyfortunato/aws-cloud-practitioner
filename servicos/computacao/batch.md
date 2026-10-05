# AWS Batch

> **Categoria:** Computação / processamento em lote · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)
>
> **Em uma frase:** executa grandes volumes de jobs em lote, escolhendo e provisionando automaticamente a computação ideal.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é como uma **linha de produção**: você entrega milhares de trabalhos e o Batch arranja as máquinas certas (inclusive as baratas, Spot) para processar tudo.

- ✅ **Escolha quando:** precisa processar **muitos jobs em lote**, longos ou pesados (renderização, simulações, análises).
- 🚫 **Não é a resposta quando:** é processamento **curto por evento** → [Lambda](lambda.md); é **big data com Spark/Hadoop** → [EMR](../analytics/emr.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "jobs em lote", "milhares de tarefas", "processamento batch", "capacidade ideal automaticamente".
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Job definition, job queue, compute environment e jobs |
| **O que você decide/configura?** | Container/comando, recursos, prioridade, tentativas e capacidade |
| **Em que ordem as coisas acontecem?** | Envie job para fila; Batch agenda em capacidade compatível |
| **O que pode fazer, e em que condição?** | Organiza processamento em lotes e dependências entre jobs |
| **O que não pode presumir?** | Não é serviço de resposta HTTP contínua nem fornece computação gratuita |

**Caso comentado:** Processar simulações independentes: jobs Batch, com resultados persistidos fora da execução efêmera.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
