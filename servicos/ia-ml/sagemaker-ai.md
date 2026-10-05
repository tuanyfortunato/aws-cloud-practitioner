# Amazon SageMaker AI

> **Categoria:** IA / machine learning · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** plataforma completa para **construir, treinar e implantar modelos de ML próprios**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **laboratório completo para criar o seu próprio modelo** de machine learning: preparar dados, treinar, testar e colocar no ar.

- ✅ **Escolha quando:** precisa **construir, treinar e implantar modelos próprios** de ML.
- 🚫 **Não é a resposta quando:** quer usar **modelos prontos de IA generativa** → [Bedrock](bedrock.md); quer **APIs prontas** (imagem, texto, voz) → [serviços de IA prontos](servicos-de-ia-prontos.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "treinar modelo próprio", "cientistas de dados", "implantar modelo de ML".
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Preparação, treinamento, modelos, endpoints e jobs |
| **O que você decide/configura?** | Dados, algoritmo, infraestrutura, acesso e modalidade de inferência |
| **Em que ordem as coisas acontecem?** | Prepare dados, treine/avalie e disponibilize inferência |
| **O que pode fazer, e em que condição?** | Permite construir e operar modelos próprios |
| **O que não pode presumir?** | Não substitui dados de qualidade e validação; endpoint ativo pode gerar custo mesmo ocioso |

**Caso comentado:** Treinar modelo da empresa: SageMaker AI; converter texto em voz sem treino próprio: Polly.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
