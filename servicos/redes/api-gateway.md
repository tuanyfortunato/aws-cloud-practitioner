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

## Tipos de API

| Tipo | Destaques | Uso |
|---|---|---|
| **REST API** | Mais recursos: **cache**, **usage plans e API keys**, validação de requisições, transformação, WAF, endpoints privados | APIs completas e gerenciadas |
| **HTTP API** | Mais simples, **mais barata** e de menor latência; JWT/OIDC nativo | Proxies para Lambda/HTTP |
| **WebSocket API** | Conexões bidirecionais persistentes | Chats, painéis em tempo real |

## Configurações importantes

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

## Cobrança

- Por **milhão de chamadas** (HTTP API é mais barata) + dados transferidos + cache-hora; WebSocket por mensagens e minutos de conexão.

## ⚠️ Pegadinhas e não confundir

- API Gateway (APIs REST/HTTP/WebSocket) × **AppSync** (APIs **GraphQL**).
- API Gateway × ALB: ambos podem chamar Lambda; API Gateway tem throttling, chaves de API, autenticação e cache.

## ❓ Perguntas típicas

- "Criar e proteger uma API REST para funções Lambda." → API Gateway.
- "Limitar requisições por cliente com chaves de API." → Usage plans + API keys.
- "API GraphQL gerenciada." → AppSync (não API Gateway).

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | API, routes/resources, stages, integrações e autorização |
| **O que você decide/configura?** | Tipo de API, endpoint, autenticação, throttling e integração |
| **Em que ordem as coisas acontecem?** | Recebe requisição e chama back-end conforme rota |
| **O que pode fazer, e em que condição?** | Publica e gerencia entrada de APIs sem administrar servidores de gateway |
| **O que não pode presumir?** | Não implementa a regra de negócio sozinho; autorização ainda precisa ser configurada |

**Caso comentado:** API chama função Lambda: API Gateway oferece entrada; Lambda executa lógica; IAM/authorizer controla acesso.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
