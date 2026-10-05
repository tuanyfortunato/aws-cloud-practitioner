# Desenvolvimento e aplicações (AppConfig, Infrastructure Composer, CodeGuru, Copilot, Refactor Spaces, AppFabric, SWF, WorkDocs)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Equipes podem precisar controlar configurações, apoiar análise de código ou modernizar aplicações. Esses trabalhos têm objetivos e ferramentas distintos.

**Como este serviço ajuda?** Esta ficha organiza ferramentas especializadas de desenvolvimento e aplicações, explicando sua finalidade e as restrições registradas no material.

**Exemplo do dia a dia:** Alterar uma configuração com controle é um problema diferente de analisar código ou dividir uma aplicação antiga em partes. Leia cada produto pelo trabalho que ele atende.

**O que ele não resolve sozinho?** Não existe uma ferramenta desta lista que faça toda a modernização sozinha. Há produtos antigos e restrições comerciais; a ficha está fora do escopo indicado da prova.

**Primeiras palavras para entender:**

- **Configuração:** valor que orienta o comportamento do programa.
- **Modernização:** mudança da forma de construir ou operar a aplicação.
- **Código:** instruções do programa.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Ferramentas de desenvolvedor e aplicações · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** ferramentas de desenvolvimento, modernização e colaboração que existem na AWS, mas não caem na prova.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Na prova, as ferramentas de desenvolvedor cobradas são só **AWS CLI, CodeBuild,
> CodePipeline e X-Ray**. Documentados aqui apenas para referência. Veja também
> [CodeDeploy, CodeArtifact e outros](../desenvolvimento/code-services.md) e [CloudShell](../desenvolvimento/cli-sdk-e-cloudshell.md),
> que também estão fora do escopo.

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Descubra se a tarefa envolve configuração, análise de código, modelagem de recursos ou modernização.

**Passo 2.** Leia o produto correspondente e suas condições atuais; não escolha apenas pelo nome da categoria.

**Passo 3.** Compare a ferramenta ao trabalho concreto. Algumas ofertas do material são históricas e têm restrições indicadas.

## 2. Recursos e opções, com significado

### AWS AppConfig

**Antes de ler este trecho:**

- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.
- **alarme:** Condição acompanhada sobre dados de monitoramento. Uma mudança de estado pode gerar ações configuradas; o alarme não diagnostica todo problema sozinho.
- **implantação:** Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.
- **rollback:** Retorno a uma configuração ou versão anterior, quando suportado e planejado. Nem toda alteração de dados pode ser desfeita automaticamente.


Parte do Systems Manager. Gerencia **feature flags** e **configuração dinâmica** de aplicações, com validação e implantação gradual (rollback automático se um alarme disparar).


Exemplo: ligar uma funcionalidade nova só para 10% dos usuários, sem novo deploy.


A lista oficial o coloca em "Database" (erro de categorização da própria página).

### AWS Infrastructure Composer (antigo AWS Application Composer)

**Antes de ler este trecho:**

- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **SAM:** Ferramentas de desenvolvimento e descrição de infraestrutura. CDK ajuda a definir recursos por programação; SAM é voltado a aplicações serverless compatíveis.


**Desenho visual** de arquiteturas serverless e de infraestrutura que gera templates do **CloudFormation/SAM**.

### Amazon CodeGuru

**Antes de ler este trecho:**

- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.


**CodeGuru Reviewer:** revisão automática de código com ML (🔄 fechado a novos clientes desde 07/11/2025).

**Antes de ler este trecho:**

- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.


**CodeGuru Profiler:** encontra trechos caros de CPU e latência em aplicações em execução.

**Antes de ler este trecho:**

- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.


**CodeGuru Security:** varredura de vulnerabilidades no código. Grande parte dessas funções migrou para o **Amazon Q Developer**.

### AWS Copilot

**Antes de ler este trecho:**

- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **CLI:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.


**CLI** para criar, publicar e operar aplicações em contêiner no ECS e no App Runner com poucos comandos (gera a infraestrutura com CloudFormation).

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.


🔄 **Fim de suporte em 12/06/2026**: segue como projeto open source, sem atualizações da AWS.

### AWS Migration Hub Refactor Spaces

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.


Ajuda a **modernizar aos poucos** uma aplicação monolítica (padrão *strangler fig*): cria o ambiente de rede e o roteamento para mover funcionalidades uma a uma para microsserviços.

### AWS AppFabric

**Antes de ler este trecho:**

- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.


Conecta aplicações **SaaS** (Slack, Zoom, Salesforce, Okta…) para **centralizar logs de segurança** e oferecer recursos de produtividade com IA generativa.

### Amazon Simple Workflow Service (SWF)

**Antes de ler este trecho:**

- **Step Functions:** Step Functions coordena fluxos de trabalho entre etapas e serviços compatíveis.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.


Serviço **legado** de coordenação de tarefas em fluxos de trabalho. A AWS recomenda o **Step Functions** (no escopo) para novos projetos.

### Amazon WorkDocs

Serviço de **armazenamento e colaboração de documentos** (editar, comentar, compartilhar). 🔄 **Encerrado em 25/04/2025** ✔️ (página oficial "Services in Full Shutdown").

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Não existe uma ferramenta desta lista que faça toda a modernização sozinha. Há produtos antigos e restrições comerciais; a ficha está fora do escopo indicado da prova.

### ⚠️ Como isso aparece na prova

**Antes de ler este trecho:**

- **SWF:** Simple Workflow Service: serviço de coordenação de trabalhos distribuídos com modelo próprio. É referência especializada, não sinônimo de todas as ferramentas de fluxo.


"Orquestrar etapas de um fluxo" → **Step Functions** (no escopo), não SWF.

**Antes de ler este trecho:**

- **CI / CD / CI/CD:** Integração contínua e entrega ou implantação contínua: práticas para construir, verificar e disponibilizar versões por etapas repetíveis.


"Esteira de CI/CD" → **CodePipeline**; "compilar e testar" → **CodeBuild** (no escopo).


"Infraestrutura como código" → **CloudFormation** (no escopo).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Alterar uma configuração com controle é um problema diferente de analisar código ou dividir uma aplicação antiga em partes. Leia cada produto pelo trabalho que ele atende.

**Aplicando a sequência à situação:**

**Etapa 1:** Descubra se a tarefa envolve configuração, análise de código, modelagem de recursos ou modernização.
**Etapa 2:** Leia o produto correspondente e suas condições atuais; não escolha apenas pelo nome da categoria.
**Etapa 3:** Compare a ferramenta ao trabalho concreto. Algumas ofertas do material são históricas e têm restrições indicadas.

**Resultado e responsabilidade:** Esta ficha organiza ferramentas especializadas de desenvolvimento e aplicações, explicando sua finalidade e as restrições registradas no material.

**Recursos envolvidos:** Ferramentas extras de configuração, modelagem, código e aplicações.

**Decisões que precisam ser tomadas:** Oferta atual e problema específico.

**Antes de ler este trecho:**

- **X-Ray:** X-Ray ajuda a acompanhar requisições em aplicações instrumentadas, reunindo rastreamentos e relações entre componentes.


**Outra situação comentada:** Para CLF-C02, diferencie CodeBuild/CodePipeline/X-Ray antes de aprofundar ferramentas extras.

**Por que não concluir mais do que isso:** Fora do escopo não implica produto recomendável atualmente; confira encerramentos

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Equipes podem precisar controlar configurações, apoiar análise de código ou modernizar aplicações. Esses trabalhos têm objetivos e ferramentas distintos.

**2. O que a solução fornece?**

Esta ficha organiza ferramentas especializadas de desenvolvimento e aplicações, explicando sua finalidade e as restrições registradas no material.

**3. Que conclusão seria incorreta?**

Não existe uma ferramenta desta lista que faça toda a modernização sozinha. Há produtos antigos e restrições comerciais; a ficha está fora do escopo indicado da prova.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) · [Infrastructure Composer](https://aws.amazon.com/infrastructure-composer/) · [CodeGuru](https://aws.amazon.com/codeguru/) · [Copilot](https://aws.github.io/copilot-cli/) · [Refactor Spaces](https://aws.amazon.com/migration-hub/features/) · [AppFabric](https://aws.amazon.com/appfabric/) · [SWF](https://aws.amazon.com/swf/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
