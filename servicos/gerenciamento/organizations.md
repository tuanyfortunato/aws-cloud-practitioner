# AWS Organizations

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma empresa tem várias contas AWS e quer organizá-las, consolidar cobrança e aplicar limites de governança de forma central.

**Como este serviço ajuda?** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.

**Exemplo do dia a dia:** A escola separa testes e produção em contas diferentes e usa a organização para administrá-las sob regras comuns.

**O que ele não resolve sozinho?** Uma política de controle não concede permissão a um usuário por si só. Permissões nas contas continuam necessárias, e a cobertura das políticas tem condições específicas.

**Primeiras palavras para entender:**

- **Conta:** ambiente administrativo AWS.
- **OU:** grupo de contas.
- **SCP:** política que limita permissões disponíveis nas contas às quais se aplica.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / governança multi-conta · **Domínio:** 2 e 4 (faturamento consolidado) · **Escopo:** **Global** · **Gratuito** · **Tópico do guia:** [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)
>
> **Em uma frase:** gerencia várias contas AWS de forma centralizada, com políticas e **uma fatura única**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Organize contas e unidades conforme a separação de trabalho da empresa.

**Passo 2.** Aplique políticas e recursos de administração central compatíveis com os objetivos.

**Passo 3.** Confira o alcance das regras e mantenha permissões nas contas. Uma restrição central não concede acesso a uma identidade.

## 2. Recursos e opções, com significado

### Estrutura

```
Root
├── Management account (paga a fatura; não é afetada por SCPs)
├── OU: Segurança  → contas Log Archive, Audit
├── OU: Produção   → contas prod-app1, prod-app2
└── OU: Desenvolvimento → contas dev-*
```

| Item | Detalhe |
|---|---|
| **Management account** | Cria a organização, convida/cria contas, paga a fatura. SCPs **não afetam** os usuários e roles dela (nem service-linked roles em nenhuma conta), mas afetam o **root das contas-membro**. |
| **Member accounts** | Pertencem a uma só organização por vez. |
| **OUs** | Unidades organizacionais hierárquicas (até 5 níveis); políticas são **herdadas**. |
| **Modos** | *All features* (recomendado, habilita políticas) ou só *consolidated billing*. |
| **Delegated administrator** | Conta-membro administra um serviço (GuardDuty, Security Hub, Config…) para toda a organização. |
| **Trusted access** | Serviços AWS atuando em todas as contas (CloudTrail org trail, Backup, Firewall Manager). |

### Tipos de política

| Política | O que faz |
|---|---|
| **SCP (Service Control Policy)** | **Teto** de permissões das identidades das contas (inclusive o root da conta-membro). **Não concede** nada. Padrão `FullAWSAccess`. Estratégias *deny list* ou *allow list*. |
| **RCP (Resource Control Policy)** | ✔️ Teto de permissões aplicado aos **recursos** (ex.: impedir acesso de identidades de fora da organização a buckets S3). A raiz recebe a política padrão `RCPFullAWSAccess`. Como as SCPs, **não afetam** a conta de gerenciamento nem service-linked roles. |
| **Declarative policies** | Impõem configurações de serviços (ex.: bloquear acesso público a AMIs/snapshots). |
| **Tag policies** | Padronizam tags. |
| **Backup policies** | Planos do AWS Backup em todas as contas. |
| **AI services opt-out** | Impede uso de dados para melhorar serviços de IA da AWS. |

**Permissão efetiva** = interseção de SCP (e RCP) **e** política IAM.

### Consolidated billing

**Uma fatura** para todas as contas; **soma o uso** para descontos por volume (ex.: faixas do S3); **compartilha RIs e Savings Plans**; sem custo extra.

**Compartilhamento de RIs e Savings Plans (task 4.1):** ✔️ ativado por padrão; a conta de gerenciamento pode **desativar** para qualquer conta (inclusive ela mesma); as duas contas precisam ter o compartilhamento ativo; o desconto vale **primeiro na conta que comprou** e a sobra vai para as demais.

🔄 ✔️ Organizações criadas **pelo console** após **10/07/2026** recebem automaticamente na raiz uma SCP que **nega às contas-membro** `organizations:LeaveOrganization` (sair da organização) e `account:CloseAccount` (fechar a conta). Não vale para organizações anteriores nem criadas por API, CLI, SDK ou CloudFormation.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Uma política de controle não concede permissão a um usuário por si só. Permissões nas contas continuam necessárias, e a cobertura das políticas tem condições específicas.

### ⚠️ Pegadinhas

SCP **não** afeta a management account e **não** concede permissões.

Organizations (contas, SCPs, fatura) × **Control Tower** (landing zone pronta sobre o Organizations).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

**Gerenciamento centralizado de acesso root:** remover credenciais root de contas-membro e executar ações privilegiadas a partir da conta de gerenciamento.

## 5. Caso resolvido: ligando as peças

A escola separa testes e produção em contas diferentes e usa a organização para administrá-las sob regras comuns.

**Aplicando a sequência à situação:**

**Etapa 1:** Organize contas e unidades conforme a separação de trabalho da empresa.
**Etapa 2:** Aplique políticas e recursos de administração central compatíveis com os objetivos.
**Etapa 3:** Confira o alcance das regras e mantenha permissões nas contas. Uma restrição central não concede acesso a uma identidade.

**Resultado e responsabilidade:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.

**Recursos envolvidos:** Organização, management account, member accounts, OUs e policies.

**Decisões que precisam ser tomadas:** Estrutura, controles e compartilhamento de benefícios de cobrança.

**Outra situação comentada:** Limitar serviços nas contas membro: SCP junto com permissões IAM necessárias.

**Por que não concluir mais do que isso:** SCP não concede permissão; dados e redes das contas não se fundem

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Impedir que contas de desenvolvimento usem uma região."

**Resposta curta:** SCP.

**Pergunta:** "SCP permite S3, mas o usuário não tem política IAM. Acessa?"

**Resposta curta:** Não.

**Pergunta:** "Desconto por volume somando várias contas."

**Resposta curta:** Consolidated billing.

**Pergunta:** "Fatura única para 20 contas."

**Resposta curta:** Organizations.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
