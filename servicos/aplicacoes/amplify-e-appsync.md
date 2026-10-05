# AWS Amplify, AWS AppSync e AWS Device Farm

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe cria uma aplicação web ou móvel e precisa de apoio para hospedar a interface e integrar recursos de sua parte interna.

**Como este serviço ajuda?** Amplify oferece ferramentas para desenvolvimento e hospedagem compatíveis. AppSync atende APIs GraphQL e outros recursos próprios; os papéis não são idênticos.

**Exemplo do dia a dia:** Uma equipe hospeda a interface do aplicativo com Amplify e avalia as integrações necessárias para cadastro e dados.

**O que ele não resolve sozinho?** Hospedar a interface não cria automaticamente todas as regras e dados da aplicação. AppSync tem escopo distinto; a ficha identifica o que priorizar na prova.

**Primeiras palavras para entender:**

- **Front-end:** parte com que a pessoa interage.
- **Back-end:** parte que processa regras e dados.
- **GraphQL:** forma de definir e consultar uma API.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Front-end web e mobile · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)
>
> **Em uma frase:** ferramentas para criar, hospedar, conectar e testar aplicações web e mobile rapidamente.
>
> **Escopo oficial:** 🔀 Amplify ✅ · AppSync ⚪ não listado · Device Farm ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## AWS Amplify

| Recurso | Detalhe |
|---|---|
| **Amplify Hosting** | Hospedagem **full-stack** e de sites estáticos/SSR (React, Next.js, Vue, Angular) com CI/CD a partir do Git, CDN, domínios e HTTPS. |
| **Back-end (Gen 2)** | Define autenticação (Cognito), dados (AppSync/DynamoDB), armazenamento (S3) e funções (Lambda) em TypeScript. |
| **Bibliotecas e UI** | SDKs para web, iOS, Android, Flutter, React Native. |

## AWS AppSync

- **APIs GraphQL** gerenciadas: um endpoint que combina várias fontes (DynamoDB, Lambda, RDS, HTTP, OpenSearch).
- **Tempo real** (subscriptions via WebSocket), **sincronização offline** em apps móveis, cache, autenticação (Cognito, IAM, OIDC, API key).
- **AppSync Events:** pub/sub serverless via WebSocket.

## AWS Device Farm ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

- Testa apps **Android, iOS e web** em **dispositivos reais** e navegadores na nuvem (testes automatizados e acesso remoto).

## ⚠️ Não confundir

- AppSync (**GraphQL**) × API Gateway (**REST/HTTP/WebSocket**).
- Amplify (front-end + back-end rápido) × Elastic Beanstalk (aplicações web tradicionais) × Lightsail (servidor simples).

## ❓ Perguntas típicas

- "Criar e hospedar rapidamente um app web ou mobile full-stack." → Amplify.
- "API GraphQL gerenciada com dados em tempo real." → AppSync.
- "Testar o app em vários modelos de celular reais." → Device Farm.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Aplicação/hosting/build do Amplify e API GraphQL do AppSync |
| **O que você decide/configura?** | Código, domínio, autenticação e integrações |
| **Em que ordem as coisas acontecem?** | Implante front-end e conecte back-end conforme configuração |
| **O que pode fazer, e em que condição?** | Amplify facilita construir/implantar web/mobile; AppSync oferece API GraphQL |
| **O que não pode presumir?** | Hosting não escreve regra de negócio; AppSync não aparece na lista consultada |

**Caso comentado:** Publicar front-end com integração AWS: Amplify; requisito específico GraphQL: entender AppSync como complemento.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amplify](https://docs.amplify.aws/) · [AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) · [Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html)
