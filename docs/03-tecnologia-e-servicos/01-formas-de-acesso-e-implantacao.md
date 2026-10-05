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

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [AWS CloudFormation (e CDK, SAM)](../../servicos/gerenciamento/cloudformation.md) · [AWS VPN (Site-to-Site VPN e Client VPN)](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) · [AWS Direct Connect](../../servicos/redes/direct-connect.md)

🏠 [Índice do domínio](README.md) · [3.2 Infraestrutura global](02-infraestrutura-global.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.


A tela, o comando e o programa são meios de pedir operações ao serviço. O recurso criado não muda de natureza porque a solicitação foi feita de outro modo. A mesma identidade continua limitada pelos controles aplicáveis.

Automatizar é descrever ações para repetir com menos trabalho manual. É necessário tratar resultado e erro, além de fornecer credenciais adequadas. Um arquivo de infraestrutura descreve recursos; uma biblioteca ajuda um programa a chamar operações.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como falar com um **banco**: pelo **site** (Console), pelo **atendimento por comandos** (CLI), por um **aplicativo seu integrado ao banco** (SDK) ou deixando **instruções programadas** que se repetem sozinhas (CloudFormation).

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**AWS Management Console:** interface web. Bom para tarefas pontuais e exploração.

**Antes de ler este trecho:**

- **CLI:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.


**AWS CLI:** linha de comando para automatizar via scripts.


**SDKs:** bibliotecas para usar a AWS dentro do código (Python/boto3, Java, JavaScript etc.).


**AWS CloudShell:** terminal no navegador, já autenticado e com a CLI instalada, sem custo adicional.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.


**APIs:** tudo na AWS é uma chamada de API; Console, CLI e SDK usam as mesmas APIs por baixo.

**Antes de ler este trecho:**

- **AWS CloudFormation:** CloudFormation usa um arquivo de descrição para criar e atualizar conjuntos de recursos AWS compatíveis, com suas dependências.
- **CloudFormation / IaC:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **JSON:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
- **YAML:** Formatos de representação de dados e configurações. Um arquivo nesses formatos descreve informações; ele não cria permissões nem recursos sem ser usado por uma ferramenta.


**Infraestrutura como código (IaC):** **AWS CloudFormation** (templates JSON/YAML que criam pilhas de recursos de forma repetível) — o Terraform é um equivalente de terceiros. Ver [3.16](16-gestao-e-governanca.md).


**Operações pontuais vs repetíveis:** tarefa única pode ser no Console; tarefa repetível deve ser automatizada (CLI, SDK, CloudFormation).

**Antes de ler este trecho:**

- **AWS VPN:** Site-to-Site VPN liga redes por um túnel criptografado.
- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **AWS Direct Connect / Direct Connect:** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.


**Conectividade com a AWS:** internet pública, AWS VPN (Site-to-Site ou Client VPN) e AWS Direct Connect. Ver [3.10](10-rede-e-entrega-de-conteudo.md).

**Antes de ler este trecho:**

- **provisionar:** Criar ou disponibilizar capacidade e recursos. Um recurso provisionado pode ter cobrança mesmo enquanto está esperando trabalho.


**Cai na prova:** "provisionar o mesmo ambiente em várias regiões de forma repetível" = CloudFormation; "executar comandos rápidos sem instalar nada" = CloudShell.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **híbrido:** Combinação de ambiente próprio e nuvem. É necessário definir quais partes ficam em cada lado e como se comunicam.


**Primeiro, identifique o funcionamento:** Console fornece interface visual; CLI executa comandos; SDK integra APIs ao código. CloudFormation descreve recursos e suas dependências em templates e stacks.

**Depois, compare as escolhas:** Operação pontual: console pode bastar. Automação repetida: CLI/SDK. Ambiente reproduzível: IaC. Híbrido mantém parte no ambiente próprio com conectividade apropriada.

**Por fim, verifique o limite:** Mudar de interface não amplia permissões. Templates não tornam recursos gratuitos. Scripts imperativos precisam lidar com erros e repetição; IaC registra o estado desejado.

## 4. Caso resolvido

A equipe recria o mesmo ambiente de teste toda semana. Qual abordagem reduz divergências?

**Raciocínio e resposta:** IaC com CloudFormation, em vez de repetir cliques manualmente. A stack usa permissões e gera custos dos recursos criados.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Você precisa criar ou consultar recursos AWS, mas pode fazer isso por uma tela, por comandos, por um programa ou por uma descrição automatizada do ambiente.

**2. O que a solução fornece?**

São maneiras diferentes de operar serviços. Console oferece interface visual; CLI usa comandos; SDK integra programas; ferramentas de infraestrutura descrevem recursos para implantação.

**3. Que conclusão seria incorreta?**

A forma de acesso não muda sozinha o que a identidade pode fazer. Uma ferramenta de operação também não é o serviço que hospeda a aplicação.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Diferenciar **Console, CLI, SDK e CloudShell**.
- [ ] Saber que tarefa **pontual** pode ser no Console e tarefa **repetível** deve ser automatizada.
- [ ] Explicar **infraestrutura como código** (CloudFormation).

**Dica de revisão para a prova:** "Repetível em várias regiões/contas" → **CloudFormation**. "Comandos rápidos sem instalar nada" → **CloudShell**. "Dentro do código da aplicação" → **SDK**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Quais são as formas de interagir com a AWS?"

**Resposta curta:** Console, CLI, SDKs e APIs (e CloudShell).


**Fundamento explicado no capítulo:** "Quais são as formas de interagir com a AWS?" → Console, CLI, SDKs e APIs (e CloudShell).

**Pergunta:** "Um desenvolvedor quer chamar a AWS de dentro do código Python."

**Resposta curta:** SDK (boto3).


**Fundamento explicado no capítulo:** "Um desenvolvedor quer chamar a AWS de dentro do código Python." → SDK (boto3).

**Pergunta:** "Como criar ambientes idênticos de forma repetível e versionada?"

**Resposta curta:** CloudFormation (infraestrutura como código).


**Fundamento explicado no capítulo:** "Como criar ambientes idênticos de forma repetível e versionada?" → CloudFormation (infraestrutura como código).

**Pergunta:** "Qual a vantagem de IaC?"

**Resposta curta:** Repetibilidade, menos erro manual, versionamento e velocidade.


**Fundamento explicado no capítulo:** "Qual a vantagem de IaC?" → Repetibilidade, menos erro manual, versionamento e velocidade.

**Pergunta:** "Qual opção de conectividade passa pela internet pública com criptografia?"

**Resposta curta:** Site-to-Site VPN.

**Antes de ler este trecho:**

- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.


**Fundamento explicado no capítulo:** "Qual opção de conectividade passa pela internet pública com criptografia?" → Site-to-Site VPN.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

🏠 [Índice do domínio](README.md) · [3.2 Infraestrutura global](02-infraestrutura-global.md) ➡️
