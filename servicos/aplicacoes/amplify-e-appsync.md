# AWS Amplify, AWS AppSync e AWS Device Farm

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

## AWS Device Farm

- Testa apps **Android, iOS e web** em **dispositivos reais** e navegadores na nuvem (testes automatizados e acesso remoto).

## ⚠️ Não confundir

- AppSync (**GraphQL**) × API Gateway (**REST/HTTP/WebSocket**).
- Amplify (front-end + back-end rápido) × Elastic Beanstalk (aplicações web tradicionais) × Lightsail (servidor simples).

## ❓ Perguntas típicas

- "Criar e hospedar rapidamente um app web ou mobile full-stack." → Amplify.
- "API GraphQL gerenciada com dados em tempo real." → AppSync.
- "Testar o app em vários modelos de celular reais." → Device Farm.

## 🔗 Documentação oficial

- [Amplify](https://docs.amplify.aws/) · [AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) · [Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html)
