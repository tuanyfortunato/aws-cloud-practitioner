# AWS Batch

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Você precisa processar muitos trabalhos que podem esperar sua vez, como converter milhares de arquivos, sem iniciar cada execução manualmente.

**Como este serviço ajuda?** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.

**Exemplo do dia a dia:** Uma produtora envia centenas de vídeos para conversão. Cada conversão vira um trabalho; o Batch agenda as execuções conforme a capacidade disponível.

**O que ele não resolve sozinho?** Batch organiza a execução, mas você fornece o programa que faz o trabalho. Ele não é a entrada interativa de um site nem um serviço que sabe converter qualquer arquivo sozinho.

**Primeiras palavras para entender:**

- **Job:** trabalho a executar.
- **Fila:** trabalhos aguardando execução.
- **Lote:** conjunto de trabalhos processados dessa forma.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação / processamento em lote · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)
>
> **Em uma frase:** executa grandes volumes de jobs em lote, escolhendo e provisionando automaticamente a computação ideal.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Prepare o programa que realiza um trabalho e descreva sua execução.

**Passo 2.** Envie trabalhos a uma fila e configure o ambiente de computação. Batch agenda as execuções conforme as necessidades e a capacidade.

**Passo 3.** Acompanhe resultados e falhas. Cada trabalho precisa gerar o resultado previsto e permitir tratamento de execução malsucedida.

## 2. Recursos e opções, com significado

### Para que serve

Milhares de jobs de processamento: renderização, simulações, genômica, análise financeira, ETL pesado.

Jobs que **duram mais de 15 min** (ao contrário do Lambda).

### Conceitos e componentes

**Job definition**

**O que é:** Imagem de contêiner, vCPU, memória, comando, retentativas, timeout.

**Job queue**

**O que é:** Fila com prioridade onde os jobs aguardam.

**Compute environment**

**O que é:** Onde os jobs rodam: **EC2 On-Demand, EC2 Spot, Fargate, Fargate Spot** ou EKS; gerenciado (a AWS escala) ou não gerenciado.

**Array jobs / dependências**

**O que é:** Milhares de jobs paralelos e encadeamento (job B após job A).

**Scheduling policies**

**O que é:** Fair-share entre usuários/times.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Batch organiza a execução, mas você fornece o programa que faz o trabalho. Ele não é a entrada interativa de um site nem um serviço que sabe converter qualquer arquivo sozinho.

### ⚠️ Pegadinhas e não confundir

Batch × Lambda: jobs longos e pesados × funções curtas por evento.

Batch × EMR: jobs genéricos em contêiner × frameworks de big data (Spark/Hadoop).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Sem custo próprio:** paga-se os recursos (EC2, Spot, Fargate). Combinar com **Spot** reduz muito o custo.

## 5. Caso resolvido: ligando as peças

Uma produtora envia centenas de vídeos para conversão. Cada conversão vira um trabalho; o Batch agenda as execuções conforme a capacidade disponível.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare o programa que realiza um trabalho e descreva sua execução.
**Etapa 2:** Envie trabalhos a uma fila e configure o ambiente de computação. Batch agenda as execuções conforme as necessidades e a capacidade.
**Etapa 3:** Acompanhe resultados e falhas. Cada trabalho precisa gerar o resultado previsto e permitir tratamento de execução malsucedida.

**Resultado e responsabilidade:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.

**Recursos envolvidos:** Job definition, job queue, compute environment e jobs.

**Decisões que precisam ser tomadas:** Container/comando, recursos, prioridade, tentativas e capacidade.

**Outra situação comentada:** Processar simulações independentes: jobs Batch, com resultados persistidos fora da execução efêmera.

**Por que não concluir mais do que isso:** Não é serviço de resposta HTTP contínua nem fornece computação gratuita

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Processar milhares de jobs em lote com a capacidade ideal."

**Resposta curta:** AWS Batch.

**Pergunta:** "Reduzir o custo de jobs em lote tolerantes a interrupção."

**Resposta curta:** Batch com instâncias Spot.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
