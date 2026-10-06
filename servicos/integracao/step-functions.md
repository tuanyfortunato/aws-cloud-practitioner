# AWS Step Functions

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um processo tem várias etapas, algumas decisões e possibilidade de falha. Controlar toda essa sequência dentro de um único programa pode dificultar o acompanhamento.

**Como este serviço ajuda?** Step Functions coordena fluxos de trabalho entre etapas e serviços compatíveis. Você define a sequência, as decisões e o comportamento diante de falhas.

**Exemplo do dia a dia:** Uma matrícula passa por verificação, cobrança e confirmação. O fluxo coordena essas tarefas e registra o estado de cada execução.

**O que ele não resolve sozinho?** O serviço coordena as etapas; ele não escreve automaticamente o código que cobra ou verifica os dados. As etapas precisam existir e ter acessos configurados.

**Primeiras palavras para entender:**

- **Workflow:** fluxo de trabalho.
- **Estado:** etapa ou condição da execução.
- **Retry:** nova tentativa após determinada falha.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Integração de aplicações / orquestração · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** orquestra **fluxos de trabalho de várias etapas** como máquinas de estado visuais, com tratamento de erros e retentativas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Descreva etapas, decisões e tratamento de falhas do processo.

**Passo 2.** Inicie uma execução com seus dados de entrada. O fluxo coordena as etapas e os componentes que realizam as tarefas.

**Passo 3.** Examine estado e resultado da execução. A coordenação não escreve automaticamente o código de cada tarefa.

## 2. Recursos e opções, com significado

### Conceitos

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **Glue:** Glue oferece catálogo e ferramentas de integração e transformação de dados.
- **Bedrock:** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **JSON:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
- **retry:** Nova tentativa após uma falha. Repetir exige considerar o efeito da execução anterior para não duplicar resultados indevidamente.
- **workflow / state machine:** Fluxo de trabalho descrito por etapas, decisões e estados. Coordenar etapas é diferente de escrever o programa que realiza cada tarefa.
- **SDK:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.

| Item | Detalhe |
|---|---|
| **State machine** | Definida em JSON (Amazon States Language) ou desenhada no **Workflow Studio**. |
| **Estados** | **Task** (chama serviço), **Choice** (decisão), **Parallel**, **Map** (para cada item — inclusive *distributed map* sobre milhões de objetos do S3), **Wait**, **Pass**, **Succeed**, **Fail**. |
| **Erros** | `Retry` (com backoff) e `Catch` declarativos. |
| **Integrações** | Lambda, ECS/Fargate, Batch, DynamoDB, SNS, SQS, Glue, SageMaker, Bedrock e **200+ serviços via SDK**. |
| **Callback / aprovação humana** | Pausa o fluxo até receber um token (ex.: aprovação por e-mail). |

### Tipos de workflow

**Antes de ler este trecho:**

- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **streaming:** Fluxo contínuo de dados ou mídia. É diferente de esperar um arquivo completo antes de iniciar o trabalho.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.

| | **Standard** | **Express** |
|---|---|---|
| Duração máxima | Até **1 ano** | Até **5 minutos** |
| Execução | Exatamente uma vez | Pelo menos uma vez |
| Uso | Processos longos, auditáveis, com humanos | Alto volume de eventos (IoT, streaming) |
| Cobrança | Por transição de estado | Por execução, duração e memória |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

O serviço coordena as etapas; ele não escreve automaticamente o código que cobra ou verifica os dados. As etapas precisam existir e ter acessos configurados.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.
- **Step Functions:** Step Functions coordena fluxos de trabalho entre etapas e serviços compatíveis.

Step Functions (**orquestra** etapas com estado) × EventBridge (**roteia** eventos) × SQS (fila).

**Antes de ler este trecho:**

- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.
- **SWF:** Simple Workflow Service: serviço de coordenação de trabalhos distribuídos com modelo próprio. É referência especializada, não sinônimo de todas as ferramentas de fluxo.

**SWF** (Simple Workflow Service) é o antecessor legado.

Solução para "processo maior que 15 min com várias Lambdas" → Step Functions encadeando etapas.

## 4. Caso resolvido: ligando as peças

Uma matrícula passa por verificação, cobrança e confirmação. O fluxo coordena essas tarefas e registra o estado de cada execução.

**Aplicando a sequência à situação:**

**Etapa 1:** Descreva etapas, decisões e tratamento de falhas do processo.
**Etapa 2:** Inicie uma execução com seus dados de entrada. O fluxo coordena as etapas e os componentes que realizam as tarefas.
**Etapa 3:** Examine estado e resultado da execução. A coordenação não escreve automaticamente o código de cada tarefa.

**Resultado e responsabilidade:** Step Functions coordena fluxos de trabalho entre etapas e serviços compatíveis. Você define a sequência, as decisões e o comportamento diante de falhas.

**Recursos envolvidos:** State machine, states, execution e integrações.

**Decisões que precisam ser tomadas:** Sequência, branches, retries, catches e modalidade.

**Outra situação comentada:** Pedido exige validar, cobrar e confirmar: fluxo coordena etapas; cada tarefa mantém seus próprios limites.

**Por que não concluir mais do que isso:** Não transforma todo código longo numa única função convencional sem limite

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Orquestrar um processo com várias etapas e tratamento de erro."

**Resposta curta:** Step Functions.

**Pergunta:** "Fluxo de pedido com aprovação humana no meio."

**Resposta curta:** Step Functions (callback).

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
