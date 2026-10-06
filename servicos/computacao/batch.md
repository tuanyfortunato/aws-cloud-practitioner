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

**Antes de ler este trecho:**

- **Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.

**Passo 1.** Prepare o programa que realiza um trabalho e descreva sua execução.

**Passo 2.** Envie trabalhos a uma fila e configure o ambiente de computação. Batch agenda as execuções conforme as necessidades e a capacidade.

**Passo 3.** Acompanhe resultados e falhas. Cada trabalho precisa gerar o resultado previsto e permitir tratamento de execução malsucedida.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **ETL:** Extrair dados de uma fonte, transformá-los e carregá-los num destino. A regra de transformação deve ser definida de acordo com o significado dos dados.

Milhares de jobs de processamento: renderização, simulações, genômica, análise financeira, ETL pesado.

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.

Jobs que **duram mais de 15 min** (ao contrário do Lambda).

### Conceitos e componentes

**Job definition**

**Antes de ler este trecho:**

- **vCPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **timeout:** Limite de espera ou duração. Ao excedê-lo, uma operação pode falhar ou exigir tratamento; não presuma que nada aconteceu antes da interrupção.
- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.
- **job:** Trabalho submetido a uma execução. Uma fila ou agendador organiza quando ele roda; seu programa realiza a tarefa.

**O que é:** Imagem de contêiner, vCPU, memória, comando, retentativas, timeout.

**Job queue**

**O que é:** Fila com prioridade onde os jobs aguardam.

**Compute environment**

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **EKS:** O EKS oferece Kubernetes gerenciado.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.

**O que é:** Onde os jobs rodam: **EC2 On-Demand, EC2 Spot, Fargate, Fargate Spot** ou EKS; gerenciado (a AWS escala) ou não gerenciado.

**Array jobs / dependências**

**O que é:** Milhares de jobs paralelos e encadeamento (job B após job A).

**Scheduling policies**

**O que é:** Fair-share entre usuários/times.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Batch organiza a execução, mas você fornece o programa que faz o trabalho. Ele não é a entrada interativa de um site nem um serviço que sabe converter qualquer arquivo sozinho.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **evento:** Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.

Batch × Lambda: jobs longos e pesados × funções curtas por evento.

**Antes de ler este trecho:**

- **EMR:** EMR oferece ambientes gerenciados para frameworks de processamento de dados, com modalidades diferentes de execução.
- **Spark:** Ferramenta de processamento de dados. O ambiente pode executar o trabalho distribuído, mas a equipe define o código e valida a transformação.

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

**Antes de ler este trecho:**

- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.

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
