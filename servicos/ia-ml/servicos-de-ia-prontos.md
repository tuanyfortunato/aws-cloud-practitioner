# Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate, Textract, Kendra, Personalize…)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A aplicação precisa de uma capacidade específica, como transcrever áudio ou extrair texto, e a equipe não quer desenvolver um modelo próprio para isso.

**Como este serviço ajuda?** Serviços de IA prontos oferecem funções delimitadas: Transcribe transforma fala em texto, Textract extrai conteúdo de documentos, Polly gera fala e outros atendem tradução, imagem ou linguagem.

**Exemplo do dia a dia:** A escola usa uma função de transcrição para produzir texto de uma gravação e revisa o resultado antes de disponibilizá-lo.

**O que ele não resolve sozinho?** Cada serviço trata um tipo de tarefa. Nenhum garante precisão perfeita nem deve ser escolhido só porque a pergunta menciona IA. Compatibilidade e escopo variam por produto.

**Primeiras palavras para entender:**

- **Transcrição:** fala convertida em texto.
- **Extração:** identificação de conteúdo.
- **API:** interface pela qual a aplicação pede a função.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** IA / serviços de alto nível · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** APIs de IA já treinadas pela AWS — você não precisa de experiência em ML, só chama a API.
>
> **Escopo oficial:** 🔀 Comprehend, Lex, Polly, Rekognition, Textract, Transcribe e Translate ✅ · Kendra ⚪ não listado · Personalize e Fraud Detector ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.

**Passo 1.** Identifique a transformação desejada, como fala para texto ou extração de campos.

**Passo 2.** Escolha o serviço específico e forneça uma entrada compatível com as permissões necessárias.

**Passo 3.** Avalie o resultado e trate erros. Produtos de tradução, voz, texto e imagem não são substitutos universais uns dos outros.

## 2. Recursos e opções, com significado

### Tabela de associação (📌 decorar)

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **AI:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **PII:** Informação que pode identificar uma pessoa. Sua identificação ajuda a planejar proteção de dados, mas não substitui avaliação do contexto e das regras aplicáveis.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **NLP:** Processamento de linguagem natural: tarefas de análise de texto ou fala. Não significa que um modelo sempre interpreta corretamente qualquer contexto.
- **A2I:** Amazon Augmented AI: integração de revisão humana em tarefas compatíveis. A participação humana é parte de um processo definido, não correção automática de todo resultado.
- **SSML:** Linguagem de marcação para controlar aspectos da síntese de fala em ferramentas compatíveis, como pronúncia e pausas.
- **EPI:** Equipamento de proteção individual. Aparece como contexto de análise de imagens, não como nome de um recurso AWS.

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

### Pares que confundem

**Textract × Rekognition:** documentos/formulários × imagens/rostos/objetos.

**Polly × Transcribe:** texto→fala × fala→texto.

**Comprehend × Kendra:** analisar texto × buscar respostas em documentos.

**Lex × Connect:** chatbot × central de atendimento (que pode usar o Lex).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Cada serviço trata um tipo de tarefa. Nenhum garante precisão perfeita nem deve ser escolhido só porque a pergunta menciona IA. Compatibilidade e escopo variam por produto.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

**Forecast:** fechado a novos clientes. **Lookout for Vision:** encerrado em 31/10/2025. **Lookout for Metrics:** encerrado em 12/09/2025. **Fraud Detector:** sem novos clientes desde 07/11/2025. **Kendra:** sem novos clientes desde 30/07/2026. Não estudar a fundo.

**Personalize** e **Fraud Detector** estão declarados **fora do escopo** da prova.

## 5. Caso resolvido: ligando as peças

A escola usa uma função de transcrição para produzir texto de uma gravação e revisa o resultado antes de disponibilizá-lo.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique a transformação desejada, como fala para texto ou extração de campos.
**Etapa 2:** Escolha o serviço específico e forneça uma entrada compatível com as permissões necessárias.
**Etapa 3:** Avalie o resultado e trate erros. Produtos de tradução, voz, texto e imagem não são substitutos universais uns dos outros.

**Resultado e responsabilidade:** Serviços de IA prontos oferecem funções delimitadas: Transcribe transforma fala em texto, Textract extrai conteúdo de documentos, Polly gera fala e outros atendem tradução, imagem ou linguagem.

**Recursos envolvidos:** APIs especializadas com entradas como texto, áudio, imagem e documento.

**Decisões que precisam ser tomadas:** Serviço, idioma/formato, processamento e acesso.

**Outra situação comentada:** Áudio para texto: Transcribe; texto para áudio: Polly. Inverter a direção muda a resposta.

**Por que não concluir mais do que isso:** Nenhum cobre todo tipo de IA nem garante acerto; serviços extras na ficha têm escopo próprio

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Identificar rostos e objetos em fotos."

**Resposta curta:** Rekognition.

**Pergunta:** "Analisar o sentimento de avaliações."

**Resposta curta:** Comprehend.

**Pergunta:** "Criar um chatbot de atendimento."

**Resposta curta:** Lex.

**Pergunta:** "Converter texto em voz."

**Resposta curta:** Polly. "Áudio em texto?" → Transcribe.

**Pergunta:** "Traduzir o site."

**Resposta curta:** Translate.

**Pergunta:** "Extrair dados de formulários escaneados."

**Resposta curta:** Textract.

**Pergunta:** "Busca inteligente nos documentos internos."

**Resposta curta:** Kendra.

**Pergunta:** "Recomendar produtos aos clientes."

**Resposta curta:** Personalize.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Serviços de IA da AWS](https://aws.amazon.com/ai/services/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
