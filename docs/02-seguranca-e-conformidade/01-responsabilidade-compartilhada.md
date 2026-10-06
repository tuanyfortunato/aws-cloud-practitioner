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

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **sistema operacional:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.

Pense em camadas: prédio e equipamento, virtualização, sistema operacional, ambiente de execução, aplicação, identidade e dados. Um serviço pode administrar mais camadas que outro, mas o cliente continua decidindo como usa a solução.

Quando a pergunta menciona uma correção, identifique em qual camada ela acontece. Atualizar Linux de uma máquina EC2 não é a mesma tarefa que corrigir uma biblioteca incluída numa função. O nome do serviço determina parte dessa divisão.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como **morar de aluguel num prédio**: o condomínio cuida da portaria, da estrutura e dos elevadores (AWS); você tranca a porta do seu apartamento e decide quem recebe a chave (cliente). Num **hotel** (serviço gerenciado), o hotel faz ainda mais por você.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **hipervisor:** Camada que permite executar máquinas virtuais sobre equipamentos físicos. No EC2, ela não é administrada pelo cliente como o sistema dentro de sua máquina.

**AWS — segurança DA nuvem:** hardware, datacenters físicos (acesso, energia, refrigeração), rede global, regiões, AZs, edge locations e a camada de virtualização (hipervisor).

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.

**Cliente — segurança NA nuvem:** dados, criptografia, identidades e permissões (IAM), configuração de rede (security groups, NACLs, rotas), sistema operacional e aplicações quando ele os gerencia.

**A divisão muda conforme o tipo de serviço:**

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **IaaS:** Infraestrutura como serviço: você obtém recursos como uma máquina virtual e administra o sistema operacional e o software instalado.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.
- **runtime:** Ambiente que executa código de uma linguagem ou plataforma. Compatibilidade de bibliotecas e versões deve ser avaliada.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
- **durabilidade:** Capacidade de preservar os dados armazenados. É diferente de disponibilidade, que trata de conseguir acessá-los quando necessário.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.

| Serviço | AWS cuida de | Cliente cuida de |
| --- | --- | --- |
| EC2 (IaaS) | Hardware, rede física, hipervisor | Patch do SO convidado, aplicações, security groups, firewall do SO, dados, IAM |
| RDS / Aurora | Hardware, SO, patch do motor do banco, backups automáticos | Usuários do banco, regras de acesso de rede, criptografia ativada, dados |
| Lambda / Fargate | Infra, SO, runtime, escalonamento | Código, permissões (roles), configuração, dados |
| S3 | Infra, durabilidade e disponibilidade do armazenamento | Políticas de bucket, quem acessa, criptografia, versionamento |
| DynamoDB | Infra, SO, software, escalonamento | Acesso via IAM, criptografia e dados |

**Controles herdados:** o cliente herda da AWS (ex.: controles físicos e ambientais).

**Antes de ler este trecho:**

- **treinamento:** Ajuste de um modelo com dados. É uma etapa diferente de utilizar o modelo já treinado para responder a uma nova entrada.

**Controles compartilhados:** cada lado faz a sua parte na sua camada — gestão de patches (AWS na infra, cliente no SO e apps), gestão de configuração e treinamento/conscientização.

**Controles específicos do cliente:** só o cliente pode fazer (ex.: proteção e zonas de segurança dos dados dele).

**Antes de ler este trecho:**

- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **security group:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.

**Cai na prova:** "quem aplica patch no SO de uma EC2?" = cliente. "Quem aplica patch no motor do RDS?" = AWS. "Quem destrói discos físicos ao fim da vida útil?" = AWS. "Quem configura o security group?" = cliente. Quanto mais gerenciado o serviço, menos responsabilidade do cliente.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.

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
