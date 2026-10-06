# AWS Directory Service

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa já organiza usuários e computadores com Active Directory e precisa usar esse tipo de identidade com aplicações e recursos na AWS.

**Como este serviço ajuda?** Directory Service oferece opções para diretórios e integração com Active Directory, conforme a modalidade. Ele atende necessidades corporativas de identidade e compatibilidade.

**Exemplo do dia a dia:** Uma aplicação Windows na AWS precisa reconhecer os usuários do diretório da empresa. A equipe escolhe uma modalidade compatível com essa integração.

**O que ele não resolve sozinho?** As modalidades não são equivalentes: encaminhar autenticação para um diretório existente é diferente de manter um diretório gerenciado. Ele também não substitui qualquer mecanismo de login de aplicativos.

**Primeiras palavras para entender:**

- **Diretório:** cadastro organizado de identidades.
- **Active Directory:** tecnologia corporativa de diretório.
- **Domínio:** conjunto administrado por esse diretório.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / identidade · **Domínio:** 2 · **Escopo:** Regional (em VPC) · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** Microsoft Active Directory gerenciado na AWS, ou ponte para o AD on-premises.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.

**Passo 1.** Identifique o diretório existente e o tipo de integração requerido pelas aplicações.

**Passo 2.** Escolha uma modalidade que cria um diretório ou usa uma relação com o ambiente existente, conforme sua função.

**Passo 3.** Prepare conexões e confiança e teste a autenticação. As modalidades não têm a mesma divisão de responsabilidades.

## 2. Recursos e opções, com significado

### Opções

**AWS Managed Microsoft AD**

**Antes de ler este trecho:**

- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **AD:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.

**O que é:** AD real gerenciado (controladores em 2 AZs)

**Uso:** Aplicações que dependem de AD (SQL Server, FSx for Windows, WorkSpaces); trust com AD on-premises

**AD Connector**

**O que é:** Proxy que redireciona autenticação para o **AD on-premises** (sem guardar dados na nuvem)

**Uso:** Usar o AD existente com WorkSpaces, Identity Center, console

**Simple AD**

**O que é:** Diretório compatível com AD (Samba), básico e barato

**Uso:** 🔄 Fechado a novos clientes desde 30/07/2026

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

As modalidades não são equivalentes: encaminhar autenticação para um diretório existente é diferente de manter um diretório gerenciado. Ele também não substitui qualquer mecanismo de login de aplicativos.

## 4. Caso resolvido: ligando as peças

Uma aplicação Windows na AWS precisa reconhecer os usuários do diretório da empresa. A equipe escolhe uma modalidade compatível com essa integração.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique o diretório existente e o tipo de integração requerido pelas aplicações.
**Etapa 2:** Escolha uma modalidade que cria um diretório ou usa uma relação com o ambiente existente, conforme sua função.
**Etapa 3:** Prepare conexões e confiança e teste a autenticação. As modalidades não têm a mesma divisão de responsabilidades.

**Resultado e responsabilidade:** Directory Service oferece opções para diretórios e integração com Active Directory, conforme a modalidade. Ele atende necessidades corporativas de identidade e compatibilidade.

**Recursos envolvidos:** Diretórios gerenciados/conectores e integração de rede.

**Decisões que precisam ser tomadas:** Tipo de diretório, DNS, rede e trusts suportados.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.

**Outra situação comentada:** Aplicação Windows precisa AD: avalie modalidade correta, em vez de presumir que IAM substitui qualquer protocolo de diretório.

**Por que não concluir mais do que isso:** AD Connector não equivale a criar nova cópia de diretório gerenciado

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Rodar Active Directory gerenciado na AWS."

**Resposta curta:** AWS Managed Microsoft AD.

**Pergunta:** "Usar o AD on-premises sem replicá-lo para a nuvem."

**Resposta curta:** AD Connector.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
