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

**Passo 1.** Escolha ou crie uma chave compatível e defina quem pode administrá-la e utilizá-la.

**Passo 2.** Configure o recurso ou a aplicação para usar a proteção apropriada. As operações de chave são avaliadas conforme as autorizações.

**Passo 3.** Planeje uso, auditoria e ciclo de vida da chave. Perder acesso à chave pode afetar o acesso aos dados protegidos.

## 2. Recursos e opções, com significado

### Tipos de chave

| Tipo | Quem cria/gerencia | Visível na conta | Rotação | Custo mensal |
|---|---|---|---|---|
| **AWS owned keys** | AWS (compartilhadas entre contas) | Não | AWS | Grátis |
| **AWS managed keys** (`aws/s3`, `aws/ebs`…) | AWS, para um serviço, na sua conta | Sim (só leitura) | Automática **todo ano**, obrigatória (era a cada 3 anos até 2022) | Grátis (paga uso) |
| **Customer managed keys** | **Você** | Sim | Opcional automática (período configurável) ou manual | Por chave/mês + uso |

Chaves **simétricas** (AES-256, padrão), **assimétricas** (RSA/ECC para assinar/criptografar fora da AWS) e **HMAC**.

### Conceitos e configurações

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

**KMS** (multi-tenant, gerenciado, integrado) × **CloudHSM** (single-tenant, você controla com exclusividade).

KMS (chaves) × **Secrets Manager** (segredos como senhas, que ele criptografa com KMS) × **ACM** (certificados TLS).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Customer managed key: taxa mensal por chave + por solicitações de API. AWS managed/owned: sem taxa mensal.

### Segurança e responsabilidade compartilhada

**AWS:** HSMs, durabilidade e disponibilidade das chaves.

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
