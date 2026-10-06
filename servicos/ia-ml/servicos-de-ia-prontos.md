<!-- autoral -->

# Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate e Textract)

> **Categoria:** IA e serviços prontos · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** serviços que a AWS já treinou para tarefas comuns (conversar, falar, transcrever, traduzir, entender textos, analisar imagens e ler documentos), usados por chamadas de API, sem conhecimento de machine learning.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A secretaria tem uma lista de desejos: um chat que tire dúvidas da matrícula a qualquer hora, ler sozinha as certidões digitalizadas, transcrever as reuniões de pais, traduzir os comunicados para as famílias que não falam português e saber se os comentários da pesquisa de satisfação são positivos ou negativos. Ninguém na equipe sabe treinar modelos.

Cada desejo tem um serviço pronto. A AWS já treinou os modelos; a aplicação da escola só envia o pedido pela API e recebe o resultado. O **Lex** cria o chatbot, o **Textract** lê as certidões, o **Transcribe** transcreve as reuniões, o **Translate** traduz, o **Comprehend** identifica o sentimento dos comentários, o **Polly** lê os comunicados em voz alta e o **Rekognition** confere se a foto enviada mostra um rosto. Os serviços também se combinam: um áudio em inglês passa pelo Transcribe, pelo Translate e pelo Polly e vira voz em português.

O limite: cada serviço faz uma tarefa definida. Uma previsão que depende dos dados da própria escola, como o risco de abandono, exige um modelo próprio no [SageMaker AI](sagemaker-ai.md). E a escola continua responsável por como usa os resultados.

## Como funciona

1. A aplicação envia o conteúdo (texto, áudio, imagem ou documento) para a API do serviço.
2. O modelo pré-treinado da AWS processa o pedido.
3. O serviço devolve o resultado: texto, áudio, rótulos, campos ou o sentimento.
4. Paga-se pelo uso: caracteres, segundos de áudio, imagens, páginas ou pedidos.

## Opções principais

| Serviço | O que faz | Na escola |
|---|---|---|
| Amazon Lex | Chatbots por voz e texto | Chat que tira dúvidas da matrícula |
| Amazon Polly | Texto em fala | Ler os comunicados em voz alta |
| Amazon Transcribe | Fala em texto, separando quem falou | Transcrever as reuniões de pais |
| Amazon Translate | Tradução de textos | Comunicados em inglês |
| Amazon Comprehend | Linguagem natural: entidades, frases-chave, idioma e sentimento | Comentários positivos ou negativos |
| Amazon Rekognition | Imagens e vídeos: objetos, textos, conteúdo impróprio e rostos | Conferir se a foto mostra um rosto |
| Amazon Textract | Texto, formulários e tabelas de documentos, inclusive à mão | Ler as certidões digitalizadas |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Polly | Cobrado por caractere convertido em fala | 06/10/2026 |
| Transcribe | Cobrado por segundo de áudio, sem mínimo | 06/10/2026 |
| Translate | Por caractere; nível gratuito de 2 milhões de caracteres por mês por 12 meses | 06/10/2026 |
| Comprehend | Unidades de 100 caracteres, mínimo de 300 por pedido | 06/10/2026 |
| Rekognition | Por imagem analisada | 06/10/2026 |
| Textract | Por página; nível gratuito de 3 meses para clientes novos | 06/10/2026 |
| Lex | Por pedido ou por conversa contínua, sem compromisso | 06/10/2026 |

## Como é cobrado

Todos são cobrados pelo uso, sem compromisso inicial, cada um na sua unidade: caracteres (Polly, Translate, Comprehend), segundos de áudio (Transcribe), imagens (Rekognition), páginas (Textract) e pedidos ou conversas (Lex).

## Não confundir com

| Par | A diferença | Pista no enunciado |
|---|---|---|
| Polly × Transcribe | Polly: texto em fala. Transcribe: fala em texto | "Ler em voz alta" × "transcrever" |
| Textract × Rekognition | Textract: conteúdo de documentos. Rekognition: o que aparece em fotos e vídeos | "Formulário", "tabela" × "rosto", "objeto" |
| Comprehend × Translate | Comprehend: sentido do texto. Translate: troca o idioma | "Sentimento" × "traduzir" |
| Lex × [Amazon Q](amazon-q.md) | Lex: chatbot da empresa. Q: assistente para trabalhar com a AWS | "Chatbot para clientes" × "assistente da AWS" |
| Serviços prontos × [SageMaker AI](sagemaker-ai.md) | Prontos: modelo da AWS. SageMaker AI: modelo próprio | "Sem conhecimento de ML" × "treinar um modelo" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html) e [preços](https://aws.amazon.com/lex/pricing/)
- [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/what-is.html) e [preços](https://aws.amazon.com/polly/pricing/)
- [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html) e [preços](https://aws.amazon.com/transcribe/pricing/)
- [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html) e [preços](https://aws.amazon.com/translate/pricing/)
- [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) e [preços](https://aws.amazon.com/comprehend/pricing/)
- [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) e [preços](https://aws.amazon.com/rekognition/pricing/)
- [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) e [preços](https://aws.amazon.com/textract/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
