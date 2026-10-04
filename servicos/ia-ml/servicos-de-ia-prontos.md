# Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate, Textract, Kendra, Personalize…)

> **Categoria:** IA / serviços de alto nível · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** APIs de IA já treinadas pela AWS — você não precisa de experiência em ML, só chama a API.
>
> **Escopo oficial:** 🔀 Comprehend, Lex, Polly, Rekognition, Textract, Transcribe e Translate ✅ · Kendra ⚪ não listado · Personalize e Fraud Detector ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** são **APIs que já vêm treinadas**: você manda a foto, o texto ou o áudio e recebe a resposta.

- ✅ **Escolha quando:** precisa de uma **capacidade de IA específica** sem ter experiência em machine learning.
- 🚫 **Não é a resposta quando:** precisa de um **modelo próprio** → [SageMaker AI](sagemaker-ai.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "rostos e objetos" → Rekognition; "sentimento" → Comprehend; "chatbot" → Lex; "texto em fala" → Polly; "fala em texto" → Transcribe; "formulários escaneados" → Textract; "traduzir" → Translate.
<!-- didatico:fim -->

## Tabela de associação (📌 decorar)

| Serviço | Entrada → saída | Recursos e casos de uso |
|---|---|---|
| **Amazon Rekognition** | **Imagem/vídeo** → rótulos | Rostos (detecção, comparação, busca), objetos, cenas, celebridades, texto em imagens, **moderação de conteúdo**, EPI, rastreamento de pessoas em vídeo |
| **Amazon Textract** | **Documento digitalizado** → texto estruturado | Extrai texto, **formulários (chave-valor)**, **tabelas**, assinaturas; APIs para notas fiscais e documentos de identidade |
| **Amazon Comprehend** | **Texto** → insights (NLP) | **Sentimento**, entidades, frases-chave, idioma, tópicos, PII; *Comprehend Medical* para textos clínicos |
| **Amazon Translate** | Texto → texto em outro idioma | Tradução neural em tempo real e em lote, terminologia customizada |
| **Amazon Polly** | **Texto → fala** | Vozes neurais, SSML, *lexicons* (pronúncia) |
| **Amazon Transcribe** | **Fala → texto** | Legendas, transcrição de chamadas, identificação de falantes, redação de PII; *Transcribe Medical*; *Call Analytics* |
| **Amazon Lex** | Conversa (voz/texto) → intenção | **Chatbots** e URAs (mesma tecnologia da Alexa); integra com Lambda e Connect |
| **Amazon Kendra** | Pergunta → resposta em documentos | **Busca inteligente corporativa** em linguagem natural (SharePoint, S3, Confluence). 🔄 Fechado a novos clientes desde 30/07/2026 e fora da lista atual |
| **Amazon Personalize** ❌ *fora do escopo* | Interações → recomendações | **Recomendações personalizadas** (como na Amazon.com), ranking |
| **Amazon Fraud Detector** ❌ *fora do escopo* | Eventos → risco de fraude | Fraude em pagamentos/cadastros (🔄 em manutenção, sem novos clientes desde 07/11/2025; ❌ fora do escopo) |
| **Amazon Augmented AI (A2I)** | Previsões → revisão humana | Fluxos de revisão humana de previsões de ML |

## Pares que confundem

- **Textract × Rekognition:** documentos/formulários × imagens/rostos/objetos.
- **Polly × Transcribe:** texto→fala × fala→texto.
- **Comprehend × Kendra:** analisar texto × buscar respostas em documentos.
- **Lex × Connect:** chatbot × central de atendimento (que pode usar o Lex).

## 🔄 Atualizações 2025-2026

- **Forecast:** fechado a novos clientes. **Lookout for Vision:** encerrado em 31/10/2025. **Lookout for Metrics:** encerrado em 12/09/2025. **Fraud Detector:** sem novos clientes desde 07/11/2025. **Kendra:** sem novos clientes desde 30/07/2026. Não estudar a fundo.
- **Personalize** e **Fraud Detector** estão declarados **fora do escopo** da prova.

## ❓ Perguntas típicas

- "Identificar rostos e objetos em fotos." → Rekognition.
- "Analisar o sentimento de avaliações." → Comprehend.
- "Criar um chatbot de atendimento." → Lex.
- "Converter texto em voz." → Polly. "Áudio em texto?" → Transcribe.
- "Traduzir o site." → Translate.
- "Extrair dados de formulários escaneados." → Textract.
- "Busca inteligente nos documentos internos." → Kendra.
- "Recomendar produtos aos clientes." → Personalize.

## 🔗 Documentação oficial

- [Serviços de IA da AWS](https://aws.amazon.com/ai/services/)
