<!-- autoral -->

# AWS Certificate Manager (ACM) e AWS Private CA

> **Categoria:** Segurança / criptografia em trânsito · **Domínio:** 2 · **Abrangência:** Regional (para o CloudFront, us-east-1) · **Ficha:** complementar
>
> **Em uma frase:** cria, guarda e renova certificados SSL/TLS públicos e privados e os instala nos serviços integrados, como Elastic Load Balancing, CloudFront e API Gateway.
>
> **Escopo oficial:** ✅ No escopo (Private CA ⚪ não listado) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

O site de matrícula precisa de HTTPS, e o certificado que prova que o site é mesmo da escola vence todo ano. O **ACM** emite o certificado, instala no balanceador ou no CloudFront e o renova sozinho quando o domínio é validado por DNS. Certificados privados, para uso interno, são assinados pela **AWS Private CA**, que não aparece na lista do exame.

1. A escola pede um certificado público para o domínio, ou importa um de terceiros.
2. Prova que o domínio é dela, por DNS ou por e-mail.
3. Associa o certificado a um serviço integrado; para o CloudFront, o certificado precisa estar na Região us-east-1 (Norte da Virgínia).
4. Com validação por DNS, o ACM renova automaticamente; por e-mail, avisa quando o vencimento se aproxima.

O limite: o certificado protege os dados **em trânsito**. Cifrar os dados guardados é trabalho do [KMS](kms.md). Certificados públicos não exportáveis, usados nos serviços integrados, não têm custo; os exportáveis são cobrados por domínio.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS KMS](kms.md) | Chaves para cifrar dados em repouso | "Criptografia do bucket" |
| [AWS CloudHSM](cloudhsm.md) | HSM dedicado para chaves | "Hardware dedicado" |
| [Amazon CloudFront](../redes/cloudfront.md) | Usa o certificado para entregar o site com HTTPS | "CDN", "cache" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)
- [Requisitos de certificado do CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html)
- [Preços do ACM](https://aws.amazon.com/certificate-manager/pricing/)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
