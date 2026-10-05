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

## Tipos de chave

| Tipo | Quem cria/gerencia | Visível na conta | Rotação | Custo mensal |
|---|---|---|---|---|
| **AWS owned keys** | AWS (compartilhadas entre contas) | Não | AWS | Grátis |
| **AWS managed keys** (`aws/s3`, `aws/ebs`…) | AWS, para um serviço, na sua conta | Sim (só leitura) | Automática **todo ano**, obrigatória (era a cada 3 anos até 2022) | Grátis (paga uso) |
| **Customer managed keys** | **Você** | Sim | Opcional automática (período configurável) ou manual | Por chave/mês + uso |

- Chaves **simétricas** (AES-256, padrão), **assimétricas** (RSA/ECC para assinar/criptografar fora da AWS) e **HMAC**.

## Conceitos e configurações

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

## Cobrança

- Customer managed key: taxa mensal por chave + por solicitações de API. AWS managed/owned: sem taxa mensal.

## Segurança e responsabilidade compartilhada

- **AWS:** HSMs, durabilidade e disponibilidade das chaves.
- **Cliente:** **ativar a criptografia** nos serviços, key policies, rotação, quem pode usar/excluir.

## ⚠️ Pegadinhas e não confundir

- **KMS** (multi-tenant, gerenciado, integrado) × **CloudHSM** (single-tenant, você controla com exclusividade).
- KMS (chaves) × **Secrets Manager** (segredos como senhas, que ele criptografa com KMS) × **ACM** (certificados TLS).

## ❓ Perguntas típicas

- "Criar e controlar chaves integradas a S3, EBS e RDS." → KMS.
- "Auditar quem usou uma chave." → CloudTrail.
- "Quem é responsável por ativar a criptografia?" → O cliente.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Chaves, aliases, key policies e grants |
| **O que você decide/configura?** | Tipo, administradores, usuários, rotação e integração |
| **Em que ordem as coisas acontecem?** | Serviço/aplicação solicita operação criptográfica autorizada |
| **O que pode fazer, e em que condição?** | Protege chaves e integra criptografia a serviços como EBS e S3 |
| **O que não pode presumir?** | Rotacionar chave não recriptografa automaticamente todos os dados; remover acesso pode impedir leitura |

**Caso comentado:** SSE-KMS: permissão S3 sem autorização na chave pode falhar ao ler objeto.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
