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

**Ao terminar este tópico, você deve saber:**

- [ ] Diferenciar **SageMaker AI** (modelo próprio) de **Bedrock** (modelos de fundação via API) e **Amazon Q** (assistente pronto).
- [ ] Ligar cada API pronta à tarefa: imagem → Rekognition; sentimento → Comprehend; chatbot → Lex; texto em fala → Polly; fala em texto → Transcribe; tradução → Translate; documentos → Textract.

<details>
<summary>Uma analogia para revisar a ideia</summary>

é como **comida**: o **SageMaker AI** é cozinhar do zero; o **Bedrock** é comprar uma massa pronta e montar o seu prato; os **serviços de IA prontos** são pratos congelados — cada um resolve uma refeição específica.

</details>

> 🎯 **Como não errar na prova:** Polly e Transcribe confundem: **P**olly **P**roduz fala (texto → voz); **Transcribe** transcreve (voz → texto). "Treinar modelo próprio" → **SageMaker AI**.

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon SageMaker AI](../../servicos/ia-ml/sagemaker-ai.md) · [Amazon Bedrock](../../servicos/ia-ml/bedrock.md) · [Amazon Q](../../servicos/ia-ml/amazon-q.md) · [Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate, Textract, Kendra, Personalize…)](../../servicos/ia-ml/servicos-de-ia-prontos.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** No escopo: SageMaker AI, Amazon Q, Comprehend, Lex, Polly, Rekognition, Textract, Transcribe e Translate. **Bedrock** e **Kendra** não aparecem na lista atual; **Personalize** e **Fraud Detector** estão **fora do escopo**. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.11 Analytics](11-analytics.md) · 🏠 [Índice do domínio](README.md) · [3.13 Integração de aplicações](13-integracao-de-aplicacoes.md) ➡️

---

## 📖 Conteúdo

Revise a função de cada serviço, porque a prova pede o serviço pelo caso de uso.

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

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Construir, treinar e implantar modelos de ML próprios." → SageMaker AI.
- "Identificar rostos e objetos em fotos." → Rekognition.
- "Analisar o sentimento de avaliações de clientes." → Comprehend.
- "Criar um chatbot de atendimento." → Lex.
- "Converter texto em voz." → Polly. "Converter áudio em texto." → Transcribe.
- "Traduzir conteúdo do site." → Translate.
- "Extrair dados de formulários escaneados." → Textract.
- "Busca inteligente nos documentos internos da empresa." → Kendra.
- "Assistente de IA generativa para funcionários e desenvolvedores." → Amazon Q.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** Serviços prontos transformam entradas em resultados por API; SageMaker AI oferece recursos para preparar, treinar e servir modelos; Amazon Q entrega assistência conforme a variante.

**Como escolher:** Texto para voz: Polly. Voz para texto: Transcribe. Texto e sentimento: Comprehend. Documento e campos: Textract. Imagens: Rekognition. Conversação: Lex. Modelo próprio: SageMaker AI.

**O que não concluir:** IA não garante resposta correta nem autorização para todo dado. Idioma, formato e região precisam ser suportados. Bedrock não citado na lista não implica automaticamente exclusão formal.

### Exercício de decisão

Um formulário escaneado tem tabelas e campos que precisam ser extraídos. Basta usar Comprehend?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Textract atende a extração documental; Comprehend pode analisar o texto depois. Escolha pelo tipo de entrada e pelo resultado esperado.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

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
