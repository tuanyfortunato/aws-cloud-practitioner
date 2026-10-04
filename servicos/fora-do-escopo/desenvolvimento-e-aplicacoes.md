# Desenvolvimento e aplicações (AppConfig, Infrastructure Composer, CodeGuru, Copilot, Refactor Spaces, AppFabric, SWF, WorkDocs)

> **Categoria:** Ferramentas de desenvolvedor e aplicações · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** ferramentas de desenvolvimento, modernização e colaboração que existem na AWS, mas não caem na prova.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Na prova, as ferramentas de desenvolvedor cobradas são só **AWS CLI, CodeBuild,
> CodePipeline e X-Ray**. Documentados aqui apenas para referência. Veja também
> [CodeDeploy, CodeArtifact e outros](../desenvolvimento/code-services.md) e [CloudShell](../desenvolvimento/cli-sdk-e-cloudshell.md),
> que também estão fora do escopo.

## AWS AppConfig

- Parte do Systems Manager. Gerencia **feature flags** e **configuração dinâmica** de aplicações, com validação e implantação gradual (rollback automático se um alarme disparar).
- Exemplo: ligar uma funcionalidade nova só para 10% dos usuários, sem novo deploy.
- A lista oficial o coloca em "Database" (erro de categorização da própria página).

## AWS Infrastructure Composer (antigo AWS Application Composer)

- **Desenho visual** de arquiteturas serverless e de infraestrutura que gera templates do **CloudFormation/SAM**.

## Amazon CodeGuru

- **CodeGuru Reviewer:** revisão automática de código com ML (🔄 fechado a novos clientes desde 07/11/2025).
- **CodeGuru Profiler:** encontra trechos caros de CPU e latência em aplicações em execução.
- **CodeGuru Security:** varredura de vulnerabilidades no código. Grande parte dessas funções migrou para o **Amazon Q Developer**.

## AWS Copilot

- **CLI** para criar, publicar e operar aplicações em contêiner no ECS e no App Runner com poucos comandos (gera a infraestrutura com CloudFormation).

## AWS Migration Hub Refactor Spaces

- Ajuda a **modernizar aos poucos** uma aplicação monolítica (padrão *strangler fig*): cria o ambiente de rede e o roteamento para mover funcionalidades uma a uma para microsserviços.

## AWS AppFabric

- Conecta aplicações **SaaS** (Slack, Zoom, Salesforce, Okta…) para **centralizar logs de segurança** e oferecer recursos de produtividade com IA generativa.

## Amazon Simple Workflow Service (SWF)

- Serviço **legado** de coordenação de tarefas em fluxos de trabalho. A AWS recomenda o **Step Functions** (no escopo) para novos projetos.

## Amazon WorkDocs

- Serviço de **armazenamento e colaboração de documentos** (editar, comentar, compartilhar). 🔄 Encerrado pela AWS (fim de suporte em 2025).

## ⚠️ Como isso aparece na prova

- "Orquestrar etapas de um fluxo" → **Step Functions** (no escopo), não SWF.
- "Esteira de CI/CD" → **CodePipeline**; "compilar e testar" → **CodeBuild** (no escopo).
- "Infraestrutura como código" → **CloudFormation** (no escopo).

## 🔗 Documentação oficial

- [AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) · [Infrastructure Composer](https://aws.amazon.com/infrastructure-composer/) · [CodeGuru](https://aws.amazon.com/codeguru/) · [Copilot](https://aws.github.io/copilot-cli/) · [Refactor Spaces](https://aws.amazon.com/migration-hub/features/) · [AppFabric](https://aws.amazon.com/appfabric/) · [SWF](https://aws.amazon.com/swf/)
