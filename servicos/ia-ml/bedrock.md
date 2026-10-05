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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Modelos fundacionais, invocação e capacidades como bases/guardrails |
| **O que você decide/configura?** | Modelo, acesso, dados e integração suportada |
| **Em que ordem as coisas acontecem?** | Aplicação chama modelo e combina capacidades conforme necessidade |
| **O que pode fazer, e em que condição?** | Simplifica uso de modelos fundacionais sem administrar sua infraestrutura base |
| **O que não pode presumir?** | Não citado na lista não significa exclusão formal; resposta exige avaliação e controle de dados |

**Caso comentado:** Usar modelo fundacional difere de treinar modelo próprio; explique o objetivo antes de escolher.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
