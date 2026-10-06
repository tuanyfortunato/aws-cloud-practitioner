# 2.5 Criptografia

## 🧠 Antes de começar

**Qual é a dificuldade?** Dados podem ser interceptados durante uma comunicação ou lidos no armazenamento por alguém sem autorização.

**A ideia em palavras simples:** Criptografia protege a leitura dos dados por meio de chaves e tecnologias de conexão. É preciso distinguir proteção durante o transporte, no armazenamento e administração de chaves.

**Exemplo do dia a dia:** O site usa HTTPS para a comunicação com o aluno e configura proteção dos documentos armazenados. São duas camadas diferentes.

**O que não concluir?** Criptografia não impede todo apagamento, erro de permissão ou vazamento por um usuário autorizado. Ela é uma proteção específica dentro de um conjunto de controles.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Em repouso** | dados guardados em disco, banco ou bucket. |
| **Em trânsito** | dados viajando pela rede. |
| **HSM** | equipamento físico feito para guardar chaves com segurança. |
| **TLS/SSL** | o protocolo que protege o HTTPS. |

---

> **Domínio 2 — Segurança e Conformidade (30%)**

> 🔎 **Fichas detalhadas:** [AWS KMS (Key Management Service)](../../servicos/seguranca/kms.md) · [AWS CloudHSM](../../servicos/seguranca/cloudhsm.md) · [AWS Certificate Manager (ACM) e AWS Private CA](../../servicos/seguranca/certificate-manager.md) · [Amazon S3 (Simple Storage Service)](../../servicos/armazenamento/s3.md)

⬅️ [2.4 Governança multi-conta](04-governanca-multi-conta.md) · 🏠 [Índice do domínio](README.md) · [2.6 Compliance e governança](06-compliance-e-governanca.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.

Proteção durante uma comunicação e proteção de dados armazenados atuam em momentos distintos. Uma conexão protegida evita leitura indevida no caminho; o armazenamento protegido envolve chaves e autorizações para obter os dados depois.

Chave e certificado não são a mesma coisa. O certificado participa da identidade e proteção da conexão; a chave criptográfica é usada nas operações de proteção dos dados. Configurar um deles não prepara automaticamente todas as camadas.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

a criptografia é um **cadeado**; a chave é o que abre. O **KMS** é um chaveiro gerenciado pela AWS; o **CloudHSM** é um **cofre só seu**; o **ACM** fornece o cadeado do HTTPS (o ícone de cadeado no navegador).

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.

**Em repouso (at rest):** dados armazenados (S3, EBS, RDS, DynamoDB) criptografados com chaves do KMS.

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **HTTPS / TLS / SSL:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.

**Em trânsito (in transit):** dados trafegando pela rede, protegidos com TLS/SSL (HTTPS).

**Antes de ler este trecho:**

- **AWS KMS:** KMS administra chaves criptográficas e oferece operações de criptografia integradas a serviços AWS.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.

**AWS KMS (Key Management Service):** cria e gerencia chaves de criptografia; integrado à maioria dos serviços.

**Antes de ler este trecho:**

- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.

  - **AWS owned keys** (invisíveis para você), **AWS managed keys** (criadas pela AWS na sua conta para um serviço) e **customer managed keys** (criadas e controladas por você, com política de chave, rotação e auditoria).
**Antes de ler este trecho:**

- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.

  - Toda utilização de chave fica registrada no CloudTrail.

  - As chaves ficam em HSMs compartilhados e gerenciados pela AWS; são regionais.
**Antes de ler este trecho:**

- **AWS CloudHSM / CloudHSM:** CloudHSM fornece módulos de segurança de hardware para operações e armazenamento criptográfico.
- **HSM:** Equipamento especializado em proteger chaves e executar operações criptográficas. A forma de administração depende da solução escolhida.

**AWS CloudHSM:** HSM **dedicado e exclusivo** (single-tenant) na nuvem. Você gerencia as chaves e a AWS não tem acesso a elas. Para exigências regulatórias fortes.

**Antes de ler este trecho:**

- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **AWS Certificate Manager / Certificate Manager:** ACM ajuda a provisionar e gerenciar certificados para integrações compatíveis.
- **ELB:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.
- **ACM:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.

**AWS Certificate Manager (ACM):** emite, gerencia e **renova automaticamente** certificados SSL/TLS. Certificados públicos do ACM são gratuitos e usados em ELB, CloudFront e API Gateway.

**Antes de ler este trecho:**

- **SSE-S3 / SSE-KMS / SSE-C:** Formas de criptografia no servidor do S3, que diferem na origem e administração das chaves e, no último caso, nas camadas. A tabela da seção distingue essas escolhas.
- **objeto:** Unidade de dados guardada no armazenamento de objetos: conteúdo, identificação e informações associadas. Não é uma máquina nem um programa em execução.

**S3:** todo objeto novo é criptografado por padrão com SSE-S3. Opções: SSE-S3 (chave da AWS), SSE-KMS (chave do KMS, com auditoria), SSE-C (chave fornecida pelo cliente) e criptografia no lado do cliente.

**Cai na prova:** "chave controlada pelo cliente em hardware dedicado" = CloudHSM; "criar e gerenciar chaves integradas aos serviços" = KMS; "certificado HTTPS para o load balancer" = ACM; "quem ativa a criptografia dos dados?" = cliente.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.

**Primeiro, identifique o funcionamento:** TLS protege o caminho da comunicação; criptografia em repouso protege os dados armazenados. KMS administra chaves e autoriza operações criptográficas; ACM administra certificados.

**Depois, compare as escolhas:** Necessidade de chave para EBS/S3: KMS. Certificado TLS: ACM. HSM dedicado com controle de usuários e chaves: CloudHSM. Segredo de aplicação: Secrets Manager.

**Por fim, verifique o limite:** Dado criptografado não fica automaticamente inacessível a um usuário autorizado. Criptografia não substitui IAM, backup ou requisitos de localização dos dados.

## 4. Caso resolvido

Um arquivo está em S3 com SSE-KMS. Dar apenas permissão de leitura no S3 é suficiente?

**Raciocínio e resposta:** Pode não ser: o leitor também precisa de autorização adequada para usar a chave KMS. Criptografia e acesso ao objeto são camadas diferentes.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar criptografia **em repouso** de **em trânsito**.
- [ ] Diferenciar **KMS** (chaves gerenciadas e integradas) de **CloudHSM** (hardware dedicado, só você controla).
- [ ] Saber que o **ACM** emite e renova certificados SSL/TLS e que o S3 criptografa objetos novos por padrão.

**Dica de revisão para a prova:** "Hardware **dedicado**" ou "controle **exclusivo** das chaves" → **CloudHSM**. "Chaves integradas aos serviços" → **KMS**. "Certificado HTTPS" → **ACM**. Quem **ativa** a criptografia dos dados é o **cliente**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).
**Pergunta:** "Qual serviço cria e controla chaves de criptografia integradas a S3, EBS e RDS?"

**Resposta curta:** AWS KMS.

**Pergunta:** "A empresa exige HSM dedicado, com chaves sob controle exclusivo dela."

**Resposta curta:** AWS CloudHSM.

**Pergunta:** "Como obter certificados SSL/TLS gratuitos com renovação automática?"

**Resposta curta:** AWS Certificate Manager.

**Pergunta:** "Como proteger dados em trânsito?"

**Resposta curta:** TLS/HTTPS. "E em repouso?" → Criptografia com KMS.

**Pergunta:** "Quem é responsável por ativar a criptografia dos dados?"

**Resposta curta:** O cliente.

**Fundamento explicado no capítulo:** **S3:** todo objeto novo é criptografado por padrão com SSE-S3. Opções: SSE-S3 (chave da AWS), SSE-KMS (chave do KMS, com auditoria), SSE-C (chave fornecida pelo cliente) e criptografia no lado do cliente.

**Pergunta:** "Como auditar quem usou uma chave do KMS?"

**Resposta curta:** CloudTrail.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **KMS × CloudHSM (📌):** "hardware **single-tenant**, controle **exclusivo** das chaves, FIPS 140 nível 3" → **CloudHSM**. "Chaves gerenciadas e integradas a vários serviços" → **KMS**.
- 🔄 O ACM passou a oferecer **certificados públicos exportáveis** (pagos) para uso fora dos serviços integrados. Na prova continua valendo: "certificado público gratuito com renovação automática para ELB/CloudFront" → ACM.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.4 Governança multi-conta](04-governanca-multi-conta.md) · 🏠 [Índice do domínio](README.md) · [2.6 Compliance e governança](06-compliance-e-governanca.md) ➡️
