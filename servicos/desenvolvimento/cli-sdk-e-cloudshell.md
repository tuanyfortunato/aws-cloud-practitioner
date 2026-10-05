# Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)

> **Categoria:** Ferramentas de desenvolvedor / acesso · **Domínio:** 3 · **Escopo:** Global (console) / por região (endpoints de API) · **Tópico do guia:** [3.1 Formas de acesso e implantação](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)
>
> **Em uma frase:** toda ação na AWS é uma **chamada de API** — Console, CLI e SDKs são apenas formas diferentes de fazê-la.
>
> **Escopo oficial:** 🔀 CLI e Management Console ✅ · CloudShell ❌ fora do escopo · Cloud9 ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** são **portas diferentes para o mesmo prédio**: o Console é a porta da frente (cliques), a CLI é o interfone (comandos), os SDKs são a entrada pelo seu próprio programa e o CloudShell é uma CLI pronta no navegador.

- ✅ **Escolha quando:** precisa decidir **como interagir com a AWS**.
- 🚫 **Não é a resposta quando:** precisa criar **ambientes repetíveis** → [CloudFormation](../gerenciamento/cloudformation.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "linha de comando" → CLI; "dentro do código" → SDK; "terminal no navegador" → CloudShell (fora da prova).
<!-- didatico:fim -->

## Comparação

| Forma | Autenticação | Melhor para |
|---|---|---|
| **AWS Management Console** | Usuário/senha + MFA (ou SSO) | Tarefas pontuais, exploração, visualização; existe **app móvel** |
| **AWS CLI** (v2) | Access keys, perfis, **`aws sso login`** (temporárias), role da instância | Scripts e automação; `aws configure`; perfis em `~/.aws/config` e `~/.aws/credentials` |
| **SDKs** | Mesmas credenciais (cadeia de provedores) | Chamar a AWS **dentro do código**: Python (**boto3**), JavaScript, Java, .NET, Go, Ruby, PHP, C++, Rust… |
| **AWS CloudShell** ❌ *fora do escopo* | Já autenticado com o usuário do console | Terminal **no navegador** com CLI e ferramentas pré-instaladas; **1 GB** de armazenamento persistente por região (apagado após 120 dias sem uso); **sem custo** |
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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Console, comandos CLI, bibliotecas SDK e ambiente CloudShell |
| **O que você decide/configura?** | Credenciais temporárias, região, serviço e operação |
| **Em que ordem as coisas acontecem?** | Interface solicita uma API com a identidade autenticada |
| **O que pode fazer, e em que condição?** | Permite operação manual/programática com as mesmas regras de autorização |
| **O que não pode presumir?** | CloudShell não concede privilégio extra e está fora do escopo; SDK permanece conceito do guia |

**Caso comentado:** Automatizar no Python: SDK; operar por terminal: CLI; reproduzir infraestrutura: IaC.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) · [SDKs e ferramentas](https://aws.amazon.com/developer/tools/) · [CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html)
