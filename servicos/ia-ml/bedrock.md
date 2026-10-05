# Amazon Bedrock

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A aplicação quer usar modelos de IA generativa existentes, sem treinar do zero um grande modelo nem administrar sua infraestrutura de execução.

**Como este serviço ajuda?** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.

**Exemplo do dia a dia:** Uma aplicação pede a um modelo um resumo de um texto fornecido. A equipe avalia a resposta e define como esse recurso pode ser usado.

**O que ele não resolve sozinho?** Respostas podem conter erros; o serviço não garante verdade nem conhece automaticamente os documentos da empresa. O acesso aos dados e os mecanismos de avaliação precisam ser definidos.

**Primeiras palavras para entender:**

- **IA generativa:** produção de conteúdo, como texto.
- **Modelo de base:** modelo previamente treinado.
- **Prompt:** instrução e contexto enviados ao modelo.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** IA generativa · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** acesso **serverless via API** a modelos de fundação (foundation models) de vários provedores para criar aplicações de IA generativa.
>
> **Escopo oficial:** ⚪ Não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.


**Passo 1.** Escolha um modelo disponível e descreva a tarefa e o contexto que pretende enviar.

**Passo 2.** Integre a aplicação pelas interfaces e autorizações compatíveis. Avalie a resposta produzida para a finalidade desejada.

**Passo 3.** Controle dados, custos e qualidade. A geração de uma resposta não é comprovação de que o conteúdo está correto.

## 2. Recursos e opções, com significado

### Destaques

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **AI:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **Bedrock:** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.
- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **PII:** Informação que pode identificar uma pessoa. Sua identificação ajuda a planejar proteção de dados, mas não substitui avaliação do contexto e das regras aplicáveis.
- **RAG:** Recuperar informações de uma fonte e usá-las como contexto de geração. Isso não elimina erros nem autoriza acesso a todos os documentos.
- **AI21:** Nome de um fornecedor de modelos de IA. O acesso e a compatibilidade dependem da oferta indicada, não apenas do nome do fornecedor.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Modelos** | Amazon **Nova** e **Titan**, Anthropic **Claude**, Meta **Llama**, **Mistral**, Cohere, AI21, Stability AI, DeepSeek, entre outros. |
| **Knowledge Bases** | **RAG** gerenciado: conecta o modelo aos seus documentos (S3, bancos vetoriais) para respostas com base nos dados da empresa. |
| **Agents** | Agentes que executam tarefas em várias etapas chamando APIs/funções (🔄 o recurso original passou a se chamar **Bedrock Agents Classic** em 2026). **AgentCore** para implantar e operar agentes em produção. |
| **Guardrails** | Filtros de conteúdo nocivo, tópicos proibidos, **dados sensíveis (PII)**, alucinação (*grounding*). |
| **Customização** | Fine-tuning, continued pre-training, distillation (sem gerenciar infraestrutura). |
| **Avaliação** | Comparar modelos (automática ou humana). |
| **Privacidade** | ✔️ Seus prompts e dados **não** são usados para melhorar os modelos base nem compartilhados com os provedores dos modelos; dados ficam na região; PrivateLink. |
| **Playgrounds** | Testar modelos no console. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Respostas podem conter erros; o serviço não garante verdade nem conhece automaticamente os documentos da empresa. O acesso aos dados e os mecanismos de avaliação precisam ser definidos.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **SageMaker AI:** SageMaker AI oferece recursos para etapas do desenvolvimento e operação de modelos.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.


**Bedrock** (usar/customizar modelos prontos, serverless) × **SageMaker AI** (construir/treinar seus modelos, controle total) × **Amazon Q** (assistente pronto para usuários finais).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **throughput:** Quantidade de dados ou de trabalho processada por unidade de tempo. É diferente de latência, que mede quanto uma operação demora.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.


**On-demand** por tokens de entrada/saída (ou por imagem), **batch** (mais barato), **provisioned throughput** (capacidade reservada), customização e armazenamento de modelos.

## 5. Caso resolvido: ligando as peças

Uma aplicação pede a um modelo um resumo de um texto fornecido. A equipe avalia a resposta e define como esse recurso pode ser usado.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha um modelo disponível e descreva a tarefa e o contexto que pretende enviar.
**Etapa 2:** Integre a aplicação pelas interfaces e autorizações compatíveis. Avalie a resposta produzida para a finalidade desejada.
**Etapa 3:** Controle dados, custos e qualidade. A geração de uma resposta não é comprovação de que o conteúdo está correto.

**Resultado e responsabilidade:** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.

**Recursos envolvidos:** Modelos fundacionais, invocação e capacidades como bases/guardrails.

**Decisões que precisam ser tomadas:** Modelo, acesso, dados e integração suportada.


**Outra situação comentada:** Usar modelo fundacional difere de treinar modelo próprio; explique o objetivo antes de escolher.

**Por que não concluir mais do que isso:** Não citado na lista não significa exclusão formal; resposta exige avaliação e controle de dados

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A aplicação quer usar modelos de IA generativa existentes, sem treinar do zero um grande modelo nem administrar sua infraestrutura de execução.

**2. O que a solução fornece?**

Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.

**3. Que conclusão seria incorreta?**

Respostas podem conter erros; o serviço não garante verdade nem conhece automaticamente os documentos da empresa. O acesso aos dados e os mecanismos de avaliação precisam ser definidos.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Criar uma aplicação de IA generativa usando modelos de fundação via API, sem gerenciar infraestrutura."

**Resposta curta:** Bedrock.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.


**Fundamento explicado no capítulo:** "Criar uma aplicação de IA generativa usando modelos de fundação via API, sem gerenciar infraestrutura." → Bedrock.

**Pergunta:** "Chatbot que responde com base nos documentos internos (RAG)."

**Resposta curta:** Bedrock Knowledge Bases.


**Fundamento explicado no capítulo:** "Chatbot que responde com base nos documentos internos (RAG)." → Bedrock Knowledge Bases.

**Pergunta:** "Impedir que a aplicação de IA gere conteúdo impróprio ou exponha PII."

**Resposta curta:** Bedrock Guardrails.


**Fundamento explicado no capítulo:** "Impedir que a aplicação de IA gere conteúdo impróprio ou exponha PII." → Bedrock Guardrails.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
