# Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma equipe precisa transformar código em uma versão executável, verificar o resultado e disponibilizá-lo com um processo repetível.

**Como este serviço ajuda?** A ficha compara ferramentas de desenvolvimento e entrega. CodeBuild executa tarefas de construção e testes; CodePipeline coordena etapas de uma entrega automatizada.

**Exemplo do dia a dia:** Ao enviar uma mudança, o processo constrói a aplicação, executa testes configurados e encaminha a versão às etapas de entrega previstas.

**O que ele não resolve sozinho?** Automatizar uma sequência não cria os testes nem garante que a aplicação esteja correta. As ferramentas da família têm papéis e condições comerciais diferentes.

**Primeiras palavras para entender:**

- **Build:** preparação de uma versão executável.
- **Pipeline:** sequência de etapas.
- **Deploy:** colocação de uma versão em funcionamento.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Ferramentas de desenvolvedor / DevOps · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.15 Ferramentas de desenvolvimento](../../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md)
>
> **Em uma frase:** serviços gerenciados que cobrem a esteira **código → build → teste → deploy**.
>
> **Escopo oficial:** 🔀 CodeBuild e CodePipeline ✅ · CodeDeploy e CodeArtifact ❌ fora do escopo · CodeCommit e CodeStar ⚪ não listados · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina as etapas e os arquivos necessários para construir e verificar uma versão.

**Passo 2.** Execute construção e organize a sequência de entrega nas ferramentas compatíveis.

**Passo 3.** Valide os resultados antes de publicar e acompanhe a execução. A automação segue suas instruções, inclusive quando elas estiverem incorretas.

## 2. Recursos e opções, com significado

### Visão da esteira

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

### 🎯 Escopo da prova

No escopo: **CodeBuild** e **CodePipeline** (além de X-Ray e CLI). **CodeDeploy**, **CodeArtifact** e **CodeGuru** estão **fora do escopo**; CodeCommit e CodeStar não aparecem. CodeCatalyst e CodeGuru Reviewer estão fechados a novos clientes desde 07/11/2025.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Automatizar uma sequência não cria os testes nem garante que a aplicação esteja correta. As ferramentas da família têm papéis e condições comerciais diferentes.

### ⚠️ Não confundir

CodeBuild (build/teste) × CodeDeploy (implantar) × CodePipeline (orquestrar tudo).

Equivalentes de terceiros: GitHub (repositório), GitHub Actions/Jenkins (pipeline).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

CodeCommit por usuário ativo; CodeBuild por minuto; CodeDeploy grátis para EC2/Lambda (pago on-premises); CodePipeline por pipeline ativo ou minuto de execução (V2); CodeArtifact por GB e requisições.

## 5. Caso resolvido: ligando as peças

Ao enviar uma mudança, o processo constrói a aplicação, executa testes configurados e encaminha a versão às etapas de entrega previstas.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina as etapas e os arquivos necessários para construir e verificar uma versão.
**Etapa 2:** Execute construção e organize a sequência de entrega nas ferramentas compatíveis.
**Etapa 3:** Valide os resultados antes de publicar e acompanhe a execução. A automação segue suas instruções, inclusive quando elas estiverem incorretas.

**Resultado e responsabilidade:** A ficha compara ferramentas de desenvolvimento e entrega. CodeBuild executa tarefas de construção e testes; CodePipeline coordena etapas de uma entrega automatizada.

**Recursos envolvidos:** Build projects, pipelines e estágios; ferramentas adicionais da esteira.

**Decisões que precisam ser tomadas:** Código fonte, comandos, artefatos, role e integrações.

**Outra situação comentada:** Compilar e rodar testes: CodeBuild; coordenar fluxo completo: CodePipeline.

**Por que não concluir mais do que isso:** Build não escreve testes; Pipeline não é repositório nem executa todo estágio sozinho

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Orquestrar a esteira de CI/CD na AWS."

**Resposta curta:** CodePipeline.

**Pergunta:** "Compilar e executar testes sem gerenciar servidores de build."

**Resposta curta:** CodeBuild.

**Pergunta:** "Automatizar deploy em EC2 e servidores on-premises."

**Resposta curta:** CodeDeploy.

**Pergunta:** "Repositório privado de pacotes npm."

**Resposta curta:** CodeArtifact.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) · [CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) · [CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
