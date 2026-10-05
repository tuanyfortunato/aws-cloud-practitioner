# AWS Certificate Manager (ACM) e AWS Private CA

> **Categoria:** Segurança / criptografia em trânsito · **Domínio:** 2 · **Escopo:** Regional (para CloudFront, **us-east-1**) · **Tópico do guia:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)
>
> **Em uma frase:** emite e gerencia certificados SSL/TLS, com renovação para certificados elegíveis; públicos não exportáveis em serviços integrados são gratuitos.
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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Certificados, validação de domínio e associação a serviços |
| **O que você decide/configura?** | Domínios, tipo de certificado e serviço/região |
| **Em que ordem as coisas acontecem?** | Solicite/importe, valide e associe ao endpoint compatível |
| **O que pode fazer, e em que condição?** | Facilita TLS em serviços integrados |
| **O que não pode presumir?** | Renovação/uso depende da modalidade; certificado não autoriza leitura de dados |

**Caso comentado:** HTTPS no ALB: certificado ACM; criptografar volume EBS: chave KMS.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [ACM](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) · [Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)
