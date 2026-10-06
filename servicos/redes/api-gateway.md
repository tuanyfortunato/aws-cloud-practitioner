<!-- autoral -->

# Amazon API Gateway

> **Categoria:** Rede e entrada de APIs · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** cria, publica, mantém, monitora e protege APIs REST, HTTP e WebSocket em qualquer escala; a porta de entrada de back-ends serverless.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.10 Redes e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) · uso com Lambda em [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

O aplicativo da escola precisa consultar notas e enviar justificativas de falta. A lógica está em funções Lambda, mas alguém precisa receber os pedidos do aplicativo, conferir quem está chamando, limitar abusos e encaminhar cada pedido para a função certa.

O API Gateway é essa porta de entrada. Ele cria e publica **APIs** (REST, HTTP e WebSocket), que recebem os pedidos e os entregam a funções Lambda, serviços da AWS ou outros servidores web. Ele também cuida de controle de acesso, limite de pedidos (*throttling*) e monitoramento, em qualquer escala.

O limite: o API Gateway recebe e encaminha; a lógica fica no back-end, como o [Lambda](../computacao/lambda.md). E ele não substitui o balanceador para distribuir tráfego entre instâncias ([Elastic Load Balancing](../computacao/elastic-load-balancing.md)).

## Como funciona

1. Você cria uma API e define os recursos e métodos, como `GET /notas`.
2. Liga cada método a um back-end: uma função Lambda, outro serviço da AWS ou um endereço HTTP.
3. Configura autorização e limites de pedidos e publica a API num **estágio** (por exemplo, produção).
4. O aplicativo chama o endereço da API, e o API Gateway encaminha o pedido e devolve a resposta.

## Opções principais

| Tipo de API | O que faz | Pista no enunciado |
|---|---|---|
| REST API | Mais recursos: chaves de API, limite por cliente, validação, cache, integração com WAF e APIs privadas | "Chaves de API", "planos de uso", "cache" |
| HTTP API | Menos recursos, preço menor | "API simples para o Lambda pelo menor custo" |
| WebSocket API | Comunicação nos dois sentidos, com estado, entre cliente e servidor | "Chat", "atualização em tempo real" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Limite padrão de pedidos por conta e Região | 10.000 por segundo (ajustável), com rajada | 06/10/2026 |
| Tipos de API | 3 (REST, HTTP e WebSocket) | 06/10/2026 |

## Como é cobrado

Você paga pelas chamadas recebidas (preço por milhão) e pela transferência de dados de saída. As APIs WebSocket cobram mensagens e minutos de conexão. O cache das REST APIs é opcional e cobrado por hora, de acordo com o tamanho.

## Não confundir com

| Serviço | Diferença para o API Gateway | Pista no enunciado |
|---|---|---|
| [AWS Lambda](../computacao/lambda.md) | Roda a lógica; o API Gateway recebe os pedidos | "Código que processa o pedido" |
| [Elastic Load Balancing](../computacao/elastic-load-balancing.md) | Distribui tráfego entre instâncias ou containers | "Várias instâncias atrás de um endereço" |
| [Amazon CloudFront](cloudfront.md) | Entrega conteúdo com cache nos locais de borda | "Baixa latência no mundo todo" |
| [Amazon EventBridge](../integracao/eventbridge.md) | Roteia eventos entre serviços, não pedidos de clientes | "Reagir a eventos" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- [REST APIs ou HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)
- [Cotas do API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html)
- [Preços do Amazon API Gateway](https://aws.amazon.com/api-gateway/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
