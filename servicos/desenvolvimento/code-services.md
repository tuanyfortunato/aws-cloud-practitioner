# Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact

> **Categoria:** Ferramentas de desenvolvedor / DevOps · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.15 Ferramentas de desenvolvimento](../../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md)
>
> **Em uma frase:** serviços gerenciados que cobrem a esteira **código → build → teste → deploy**.
>
> **Escopo oficial:** 🔀 CodeBuild e CodePipeline ✅ · CodeDeploy e CodeArtifact ❌ fora do escopo · CodeCommit e CodeStar ⚪ não listados · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Visão da esteira

```
CodeCommit / GitHub ──▶ CodeBuild ──▶ (testes) ──▶ CodeDeploy / ECS / CloudFormation
          └─────────────── orquestrado pelo CodePipeline ───────────────┘
                     pacotes de dependências: CodeArtifact
```

| Serviço | Função | Detalhes |
|---|---|---|
| **AWS CodeCommit** | Repositórios **Git privados** gerenciados | Criptografados, integrados ao IAM. 🔄 Fechado a novos clientes em 2024 e **de volta a GA em 24/11/2025**. |
| **AWS CodeBuild** | **Compila, testa e empacota** código | Serverless, contêineres de build, arquivo **`buildspec.yml`**; cobrado **por minuto** de build. |
| **AWS CodeDeploy** ❌ *fora do escopo* | **Automatiza deploys** | Destinos: **EC2, on-premises, Lambda, ECS**; arquivo **`appspec.yml`**; estratégias **in-place** ou **blue/green**, canary/linear (Lambda/ECS); rollback automático por alarme. |
| **AWS CodePipeline** | **Orquestra a esteira de CI/CD** | Estágios (source, build, test, deploy, aprovação manual); integra GitHub, Bitbucket, S3, ECR, CloudFormation, Elastic Beanstalk. |
| **AWS CodeArtifact** ❌ *fora do escopo* | **Repositório de pacotes** | npm, Maven, PyPI, NuGet, Gradle…; faz proxy de repositórios públicos. |
| **CodeGuru** ❌ *fora do escopo* | Revisão de código e profiling com ML | 🧊 Parte dos recursos foi descontinuada/absorvida pelo Amazon Q Developer. |
| **AWS CodeStar** | Gestão de projetos de CI/CD | 🔄 **Descontinuado** (31/07/2024) — ainda listado no exam guide. |
| **Amazon CodeCatalyst** | Plataforma unificada de desenvolvimento | 🧊 |

## 🎯 Escopo da prova

- No escopo: **CodeBuild** e **CodePipeline** (além de X-Ray e CLI). **CodeDeploy**, **CodeArtifact** e **CodeGuru** estão **fora do escopo**; CodeCommit e CodeStar não aparecem. CodeCatalyst e CodeGuru Reviewer estão fechados a novos clientes desde 07/11/2025.

## Cobrança

- CodeCommit por usuário ativo; CodeBuild por minuto; CodeDeploy grátis para EC2/Lambda (pago on-premises); CodePipeline por pipeline ativo ou minuto de execução (V2); CodeArtifact por GB e requisições.

## ⚠️ Não confundir

- CodeBuild (build/teste) × CodeDeploy (implantar) × CodePipeline (orquestrar tudo).
- Equivalentes de terceiros: GitHub (repositório), GitHub Actions/Jenkins (pipeline).

## ❓ Perguntas típicas

- "Orquestrar a esteira de CI/CD na AWS." → CodePipeline.
- "Compilar e executar testes sem gerenciar servidores de build." → CodeBuild.
- "Automatizar deploy em EC2 e servidores on-premises." → CodeDeploy.
- "Repositório privado de pacotes npm." → CodeArtifact.

## 🔗 Documentação oficial

- [CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) · [CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) · [CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
