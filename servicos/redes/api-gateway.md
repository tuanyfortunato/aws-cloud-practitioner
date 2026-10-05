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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.


**Passo 1.** Descreva as operações que outro programa pode solicitar e seus dados de entrada.

**Passo 2.** Configure uma API e suas integrações e controles. Cada chamada segue para o componente que realiza o trabalho.

**Passo 3.** Observe falhas e acesso. A API não cria por si só o banco nem as regras que aprovam ou recusam uma operação.

## 2. Recursos e opções, com significado

### Tipos de API

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **WebSocket:** Comunicação que mantém uma conexão para troca de mensagens entre cliente e servidor. É diferente de uma sequência de pedidos web independentes.
- **REST:** Estilo de API que usa recursos e operações, frequentemente por HTTP. O código integrado continua sendo responsável pelo comportamento da aplicação.
- **OIDC:** Padrões de integração de identidade entre sistemas. Permitem que uma aplicação ou serviço confie em informações fornecidas por um provedor de identidade compatível.
- **JWT:** Formato de token com informações verificáveis. Receber um token não dispensa validar sua origem, condições e permissões na aplicação.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Tipo | Destaques | Uso |
|---|---|---|
| **REST API** | Mais recursos: **cache**, **usage plans e API keys**, validação de requisições, transformação, WAF, endpoints privados | APIs completas e gerenciadas |
| **HTTP API** | Mais simples, **mais barata** e de menor latência; JWT/OIDC nativo | Proxies para Lambda/HTTP |
| **WebSocket API** | Conexões bidirecionais persistentes | Chats, painéis em tempo real |

### Configurações importantes

**Antes de ler este trecho:**

- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **X-Ray:** X-Ray ajuda a acompanhar requisições em aplicações instrumentadas, reunindo rastreamentos e relações entre componentes.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **segundo:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.
- **TTL:** Tempo de vida de uma informação. Em DNS pode orientar cache; em um banco pode indicar expiração de itens. O efeito concreto depende do serviço.
- **ALB / NLB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.
- **ACM:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.
- **back-end:** Parte que processa regras e dados de uma aplicação. É diferente da interface que a pessoa vê no navegador ou aplicativo.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **GraphQL:** Forma de definir uma API e solicitar campos de dados. A aplicação ainda precisa de lógica de resolução, acesso e fontes adequadas.


API Gateway (APIs REST/HTTP/WebSocket) × **AppSync** (APIs **GraphQL**).

**Antes de ler este trecho:**

- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.


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

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Um aplicativo precisa pedir dados ou executar ações em outro sistema por uma interface controlada, em vez de acessar diretamente todos os componentes internos.

**2. O que a solução fornece?**

API Gateway ajuda a publicar e administrar APIs. Ele recebe chamadas e as encaminha a integrações configuradas, com opções de controle e acompanhamento.

**3. Que conclusão seria incorreta?**

Ele não escreve a regra de matrícula nem armazena os registros como um banco. Você define a API, seus acessos e a integração que realiza o trabalho.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Criar e proteger uma API REST para funções Lambda."

**Resposta curta:** API Gateway.


**Fundamento explicado no capítulo:** "Criar e proteger uma API REST para funções Lambda." → API Gateway.

**Pergunta:** "Limitar requisições por cliente com chaves de API."

**Resposta curta:** Usage plans + API keys.


**Fundamento explicado no capítulo:** "Limitar requisições por cliente com chaves de API." → Usage plans + API keys.

**Pergunta:** "API GraphQL gerenciada."

**Resposta curta:** AppSync (não API Gateway).


**Fundamento explicado no capítulo:** "API GraphQL gerenciada." → AppSync (não API Gateway).


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
