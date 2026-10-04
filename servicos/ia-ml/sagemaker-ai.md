# Amazon SageMaker AI

> **Categoria:** IA / machine learning · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** plataforma completa para **construir, treinar e implantar modelos de ML próprios**.

## Ciclo de ML e recursos

| Etapa | Recurso |
|---|---|
| Rotular dados | **Ground Truth** (rotulagem humana + automática) |
| Preparar dados | **Data Wrangler** (no Canvas), **Feature Store** |
| Construir | **SageMaker Studio** (IDE, notebooks JupyterLab), algoritmos embutidos, frameworks (PyTorch, TensorFlow) |
| Sem código | **SageMaker Canvas** (analistas de negócio criam modelos visualmente) |
| AutoML | **Autopilot** (dentro do Canvas) |
| Modelos prontos | **JumpStart** (modelos de fundação e soluções prontas) |
| Treinar | Treinamento gerenciado, distribuído, com **Spot** (*managed spot training*), HyperPod para modelos grandes |
| Ajustar | **Automatic Model Tuning** (hiperparâmetros) |
| Explicar/viés | **Clarify** (detecção de viés e explicabilidade) |
| Implantar | Endpoints **real-time**, **serverless**, **asynchronous** e **batch transform** |
| Monitorar | **Model Monitor** (drift de dados/qualidade) |
| MLOps | **Pipelines**, Model Registry |

## Cobrança

- Por instância/hora de notebook, treinamento e inferência + armazenamento; **SageMaker AI Savings Plans** (até 64%).

## 🔄 Atualizações 2025-2026

- O serviço passou a se chamar **Amazon SageMaker AI**; o nome "Amazon SageMaker" virou a plataforma unificada de dados e IA (Unified Studio). Na prova pode aparecer "SageMaker".

## ⚠️ Não confundir

- **SageMaker AI** (treinar **seus** modelos) × **Bedrock** (usar modelos de fundação prontos via API) × serviços de IA prontos (Rekognition, Comprehend…).

## ❓ Perguntas típicas

- "Construir, treinar e implantar modelos de ML próprios." → SageMaker AI.
- "Analista de negócio sem código quer criar previsões." → SageMaker Canvas.
- "Detectar viés no modelo." → SageMaker Clarify.

## 🔗 Documentação oficial

- [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
