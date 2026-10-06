# AWS KMS (Key Management Service)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Dados protegidos por criptografia dependem de chaves. A empresa precisa controlar quem pode usar essas chaves e para quais operações.

**Como este serviço ajuda?** KMS administra chaves criptográficas e oferece operações de criptografia integradas a serviços AWS. Você define políticas e autorizações de uso.

**Exemplo do dia a dia:** A escola usa uma chave KMS com armazenamento compatível e permite que apenas identidades autorizadas realizem as operações necessárias sobre os dados protegidos.

**O que ele não resolve sozinho?** Ter uma chave não criptografa automaticamente todos os dados da conta. É preciso configurar os serviços e controlar tanto o acesso aos dados quanto o uso da chave.

**Primeiras palavras para entender:**

- **Criptografia:** transformação que protege a leitura dos dados.
- **Chave:** elemento usado para proteger ou recuperar o conteúdo.
- **Política da chave:** regras de acesso a ela.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / criptografia · **Domínio:** 2 · **Escopo:** **Regional** (chaves multi-região opcionais) · **Tópico do guia:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)
>
> **Em uma frase:** cria e controla chaves de criptografia integradas a mais de 100 serviços AWS, com auditoria de cada uso.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.

**Passo 1.** Escolha ou crie uma chave compatível e defina quem pode administrá-la e utilizá-la.

**Passo 2.** Configure o recurso ou a aplicação para usar a proteção apropriada. As operações de chave são avaliadas conforme as autorizações.

**Passo 3.** Planeje uso, auditoria e ciclo de vida da chave. Perder acesso à chave pode afetar o acesso aos dados protegidos.

## 2. Recursos e opções, com significado

### Tipos de chave

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

| Tipo | Quem cria/gerencia | Visível na conta | Rotação | Custo mensal |
|---|---|---|---|---|
| **AWS owned keys** | AWS (compartilhadas entre contas) | Não | AWS | Grátis |
| **AWS managed keys** (`aws/s3`, `aws/ebs`…) | AWS, para um serviço, na sua conta | Sim (só leitura) | Automática **todo ano**, obrigatória (era a cada 3 anos até 2022) | Grátis (paga uso) |
| **Customer managed keys** | **Você** | Sim | Opcional automática (período configurável) ou manual | Por chave/mês + uso |

**Antes de ler este trecho:**

- **AES-256:** Algoritmo de criptografia com chave de 256 bits. Esse nome descreve a tecnologia de proteção; autorização e administração das chaves continuam necessárias.
- **HMAC / RSA / ECC:** Tecnologias criptográficas para finalidades próprias. HMAC verifica autenticidade/integridade com chave; RSA e ECC são famílias de criptografia assimétrica. Não são certificados ou políticas de acesso.

Chaves **simétricas** (AES-256, padrão), **assimétricas** (RSA/ECC para assinar/criptografar fora da AWS) e **HMAC**.

### Conceitos e configurações

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **CloudHSM:** CloudHSM fornece módulos de segurança de hardware para operações e armazenamento criptográfico.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **KB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **Multi-Region:** Uso de mais de uma região. Replicação, comunicação e recuperação entre regiões exigem configuração e podem ter custos próprios.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.
- **policy / política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.
- **HSM:** Equipamento especializado em proteger chaves e executar operações criptográficas. A forma de administração depende da solução escolhida.
- **FIPS:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.
- **BYOK / XKS:** Trazer chaves próprias e usar armazenamento externo de chaves são opções diferentes de controle criptográfico. Avalie o produto e as condições específicas.

| Item | Detalhe |
|---|---|
| **Key policy** | Política de recurso **obrigatória** de cada chave — quem administra e quem usa. Complementada por IAM e *grants*. |
| **Envelope encryption** | O KMS gera uma *data key* que criptografa os dados; a data key é criptografada pela chave do KMS. Chamadas diretas criptografam até 4 KB. |
| **Auditoria** | Todo uso da chave fica no **CloudTrail**. |
| **Exclusão** | Só para customer managed keys: agendada com espera de **7 a 30 dias** (padrão 30); dá para desativar antes. Chave apagada = dados irrecuperáveis. |
| **Multi-Region keys** | Mesma chave em várias regiões (DR, replicação). |
| **Importar material de chave (BYOK)** | Você gera a chave fora e importa. |
| **Custom key stores** | Chaves em **CloudHSM** seu ou em HSM externo (XKS). |
| **HSMs** | Validados FIPS 140, compartilhados e gerenciados pela AWS — a AWS não exporta as chaves em texto claro. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ter uma chave não criptografa automaticamente todos os dados da conta. É preciso configurar os serviços e controlar tanto o acesso aos dados quanto o uso da chave.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.

**KMS** (multi-tenant, gerenciado, integrado) × **CloudHSM** (single-tenant, você controla com exclusividade).

**Antes de ler este trecho:**

- **TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **ACM:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.

KMS (chaves) × **Secrets Manager** (segredos como senhas, que ele criptografa com KMS) × **ACM** (certificados TLS).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.

Customer managed key: taxa mensal por chave + por solicitações de API. AWS managed/owned: sem taxa mensal.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **durabilidade:** Capacidade de preservar os dados armazenados. É diferente de disponibilidade, que trata de conseguir acessá-los quando necessário.

**AWS:** HSMs, durabilidade e disponibilidade das chaves.

**Antes de ler este trecho:**

- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.

**Cliente:** **ativar a criptografia** nos serviços, key policies, rotação, quem pode usar/excluir.

## 5. Caso resolvido: ligando as peças

A escola usa uma chave KMS com armazenamento compatível e permite que apenas identidades autorizadas realizem as operações necessárias sobre os dados protegidos.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha ou crie uma chave compatível e defina quem pode administrá-la e utilizá-la.
**Etapa 2:** Configure o recurso ou a aplicação para usar a proteção apropriada. As operações de chave são avaliadas conforme as autorizações.
**Etapa 3:** Planeje uso, auditoria e ciclo de vida da chave. Perder acesso à chave pode afetar o acesso aos dados protegidos.

**Resultado e responsabilidade:** KMS administra chaves criptográficas e oferece operações de criptografia integradas a serviços AWS. Você define políticas e autorizações de uso.

**Recursos envolvidos:** Chaves, aliases, key policies e grants.

**Decisões que precisam ser tomadas:** Tipo, administradores, usuários, rotação e integração.

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.
- **SSE-KMS:** Formas de criptografia no servidor do S3, que diferem na origem e administração das chaves e, no último caso, nas camadas. A tabela da seção distingue essas escolhas.
- **objeto:** Unidade de dados guardada no armazenamento de objetos: conteúdo, identificação e informações associadas. Não é uma máquina nem um programa em execução.

**Outra situação comentada:** SSE-KMS: permissão S3 sem autorização na chave pode falhar ao ler objeto.

**Por que não concluir mais do que isso:** Rotacionar chave não recriptografa automaticamente todos os dados; remover acesso pode impedir leitura

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Criar e controlar chaves integradas a S3, EBS e RDS."

**Resposta curta:** KMS.

**Pergunta:** "Auditar quem usou uma chave."

**Resposta curta:** CloudTrail.

**Fundamento explicado no capítulo:** **Auditoria**; Todo uso da chave fica no **CloudTrail**.

**Pergunta:** "Quem é responsável por ativar a criptografia?"

**Resposta curta:** O cliente.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
