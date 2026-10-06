# Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Operar tudo clicando em telas pode ser lento. A equipe quer executar comandos ou fazer seu próprio programa interagir com a AWS.

**Como este serviço ajuda?** CLI oferece comandos; SDKs oferecem bibliotecas para programação; CloudShell fornece um terminal pelo navegador. São formas diferentes de acessar operações AWS.

**Exemplo do dia a dia:** Uma desenvolvedora usa um comando para consultar recursos. Seu aplicativo usa um SDK para enviar um arquivo a um serviço autorizado.

**O que ele não resolve sozinho?** Mudar a forma de acesso não concede mais permissões. CLI e SDK não são recursos de hospedagem; o escopo da prova para cada ferramenta está indicado abaixo.

**Primeiras palavras para entender:**

- **CLI:** interface por comandos de texto.
- **SDK:** biblioteca para desenvolver integrações.
- **Terminal:** ambiente para executar comandos.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Ferramentas de desenvolvedor / acesso · **Domínio:** 3 · **Escopo:** Global (console) / por região (endpoints de API) · **Tópico do guia:** [3.1 Formas de acesso e implantação](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)
>
> **Em uma frase:** toda ação na AWS é uma **chamada de API** — Console, CLI e SDKs são apenas formas diferentes de fazê-la.
>
> **Escopo oficial:** 🔀 CLI e Management Console ✅ · CloudShell ❌ fora do escopo · Cloud9 ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Escolha comandos, biblioteca de programação ou terminal conforme a forma de trabalho.

**Passo 2.** Configure identidade e ambiente e solicite a operação AWS desejada.

**Passo 3.** Leia o resultado ou erro e trate-o no processo. Alterar a ferramenta de acesso não altera automaticamente a permissão da identidade.

## 2. Recursos e opções, com significado

### Comparação

| Forma | Autenticação | Melhor para |
|---|---|---|
| **AWS Management Console** | Usuário/senha + MFA (ou SSO) | Tarefas pontuais, exploração, visualização; existe **app móvel** |
| **AWS CLI** (v2) | Access keys, perfis, **`aws sso login`** (temporárias), role da instância | Scripts e automação; `aws configure`; perfis em `~/.aws/config` e `~/.aws/credentials` |
| **SDKs** | Mesmas credenciais (cadeia de provedores) | Chamar a AWS **dentro do código**: Python (**boto3**), JavaScript, Java, .NET, Go, Ruby, PHP, C++, Rust… |
| **AWS CloudShell** ❌ *fora do escopo* | Já autenticado com o usuário do console | Terminal **no navegador** com CLI e ferramentas pré-instaladas; **1 GB** de armazenamento persistente por região (apagado após 120 dias sem uso); **sem custo** |
| **APIs REST/Query** | Assinatura SigV4 | Integrações de baixo nível |
| **IaC** | — | Ambientes repetíveis: [CloudFormation/CDK](../gerenciamento/cloudformation.md) |

### 🎯 Escopo da prova

**AWS CLI** e **AWS Management Console** estão no escopo. **CloudShell** está declarado **fora do escopo** (continua útil no dia a dia); Cloud9 não aparece.

### Boas práticas

Preferir credenciais **temporárias** (Identity Center, roles) a access keys de longo prazo.

Nunca colocar access keys no código ou em repositórios.

Tarefas repetíveis → automatizar (CLI, SDK, CloudFormation), não clicar no console.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Mudar a forma de acesso não concede mais permissões. CLI e SDK não são recursos de hospedagem; o escopo da prova para cada ferramenta está indicado abaixo.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

**AWS Cloud9** (IDE no navegador) está **fechado a novos clientes** desde 25/07/2024 → use **CloudShell** ou IDEs locais com o AWS Toolkit. Ainda pode aparecer na prova como "IDE baseada em navegador".

**AWS Toolkits** (VS Code, JetBrains) e **Amazon Q Developer** integram a AWS às IDEs.

## 5. Caso resolvido: ligando as peças

Uma desenvolvedora usa um comando para consultar recursos. Seu aplicativo usa um SDK para enviar um arquivo a um serviço autorizado.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha comandos, biblioteca de programação ou terminal conforme a forma de trabalho.
**Etapa 2:** Configure identidade e ambiente e solicite a operação AWS desejada.
**Etapa 3:** Leia o resultado ou erro e trate-o no processo. Alterar a ferramenta de acesso não altera automaticamente a permissão da identidade.

**Resultado e responsabilidade:** CLI oferece comandos; SDKs oferecem bibliotecas para programação; CloudShell fornece um terminal pelo navegador. São formas diferentes de acessar operações AWS.

**Recursos envolvidos:** Console, comandos CLI, bibliotecas SDK e ambiente CloudShell.

**Decisões que precisam ser tomadas:** Credenciais temporárias, região, serviço e operação.

**Outra situação comentada:** Automatizar no Python: SDK; operar por terminal: CLI; reproduzir infraestrutura: IaC.

**Por que não concluir mais do que isso:** CloudShell não concede privilégio extra e está fora do escopo; SDK permanece conceito do guia

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Formas de interagir com a AWS?"

**Resposta curta:** Console, CLI, SDKs, APIs (e CloudShell).

**Pergunta:** "Chamar a AWS dentro de um código Python."

**Resposta curta:** SDK (boto3).

**Pergunta:** "Executar comandos da CLI sem instalar nada."

**Resposta curta:** CloudShell.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) · [SDKs e ferramentas](https://aws.amazon.com/developer/tools/) · [CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
