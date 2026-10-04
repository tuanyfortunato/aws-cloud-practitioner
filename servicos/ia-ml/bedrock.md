# Amazon Bedrock

> **Categoria:** IA generativa · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** acesso **serverless via API** a modelos de fundação (foundation models) de vários provedores para criar aplicações de IA generativa.
>
> **Escopo oficial:** ⚪ Não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **loja de "cérebros" prontos**: você escolhe um modelo de IA generativa e usa pela API, sem treinar do zero.

- ✅ **Escolha quando:** precisa criar **aplicações de IA generativa** (chatbots, resumos, respostas sobre documentos) com modelos de fundação.
- 🚫 **Não é a resposta quando:** precisa **treinar um modelo próprio** → [SageMaker AI](sagemaker-ai.md); quer um **assistente pronto** → [Amazon Q](amazon-q.md). (O Bedrock não aparece na lista atual da prova.)
- 🎯 **Palavras do enunciado que apontam para ele:** "IA generativa", "modelos de fundação", "via API", "RAG".
<!-- didatico:fim -->

## Destaques

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

## Cobrança

- **On-demand** por tokens de entrada/saída (ou por imagem), **batch** (mais barato), **provisioned throughput** (capacidade reservada), customização e armazenamento de modelos.

## ⚠️ Não confundir

- **Bedrock** (usar/customizar modelos prontos, serverless) × **SageMaker AI** (construir/treinar seus modelos, controle total) × **Amazon Q** (assistente pronto para usuários finais).

## ❓ Perguntas típicas

- "Criar uma aplicação de IA generativa usando modelos de fundação via API, sem gerenciar infraestrutura." → Bedrock.
- "Chatbot que responde com base nos documentos internos (RAG)." → Bedrock Knowledge Bases.
- "Impedir que a aplicação de IA gere conteúdo impróprio ou exponha PII." → Bedrock Guardrails.

## 🔗 Documentação oficial

- [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
