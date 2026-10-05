# 2.3 AWS IAM (Identity and Access Management)

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma aplicação precisa ler documentos, enquanto uma pessoa administra recursos. Dar o mesmo acesso a todos deixa permissões desnecessárias disponíveis.

**A ideia em palavras simples:** Identidade e acesso tratam de quem faz uma ação e do que essa identidade está autorizada a fazer. IAM organiza permissões AWS; outros serviços atendem funcionários ou usuários de aplicações.

**Exemplo do dia a dia:** O programa da escola recebe permissão para ler um conjunto de arquivos, sem poder apagar tudo ou administrar a conta.

**O que não concluir?** Confirmar um login é diferente de conceder uma ação. Você precisa distinguir a identidade, o recurso e a permissão necessária, não apenas decorar o nome de um serviço.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Autenticação** | provar quem você é (login). |
| **Autorização** | o que você tem permissão de fazer. |
| **Role** | identidade com credenciais temporárias, assumida por quem precisa. |
| **Federação** | entrar com uma identidade de fora (AD, Google, Okta) sem criar usuário IAM. |

---

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS IAM (Identity and Access Management) e AWS STS](../../servicos/seguranca/iam.md) · [AWS IAM Identity Center (antigo AWS SSO)](../../servicos/seguranca/iam-identity-center.md) · [Amazon Cognito](../../servicos/seguranca/cognito.md) · [AWS Directory Service](../../servicos/seguranca/directory-service.md) · [AWS Secrets Manager e Systems Manager Parameter Store](../../servicos/seguranca/secrets-manager-e-parameter-store.md)

⬅️ [2.2 Usuário root](02-usuario-root.md) · 🏠 [Índice do domínio](README.md) · [2.4 Governança multi-conta](04-governanca-multi-conta.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.


Uma solicitação possui autor, ação e alvo. Primeiro o sistema verifica a identidade; depois avalia se aquela ação pode ocorrer sobre aquele recurso. Uma identidade autenticada pode continuar sem permissão para realizar a operação.

Um programa que lê um bucket precisa de acesso adequado aos dados e, quando aplicável, à chave de proteção. Usar credenciais temporárias melhora a forma de acesso, mas não elimina políticas e limites. Funcionários e clientes de aplicativos também pedem soluções de identidade diferentes.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é o **sistema de crachás de uma empresa**: o usuário é a pessoa com crachá; o grupo é o departamento; a role é um **crachá de visitante** temporário que alguém pega emprestado; a política é a lista de salas que o crachá abre.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.


**Serviço global e gratuito** para controlar quem (autenticação) pode fazer o quê (autorização) na conta.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **CLI / SDK:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.


**Usuário IAM:** identidade com credenciais de longo prazo (senha para console, access keys para CLI/SDK). Representa uma pessoa ou aplicação.


**Grupo IAM:** coleção de usuários que recebem as mesmas permissões. Grupos não contêm outros grupos e não são identidades (não fazem login).

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **role:** Papel que fornece permissões a uma sessão que o assume. O termo função IAM não significa um trecho de código como uma função Lambda.


**Role IAM:** identidade com credenciais **temporárias**, assumida por quem precisa: serviços AWS (ex.: EC2 ou Lambda acessando S3), usuários de outra conta (cross-account) ou usuários federados. Não tem senha nem access key fixa.

**Antes de ler este trecho:**

- **JSON:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.


**Policies:** documentos JSON com Effect (Allow/Deny), Action, Resource e Condition.


  - **Identity-based:** anexadas a usuários, grupos ou roles.
**Antes de ler este trecho:**

- **policy:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.


  - **Resource-based:** anexadas ao recurso (ex.: bucket policy no S3) e indicam quem pode acessá-lo.

  - **AWS managed** (prontas, mantidas pela AWS), **customer managed** (criadas por você, reutilizáveis) e **inline** (embutidas em uma só identidade).

  - **Regra de avaliação:** tudo começa negado (implicit deny); um Allow libera; um Deny explícito sempre vence.
**Antes de ler este trecho:**

- **menor privilégio:** Conceder apenas o acesso necessário ao trabalho. Evita que uma tarefa simples carregue poder desnecessário sobre outros recursos.


**Princípio do menor privilégio:** conceder só as permissões necessárias para a tarefa. Aparece em muitas respostas corretas.


**Credenciais e boas práticas:**

**Antes de ler este trecho:**

- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **TOTP:** Mecanismos de autenticação. FIDO2 usa padrões para credenciais com dispositivos ou autenticadores; TOTP é código temporário calculado com base em tempo.


  - **MFA:** apps de autenticação (virtual), chaves físicas FIDO/passkeys e tokens de hardware TOTP.

  - **Password policy:** tamanho mínimo, complexidade, expiração e reuso de senhas dos usuários IAM.
**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.


  - **Access keys:** para CLI, SDK e API. Nunca colocar no código; rotacionar; preferir roles.
**Antes de ler este trecho:**

- **instance profile:** Forma de associar uma role IAM a uma máquina EC2. A aplicação obtém permissões temporárias em vez de manter chaves fixas no código.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


  - **Roles para EC2 (instance profile):** forma correta de dar permissão a uma aplicação em EC2, em vez de guardar access keys na instância.

**Ferramentas de auditoria do IAM:**


  - **Credential report:** relatório da conta com todos os usuários e o status das credenciais (senha, MFA, idade das access keys).

  - **Access Advisor (last accessed):** mostra quais serviços um usuário ou role realmente usou, para remover permissões sobrando.

  - **IAM Access Analyzer:** identifica recursos compartilhados com entidades externas e ajuda a gerar políticas de menor privilégio.
**Antes de ler este trecho:**

- **SAML / OIDC:** Padrões de integração de identidade entre sistemas. Permitem que uma aplicação ou serviço confie em informações fornecidas por um provedor de identidade compatível.
- **federação:** Uso de uma identidade de um provedor em outro ambiente por uma relação de confiança. Não significa que todos os usuários passam a ser administradores.
- **Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.


**Federação:** usar identidades externas (Active Directory, Google, Okta) via SAML 2.0 ou OIDC, sem criar usuários IAM.

**Antes de ler este trecho:**

- **AWS IAM:** IAM define identidades e permissões.
- **AWS IAM Identity Center:** IAM Identity Center centraliza o acesso da força de trabalho.
- **IAM Identity Center:** Serviço de acesso central para a força de trabalho. Atribuições de contas e aplicações não são o cadastro de clientes de um aplicativo.
- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.
- **SSO:** Uma entrada para vários ambientes autorizados. O usuário ainda recebe acessos definidos para cada ambiente.
- **Permission sets:** Conjuntos de permissões atribuídos no IAM Identity Center para acesso às contas. Uma entrada central não transforma toda sessão em administradora.


**AWS IAM Identity Center** (antigo AWS SSO): login único centralizado para várias contas do Organizations e aplicações SaaS, com conjuntos de permissões (permission sets). É a forma recomendada de dar acesso humano a ambientes multi-conta.

**Antes de ler este trecho:**

- **Amazon Cognito / Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.


**Amazon Cognito:** autenticação de **usuários finais** de aplicações web e mobile (cadastro, login, login social). Não é para funcionários acessarem a AWS.

**Antes de ler este trecho:**

- **AWS Directory Service / Directory Service:** Directory Service oferece opções para diretórios e integração com Active Directory, conforme a modalidade.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.


**AWS Directory Service:** Microsoft Active Directory gerenciado na AWS, ou conector para o AD on-premises.

**Antes de ler este trecho:**

- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.


**Secrets Manager:** Guarda segredos (senhas de banco, chaves de API) criptografados com KMS. **Cai na prova:** é o serviço com **rotação automática** de segredos, com integração nativa com RDS. É pago por segredo.

**Antes de ler este trecho:**

- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.
- **Parameter Store:** Recurso de armazenamento de parâmetros do Systems Manager. É necessário configurar proteção e permissão, inclusive para valores sensíveis.


**Systems Manager Parameter Store:** guarda parâmetros e segredos simples; tem camada gratuita; não faz rotação automática nativa.


**Formas de acessar a AWS:** Console (usuário/senha + MFA), CLI e SDKs (access keys ou credenciais temporárias), CloudShell (terminal no navegador, já autenticado).

### ➕ Complemento — boas práticas do IAM

Atribuir permissões a **grupos**, não diretamente a usuários.


Preferir **credenciais temporárias** (roles, Identity Center) a usuários com access keys de longo prazo.


Exigir MFA, aplicar política de senhas, rotacionar credenciais e remover usuários e permissões sem uso.

**Antes de ler este trecho:**

- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.


Usar **condições** nas políticas (ex.: exigir MFA, limitar por IP).

**Antes de ler este trecho:**

- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.


IAM é **global** (não regional) e **gratuito**.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **SCP:** Política de controle de serviços usada na organização para limitar permissões disponíveis em contas às quais se aplica. Ela não concede acesso ao usuário sozinha.


**Primeiro, identifique o funcionamento:** Autenticação confirma a identidade; autorização avalia a ação sobre o recurso. Policies definem permissões; roles fornecem sessões temporárias. Grupos agrupam usuários IAM, não roles.

**Depois, compare as escolhas:** Funcionários em várias contas: IAM Identity Center. Aplicação na EC2: role. Clientes de um aplicativo: Cognito. API requer credenciais apropriadas, normalmente temporárias.

**Por fim, verifique o limite:** Um Allow pode ser limitado por boundary ou SCP, e um Deny explícito prevalece. MFA não concede autorização. Criar usuário não fornece acesso automaticamente.

## 4. Caso resolvido

Uma aplicação na EC2 precisa ler um bucket e não deve guardar chaves de longa duração. O que usar?

**Raciocínio e resposta:** IAM role associada à instância. A aplicação obtém credenciais temporárias; ainda é preciso permitir as operações no bucket e, se aplicável, na chave KMS.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma aplicação precisa ler documentos, enquanto uma pessoa administra recursos. Dar o mesmo acesso a todos deixa permissões desnecessárias disponíveis.

**2. O que a solução fornece?**

Identidade e acesso tratam de quem faz uma ação e do que essa identidade está autorizada a fazer. IAM organiza permissões AWS; outros serviços atendem funcionários ou usuários de aplicações.

**3. Que conclusão seria incorreta?**

Confirmar um login é diferente de conceder uma ação. Você precisa distinguir a identidade, o recurso e a permissão necessária, não apenas decorar o nome de um serviço.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Diferenciar **usuário, grupo, role e política**.
- [ ] Aplicar a regra de avaliação: tudo começa **negado**, um **Allow** libera e um **Deny explícito sempre vence**.
- [ ] Explicar o **menor privilégio** e por que usar **roles** em vez de access keys no EC2.
- [ ] Diferenciar **IAM Identity Center** (funcionários, várias contas) de **Cognito** (clientes de um app).

**Dica de revisão para a prova:** "Aplicação no EC2 precisa acessar o S3" → **role**, nunca access key. "Login único em várias contas" → **Identity Center**. "Usuários do aplicativo" → **Cognito**. "Rotação automática de senhas" → **Secrets Manager**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).
**Pergunta:** "Uma aplicação no EC2 precisa ler um bucket S3. Qual a forma mais segura?"

**Resposta curta:** Anexar uma IAM role à instância.


**Fundamento explicado no capítulo:** "Uma aplicação no EC2 precisa ler um bucket S3. Qual a forma mais segura?" → Anexar uma IAM role à instância.

**Pergunta:** "Dez desenvolvedores precisam das mesmas permissões."

**Resposta curta:** Criar um grupo IAM e anexar a política ao grupo.


**Fundamento explicado no capítulo:** "Dez desenvolvedores precisam das mesmas permissões." → Criar um grupo IAM e anexar a política ao grupo.

**Pergunta:** "Uma política tem Allow e outra tem Deny explícito para a mesma ação. O que vale?"

**Resposta curta:** Deny explícito.


**Fundamento explicado no capítulo:** "Uma política tem Allow e outra tem Deny explícito para a mesma ação. O que vale?" → Deny explícito.

**Pergunta:** "Qual princípio diz para dar só as permissões necessárias?"

**Resposta curta:** Menor privilégio.


**Fundamento explicado no capítulo:** "Qual princípio diz para dar só as permissões necessárias?" → Menor privilégio.

**Pergunta:** "Qual relatório lista os usuários e o status de MFA e access keys?"

**Resposta curta:** IAM credential report.


**Fundamento explicado no capítulo:** "Qual relatório lista os usuários e o status de MFA e access keys?" → IAM credential report.

**Pergunta:** "Como dar login único a funcionários em várias contas?"

**Resposta curta:** IAM Identity Center.


**Fundamento explicado no capítulo:** "Como dar login único a funcionários em várias contas?" → IAM Identity Center.

**Pergunta:** "Como permitir login com Google em um app mobile?"

**Resposta curta:** Amazon Cognito.


**Fundamento explicado no capítulo:** "Como permitir login com Google em um app mobile?" → Amazon Cognito.

**Pergunta:** "Onde guardar a senha do banco com rotação automática?"

**Resposta curta:** Secrets Manager.


**Fundamento explicado no capítulo:** "Onde guardar a senha do banco com rotação automática?" → Secrets Manager.

**Pergunta:** "Funcionários usam o Active Directory da empresa e precisam acessar a AWS."

**Resposta curta:** Federação (via Identity Center ou SAML) ou AWS Directory Service.


**Fundamento explicado no capítulo:** "Funcionários usam o Active Directory da empresa e precisam acessar a AWS." → Federação (via Identity Center ou SAML) ou AWS Directory Service.

**Pergunta:** "Como acessar a AWS por linha de comando?"

**Resposta curta:** AWS CLI com access keys (ou credenciais temporárias).


**Fundamento explicado no capítulo:** "Como acessar a AWS por linha de comando?" → AWS CLI com access keys (ou credenciais temporárias).

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **Secrets Manager × Parameter Store (📌):** a **rotação automática nativa** de credenciais (ex.: RDS) é do **Secrets Manager**. O Parameter Store guarda configurações e segredos simples, **sem rotação nativa**.
- 🔄 **MFA obrigatório para o root:** a AWS passou a exigir MFA para usuários root (primeiro nas contas de gerenciamento do Organizations, depois nas contas independentes). Em Organizations também existe o **gerenciamento centralizado de acesso root**, que permite remover as credenciais root das contas-membro.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.2 Usuário root](02-usuario-root.md) · 🏠 [Índice do domínio](README.md) · [2.4 Governança multi-conta](04-governanca-multi-conta.md) ➡️
