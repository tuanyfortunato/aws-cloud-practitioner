<!-- autoral -->

# AWS CloudHSM

> **Categoria:** Segurança / criptografia · **Domínio:** 2 · **Abrangência:** Regional (cluster na VPC) · **Ficha:** complementar
>
> **Em uma frase:** módulos de segurança de hardware (HSMs) dedicados a um único cliente, na nuvem, para guardar chaves e fazer operações criptográficas sob controle exclusivo.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Um **HSM** é um equipamento que faz operações criptográficas e guarda chaves com segurança. O KMS usa HSMs compartilhados e gerenciados pela AWS. Se uma regra interna ou um regulador exigir hardware **dedicado**, sob controle do próprio cliente, a resposta é o **AWS CloudHSM**: HSMs de uso exclusivo (*single-tenant*), com validação FIPS 140-2 ou 140-3 nível 3 nos clusters em modo FIPS.

1. Cria-se um cluster do CloudHSM na VPC, em modo FIPS ou não FIPS.
2. A AWS cuida do provisionamento, dos backups, da configuração e da manutenção dos HSMs.
3. O cliente administra os próprios usuários e chaves dentro dos HSMs.
4. As aplicações usam as chaves; o KMS também pode guardar chaves num repositório apoiado no cluster do cliente.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS KMS](kms.md) | Chaves gerenciadas e integradas aos serviços, em HSMs compartilhados | "Criptografia integrada ao S3", "rotação de chaves" |
| [AWS Secrets Manager](secrets-manager-e-parameter-store.md) | Guarda e troca senhas e segredos | "Senha do banco" |
| [AWS Certificate Manager](certificate-manager.md) | Certificados SSL/TLS para HTTPS | "Certificado", "HTTPS" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
