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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **stack:** Conjunto de recursos administrados a partir de uma descrição CloudFormation. Excluir ou atualizar a stack pode afetar os recursos conforme suas políticas.


**Passo 1.** Escreva um template com recursos, parâmetros e dependências do ambiente.

**Passo 2.** Crie ou atualize uma stack. A ferramenta realiza operações sobre os recursos conforme a descrição e as políticas.

**Passo 3.** Examine mudanças e possíveis efeitos nos dados. Repetir infraestrutura não significa que qualquer alteração pode ser desfeita sem risco.

## 2. Recursos e opções, com significado

### Template

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **URL:** Endereço usado para acessar um recurso. Uma URL pode incluir domínio, caminho e parâmetros; possuir o endereço não significa ter autorização.
- **AMI:** Imagem de máquina EC2: modelo com o software necessário para iniciar uma instância. A imagem precisa ser compatível com a configuração de execução escolhida.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
- **retain:** Estratégias de migração: trocar por outra oferta, manter onde está, desativar ou mover a plataforma, respectivamente. A decisão vem do objetivo da aplicação e do negócio.


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

**Antes de ler este trecho:**

- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **Control Tower:** Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.
- **snapshot:** Cópia de estado de um recurso em determinado momento, conforme o serviço. Restauração pode criar um novo recurso; não presuma uma máquina pronta e instantânea.
- **policy:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.
- **rollback:** Retorno a uma configuração ou versão anterior, quando suportado e planejado. Nem toda alteração de dados pode ser desfeita automaticamente.
- **IaC:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **CDK:** Ferramentas de desenvolvimento e descrição de infraestrutura. CDK ajuda a definir recursos por programação; SAM é voltado a aplicações serverless compatíveis.


**AWS CDK:** define a infraestrutura em linguagens de programação (TypeScript, Python, Java, C#, Go) e **gera CloudFormation**.

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.


**AWS SAM:** extensão do CloudFormation simplificada para aplicações **serverless** (Lambda, API Gateway, DynamoDB).


**Infrastructure Composer:** desenha arquiteturas visualmente e gera templates.


Terraform: equivalente de terceiros.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não inventa uma arquitetura segura nem impede todo erro de configuração. A descrição precisa estar correta, e mudanças ou exclusões podem afetar recursos e dados.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Elastic Beanstalk:** O Elastic Beanstalk ajuda a implantar aplicações em plataformas compatíveis, provisionando e coordenando recursos AWS para esse ambiente.
- **CFN:** Abreviação usada para CloudFormation. Templates descrevem recursos e stacks administram conjuntos desses recursos.


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

**Antes de ler este trecho:**

- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.


**Outra situação comentada:** Recriar rede e aplicação em teste: template versionado; valide change set antes de atualização sensível.

**Por que não concluir mais do que isso:** Deletar stack pode apagar recursos salvo proteção/retenção configurada; rollback não recupera todo dado

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Criar recursos manualmente dificulta repetir o mesmo ambiente e acompanhar exatamente o que foi configurado.

**2. O que a solução fornece?**

CloudFormation usa um arquivo de descrição para criar e atualizar conjuntos de recursos AWS compatíveis, com suas dependências.

**3. Que conclusão seria incorreta?**

Ele não inventa uma arquitetura segura nem impede todo erro de configuração. A descrição precisa estar correta, e mudanças ou exclusões podem afetar recursos e dados.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Provisionar infraestrutura a partir de templates JSON/YAML."

**Resposta curta:** CloudFormation.

**Antes de ler este trecho:**

- **provisionar:** Criar ou disponibilizar capacidade e recursos. Um recurso provisionado pode ter cobrança mesmo enquanto está esperando trabalho.
- **JSON:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
- **YAML:** Formatos de representação de dados e configurações. Um arquivo nesses formatos descreve informações; ele não cria permissões nem recursos sem ser usado por uma ferramenta.


**Fundamento explicado no capítulo:** "Provisionar infraestrutura a partir de templates JSON/YAML." → CloudFormation.

**Pergunta:** "Mesma infraestrutura em várias contas e regiões."

**Resposta curta:** StackSets.


**Fundamento explicado no capítulo:** "Mesma infraestrutura em várias contas e regiões." → StackSets.

**Pergunta:** "Detectar alterações manuais fora do template."

**Resposta curta:** Drift detection.


**Fundamento explicado no capítulo:** "Detectar alterações manuais fora do template." → Drift detection.

**Pergunta:** "Vantagem de IaC?"

**Resposta curta:** Repetibilidade, versionamento, menos erro manual, velocidade.


**Fundamento explicado no capítulo:** "Vantagem de IaC?" → Repetibilidade, versionamento, menos erro manual, velocidade.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) · [CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) · [SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
