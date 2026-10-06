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

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.

**Passo 1.** Separe a necessidade de publicar a interface da necessidade de uma API e de dados.

**Passo 2.** Prepare a hospedagem e as integrações compatíveis com o projeto, escolhendo a ferramenta apropriada para cada função.

**Passo 3.** Teste autenticação, dados e entrega. Uma interface publicada não demonstra que todas as operações internas funcionam corretamente.

## 2. Recursos e opções, com significado

### AWS Amplify

**Amplify Hosting**

**Antes de ler este trecho:**

- **CI / CD / CI/CD:** Integração contínua e entrega ou implantação contínua: práticas para construir, verificar e disponibilizar versões por etapas repetíveis.
- **HTTPS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **CDN:** Rede de distribuição de conteúdo. Ela aproxima entrega de conteúdo dos usuários e pode manter cópias em cache conforme as regras.
- **SSR:** Renderização de páginas no servidor. É diferente de entregar somente arquivos estáticos sem executar essa etapa de aplicação.

**Detalhe:** Hospedagem **full-stack** e de sites estáticos/SSR (React, Next.js, Vue, Angular) com CI/CD a partir do Git, CDN, domínios e HTTPS.

**Back-end (Gen 2)**

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **back-end:** Parte que processa regras e dados de uma aplicação. É diferente da interface que a pessoa vê no navegador ou aplicativo.

**Detalhe:** Define autenticação (Cognito), dados (AppSync/DynamoDB), armazenamento (S3) e funções (Lambda) em TypeScript.

**Bibliotecas e UI**

**Detalhe:** SDKs para web, iOS, Android, Flutter, React Native.

### AWS AppSync

**Antes de ler este trecho:**

- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.
- **GraphQL:** Forma de definir uma API e solicitar campos de dados. A aplicação ainda precisa de lógica de resolução, acesso e fontes adequadas.

**APIs GraphQL** gerenciadas: um endpoint que combina várias fontes (DynamoDB, Lambda, RDS, HTTP, OpenSearch).

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **WebSocket:** Comunicação que mantém uma conexão para troca de mensagens entre cliente e servidor. É diferente de uma sequência de pedidos web independentes.
- **OIDC:** Padrões de integração de identidade entre sistemas. Permitem que uma aplicação ou serviço confie em informações fornecidas por um provedor de identidade compatível.

**Tempo real** (subscriptions via WebSocket), **sincronização offline** em apps móveis, cache, autenticação (Cognito, IAM, OIDC, API key).

**Antes de ler este trecho:**

- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **pub/sub:** Publicação de uma mensagem para destinatários inscritos. Distribuir avisos a vários destinos é diferente de manter uma tarefa aguardando um consumidor.

**AppSync Events:** pub/sub serverless via WebSocket.

### AWS Device Farm ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

Testa apps **Android, iOS e web** em **dispositivos reais** e navegadores na nuvem (testes automatizados e acesso remoto).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Hospedar a interface não cria automaticamente todas as regras e dados da aplicação. AppSync tem escopo distinto; a ficha identifica o que priorizar na prova.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **REST:** Estilo de API que usa recursos e operações, frequentemente por HTTP. O código integrado continua sendo responsável pelo comportamento da aplicação.

AppSync (**GraphQL**) × API Gateway (**REST/HTTP/WebSocket**).

**Antes de ler este trecho:**

- **Elastic Beanstalk:** O Elastic Beanstalk ajuda a implantar aplicações em plataformas compatíveis, provisionando e coordenando recursos AWS para esse ambiente.
- **Lightsail:** O Lightsail reúne recursos como servidores virtuais, armazenamento e rede em ofertas simplificadas.
- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **front-end:** Parte da aplicação com que a pessoa interage. Publicá-la não cria automaticamente todas as operações e bancos da parte interna.

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

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

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
