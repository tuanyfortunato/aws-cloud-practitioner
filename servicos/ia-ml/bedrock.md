# Amazon Bedrock

> **Categoria:** IA generativa · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** acesso **serverless via API** a modelos de fundação (foundation models) de vários provedores para criar aplicações de IA generativa.

## Destaques

| Item | Detalhe |
|---|---|
| **Modelos** | Amazon **Nova** e **Titan**, Anthropic **Claude**, Meta **Llama**, **Mistral**, Cohere, AI21, Stability AI, DeepSeek, entre outros. |
| **Knowledge Bases** | **RAG** gerenciado: conecta o modelo aos seus documentos (S3, bancos vetoriais) para respostas com base nos dados da empresa. |
| **Agents** | Agentes que executam tarefas em várias etapas chamando APIs/funções. **AgentCore** para implantar e operar agentes em produção. |
| **Guardrails** | Filtros de conteúdo nocivo, tópicos proibidos, **dados sensíveis (PII)**, alucinação (*grounding*). |
| **Customização** | Fine-tuning, continued pre-training, distillation (sem gerenciar infraestrutura). |
| **Avaliação** | Comparar modelos (automática ou humana). |
| **Privacidade** | Seus prompts e dados **não** são usados para treinar os modelos base; dados ficam na região; PrivateLink. |
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
