# Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate, Textract, Kendra, Personalize…)

> **Categoria:** IA / serviços de alto nível · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** APIs de IA já treinadas pela AWS — você não precisa de experiência em ML, só chama a API.

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
| **Amazon Kendra** | Pergunta → resposta em documentos | **Busca inteligente corporativa** em linguagem natural (SharePoint, S3, Confluence) |
| **Amazon Personalize** | Interações → recomendações | **Recomendações personalizadas** (como na Amazon.com), ranking |
| **Amazon Fraud Detector** | Eventos → risco de fraude | Fraude em pagamentos/cadastros (🔄 fechado a novos clientes) |
| **Amazon Augmented AI (A2I)** | Previsões → revisão humana | Fluxos de revisão humana de previsões de ML |

## Pares que confundem

- **Textract × Rekognition:** documentos/formulários × imagens/rostos/objetos.
- **Polly × Transcribe:** texto→fala × fala→texto.
- **Comprehend × Kendra:** analisar texto × buscar respostas em documentos.
- **Lex × Connect:** chatbot × central de atendimento (que pode usar o Lex).

## 🔄 Atualizações 2025-2026

- Serviços mais antigos como Forecast, Lookout for Vision/Equipment/Metrics e Fraud Detector foram fechados a novos clientes — **não estudar**.

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
