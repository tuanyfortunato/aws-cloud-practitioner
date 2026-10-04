# Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)

> **Categoria:** Ferramentas de desenvolvedor / acesso · **Domínio:** 3 · **Escopo:** Global (console) / por região (endpoints de API) · **Tópico do guia:** [3.1 Formas de acesso e implantação](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)
>
> **Em uma frase:** toda ação na AWS é uma **chamada de API** — Console, CLI e SDKs são apenas formas diferentes de fazê-la.
>
> **Escopo oficial:** 🔀 CLI e Management Console ✅ · CloudShell ❌ fora do escopo · Cloud9 ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Comparação

| Forma | Autenticação | Melhor para |
|---|---|---|
| **AWS Management Console** | Usuário/senha + MFA (ou SSO) | Tarefas pontuais, exploração, visualização; existe **app móvel** |
| **AWS CLI** (v2) | Access keys, perfis, **`aws sso login`** (temporárias), role da instância | Scripts e automação; `aws configure`; perfis em `~/.aws/config` e `~/.aws/credentials` |
| **SDKs** | Mesmas credenciais (cadeia de provedores) | Chamar a AWS **dentro do código**: Python (**boto3**), JavaScript, Java, .NET, Go, Ruby, PHP, C++, Rust… |
| **AWS CloudShell** ❌ *fora do escopo* | Já autenticado com o usuário do console | Terminal **no navegador** com CLI e ferramentas pré-instaladas; **1 GB** de armazenamento persistente por região; **sem custo** |
| **APIs REST/Query** | Assinatura SigV4 | Integrações de baixo nível |
| **IaC** | — | Ambientes repetíveis: [CloudFormation/CDK](../gerenciamento/cloudformation.md) |

## 🔄 Atualizações 2025-2026

- **AWS Cloud9** (IDE no navegador) está **fechado a novos clientes** desde 25/07/2024 → use **CloudShell** ou IDEs locais com o AWS Toolkit. Ainda pode aparecer na prova como "IDE baseada em navegador".
- **AWS Toolkits** (VS Code, JetBrains) e **Amazon Q Developer** integram a AWS às IDEs.

## 🎯 Escopo da prova

- **AWS CLI** e **AWS Management Console** estão no escopo. **CloudShell** está declarado **fora do escopo** (continua útil no dia a dia); Cloud9 não aparece.

## Boas práticas

- Preferir credenciais **temporárias** (Identity Center, roles) a access keys de longo prazo.
- Nunca colocar access keys no código ou em repositórios.
- Tarefas repetíveis → automatizar (CLI, SDK, CloudFormation), não clicar no console.

## ❓ Perguntas típicas

- "Formas de interagir com a AWS?" → Console, CLI, SDKs, APIs (e CloudShell).
- "Chamar a AWS dentro de um código Python." → SDK (boto3).
- "Executar comandos da CLI sem instalar nada." → CloudShell.

## 🔗 Documentação oficial

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) · [SDKs e ferramentas](https://aws.amazon.com/developer/tools/) · [CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html)
