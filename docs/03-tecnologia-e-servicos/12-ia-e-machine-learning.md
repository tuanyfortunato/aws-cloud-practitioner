# 3.12 IA e machine learning

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma aplicação quer transcrever áudio, fazer previsões ou gerar texto. Embora todas envolvam IA, o trabalho necessário e a solução são diferentes.

**A ideia em palavras simples:** Serviços de IA podem oferecer funções prontas, ferramentas para desenvolver modelos próprios ou acesso a modelos generativos existentes. A escolha depende da tarefa.

**Exemplo do dia a dia:** Para transcrever uma aula, a escola avalia Transcribe. Para criar um modelo com seus dados, avalia SageMaker AI. Para gerar conteúdo com modelos existentes, há ofertas específicas.

**O que não concluir?** IA não garante precisão e não conhece automaticamente os dados da empresa. Compatibilidade, acesso, avaliação e escopo da prova precisam ser considerados.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Modelo de ML** | programa treinado com dados para prever ou classificar. |
| **IA generativa** | IA que cria conteúdo novo (texto, imagem, código). |
| **Modelo de fundação** | modelo grande, pré-treinado, usado como base para várias tarefas. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon SageMaker AI](../../servicos/ia-ml/sagemaker-ai.md) · [Amazon Bedrock](../../servicos/ia-ml/bedrock.md) · [Amazon Q](../../servicos/ia-ml/amazon-q.md) · [Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate, Textract, Kendra, Personalize…)](../../servicos/ia-ml/servicos-de-ia-prontos.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** No escopo: SageMaker AI, Amazon Q, Comprehend, Lex, Polly, Rekognition, Textract, Transcribe e Translate. **Bedrock** e **Kendra** não aparecem na lista atual; **Personalize** e **Fraud Detector** estão **fora do escopo**. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.11 Analytics](11-analytics.md) · 🏠 [Índice do domínio](README.md) · [3.13 Integração de aplicações](13-integracao-de-aplicacoes.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.
- **treinamento:** Ajuste de um modelo com dados. É uma etapa diferente de utilizar o modelo já treinado para responder a uma nova entrada.


Diferencie usar uma função pronta, construir um modelo próprio e usar um modelo generativo existente. Na função pronta, você solicita uma transformação específica. No modelo próprio, precisa preparar treinamento e avaliação. Na geração, fornece instrução e contexto para uma resposta.

Em todos os casos, dados e resultados exigem cuidado. Precisão não é garantida; acesso aos documentos deve ser autorizado; produzir uma resposta não a transforma em evidência. O requisito da tarefa e o escopo da prova orientam qual produto estudar.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como **comida**: o **SageMaker AI** é cozinhar do zero; o **Bedrock** é comprar uma massa pronta e montar o seu prato; os **serviços de IA prontos** são pratos congelados — cada um resolve uma refeição específica.

</details>

## 2. Conceitos e opções explicados

Revise a função de cada serviço, porque a prova pede o serviço pelo caso de uso.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **Amazon SageMaker AI / SageMaker AI:** SageMaker AI oferece recursos para etapas do desenvolvimento e operação de modelos.
- **AI / IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **Amazon Bedrock / Bedrock:** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Serviço | Função |
| --- | --- |
| Amazon SageMaker AI | Criar, treinar e implantar modelos de ML próprios |
| Amazon Bedrock | Usar modelos de IA generativa (foundation models) via API |
| Amazon Q | Assistente de IA generativa para empresas (Q Business) e desenvolvedores (Q Developer) |
| Amazon Rekognition | Análise de imagens e vídeos: rostos, objetos, textos, conteúdo impróprio |
| Amazon Comprehend | Processamento de linguagem natural: sentimento, entidades, idioma, tópicos |
| Amazon Lex | Chatbots e interfaces conversacionais por voz e texto (mesma tecnologia da Alexa) |
| Amazon Polly | Texto para fala |
| Amazon Transcribe | Fala para texto |
| Amazon Translate | Tradução de textos |
| Amazon Textract | Extrair texto, formulários e tabelas de documentos digitalizados |
| Amazon Kendra | Busca inteligente em documentos corporativos |

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.


**Primeiro, identifique o funcionamento:** Serviços prontos transformam entradas em resultados por API; SageMaker AI oferece recursos para preparar, treinar e servir modelos; Amazon Q entrega assistência conforme a variante.

**Depois, compare as escolhas:** Texto para voz: Polly. Voz para texto: Transcribe. Texto e sentimento: Comprehend. Documento e campos: Textract. Imagens: Rekognition. Conversação: Lex. Modelo próprio: SageMaker AI.

**Por fim, verifique o limite:** IA não garante resposta correta nem autorização para todo dado. Idioma, formato e região precisam ser suportados. Bedrock não citado na lista não implica automaticamente exclusão formal.

## 4. Caso resolvido

Um formulário escaneado tem tabelas e campos que precisam ser extraídos. Basta usar Comprehend?

**Raciocínio e resposta:** Textract atende a extração documental; Comprehend pode analisar o texto depois. Escolha pelo tipo de entrada e pelo resultado esperado.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma aplicação quer transcrever áudio, fazer previsões ou gerar texto. Embora todas envolvam IA, o trabalho necessário e a solução são diferentes.

**2. O que a solução fornece?**

Serviços de IA podem oferecer funções prontas, ferramentas para desenvolver modelos próprios ou acesso a modelos generativos existentes. A escolha depende da tarefa.

**3. Que conclusão seria incorreta?**

IA não garante precisão e não conhece automaticamente os dados da empresa. Compatibilidade, acesso, avaliação e escopo da prova precisam ser considerados.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Diferenciar **SageMaker AI** (modelo próprio) de **Bedrock** (modelos de fundação via API) e **Amazon Q** (assistente pronto).
- [ ] Ligar cada API pronta à tarefa: imagem → Rekognition; sentimento → Comprehend; chatbot → Lex; texto em fala → Polly; fala em texto → Transcribe; tradução → Translate; documentos → Textract.

**Dica de revisão para a prova:** Polly e Transcribe confundem: **P**olly **P**roduz fala (texto → voz); **Transcribe** transcreve (voz → texto). "Treinar modelo próprio" → **SageMaker AI**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Construir, treinar e implantar modelos de ML próprios."

**Resposta curta:** SageMaker AI.


**Fundamento explicado no capítulo:** "Construir, treinar e implantar modelos de ML próprios." → SageMaker AI.

**Pergunta:** "Identificar rostos e objetos em fotos."

**Resposta curta:** Rekognition.


**Fundamento explicado no capítulo:** "Identificar rostos e objetos em fotos." → Rekognition.

**Pergunta:** "Analisar o sentimento de avaliações de clientes."

**Resposta curta:** Comprehend.


**Fundamento explicado no capítulo:** "Analisar o sentimento de avaliações de clientes." → Comprehend.

**Pergunta:** "Criar um chatbot de atendimento."

**Resposta curta:** Lex.


**Fundamento explicado no capítulo:** "Criar um chatbot de atendimento." → Lex.

**Pergunta:** "Converter texto em voz."

**Resposta curta:** Polly. "Converter áudio em texto." → Transcribe.


**Fundamento explicado no capítulo:** "Converter texto em voz." → Polly. "Converter áudio em texto." → Transcribe.

**Pergunta:** "Traduzir conteúdo do site."

**Resposta curta:** Translate.


**Fundamento explicado no capítulo:** "Traduzir conteúdo do site." → Translate.

**Pergunta:** "Extrair dados de formulários escaneados."

**Resposta curta:** Textract.


**Fundamento explicado no capítulo:** "Extrair dados de formulários escaneados." → Textract.

**Pergunta:** "Busca inteligente nos documentos internos da empresa."

**Resposta curta:** Kendra.


**Fundamento explicado no capítulo:** "Busca inteligente nos documentos internos da empresa." → Kendra.

**Pergunta:** "Assistente de IA generativa para funcionários e desenvolvedores."

**Resposta curta:** Amazon Q.


**Fundamento explicado no capítulo:** "Assistente de IA generativa para funcionários e desenvolvedores." → Amazon Q.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- 🔄 **Nomes:** "Amazon **SageMaker AI**" (construir/treinar/implantar modelos próprios). Na prova pode aparecer "SageMaker".
- **Bedrock** = modelos de fundação via API (IA generativa sem treinar do zero). **Amazon Q** = assistente de IA generativa (Q Developer para código, Q Business para dados corporativos).
- **Associações frase → serviço (📌):** texto → fala = **Polly** · fala → texto = **Transcribe** · chatbot = **Lex** · sentimento/entidades = **Comprehend** · texto/formulários de documentos digitalizados = **Textract** (⚠️ não Rekognition) · rostos/objetos em imagem e vídeo = **Rekognition** · busca inteligente corporativa = **Kendra** · traduzir = **Translate**.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.11 Analytics](11-analytics.md) · 🏠 [Índice do domínio](README.md) · [3.13 Integração de aplicações](13-integracao-de-aplicacoes.md) ➡️
