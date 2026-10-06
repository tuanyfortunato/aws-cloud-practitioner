<!-- autoral -->

# AWS Lambda

> **Categoria:** Computação serverless · **Domínio:** 1 (serverless) e 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** roda código em resposta a eventos sem que você provisione ou gerencie servidores, cobrando pelos pedidos e pela duração.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) · base em [1.1 O que é computação em nuvem](../../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A escola quer gerar uma miniatura toda vez que alguém envia uma foto. As fotos chegam algumas vezes por dia, sem horário certo. Deixar uma instância EC2 ligada o tempo todo esperando por elas significa pagar por horas paradas e ainda cuidar de sistema operacional e patches.

O Lambda roda o código só quando algo acontece. Você escreve uma **função** e a liga a um **gatilho**, como um arquivo novo no S3, um pedido no API Gateway, uma mensagem numa fila do SQS ou uma regra do EventBridge. A AWS cuida dos servidores, da capacidade, do escalonamento e dos patches, e cobra só pelas execuções. É o exemplo de **serverless** da [aula 1.1](../../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md).

O limite: uma execução comum dura **até 15 minutos**, e cada execução é independente, sem guardar estado para a próxima. Uma conversão de vídeo de duas horas cabe melhor em containers com Fargate, no AWS Batch ou no EC2 ([aula 3.5](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)).

## Como funciona

1. Você escreve a função numa linguagem que o Lambda roda e escolhe a **memória**; o processamento é proporcional a ela.
2. Liga a função a um gatilho e dá a ela uma **função de execução** do IAM, com as permissões de que precisa (por exemplo, ler e gravar no S3).
3. Quando o evento acontece, o Lambda cria um ambiente de execução e roda o código. Muitos eventos ao mesmo tempo viram muitas execuções em paralelo.
4. A função entrega o resultado a outro serviço, como gravar a miniatura no S3. O que precisa durar fica num armazenamento, não na função.

## Opções principais

| Opção | O que faz | Quando lembrar |
|---|---|---|
| Memória | De 128 MB a 10.240 MB; o processamento cresce junto | Não existe "escolher vCPU" no Lambda: aumenta-se a memória |
| Tempo limite (*timeout*) | Até 15 minutos por execução | Tarefas mais longas vão para outro serviço |
| Concorrência provisionada | Mantém ambientes já iniciados, prontos para responder | Eliminar a demora da primeira execução (*cold start*) |
| Arquitetura arm64 (Graviton) | Roda a função em processadores Graviton2 | Melhor relação entre preço e desempenho que a x86 |
| Funções duráveis (*durable functions*) | Aplicações de várias etapas que salvam o progresso e podem durar até um ano | Processos longos com espera; não confundir com uma execução comum |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Duração máxima de uma execução comum | 15 minutos | 06/10/2026 |
| Memória | De 128 MB a 10.240 MB | 06/10/2026 |
| Nível gratuito | 1 milhão de pedidos e 400.000 GB-segundo por mês | 06/10/2026 |

## Como é cobrado

Você paga pelos **pedidos** (preço por milhão) e pela **duração** em GB-segundo, que combina o tempo de execução com a memória escolhida. O nível gratuito cobre 1 milhão de pedidos e 400.000 GB-segundo por mês. Função parada, sem eventos, não gera cobrança de pedidos nem de duração.

Alguns recursos cobram à parte: a concorrência provisionada é cobrada pelo tempo em que fica configurada, mesmo sem execuções; o armazenamento temporário acima de 512 MB também é cobrado. O Compute Savings Plans dá desconto no Lambda ([aula 4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)).

## Não confundir com

| Serviço | Diferença para o Lambda | Pista no enunciado |
|---|---|---|
| [Amazon EC2](ec2.md) | Servidor virtual com controle do sistema operacional, cobrado enquanto está ligado | "Controle do sistema operacional", "software legado" |
| [AWS Fargate](fargate.md) | Roda containers sem servidores para gerenciar, sem o limite de 15 minutos | "Container", "tarefa de horas sem servidor" |
| [AWS Step Functions](../integracao/step-functions.md) | Encadeia várias funções num fluxo de etapas | "Processo de várias etapas", "passa de 15 minutos" |
| [AWS Batch](batch.md) | Roda grandes volumes de trabalhos em lote, escolhendo a computação | "Milhares de jobs em lote" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Cotas do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Memória da função](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html)
- [Tempo limite da função](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html)
- [Concorrência provisionada](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)
- [Funções duráveis](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Arquitetura arm64](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html)
- [Preços do AWS Lambda](https://aws.amazon.com/lambda/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
