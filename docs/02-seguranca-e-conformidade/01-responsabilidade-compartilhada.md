# 2.1 Modelo de responsabilidade compartilhada

## 🧠 Antes de começar

**Qual é a dificuldade?** Ao usar um serviço AWS, a equipe precisa saber quem protege cada parte. Se ambos presumirem que o outro fará uma tarefa, ela pode ficar sem responsável.

**A ideia em palavras simples:** A responsabilidade compartilhada divide tarefas entre AWS e cliente. A divisão muda com o tipo de serviço: quanto mais gerenciado, mais tarefas de infraestrutura a AWS assume.

**Exemplo do dia a dia:** Em uma máquina EC2, o cliente atualiza o sistema operacional. Num banco RDS, a AWS assume tarefas de administração previstas pelo serviço, enquanto o cliente controla dados e acessos.

**O que não concluir?** Gerenciado não significa que o cliente deixou de ser responsável pela segurança. Sempre identifique o serviço e a camada de que a pergunta trata.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Patch** | atualização de correção de software. |
| **Hipervisor** | a camada que divide um servidor físico em várias máquinas virtuais (responsabilidade da AWS). |

---

> **Domínio 2 — Segurança e Conformidade (30%)**

> 🔎 **Fichas detalhadas:** [Amazon EC2 (Elastic Compute Cloud)](../../servicos/computacao/ec2.md) · [Amazon RDS (Relational Database Service)](../../servicos/banco-de-dados/rds.md) · [AWS Lambda](../../servicos/computacao/lambda.md) · [Amazon S3 (Simple Storage Service)](../../servicos/armazenamento/s3.md) · [Amazon DynamoDB](../../servicos/banco-de-dados/dynamodb.md)

🏠 [Índice do domínio](README.md) · [2.2 Usuário root](02-usuario-root.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Pense em camadas: prédio e equipamento, virtualização, sistema operacional, ambiente de execução, aplicação, identidade e dados. Um serviço pode administrar mais camadas que outro, mas o cliente continua decidindo como usa a solução.

Quando a pergunta menciona uma correção, identifique em qual camada ela acontece. Atualizar Linux de uma máquina EC2 não é a mesma tarefa que corrigir uma biblioteca incluída numa função. O nome do serviço determina parte dessa divisão.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como **morar de aluguel num prédio**: o condomínio cuida da portaria, da estrutura e dos elevadores (AWS); você tranca a porta do seu apartamento e decide quem recebe a chave (cliente). Num **hotel** (serviço gerenciado), o hotel faz ainda mais por você.

</details>

## 2. Conceitos e opções explicados

**AWS — segurança DA nuvem:** hardware, datacenters físicos (acesso, energia, refrigeração), rede global, regiões, AZs, edge locations e a camada de virtualização (hipervisor).

**Cliente — segurança NA nuvem:** dados, criptografia, identidades e permissões (IAM), configuração de rede (security groups, NACLs, rotas), sistema operacional e aplicações quando ele os gerencia.

**A divisão muda conforme o tipo de serviço:**

| Serviço | AWS cuida de | Cliente cuida de |
| --- | --- | --- |
| EC2 (IaaS) | Hardware, rede física, hipervisor | Patch do SO convidado, aplicações, security groups, firewall do SO, dados, IAM |
| RDS / Aurora | Hardware, SO, patch do motor do banco, backups automáticos | Usuários do banco, regras de acesso de rede, criptografia ativada, dados |
| Lambda / Fargate | Infra, SO, runtime, escalonamento | Código, permissões (roles), configuração, dados |
| S3 | Infra, durabilidade e disponibilidade do armazenamento | Políticas de bucket, quem acessa, criptografia, versionamento |
| DynamoDB | Infra, SO, software, escalonamento | Acesso via IAM, criptografia e dados |

**Controles herdados:** o cliente herda da AWS (ex.: controles físicos e ambientais).

**Controles compartilhados:** cada lado faz a sua parte na sua camada — gestão de patches (AWS na infra, cliente no SO e apps), gestão de configuração e treinamento/conscientização.

**Controles específicos do cliente:** só o cliente pode fazer (ex.: proteção e zonas de segurança dos dados dele).

**Cai na prova:** "quem aplica patch no SO de uma EC2?" = cliente. "Quem aplica patch no motor do RDS?" = AWS. "Quem destrói discos físicos ao fim da vida útil?" = AWS. "Quem configura o security group?" = cliente. Quanto mais gerenciado o serviço, menos responsabilidade do cliente.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** Na EC2, a AWS mantém infraestrutura e hipervisor, e o cliente mantém SO e aplicação. No RDS, a AWS também administra SO e tarefas do banco. Em Lambda, o cliente mantém código, bibliotecas e permissões.

**Depois, compare as escolhas:** Pergunte qual camada o serviço gerencia e qual decisão o cliente continua tomando. Dados, acesso e uso adequado permanecem responsabilidades do cliente.

**Por fim, verifique o limite:** Gerenciado não significa segurança automática da aplicação. Em RDS, o cliente ainda decide acesso, parâmetros aplicáveis, retenção e proteção dos dados.

## 4. Caso resolvido

Quem corrige uma biblioteca vulnerável empacotada na função Lambda?

**Raciocínio e resposta:** O cliente. O gerenciamento da infraestrutura e do runtime gerenciado pela AWS não corrige automaticamente as dependências incluídas no pacote do cliente.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Separar **segurança DA nuvem** (AWS) de **segurança NA nuvem** (cliente).
- [ ] Dizer quem aplica patch no SO do **EC2** (cliente) e no motor do **RDS** (AWS).
- [ ] Explicar controles **herdados**, **compartilhados** e **específicos do cliente**.

**Dica de revisão para a prova:** Pergunte: **"isso é físico ou é configuração/dado?"**. Físico, hardware, datacenter → AWS. Dados, IAM, security group, criptografia ativada → cliente. Quanto **mais gerenciado** o serviço, **menos** o cliente faz.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).
**Pergunta:** "Qual é responsabilidade da AWS?"

**Resposta curta:** Segurança física dos datacenters, hardware, rede global, hipervisor, patch do SO em serviços gerenciados (RDS, Lambda).

**Pergunta:** "Qual é responsabilidade do cliente?"

**Resposta curta:** Dados, IAM, security groups, criptografia, patch do SO no EC2, configuração dos serviços.

**Pergunta:** "Qual é um controle compartilhado?"

**Resposta curta:** Gestão de patches, gestão de configuração ou treinamento.

**Pergunta:** "Qual é um controle herdado da AWS?"

**Resposta curta:** Controles físicos e ambientais.

**Pergunta:** "Ao trocar EC2 por Lambda, o que muda?"

**Resposta curta:** A responsabilidade do cliente diminui (SO e runtime passam para a AWS).

**Pergunta:** "Quem é responsável pela segurança dos dados no S3?"

**Resposta curta:** O cliente (políticas, acesso e criptografia).

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

🏠 [Índice do domínio](README.md) · [2.2 Usuário root](02-usuario-root.md) ➡️
