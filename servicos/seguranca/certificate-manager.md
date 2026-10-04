# AWS Certificate Manager (ACM) e AWS Private CA

> **Categoria:** Segurança / criptografia em trânsito · **Domínio:** 2 · **Escopo:** Regional (para CloudFront, **us-east-1**) · **Tópico do guia:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)
>
> **Em uma frase:** emite, gerencia e **renova automaticamente** certificados SSL/TLS — os públicos são gratuitos.
>
> **Escopo oficial:** ✅ No escopo (Private CA ⚪ não listado) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **cartório dos cadeados HTTPS**: emite e renova sozinho os certificados que fazem aparecer o cadeado no navegador.

- ✅ **Escolha quando:** precisa de **certificados SSL/TLS** para ELB, CloudFront ou API Gateway.
- 🚫 **Não é a resposta quando:** precisa de **chaves para criptografar dados** → [KMS](kms.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "certificado SSL/TLS", "HTTPS", "renovação automática", "gratuito".
<!-- didatico:fim -->

## Destaques

| Item | Detalhe |
|---|---|
| **Certificados públicos** | **Gratuitos** para uso em serviços integrados: **ELB, CloudFront, API Gateway**, App Runner, Amplify… |
| **Validação** | **DNS** (recomendada, permite renovação automática; com Route 53 é um clique) ou e-mail. |
| **Renovação automática** | Para certificados validados por DNS em uso. |
| **Importar certificados** | De outras CAs (sem renovação automática). |
| **CloudFront** | Certificado precisa estar em **us-east-1**. |
| **Monitoramento** | Métricas de expiração e eventos no EventBridge. |

## AWS Private CA

- Autoridade certificadora **privada** gerenciada para emitir certificados internos (serviços, dispositivos IoT, mTLS). Paga por CA/mês + certificados.

## 🔄 Atualizações 2025-2026

- **Certificados públicos exportáveis** (desde 17/06/2025, pagos): permitem usar certificados do ACM em servidores próprios (EC2, on-premises). Validade de 395 dias; lançados a US$ 15 (FQDN) e US$ 149 (wildcard), hoje **US$ 7 e US$ 79** na página de preços. Na prova, siga: "público, gratuito, renovação automática, ELB/CloudFront" → ACM.

## ❓ Perguntas típicas

- "Certificados SSL/TLS gratuitos com renovação automática para o load balancer." → ACM.
- "Certificados para serviços internos, não públicos." → AWS Private CA.

## 🔗 Documentação oficial

- [ACM](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) · [Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)
