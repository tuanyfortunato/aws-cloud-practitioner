<!-- autoral -->

# Ferramentas de CI/CD: CodeBuild e CodePipeline

> **Categoria:** Ferramentas de desenvolvedor / DevOps · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** o CodeBuild compila e testa o código sem servidores de build; o CodePipeline automatiza a esteira que leva cada mudança do repositório à produção.
>
> **Escopo oficial:** 🔀 CodeBuild e CodePipeline ✅ · CodeDeploy e CodeArtifact ❌ fora do escopo · CodeCommit e CodeStar ⚪ não listados · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.15 Ferramentas de desenvolvimento](../../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

A equipe do sistema de matrícula junta o código à mão toda sexta-feira, e às vezes uma mudança quebra outra. A solução é **integração contínua** (cada junção dispara compilação e testes) e **entrega contínua** (o que passa nos testes é preparado para ir à produção). O **AWS CodeBuild** é o serviço de compilação totalmente gerenciado, e o **AWS CodePipeline** modela e automatiza a esteira (*pipeline*).

1. Origem: alguém junta uma mudança no repositório, e o CodePipeline percebe.
2. Build: o CodePipeline chama o CodeBuild, que compila, roda os testes e gera o pacote.
3. Implantação: a nova versão vai para o ambiente de testes.
4. Com a aprovação, a versão segue para a produção.

O AWS CodeDeploy (automatiza implantações) e o AWS CodeArtifact (repositório de pacotes) estão fora do escopo da prova; o CodeCommit e o CodeStar não aparecem na lista.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS CloudFormation](../gerenciamento/cloudformation.md) | Cria a infraestrutura a partir de modelos | "Infraestrutura como código" |
| [AWS Elastic Beanstalk](../computacao/elastic-beanstalk.md) | Sobe e escala a aplicação a partir do código | "Só enviar o código" |
| [AWS X-Ray](x-ray.md) | Rastreia requisições para achar lentidão | "Onde a requisição ficou lenta" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
- [O que é o AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
