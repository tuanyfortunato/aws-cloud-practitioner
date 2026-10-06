# AWS IAM (Identity and Access Management) e AWS STS

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Pessoas e programas precisam acessar recursos AWS, mas nem todos devem poder ler, alterar ou apagar as mesmas coisas.

**Como este serviço ajuda?** IAM define identidades e permissões. Você descreve quais ações uma identidade pode realizar em quais recursos, usando políticas e mecanismos de acesso.

**Exemplo do dia a dia:** A escola permite que um programa leia documentos num bucket S3, sem dar a ele permissão para apagar os arquivos ou administrar a conta inteira.

**O que ele não resolve sozinho?** Dar acesso à AWS não cria automaticamente o cadastro dos alunos dentro do aplicativo. IAM trata acesso a recursos AWS; o acesso dos clientes à aplicação é outra necessidade.

**Primeiras palavras para entender:**

- **Identidade:** quem faz a ação.
- **Política:** regras de permissão.
- **Role:** papel assumido para obter permissões, geralmente por credenciais temporárias.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / identidade · **Domínio:** 2 · **Escopo:** **Global** · **Gratuito** · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md) · [2.2 Usuário root](../../docs/02-seguranca-e-conformidade/02-usuario-root.md)
>
> **Em uma frase:** controla **quem** pode se autenticar e **o que** cada identidade pode fazer em quais recursos da conta.
>
> **Escopo oficial:** ✅ No escopo (STS ⚪ não listado) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Identifique a pessoa ou programa, a ação necessária e o recurso sobre o qual ela acontecerá.

**Passo 2.** Configure a identidade e políticas adequadas, considerando limites e relações de confiança aplicáveis.

**Passo 3.** A solicitação é avaliada pelos controles. Falta de acesso pode ser problema de permissão, não impossibilidade do serviço.

## 2. Recursos e opções, com significado

### Identidades

| Identidade | Credenciais | Uso |
|---|---|---|
| **Usuário root** | E-mail + senha (+ MFA) | Só tarefas que exigem root. **Não** pode ser limitado por políticas IAM (só por SCP, na Organization). |
| **Usuário IAM** | **Longo prazo**: senha (console) e até **2 access keys** (CLI/SDK) | Pessoa ou aplicação — hoje prefira Identity Center/roles. |
| **Grupo IAM** | — (não faz login) | Agrupar usuários e atribuir permissões. Grupos **não** contêm grupos. |
| **Role IAM** | **Temporárias** (via STS) | Serviços AWS (EC2, Lambda), **cross-account**, usuários federados, Identity Center. |

#### Roles em detalhe

**Trust policy:** quem pode **assumir** a role (principal: serviço, conta, IdP).

**Permission policy:** o que a role pode fazer.

**Instance profile:** entrega a role a uma instância EC2 (credenciais via IMDS, rotacionadas automaticamente).

**Service-linked role:** criada e gerenciada por um serviço AWS.

### Políticas

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::meu-bucket/*",
    "Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}
  }]
}
```

| Tipo | Anexada a | Observação |
|---|---|---|
| **Identity-based** | Usuário, grupo, role | AWS managed, customer managed ou inline |
| **Resource-based** | Recurso (bucket policy, key policy, política de fila SQS, Lambda) | Tem `Principal`; permite acesso **cross-account** |
| **Permissions boundary** | Usuário/role | **Teto** de permissões (delegar criação de usuários com segurança) |
| **SCP / RCP** | Contas/OUs (Organizations) | Teto para a conta inteira — não concedem nada |
| **Session policy** | Sessão temporária | Restringe uma sessão assumida |

#### Lógica de avaliação

1. Tudo começa **negado** (implicit deny).

2. Um **Deny explícito** em qualquer política → **negado** (sempre vence).

3. SCP/boundary/session limitam; precisa haver um **Allow** em identity- ou resource-based.

### Credenciais e boas práticas

| Prática | Detalhe |
|---|---|
| **MFA** | Virtual (app), chave de segurança FIDO2/**passkey**, token de hardware TOTP ✔️; até 8 dispositivos por identidade. Pode ser exigido via condição. |
| **Password policy** | Tamanho, complexidade, expiração, reuso. |
| **Menor privilégio** | Começar com o mínimo; usar Access Analyzer para gerar políticas. |
| **Credenciais temporárias** | Preferir roles e Identity Center a access keys de longo prazo. |
| **Access keys** | Nunca no código/repositório; rotacionar; apagar as sem uso. |
| **Root** | MFA, sem access keys, uso mínimo. |
| **Grupos** | Permissões em grupos, não em usuários. |
| **ABAC** | Controle por tags (ex.: só acessar recursos com `projeto=x`). |

### Ferramentas de auditoria

**Credential report**

**O que mostra:** Todos os usuários da conta e status de senha, MFA, idade das access keys (CSV).

**Access Advisor / last accessed**

**O que mostra:** Quais serviços cada identidade realmente usou → remover permissões sobrando.

**IAM Access Analyzer**

**O que mostra:** Recursos compartilhados com **entidades externas**, acessos não usados, validação e **geração de políticas** de menor privilégio.

**Policy simulator**

**O que mostra:** Testa se uma ação seria permitida.

### AWS STS (Security Token Service)

Emite **credenciais temporárias** (access key + secret + session token, com expiração de minutos a horas).

APIs: `AssumeRole` (roles e cross-account), `AssumeRoleWithSAML`, `AssumeRoleWithWebIdentity` (federação), `GetSessionToken` (MFA).

É o que está por trás de toda role.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Dar acesso à AWS não cria automaticamente o cadastro dos alunos dentro do aplicativo. IAM trata acesso a recursos AWS; o acesso dos clientes à aplicação é outra necessidade.

### ⚠️ Pegadinhas e não confundir

IAM é **global** e **gratuito**.

**User × Role:** longo prazo × temporário.

**SCP não concede** permissão.

**Identity Center** (funcionários, SSO multi-conta) × **Cognito** (usuários finais de apps).

Criar usuários IAM e ver a fatura (com permissão) **não** exigem root.

✔️ 🔄 **Alterar o nome da conta**, contatos, contatos alternativos, moeda de pagamento e regiões **não exigem root**; **mudar o plano de suporte** também saiu da lista oficial de tarefas do root.

✔️ Até **8 dispositivos MFA** de qualquer tipo por usuário IAM e para o root.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

**MFA obrigatório para root:** contas de gerenciamento (maio/2024), contas standalone (junho/2024) e contas-membro (2025).

**Gerenciamento centralizado de acesso root** (Organizations, novembro/2024): remove credenciais root das contas-membro e executa ações privilegiadas de forma central.

### Segurança e responsabilidade compartilhada

**AWS:** disponibilidade e segurança do serviço IAM.

**Cliente:** **tudo o que é configurado**: identidades, políticas, MFA, rotação de credenciais (controle **específico do cliente**).

## 5. Caso resolvido: ligando as peças

O programa da escola precisa ler materiais do S3, mas não precisa apagar arquivos nem administrar a conta. O objetivo é conceder uma ação limitada ao componente que realmente a executa.

A equipe define uma role apropriada para o ambiente de execução e políticas para as leituras e recursos necessários. A aplicação usa credenciais temporárias da sessão autorizada. Rede, políticas do recurso e chave criptográfica, quando aplicáveis, também podem influenciar o acesso.

Um login válido não garante que a leitura será permitida. Uma negação ou um limite aplicável pode impedir a operação mesmo com uma concessão em outra política. Não use o root ou uma chave administrativa fixa só porque é mais fácil: essas identidades oferecem poder além da tarefa descrita.

**Recursos envolvidos:** Usuários, grupos, roles e policies.

**Decisões que precisam ser tomadas:** Actions, resources, conditions e identidade confiável.

**Outra situação comentada:** Aplicação EC2 lê S3 com role; permissões e rede continuam requisitos distintos.

**Por que não concluir mais do que isso:** Policy é permissão, não conexão de rede; Deny explícito prevalece nos contextos aplicáveis

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Aplicação no EC2 precisa ler o S3 com segurança."

**Resposta curta:** IAM role na instância.

**Pergunta:** "Dez desenvolvedores com as mesmas permissões."

**Resposta curta:** Grupo IAM.

**Pergunta:** "Allow e Deny explícito para a mesma ação."

**Resposta curta:** Deny vence.

**Pergunta:** "Relatório com status de MFA e access keys de todos os usuários."

**Resposta curta:** Credential report.

**Pergunta:** "Quais serviços um usuário nunca usa?"

**Resposta curta:** Access Advisor (last accessed).

**Pergunta:** "Recursos compartilhados com contas externas."

**Resposta curta:** IAM Access Analyzer.

**Pergunta:** "Serviço que emite credenciais temporárias."

**Resposta curta:** AWS STS.

**Pergunta:** "Acesso de uma conta a recursos de outra."

**Resposta curta:** Role cross-account.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Boas práticas do IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Tarefas que exigem root](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
