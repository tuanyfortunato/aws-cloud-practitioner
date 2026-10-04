# AWS CloudFormation (e CDK, SAM)

> **Categoria:** Gerenciamento / infraestrutura como código · **Domínio:** 1 (automação), 3 · **Escopo:** Regional (StackSets: multi-conta/região) · **Gratuito** · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md) · [3.1 Formas de acesso](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)
>
> **Em uma frase:** descreve a infraestrutura em templates JSON/YAML e cria tudo de forma **repetível, versionada e automatizada**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Template

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: Bucket de exemplo
Parameters:      # entradas (ex.: ambiente)
  Ambiente: {Type: String, AllowedValues: [dev, prod]}
Mappings: {}     # tabelas de valores (ex.: AMI por região)
Conditions: {}   # criar recursos condicionalmente
Resources:       # ÚNICA seção obrigatória
  MeuBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
Outputs:         # valores exportados (ex.: URL)
  NomeBucket: {Value: !Ref MeuBucket}
```

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Stack** | Conjunto de recursos criado, atualizado e apagado **como uma unidade**. |
| **Change sets** | Pré-visualizam o que uma atualização vai mudar. |
| **Rollback** | Se algo falha, desfaz automaticamente. |
| **Drift detection** | Detecta recursos alterados **manualmente** fora do template. |
| **StackSets** | Mesma stack em **várias contas e regiões** (com Organizations). |
| **Nested stacks / modules** | Reuso de componentes. |
| **DeletionPolicy** | `Retain` ou `Snapshot` para não perder dados ao apagar a stack. |
| **Termination protection / stack policy** | Evitam exclusões/alterações acidentais. |
| **IaC generator** | Gera template a partir de recursos existentes. |
| **Hooks** | Validações proativas antes de criar recursos (usados pelo Control Tower). |

## Ferramentas relacionadas

- **AWS CDK:** define a infraestrutura em linguagens de programação (TypeScript, Python, Java, C#, Go) e **gera CloudFormation**.
- **AWS SAM:** extensão do CloudFormation simplificada para aplicações **serverless** (Lambda, API Gateway, DynamoDB).
- **Infrastructure Composer:** desenha arquiteturas visualmente e gera templates.
- Terraform: equivalente de terceiros.

## Cobrança

- **Gratuito** para recursos da AWS (paga-se os recursos criados); pequena taxa para extensões de terceiros/hooks.

## ⚠️ Não confundir

- CloudFormation (qualquer infra como código) × **Elastic Beanstalk** (sobe a aplicação, usa CFN por baixo) × **Service Catalog** (catálogo de templates aprovados).

## ❓ Perguntas típicas

- "Provisionar infraestrutura a partir de templates JSON/YAML." → CloudFormation.
- "Mesma infraestrutura em várias contas e regiões." → StackSets.
- "Detectar alterações manuais fora do template." → Drift detection.
- "Vantagem de IaC?" → Repetibilidade, versionamento, menos erro manual, velocidade.

## 🔗 Documentação oficial

- [Guia do CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) · [CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) · [SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
