# 2.1 Modelo de responsabilidade compartilhada

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon EC2 (Elastic Compute Cloud)](../../servicos/computacao/ec2.md) · [Amazon RDS (Relational Database Service)](../../servicos/banco-de-dados/rds.md) · [AWS Lambda](../../servicos/computacao/lambda.md) · [Amazon S3 (Simple Storage Service)](../../servicos/armazenamento/s3.md) · [Amazon DynamoDB](../../servicos/banco-de-dados/dynamodb.md)

🏠 [Índice do domínio](README.md) · [2.2 Usuário root](02-usuario-root.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** A segurança é dividida: a **AWS protege a nuvem em si** (prédios, hardware, rede) e **o cliente protege o que coloca nela** (dados, acessos, configurações). A fronteira muda conforme o serviço.
>
> 🏠 **Analogia:** é como **morar de aluguel num prédio**: o condomínio cuida da portaria, da estrutura e dos elevadores (AWS); você tranca a porta do seu apartamento e decide quem recebe a chave (cliente). Num **hotel** (serviço gerenciado), o hotel faz ainda mais por você.

**Ao terminar este tópico, você deve saber:**

- [ ] Separar **segurança DA nuvem** (AWS) de **segurança NA nuvem** (cliente).
- [ ] Dizer quem aplica patch no SO do **EC2** (cliente) e no motor do **RDS** (AWS).
- [ ] Explicar controles **herdados**, **compartilhados** e **específicos do cliente**.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Patch** | atualização de correção de software. |
| **Hipervisor** | a camada que divide um servidor físico em várias máquinas virtuais (responsabilidade da AWS). |

> 🎯 **Como não errar na prova:** Pergunte: **"isso é físico ou é configuração/dado?"**. Físico, hardware, datacenter → AWS. Dados, IAM, security group, criptografia ativada → cliente. Quanto **mais gerenciado** o serviço, **menos** o cliente faz.

## 📖 Conteúdo

- **AWS — segurança DA nuvem:** hardware, datacenters físicos (acesso, energia, refrigeração), rede global, regiões, AZs, edge locations e a camada de virtualização (hipervisor).
- **Cliente — segurança NA nuvem:** dados, criptografia, identidades e permissões (IAM), configuração de rede (security groups, NACLs, rotas), sistema operacional e aplicações quando ele os gerencia.
- **A divisão muda conforme o tipo de serviço:**

| Serviço | AWS cuida de | Cliente cuida de |
| --- | --- | --- |
| EC2 (IaaS) | Hardware, rede física, hipervisor | Patch do SO convidado, aplicações, security groups, firewall do SO, dados, IAM |
| RDS / Aurora | Hardware, SO, patch do motor do banco, backups automáticos | Usuários do banco, regras de acesso de rede, criptografia ativada, dados |
| Lambda / Fargate | Infra, SO, runtime, escalonamento | Código, permissões (roles), configuração, dados |
| S3 | Infra, durabilidade e disponibilidade do armazenamento | Políticas de bucket, quem acessa, criptografia, versionamento |
| DynamoDB | Infra, SO, software, escalonamento | Acesso via IAM, criptografia e dados |

- **Controles herdados:** o cliente herda da AWS (ex.: controles físicos e ambientais).
- **Controles compartilhados:** cada lado faz a sua parte na sua camada — gestão de patches (AWS na infra, cliente no SO e apps), gestão de configuração e treinamento/conscientização.
- **Controles específicos do cliente:** só o cliente pode fazer (ex.: proteção e zonas de segurança dos dados dele).
- **Cai na prova:** "quem aplica patch no SO de uma EC2?" = cliente. "Quem aplica patch no motor do RDS?" = AWS. "Quem destrói discos físicos ao fim da vida útil?" = AWS. "Quem configura o security group?" = cliente. Quanto mais gerenciado o serviço, menos responsabilidade do cliente.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Qual é responsabilidade da AWS?" → Segurança física dos datacenters, hardware, rede global, hipervisor, patch do SO em serviços gerenciados (RDS, Lambda).
- "Qual é responsabilidade do cliente?" → Dados, IAM, security groups, criptografia, patch do SO no EC2, configuração dos serviços.
- "Qual é um controle compartilhado?" → Gestão de patches, gestão de configuração ou treinamento.
- "Qual é um controle herdado da AWS?" → Controles físicos e ambientais.
- "Ao trocar EC2 por Lambda, o que muda?" → A responsabilidade do cliente diminui (SO e runtime passam para a AWS).
- "Quem é responsável pela segurança dos dados no S3?" → O cliente (políticas, acesso e criptografia).

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

🏠 [Índice do domínio](README.md) · [2.2 Usuário root](02-usuario-root.md) ➡️
