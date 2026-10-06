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

## 1. A sequência de funcionamento

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

**Recurso:** **SageMaker Studio** (IDE, notebooks JupyterLab), algoritmos embutidos, frameworks (PyTorch, TensorFlow)

**Sem código**

**Recurso:** **SageMaker Canvas** (analistas de negócio criam modelos visualmente)

**AutoML**

**Recurso:** **Autopilot** (dentro do Canvas)

**Modelos prontos**

**Recurso:** **JumpStart** (modelos de fundação e soluções prontas)

**Treinar**

**Recurso:** Treinamento gerenciado, distribuído, com **Spot** (*managed spot training*), HyperPod para modelos grandes

**Ajustar**

**Recurso:** **Automatic Model Tuning** (hiperparâmetros)

**Explicar/viés**

**Recurso:** **Clarify** (detecção de viés e explicabilidade)

**Implantar**

**Recurso:** Endpoints **real-time**, **serverless**, **asynchronous** e **batch transform**

**Monitorar**

**Recurso:** **Model Monitor** (drift de dados/qualidade)

**MLOps**

**Recurso:** **Pipelines**, Model Registry

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

O serviço não garante previsões corretas nem dispensa dados adequados, avaliação e controle de acesso. Criar seu modelo é diferente de usar uma função de IA pronta.

### ⚠️ Não confundir

**SageMaker AI** (treinar **seus** modelos) × **Bedrock** (usar modelos de fundação prontos via API) × serviços de IA prontos (Rekognition, Comprehend…).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

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

**Outra situação comentada:** Treinar modelo da empresa: SageMaker AI; converter texto em voz sem treino próprio: Polly.

**Por que não concluir mais do que isso:** Não substitui dados de qualidade e validação; endpoint ativo pode gerar custo mesmo ocioso

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Construir, treinar e implantar modelos de ML próprios."

**Resposta curta:** SageMaker AI.

**Pergunta:** "Analista de negócio sem código quer criar previsões."

**Resposta curta:** SageMaker Canvas.

**Pergunta:** "Detectar viés no modelo."

**Resposta curta:** SageMaker Clarify.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
