# AWS CloudHSM

> **Categoria:** Segurança / criptografia · **Domínio:** 2 · **Escopo:** Regional (cluster multi-AZ na VPC) · **Tópico do guia:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)
>
> **Em uma frase:** HSM (hardware security module) **dedicado e exclusivo** na nuvem, em que só você controla as chaves.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **cofre de chaves só seu**, num hardware dedicado: nem a AWS tem a combinação.

- ✅ **Escolha quando:** a regulação exige **HSM dedicado** (single-tenant), **FIPS 140 nível 3** e **controle exclusivo** das chaves.
- 🚫 **Não é a resposta quando:** não há essa exigência e você quer chaves gerenciadas e integradas → [KMS](kms.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "HSM dedicado", "single-tenant", "controle exclusivo das chaves", "FIPS 140 nível 3".
<!-- didatico:fim -->

## Destaques

| Item | Detalhe |
|---|---|
| **Single-tenant** | Hardware dedicado a você; validação **FIPS 140 nível 3**. |
| **Controle** | **Você** gerencia usuários e chaves; a **AWS não tem acesso** às chaves. Perdeu as credenciais → perdeu as chaves. |
| **Alta disponibilidade** | Cluster com HSMs em várias AZs (responsabilidade do cliente montar). |
| **APIs padrão** | PKCS#11, JCE (Java), CNG/KSP (Windows), OpenSSL. |
| **Integração** | Custom key store do KMS; offload SSL/TLS de servidores web; Oracle TDE; assinatura de código; CA privada. |

## Cobrança

- Por **HSM por hora** (custo bem maior que o KMS).

## Responsabilidade compartilhada

- **AWS:** hardware, disponibilidade do HSM, patches de firmware.
- **Cliente:** usuários, chaves, backup das credenciais, montar cluster multi-AZ, aplicação.

## ⚠️ Pegadinhas

- "Hardware dedicado", "single-tenant", "controle exclusivo das chaves", "FIPS 140 nível 3", "a AWS não pode acessar" → **CloudHSM**.

## ❓ Perguntas típicas

- "Exigência regulatória de HSM dedicado com chaves sob controle exclusivo." → CloudHSM.

## 🔗 Documentação oficial

- [CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)
