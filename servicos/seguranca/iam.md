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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.


**Passo 1.** Identifique a pessoa ou programa, a ação necessária e o recurso sobre o qual ela acontecerá.

**Passo 2.** Configure a identidade e políticas adequadas, considerando limites e relações de confiança aplicáveis.

**Passo 3.** A solicitação é avaliada pelos controles. Falta de acesso pode ser problema de permissão, não impossibilidade do serviço.

## 2. Recursos e opções, com significado

### Identidades

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **CLI / SDK:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **role:** Papel que fornece permissões a uma sessão que o assume. O termo função IAM não significa um trecho de código como uma função Lambda.
- **STS:** Serviço que fornece credenciais temporárias AWS. Essas credenciais permitem uma sessão autorizada dentro das permissões aplicáveis.
- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.
- **SCP:** Política de controle de serviços usada na organização para limitar permissões disponíveis em contas às quais se aplica. Ela não concede acesso ao usuário sozinha.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Identidade | Credenciais | Uso |
|---|---|---|
| **Usuário root** | E-mail + senha (+ MFA) | Só tarefas que exigem root. **Não** pode ser limitado por políticas IAM (só por SCP, na Organization). |
| **Usuário IAM** | **Longo prazo**: senha (console) e até **2 access keys** (CLI/SDK) | Pessoa ou aplicação — hoje prefira Identity Center/roles. |
| **Grupo IAM** | — (não faz login) | Agrupar usuários e atribuir permissões. Grupos **não** contêm grupos. |
| **Role IAM** | **Temporárias** (via STS) | Serviços AWS (EC2, Lambda), **cross-account**, usuários federados, Identity Center. |


#### Roles em detalhe


**Antes de ler este trecho:**

- **policy:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.


**Trust policy:** quem pode **assumir** a role (principal: serviço, conta, IdP).


**Permission policy:** o que a role pode fazer.

**Antes de ler este trecho:**

- **instance profile:** Forma de associar uma role IAM a uma máquina EC2. A aplicação obtém permissões temporárias em vez de manter chaves fixas no código.
- **IMDS:** Serviço de metadados da instância. A versão 2 usa um mecanismo de token; metadados e credenciais devem ser usados conforme as recomendações de segurança.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


**Instance profile:** entrega a role a uma instância EC2 (credenciais via IMDS, rotacionadas automaticamente).

**Antes de ler este trecho:**

- **service-linked role:** Role IAM vinculada a um serviço, com relação e função próprias. Seu uso não elimina a necessidade de controlar quem pode operar o serviço.


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


**Antes de ler este trecho:**

- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **RCP:** Política de controle de recursos que limita permissões aplicáveis a recursos compatíveis da organização. É um limite, não uma concessão isolada de acesso.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
- **permissions boundary:** Limite de permissões de uma identidade IAM. Ele restringe a concessão efetiva, mas não concede acesso por si só.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **menor privilégio:** Conceder apenas o acesso necessário ao trabalho. Evita que uma tarefa simples carregue poder desnecessário sobre outros recursos.
- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.
- **ABAC:** Controle de acesso baseado em atributos, como tags, dentro das condições de políticas compatíveis. Não concede acesso sem regras aplicáveis.
- **FIDO2 / TOTP:** Mecanismos de autenticação. FIDO2 usa padrões para credenciais com dispositivos ou autenticadores; TOTP é código temporário calculado com base em tempo.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **CSV:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.


**O que mostra:** Todos os usuários da conta e status de senha, MFA, idade das access keys (CSV).

**Access Advisor / last accessed**


**O que mostra:** Quais serviços cada identidade realmente usou → remover permissões sobrando.

**IAM Access Analyzer**


**O que mostra:** Recursos compartilhados com **entidades externas**, acessos não usados, validação e **geração de políticas** de menor privilégio.

**Policy simulator**


**O que mostra:** Testa se uma ação seria permitida.

### AWS STS (Security Token Service)

Emite **credenciais temporárias** (access key + secret + session token, com expiração de minutos a horas).

**Antes de ler este trecho:**

- **federação:** Uso de uma identidade de um provedor em outro ambiente por uma relação de confiança. Não significa que todos os usuários passam a ser administradores.


APIs: `AssumeRole` (roles e cross-account), `AssumeRoleWithSAML`, `AssumeRoleWithWebIdentity` (federação), `GetSessionToken` (MFA).


É o que está por trás de toda role.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Dar acesso à AWS não cria automaticamente o cadastro dos alunos dentro do aplicativo. IAM trata acesso a recursos AWS; o acesso dos clientes à aplicação é outra necessidade.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.


IAM é **global** e **gratuito**.


**User × Role:** longo prazo × temporário.


**SCP não concede** permissão.

**Antes de ler este trecho:**

- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **SSO:** Uma entrada para vários ambientes autorizados. O usuário ainda recebe acessos definidos para cada ambiente.


**Identity Center** (funcionários, SSO multi-conta) × **Cognito** (usuários finais de apps).


Criar usuários IAM e ver a fatura (com permissão) **não** exigem root.

**Antes de ler este trecho:**

- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.


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

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.


O programa da escola precisa ler materiais do S3, mas não precisa apagar arquivos nem administrar a conta. O objetivo é conceder uma ação limitada ao componente que realmente a executa.

A equipe define uma role apropriada para o ambiente de execução e políticas para as leituras e recursos necessários. A aplicação usa credenciais temporárias da sessão autorizada. Rede, políticas do recurso e chave criptográfica, quando aplicáveis, também podem influenciar o acesso.

Um login válido não garante que a leitura será permitida. Uma negação ou um limite aplicável pode impedir a operação mesmo com uma concessão em outra política. Não use o root ou uma chave administrativa fixa só porque é mais fácil: essas identidades oferecem poder além da tarefa descrita.

**Recursos envolvidos:** Usuários, grupos, roles e policies.

**Decisões que precisam ser tomadas:** Actions, resources, conditions e identidade confiável.


**Outra situação comentada:** Aplicação EC2 lê S3 com role; permissões e rede continuam requisitos distintos.

**Por que não concluir mais do que isso:** Policy é permissão, não conexão de rede; Deny explícito prevalece nos contextos aplicáveis

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Pessoas e programas precisam acessar recursos AWS, mas nem todos devem poder ler, alterar ou apagar as mesmas coisas.

**2. O que a solução fornece?**

IAM define identidades e permissões. Você descreve quais ações uma identidade pode realizar em quais recursos, usando políticas e mecanismos de acesso.

**3. Que conclusão seria incorreta?**

Dar acesso à AWS não cria automaticamente o cadastro dos alunos dentro do aplicativo. IAM trata acesso a recursos AWS; o acesso dos clientes à aplicação é outra necessidade.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Aplicação no EC2 precisa ler o S3 com segurança."

**Resposta curta:** IAM role na instância.


**Fundamento explicado no capítulo:** "Aplicação no EC2 precisa ler o S3 com segurança." → IAM role na instância.

**Pergunta:** "Dez desenvolvedores com as mesmas permissões."

**Resposta curta:** Grupo IAM.


**Fundamento explicado no capítulo:** "Dez desenvolvedores com as mesmas permissões." → Grupo IAM.

**Pergunta:** "Allow e Deny explícito para a mesma ação."

**Resposta curta:** Deny vence.


**Fundamento explicado no capítulo:** "Allow e Deny explícito para a mesma ação." → Deny vence.

**Pergunta:** "Relatório com status de MFA e access keys de todos os usuários."

**Resposta curta:** Credential report.


**Fundamento explicado no capítulo:** "Relatório com status de MFA e access keys de todos os usuários." → Credential report.

**Pergunta:** "Quais serviços um usuário nunca usa?"

**Resposta curta:** Access Advisor (last accessed).


**Fundamento explicado no capítulo:** "Quais serviços um usuário nunca usa?" → Access Advisor (last accessed).

**Pergunta:** "Recursos compartilhados com contas externas."

**Resposta curta:** IAM Access Analyzer.


**Fundamento explicado no capítulo:** "Recursos compartilhados com contas externas." → IAM Access Analyzer.

**Pergunta:** "Serviço que emite credenciais temporárias."

**Resposta curta:** AWS STS.


**Fundamento explicado no capítulo:** "Serviço que emite credenciais temporárias." → AWS STS.

**Pergunta:** "Acesso de uma conta a recursos de outra."

**Resposta curta:** Role cross-account.


**Fundamento explicado no capítulo:** "Acesso de uma conta a recursos de outra." → Role cross-account.


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
