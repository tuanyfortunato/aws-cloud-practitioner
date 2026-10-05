# Amazon SageMaker AI

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe quer criar um modelo de aprendizado de máquina com seus dados e precisa de ferramentas para preparar, treinar, avaliar e disponibilizar esse modelo.

**Como este serviço ajuda?** SageMaker AI oferece recursos para etapas do desenvolvimento e operação de modelos. A equipe escolhe o processo, fornece dados e avalia a qualidade do resultado.

**Exemplo do dia a dia:** A escola usa um histórico autorizado para experimentar um modelo de previsão de demanda e verifica seu desempenho antes de usar previsões no planejamento.

**O que ele não resolve sozinho?** O serviço não garante previsões corretas nem dispensa dados adequados, avaliação e controle de acesso. Criar seu modelo é diferente de usar uma função de IA pronta.

**Primeiras palavras para entender:**

- **Modelo:** sistema que aprende padrões.
- **Treinamento:** ajuste com dados.
- **Inferência:** uso do modelo para produzir uma resposta.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** IA / machine learning · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** plataforma completa para **construir, treinar e implantar modelos de ML próprios**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.
- **treinamento:** Ajuste de um modelo com dados. É uma etapa diferente de utilizar o modelo já treinado para responder a uma nova entrada.
- **inferência:** Uso de um modelo para produzir um resultado com uma nova entrada. Pode acontecer sem um novo treinamento em cada solicitação.


**Passo 1.** Defina a tarefa, prepare dados adequados e escolha o processo de desenvolvimento do modelo.

**Passo 2.** Treine e avalie o modelo com critérios pertinentes. Separe dados e etapas de forma adequada ao método escolhido.

**Passo 3.** Disponibilize inferência compatível e acompanhe qualidade. Um resultado de treinamento não garante bom desempenho para toda entrada futura.

## 2. Recursos e opções, com significado

### Ciclo de ML e recursos

**Rotular dados**


**Recurso:** **Ground Truth** (rotulagem humana + automática)

**Preparar dados**


**Recurso:** **Data Wrangler** (no Canvas), **Feature Store**

**Construir**

**Antes de ler este trecho:**

- **IDE:** Ambiente de desenvolvimento com ferramentas para editar e trabalhar com código. Não é necessariamente o local que hospeda a aplicação em produção.


**Recurso:** **SageMaker Studio** (IDE, notebooks JupyterLab), algoritmos embutidos, frameworks (PyTorch, TensorFlow)

**Sem código**


**Recurso:** **SageMaker Canvas** (analistas de negócio criam modelos visualmente)

**AutoML**


**Recurso:** **Autopilot** (dentro do Canvas)

**Modelos prontos**


**Recurso:** **JumpStart** (modelos de fundação e soluções prontas)

**Treinar**

**Antes de ler este trecho:**

- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.


**Recurso:** Treinamento gerenciado, distribuído, com **Spot** (*managed spot training*), HyperPod para modelos grandes

**Ajustar**


**Recurso:** **Automatic Model Tuning** (hiperparâmetros)

**Explicar/viés**


**Recurso:** **Clarify** (detecção de viés e explicabilidade)

**Implantar**

**Antes de ler este trecho:**

- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.


**Recurso:** Endpoints **real-time**, **serverless**, **asynchronous** e **batch transform**

**Monitorar**


**Recurso:** **Model Monitor** (drift de dados/qualidade)

**MLOps**

**Antes de ler este trecho:**

- **MLOps:** Práticas para organizar desenvolvimento, implantação e acompanhamento de modelos. Não se resume a treinar uma vez e deixar o modelo sem observação.


**Recurso:** **Pipelines**, Model Registry

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.


O serviço não garante previsões corretas nem dispensa dados adequados, avaliação e controle de acesso. Criar seu modelo é diferente de usar uma função de IA pronta.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **SageMaker AI:** SageMaker AI oferece recursos para etapas do desenvolvimento e operação de modelos.
- **Bedrock:** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.


**SageMaker AI** (treinar **seus** modelos) × **Bedrock** (usar modelos de fundação prontos via API) × serviços de IA prontos (Rekognition, Comprehend…).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


Por instância/hora de notebook, treinamento e inferência + armazenamento; **SageMaker AI Savings Plans** (até 64%).

### 🔄 Atualizações 2025-2026

O serviço passou a se chamar **Amazon SageMaker AI**; o nome "Amazon SageMaker" virou a plataforma unificada de dados e IA (Unified Studio). Na prova pode aparecer "SageMaker".

## 5. Caso resolvido: ligando as peças

A escola usa um histórico autorizado para experimentar um modelo de previsão de demanda e verifica seu desempenho antes de usar previsões no planejamento.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina a tarefa, prepare dados adequados e escolha o processo de desenvolvimento do modelo.
**Etapa 2:** Treine e avalie o modelo com critérios pertinentes. Separe dados e etapas de forma adequada ao método escolhido.
**Etapa 3:** Disponibilize inferência compatível e acompanhe qualidade. Um resultado de treinamento não garante bom desempenho para toda entrada futura.

**Resultado e responsabilidade:** SageMaker AI oferece recursos para etapas do desenvolvimento e operação de modelos. A equipe escolhe o processo, fornece dados e avalia a qualidade do resultado.

**Recursos envolvidos:** Preparação, treinamento, modelos, endpoints e jobs.

**Decisões que precisam ser tomadas:** Dados, algoritmo, infraestrutura, acesso e modalidade de inferência.

**Antes de ler este trecho:**

- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.


**Outra situação comentada:** Treinar modelo da empresa: SageMaker AI; converter texto em voz sem treino próprio: Polly.

**Por que não concluir mais do que isso:** Não substitui dados de qualidade e validação; endpoint ativo pode gerar custo mesmo ocioso

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A equipe quer criar um modelo de aprendizado de máquina com seus dados e precisa de ferramentas para preparar, treinar, avaliar e disponibilizar esse modelo.

**2. O que a solução fornece?**

SageMaker AI oferece recursos para etapas do desenvolvimento e operação de modelos. A equipe escolhe o processo, fornece dados e avalia a qualidade do resultado.

**3. Que conclusão seria incorreta?**

O serviço não garante previsões corretas nem dispensa dados adequados, avaliação e controle de acesso. Criar seu modelo é diferente de usar uma função de IA pronta.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Construir, treinar e implantar modelos de ML próprios."

**Resposta curta:** SageMaker AI.

**Antes de ler este trecho:**

- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.


**Fundamento explicado no capítulo:** "Construir, treinar e implantar modelos de ML próprios." → SageMaker AI.

**Pergunta:** "Analista de negócio sem código quer criar previsões."

**Resposta curta:** SageMaker Canvas.


**Fundamento explicado no capítulo:** "Analista de negócio sem código quer criar previsões." → SageMaker Canvas.

**Pergunta:** "Detectar viés no modelo."

**Resposta curta:** SageMaker Clarify.


**Fundamento explicado no capítulo:** "Detectar viés no modelo." → SageMaker Clarify.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
