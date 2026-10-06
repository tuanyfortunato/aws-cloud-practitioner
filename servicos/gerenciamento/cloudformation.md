# AWS CloudFormation (e CDK, SAM)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Criar recursos manualmente dificulta repetir o mesmo ambiente e acompanhar exatamente o que foi configurado.

**Como este serviço ajuda?** CloudFormation usa um arquivo de descrição para criar e atualizar conjuntos de recursos AWS compatíveis, com suas dependências.

**Exemplo do dia a dia:** A escola descreve seu ambiente de testes num template e usa uma stack para administrar os recursos desse ambiente em conjunto.

**O que ele não resolve sozinho?** Ele não inventa uma arquitetura segura nem impede todo erro de configuração. A descrição precisa estar correta, e mudanças ou exclusões podem afetar recursos e dados.

**Primeiras palavras para entender:**

- **Template:** arquivo que descreve recursos.
- **Stack:** conjunto administrado a partir do template.
- **Infraestrutura como código:** recursos descritos em arquivos versionáveis.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / infraestrutura como código · **Domínio:** 1 (automação), 3 · **Escopo:** Regional (StackSets: multi-conta/região) · **Gratuito** · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md) · [3.1 Formas de acesso](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)
>
> **Em uma frase:** descreve a infraestrutura em templates JSON/YAML e cria tudo de forma **repetível, versionada e automatizada**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Escreva um template com recursos, parâmetros e dependências do ambiente.

**Passo 2.** Crie ou atualize uma stack. A ferramenta realiza operações sobre os recursos conforme a descrição e as políticas.

**Passo 3.** Examine mudanças e possíveis efeitos nos dados. Repetir infraestrutura não significa que qualquer alteração pode ser desfeita sem risco.

## 2. Recursos e opções, com significado

### Template

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

### Conceitos e configurações

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

### Ferramentas relacionadas

**AWS CDK:** define a infraestrutura em linguagens de programação (TypeScript, Python, Java, C#, Go) e **gera CloudFormation**.

**AWS SAM:** extensão do CloudFormation simplificada para aplicações **serverless** (Lambda, API Gateway, DynamoDB).

**Infrastructure Composer:** desenha arquiteturas visualmente e gera templates.

Terraform: equivalente de terceiros.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não inventa uma arquitetura segura nem impede todo erro de configuração. A descrição precisa estar correta, e mudanças ou exclusões podem afetar recursos e dados.

### ⚠️ Não confundir

CloudFormation (qualquer infra como código) × **Elastic Beanstalk** (sobe a aplicação, usa CFN por baixo) × **Service Catalog** (catálogo de templates aprovados).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Gratuito** para recursos da AWS (paga-se os recursos criados); pequena taxa para extensões de terceiros/hooks.

## 5. Caso resolvido: ligando as peças

A escola descreve seu ambiente de testes num template e usa uma stack para administrar os recursos desse ambiente em conjunto.

**Aplicando a sequência à situação:**

**Etapa 1:** Escreva um template com recursos, parâmetros e dependências do ambiente.
**Etapa 2:** Crie ou atualize uma stack. A ferramenta realiza operações sobre os recursos conforme a descrição e as políticas.
**Etapa 3:** Examine mudanças e possíveis efeitos nos dados. Repetir infraestrutura não significa que qualquer alteração pode ser desfeita sem risco.

**Resultado e responsabilidade:** CloudFormation usa um arquivo de descrição para criar e atualizar conjuntos de recursos AWS compatíveis, com suas dependências.

**Recursos envolvidos:** Template, stack, parameters, outputs e change sets.

**Decisões que precisam ser tomadas:** Recursos, dependências, permissões e tratamento de atualização.

**Outra situação comentada:** Recriar rede e aplicação em teste: template versionado; valide change set antes de atualização sensível.

**Por que não concluir mais do que isso:** Deletar stack pode apagar recursos salvo proteção/retenção configurada; rollback não recupera todo dado

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Provisionar infraestrutura a partir de templates JSON/YAML."

**Resposta curta:** CloudFormation.

**Fundamento explicado no capítulo:** **AWS CDK:** define a infraestrutura em linguagens de programação (TypeScript, Python, Java, C#, Go) e **gera CloudFormation**.

**Pergunta:** "Mesma infraestrutura em várias contas e regiões."

**Resposta curta:** StackSets.

**Pergunta:** "Detectar alterações manuais fora do template."

**Resposta curta:** Drift detection.

**Pergunta:** "Vantagem de IaC?"

**Resposta curta:** Repetibilidade, versionamento, menos erro manual, velocidade.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) · [CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) · [SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
