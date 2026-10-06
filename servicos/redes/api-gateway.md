# Amazon API Gateway

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um aplicativo precisa pedir dados ou executar ações em outro sistema por uma interface controlada, em vez de acessar diretamente todos os componentes internos.

**Como este serviço ajuda?** API Gateway ajuda a publicar e administrar APIs. Ele recebe chamadas e as encaminha a integrações configuradas, com opções de controle e acompanhamento.

**Exemplo do dia a dia:** O aplicativo da escola chama uma API para consultar matrículas. API Gateway recebe a chamada e a encaminha ao código que realiza a consulta.

**O que ele não resolve sozinho?** Ele não escreve a regra de matrícula nem armazena os registros como um banco. Você define a API, seus acessos e a integração que realiza o trabalho.

**Primeiras palavras para entender:**

- **API:** interface para programas conversarem.
- **Chamada:** pedido feito a essa interface.
- **Integração:** componente acionado para atender o pedido.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Rede / front-end de APIs · **Domínio:** 3 · **Escopo:** Regional (endpoints edge-optimized usam CloudFront) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** cria, publica, protege e monitora APIs em qualquer escala — a "porta da frente" de back-ends serverless.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Descreva as operações que outro programa pode solicitar e seus dados de entrada.

**Passo 2.** Configure uma API e suas integrações e controles. Cada chamada segue para o componente que realiza o trabalho.

**Passo 3.** Observe falhas e acesso. A API não cria por si só o banco nem as regras que aprovam ou recusam uma operação.

## 2. Recursos e opções, com significado

### Tipos de API

| Tipo | Destaques | Uso |
|---|---|---|
| **REST API** | Mais recursos: **cache**, **usage plans e API keys**, validação de requisições, transformação, WAF, endpoints privados | APIs completas e gerenciadas |
| **HTTP API** | Mais simples, **mais barata** e de menor latência; JWT/OIDC nativo | Proxies para Lambda/HTTP |
| **WebSocket API** | Conexões bidirecionais persistentes | Chats, painéis em tempo real |

### Configurações importantes

| Item | Detalhe |
|---|---|
| **Integrações** | **Lambda** (clássico serverless), HTTP, serviços AWS (ex.: gravar direto no SQS/DynamoDB), VPC link (recursos privados via NLB/ALB). |
| **Tipos de endpoint** | **Edge-optimized** (via CloudFront), **Regional**, **Private** (só da VPC via interface endpoint). |
| **Autorização** | **IAM**, **Cognito user pools**, **Lambda authorizer**, JWT (HTTP API). |
| **Throttling** | Limites de requisições por segundo (conta, stage, método, usage plan) → protege o back-end. Padrão: **10.000 req/s por conta e região**, burst de 5.000 (algumas regiões novas: 2.500 / 1.250) 🧊. |
| **Stages** | `dev`, `prod`… com variáveis e deploys separados; *canary release*. |
| **Cache** | Respostas em cache por TTL (REST). |
| **Domínio customizado** | Com certificado do ACM. |
| **Monitoramento** | CloudWatch (métricas, logs de acesso), X-Ray. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não escreve a regra de matrícula nem armazena os registros como um banco. Você define a API, seus acessos e a integração que realiza o trabalho.

### ⚠️ Pegadinhas e não confundir

API Gateway (APIs REST/HTTP/WebSocket) × **AppSync** (APIs **GraphQL**).

API Gateway × ALB: ambos podem chamar Lambda; API Gateway tem throttling, chaves de API, autenticação e cache.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por **milhão de chamadas** (HTTP API é mais barata) + dados transferidos + cache-hora; WebSocket por mensagens e minutos de conexão.

## 5. Caso resolvido: ligando as peças

O aplicativo da escola chama uma API para consultar matrículas. API Gateway recebe a chamada e a encaminha ao código que realiza a consulta.

**Aplicando a sequência à situação:**

**Etapa 1:** Descreva as operações que outro programa pode solicitar e seus dados de entrada.
**Etapa 2:** Configure uma API e suas integrações e controles. Cada chamada segue para o componente que realiza o trabalho.
**Etapa 3:** Observe falhas e acesso. A API não cria por si só o banco nem as regras que aprovam ou recusam uma operação.

**Resultado e responsabilidade:** API Gateway ajuda a publicar e administrar APIs. Ele recebe chamadas e as encaminha a integrações configuradas, com opções de controle e acompanhamento.

**Recursos envolvidos:** API, routes/resources, stages, integrações e autorização.

**Decisões que precisam ser tomadas:** Tipo de API, endpoint, autenticação, throttling e integração.

**Outra situação comentada:** API chama função Lambda: API Gateway oferece entrada; Lambda executa lógica; IAM/authorizer controla acesso.

**Por que não concluir mais do que isso:** Não implementa a regra de negócio sozinho; autorização ainda precisa ser configurada

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Criar e proteger uma API REST para funções Lambda."

**Resposta curta:** API Gateway.

**Pergunta:** "Limitar requisições por cliente com chaves de API."

**Resposta curta:** Usage plans + API keys.

**Pergunta:** "API GraphQL gerenciada."

**Resposta curta:** AppSync (não API Gateway).

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
