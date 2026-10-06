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

## 1. A sequência de funcionamento

**Passo 1.** Separe a necessidade de publicar a interface da necessidade de uma API e de dados.

**Passo 2.** Prepare a hospedagem e as integrações compatíveis com o projeto, escolhendo a ferramenta apropriada para cada função.

**Passo 3.** Teste autenticação, dados e entrega. Uma interface publicada não demonstra que todas as operações internas funcionam corretamente.

## 2. Recursos e opções, com significado

### AWS Amplify

**Amplify Hosting**

**Detalhe:** Hospedagem **full-stack** e de sites estáticos/SSR (React, Next.js, Vue, Angular) com CI/CD a partir do Git, CDN, domínios e HTTPS.

**Back-end (Gen 2)**

**Detalhe:** Define autenticação (Cognito), dados (AppSync/DynamoDB), armazenamento (S3) e funções (Lambda) em TypeScript.

**Bibliotecas e UI**

**Detalhe:** SDKs para web, iOS, Android, Flutter, React Native.

### AWS AppSync

**APIs GraphQL** gerenciadas: um endpoint que combina várias fontes (DynamoDB, Lambda, RDS, HTTP, OpenSearch).

**Tempo real** (subscriptions via WebSocket), **sincronização offline** em apps móveis, cache, autenticação (Cognito, IAM, OIDC, API key).

**AppSync Events:** pub/sub serverless via WebSocket.

### AWS Device Farm ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

Testa apps **Android, iOS e web** em **dispositivos reais** e navegadores na nuvem (testes automatizados e acesso remoto).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Hospedar a interface não cria automaticamente todas as regras e dados da aplicação. AppSync tem escopo distinto; a ficha identifica o que priorizar na prova.

### ⚠️ Não confundir

AppSync (**GraphQL**) × API Gateway (**REST/HTTP/WebSocket**).

Amplify (front-end + back-end rápido) × Elastic Beanstalk (aplicações web tradicionais) × Lightsail (servidor simples).

## 4. Caso resolvido: ligando as peças

Uma equipe hospeda a interface do aplicativo com Amplify e avalia as integrações necessárias para cadastro e dados.

**Aplicando a sequência à situação:**

**Etapa 1:** Separe a necessidade de publicar a interface da necessidade de uma API e de dados.
**Etapa 2:** Prepare a hospedagem e as integrações compatíveis com o projeto, escolhendo a ferramenta apropriada para cada função.
**Etapa 3:** Teste autenticação, dados e entrega. Uma interface publicada não demonstra que todas as operações internas funcionam corretamente.

**Resultado e responsabilidade:** Amplify oferece ferramentas para desenvolvimento e hospedagem compatíveis. AppSync atende APIs GraphQL e outros recursos próprios; os papéis não são idênticos.

**Recursos envolvidos:** Aplicação/hosting/build do Amplify e API GraphQL do AppSync.

**Decisões que precisam ser tomadas:** Código, domínio, autenticação e integrações.

**Outra situação comentada:** Publicar front-end com integração AWS: Amplify; requisito específico GraphQL: entender AppSync como complemento.

**Por que não concluir mais do que isso:** Hosting não escreve regra de negócio; AppSync não aparece na lista consultada

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Criar e hospedar rapidamente um app web ou mobile full-stack."

**Resposta curta:** Amplify.

**Pergunta:** "API GraphQL gerenciada com dados em tempo real."

**Resposta curta:** AppSync.

**Pergunta:** "Testar o app em vários modelos de celular reais."

**Resposta curta:** Device Farm.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amplify](https://docs.amplify.aws/) · [AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) · [Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
