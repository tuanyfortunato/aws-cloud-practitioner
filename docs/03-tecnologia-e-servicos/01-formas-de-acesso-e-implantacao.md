# 3.1 Formas de acessar e implantar na AWS

## 🧠 Antes de começar

**Qual é a dificuldade?** Você precisa criar ou consultar recursos AWS, mas pode fazer isso por uma tela, por comandos, por um programa ou por uma descrição automatizada do ambiente.

**A ideia em palavras simples:** São maneiras diferentes de operar serviços. Console oferece interface visual; CLI usa comandos; SDK integra programas; ferramentas de infraestrutura descrevem recursos para implantação.

**Exemplo do dia a dia:** Uma pessoa cria um recurso pelo console e depois automatiza tarefas repetidas com comandos ou código. A permissão necessária continua sendo parte do acesso.

**O que não concluir?** A forma de acesso não muda sozinha o que a identidade pode fazer. Uma ferramenta de operação também não é o serviço que hospeda a aplicação.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **API** | a forma padronizada de um programa pedir algo a outro. |
| **IaC** | infraestrutura como código: descrever servidores e redes num arquivo e criar tudo automaticamente. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [AWS CloudFormation (e CDK, SAM)](../../servicos/gerenciamento/cloudformation.md) · [AWS VPN (Site-to-Site VPN e Client VPN)](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) · [AWS Direct Connect](../../servicos/redes/direct-connect.md)

🏠 [Índice do domínio](README.md) · [3.2 Infraestrutura global](02-infraestrutura-global.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

A tela, o comando e o programa são meios de pedir operações ao serviço. O recurso criado não muda de natureza porque a solicitação foi feita de outro modo. A mesma identidade continua limitada pelos controles aplicáveis.

Automatizar é descrever ações para repetir com menos trabalho manual. É necessário tratar resultado e erro, além de fornecer credenciais adequadas. Um arquivo de infraestrutura descreve recursos; uma biblioteca ajuda um programa a chamar operações.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como falar com um **banco**: pelo **site** (Console), pelo **atendimento por comandos** (CLI), por um **aplicativo seu integrado ao banco** (SDK) ou deixando **instruções programadas** que se repetem sozinhas (CloudFormation).

</details>

## 2. Conceitos e opções explicados

**AWS Management Console:** interface web. Bom para tarefas pontuais e exploração.

**AWS CLI:** linha de comando para automatizar via scripts.

**SDKs:** bibliotecas para usar a AWS dentro do código (Python/boto3, Java, JavaScript etc.).

**AWS CloudShell:** terminal no navegador, já autenticado e com a CLI instalada, sem custo adicional.

**APIs:** tudo na AWS é uma chamada de API; Console, CLI e SDK usam as mesmas APIs por baixo.

**Infraestrutura como código (IaC):** **AWS CloudFormation** (templates JSON/YAML que criam pilhas de recursos de forma repetível) — o Terraform é um equivalente de terceiros. Ver [3.16](16-gestao-e-governanca.md).

**Operações pontuais vs repetíveis:** tarefa única pode ser no Console; tarefa repetível deve ser automatizada (CLI, SDK, CloudFormation).

**Conectividade com a AWS:** internet pública, AWS VPN (Site-to-Site ou Client VPN) e AWS Direct Connect. Ver [3.10](10-rede-e-entrega-de-conteudo.md).

**Cai na prova:** "provisionar o mesmo ambiente em várias regiões de forma repetível" = CloudFormation; "executar comandos rápidos sem instalar nada" = CloudShell.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** Console fornece interface visual; CLI executa comandos; SDK integra APIs ao código. CloudFormation descreve recursos e suas dependências em templates e stacks.

**Depois, compare as escolhas:** Operação pontual: console pode bastar. Automação repetida: CLI/SDK. Ambiente reproduzível: IaC. Híbrido mantém parte no ambiente próprio com conectividade apropriada.

**Por fim, verifique o limite:** Mudar de interface não amplia permissões. Templates não tornam recursos gratuitos. Scripts imperativos precisam lidar com erros e repetição; IaC registra o estado desejado.

## 4. Caso resolvido

A equipe recria o mesmo ambiente de teste toda semana. Qual abordagem reduz divergências?

**Raciocínio e resposta:** IaC com CloudFormation, em vez de repetir cliques manualmente. A stack usa permissões e gera custos dos recursos criados.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **Console, CLI, SDK e CloudShell**.
- [ ] Saber que tarefa **pontual** pode ser no Console e tarefa **repetível** deve ser automatizada.
- [ ] Explicar **infraestrutura como código** (CloudFormation).

**Dica de revisão para a prova:** "Repetível em várias regiões/contas" → **CloudFormation**. "Comandos rápidos sem instalar nada" → **CloudShell**. "Dentro do código da aplicação" → **SDK**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Quais são as formas de interagir com a AWS?"

**Resposta curta:** Console, CLI, SDKs e APIs (e CloudShell).

**Pergunta:** "Um desenvolvedor quer chamar a AWS de dentro do código Python."

**Resposta curta:** SDK (boto3).

**Pergunta:** "Como criar ambientes idênticos de forma repetível e versionada?"

**Resposta curta:** CloudFormation (infraestrutura como código).

**Pergunta:** "Qual a vantagem de IaC?"

**Resposta curta:** Repetibilidade, menos erro manual, versionamento e velocidade.

**Pergunta:** "Qual opção de conectividade passa pela internet pública com criptografia?"

**Resposta curta:** Site-to-Site VPN.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

🏠 [Índice do domínio](README.md) · [3.2 Infraestrutura global](02-infraestrutura-global.md) ➡️
