<!-- autoral -->

# Amazon Q

> **Categoria:** IA generativa · **Domínio:** 3 · **Abrangência:** Console, documentação, IDEs, linha de comando e aplicativos de chat · **Ficha:** núcleo
>
> **Em uma frase:** família de assistentes de IA generativa da AWS; o Amazon Q Developer responde perguntas sobre a AWS e os recursos da conta e ajuda a escrever e melhorar código.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A equipe de TI da escola é pequena e aprende a AWS no caminho. Cada dúvida (qual serviço usar, por que a instância não aceita conexão, como escrever a função que redimensiona fotos) vira uma busca longa na documentação.

O **Amazon Q Developer** é um assistente conversacional de IA generativa que ajuda a entender, criar, estender e operar aplicações na AWS. No console, na documentação e no aplicativo móvel, ele responde perguntas sobre arquitetura, sobre os recursos da conta, boas práticas e suporte. Nos editores de código (IDEs) e na linha de comando, conversa sobre o código, sugere e gera código, procura vulnerabilidades e ajuda a atualizar versões de linguagem. Ele também atende em aplicativos de chat como Microsoft Teams e Slack. O Q Developer roda sobre o [Amazon Bedrock](bedrock.md).

O limite: as respostas são geradas por IA e precisam ser conferidas antes de ir para produção. Duas mudanças recentes: o **Amazon Q Business** não aceita mais clientes novos (a AWS indica o Amazon Quick), e os plugins do Q Developer para IDEs deixam de ter suporte em 30/04/2027.

## Como funciona

1. No console da AWS, quem tem as permissões necessárias no IAM abre o ícone do Amazon Q e faz a pergunta.
2. Nos IDEs, instala-se a extensão e entra-se com um AWS Builder ID, sem precisar de conta da AWS, no nível gratuito.
3. O Q responde com base em conteúdo de qualidade da AWS e pode responder sobre os recursos da conta.
4. Empresas podem assinar o nível Pro, com limites maiores e administração pelo IAM Identity Center.

## Opções principais

| Onde ou nível | O que oferece | Exemplo na escola |
|---|---|---|
| Console e documentação | Perguntas sobre serviços, recursos da conta e boas práticas | "Por que minha instância não aceita SSH?" |
| IDEs e linha de comando | Chat sobre código, sugestões, geração e varredura de segurança | Escrever a função que redimensiona fotos |
| Aplicativos de chat | Perguntas sobre a AWS no Teams ou no Slack | Equipe consulta pelo canal de TI |
| Nível gratuito | Recursos avançados com limite mensal de uso | Equipe pequena experimenta |
| Nível Pro | Limites maiores, administração e indenização de propriedade intelectual | Uso por toda a equipe |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Nível Pro | US$ 19 por usuário por mês | 06/10/2026 |
| Nível gratuito | 50 solicitações de agente por mês | 06/10/2026 |
| Fim do suporte aos plugins de IDE | 30/04/2027 | 06/10/2026 |
| Amazon Q Business | Fechado a novos clientes | 06/10/2026 |

## Como é cobrado

O Q Developer tem um nível gratuito, com limites mensais, e o nível Pro, cobrado por usuário por mês.

## Não confundir com

| Serviço | Diferença para o Amazon Q | Pista no enunciado |
|---|---|---|
| [Amazon Bedrock](bedrock.md) | Base para criar as próprias aplicações de IA generativa | "Modelos de fundação", "criar meu assistente" |
| [Amazon SageMaker AI](sagemaker-ai.md) | Treinar e implantar modelos próprios | "Treinar um modelo" |
| [Amazon Lex](servicos-de-ia-prontos.md) | Cria o chatbot para os clientes da empresa | "Chatbot para os pais" |
| [AWS Trusted Advisor](../gerenciamento/trusted-advisor.md) | Verificações automáticas de boas práticas | "Recomendações para a conta" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html)
- [Mudança de disponibilidade do Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html)
- [Preços do Amazon Q Developer](https://aws.amazon.com/q/developer/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
