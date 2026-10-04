# AWS KMS (Key Management Service)

> **Categoria:** Segurança / criptografia · **Domínio:** 2 · **Escopo:** **Regional** (chaves multi-região opcionais) · **Tópico do guia:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)
>
> **Em uma frase:** cria e controla chaves de criptografia integradas a mais de 100 serviços AWS, com auditoria de cada uso.

## Tipos de chave

| Tipo | Quem cria/gerencia | Visível na conta | Rotação | Custo mensal |
|---|---|---|---|---|
| **AWS owned keys** | AWS (compartilhadas entre contas) | Não | AWS | Grátis |
| **AWS managed keys** (`aws/s3`, `aws/ebs`…) | AWS, para um serviço, na sua conta | Sim (só leitura) | Automática anual | Grátis (paga uso) |
| **Customer managed keys** | **Você** | Sim | Opcional automática (período configurável) ou manual | Por chave/mês + uso |

- Chaves **simétricas** (AES-256, padrão), **assimétricas** (RSA/ECC para assinar/criptografar fora da AWS) e **HMAC**.

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Key policy** | Política de recurso **obrigatória** de cada chave — quem administra e quem usa. Complementada por IAM e *grants*. |
| **Envelope encryption** | O KMS gera uma *data key* que criptografa os dados; a data key é criptografada pela chave do KMS. Chamadas diretas criptografam até 4 KB. |
| **Auditoria** | Todo uso da chave fica no **CloudTrail**. |
| **Exclusão** | Agendada com espera de **7 a 30 dias**; dá para desativar antes. Chave apagada = dados irrecuperáveis. |
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

## 🔗 Documentação oficial

- [Guia do KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
