<!-- autoral -->

# Formas de acesso: Console, CLI, SDKs e CloudShell

> **Categoria:** Ferramentas de desenvolvimento e acesso · **Domínio:** 3 · **Abrangência:** Console global; APIs por Região · **Ficha:** núcleo
>
> **Em uma frase:** as formas de usar a AWS: cliques no console, comandos na CLI, código com os SDKs e um terminal no navegador com o CloudShell, todas chegando às mesmas APIs.
>
> **Escopo oficial:** 🔀 CLI e Management Console ✅ · CloudShell ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.1 Formas de acessar e implantar na AWS](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Na escola, três pessoas usam a AWS de jeitos diferentes. A coordenadora confere a conta uma vez por mês. O professor de informática faz o backup das fotos toda noite. E o sistema de matrícula precisa guardar o comprovante de cada aluno sozinho, sem ninguém clicar.

Cada uma tem a sua forma de acesso, e todas acabam fazendo **chamadas às APIs** dos serviços. O **AWS Management Console** é a aplicação web para explorar e fazer tarefas pontuais. A **AWS CLI** é uma ferramenta de código aberto para usar os serviços por comandos no terminal e escrever roteiros (*scripts*) que repetem tarefas. Os **AWS SDKs** são bibliotecas para chamar as APIs de dentro de um programa, em linguagens como Python, JavaScript e Java. O **AWS CloudShell** é um terminal no navegador, aberto a partir do console, com a CLI já instalada e as credenciais de quem entrou.

O limite: trocar o console pela CLI não dá mais poder a ninguém. Toda chamada chega com uma identidade e passa pelas mesmas permissões do [IAM](../seguranca/iam.md). E para criar ambientes inteiros, de forma repetível, o caminho é a infraestrutura como código com o [CloudFormation](../gerenciamento/cloudformation.md).

## Como funciona

1. A pessoa ou o programa se identifica: login no console, ou credenciais configuradas na CLI e no SDK.
2. Cada clique, comando ou linha de código vira uma chamada à API do serviço, na Região escolhida.
3. O IAM avalia a chamada contra as permissões da identidade.
4. Se permitida, o serviço executa a ação; o CloudTrail registra a chamada.

## Opções principais

| Forma | Quando usar | Exemplo na escola |
|---|---|---|
| Management Console | Explorar um serviço ou fazer uma tarefa pontual | Conferência mensal da coordenadora |
| AWS CLI | Repetir tarefas com comandos e roteiros | Backup noturno do professor |
| AWS SDKs | A aplicação usa a AWS no próprio código | Sistema de matrícula grava comprovantes |
| AWS CloudShell | Terminal rápido no navegador, sem instalar nada | Rodar um comando sem configurar o computador |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Versão atual da CLI | Versão 2, com recursos que a 1 não recebe | 06/10/2026 |
| Armazenamento persistente do CloudShell | Até 1 GB por Região, sem custo adicional | 06/10/2026 |
| CloudShell na prova | Fora do escopo | 06/10/2026 |
| AWS Cloud9 | Não aceita novos clientes | 06/10/2026 |

## Como é cobrado

O console, a CLI, os SDKs e o CloudShell não têm cobrança própria; paga-se pelos recursos e serviços que eles criam e usam.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS CloudFormation](../gerenciamento/cloudformation.md) | Descreve o ambiente inteiro num modelo | "Repetir o ambiente em várias Regiões" |
| [AWS Systems Manager](../gerenciamento/systems-manager.md) | Opera muitas máquinas de uma vez | "Rodar um comando em 50 instâncias" |
| [Amazon Q Developer](../ia-ml/amazon-q.md) | Assistente de IA no console e nos editores | "Perguntar como fazer" |
| [AWS IAM](../seguranca/iam.md) | Define quem pode fazer cada chamada | "Permissão", "chave de acesso" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html)
- [O que é a AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
- [Ferramentas para desenvolver na AWS](https://aws.amazon.com/developer/tools/)
- [O que é o AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html)
- [O que é o AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
