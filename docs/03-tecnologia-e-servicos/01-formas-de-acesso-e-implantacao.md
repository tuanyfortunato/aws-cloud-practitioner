# 3.1 Formas de acessar e implantar na AWS

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [AWS CloudFormation (e CDK, SAM)](../../servicos/gerenciamento/cloudformation.md) · [AWS VPN (Site-to-Site VPN e Client VPN)](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) · [AWS Direct Connect](../../servicos/redes/direct-connect.md)

🏠 [Índice do domínio](README.md) · [3.2 Infraestrutura global](02-infraestrutura-global.md) ➡️

---

## 📖 Conteúdo

- **AWS Management Console:** interface web. Bom para tarefas pontuais e exploração.
- **AWS CLI:** linha de comando para automatizar via scripts.
- **SDKs:** bibliotecas para usar a AWS dentro do código (Python/boto3, Java, JavaScript etc.).
- **AWS CloudShell:** terminal no navegador, já autenticado e com a CLI instalada, sem custo adicional.
- **APIs:** tudo na AWS é uma chamada de API; Console, CLI e SDK usam as mesmas APIs por baixo.
- **Infraestrutura como código (IaC):** **AWS CloudFormation** (templates JSON/YAML que criam pilhas de recursos de forma repetível) — o Terraform é um equivalente de terceiros. Ver [3.16](16-gestao-e-governanca.md).
- **Operações pontuais vs repetíveis:** tarefa única pode ser no Console; tarefa repetível deve ser automatizada (CLI, SDK, CloudFormation).
- **Conectividade com a AWS:** internet pública, AWS VPN (Site-to-Site ou Client VPN) e AWS Direct Connect. Ver [3.10](10-rede-e-entrega-de-conteudo.md).
- **Cai na prova:** "provisionar o mesmo ambiente em várias regiões de forma repetível" = CloudFormation; "executar comandos rápidos sem instalar nada" = CloudShell.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Quais são as formas de interagir com a AWS?" → Console, CLI, SDKs e APIs (e CloudShell).
- "Um desenvolvedor quer chamar a AWS de dentro do código Python." → SDK (boto3).
- "Como criar ambientes idênticos de forma repetível e versionada?" → CloudFormation (infraestrutura como código).
- "Qual a vantagem de IaC?" → Repetibilidade, menos erro manual, versionamento e velocidade.
- "Qual opção de conectividade passa pela internet pública com criptografia?" → Site-to-Site VPN.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

🏠 [Índice do domínio](README.md) · [3.2 Infraestrutura global](02-infraestrutura-global.md) ➡️
