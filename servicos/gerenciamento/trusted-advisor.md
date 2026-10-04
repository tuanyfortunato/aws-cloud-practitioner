# AWS Trusted Advisor

> **Categoria:** Gerenciamento / boas práticas · **Domínio:** 2, 3 e 4 · **Escopo:** Global (conta e organização) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) · [4.5 Planos de suporte](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)
>
> **Em uma frase:** inspeciona sua conta e recomenda melhorias com base nas boas práticas da AWS.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Categorias

1. **Cost optimization** — instâncias ociosas, volumes EBS sem uso, Elastic IPs não associados, RIs/SPs subutilizados.
2. **Performance** — instâncias sobrecarregadas, configuração do CloudFront.
3. **Security** — buckets S3 abertos, SGs com portas irrestritas, **MFA no root**, uso do IAM, snapshots públicos, access keys expostas.
4. **Fault tolerance** — EBS sem snapshot, instâncias numa só AZ, RDS sem Multi-AZ, backups.
5. **Service limits (quotas)** — uso acima de 80% da cota.
6. 🔄 **Operational excellence** — práticas operacionais (logs, monitoramento). *(confirmado na documentação oficial; materiais antigos listam só as 5 primeiras)*

Status das verificações: 🟢 sem problema · 🟡 investigação recomendada · 🔴 ação recomendada.

## Por plano de suporte

| Plano | Verificações | Extras |
|---|---|---|
| **Basic / Developer** | 📌 **Core checks**: todos de **Service Limits** + **5 de segurança**: S3 Bucket Permissions, Security Groups – Specific Ports Unrestricted, MFA on Root Account, EBS Public Snapshots, RDS Public Snapshots (✔️ lista oficial de 10/2026; "IAM Use" não aparece mais) | Refresh manual |
| **Business Support+ / Enterprise / Unified Operations** (e os clássicos Business / Enterprise On-Ramp) | **Todas** as verificações | **AWS Support API**, integração com **EventBridge**, notificações semanais, visão organizacional |
| **Enterprise e superior** | + **Trusted Advisor Priority** (recomendações priorizadas pelo time de conta) | — |

## ⚠️ Não confundir

- Trusted Advisor (boas práticas amplas: custo, desempenho, segurança, cotas) × **Security Hub** (achados de segurança) × **Compute Optimizer** (rightsizing com ML) × **Well-Architected Tool** (revisão de uma carga contra os pilares).

## ❓ Perguntas típicas

- "Recomendar melhorias de custo, segurança, desempenho e limites." → Trusted Advisor.
- "Menor plano com todas as verificações do Trusted Advisor." → Business Support+ (no modelo clássico, Business).
- "Menor plano com Trusted Advisor Priority." → Enterprise.
- "Verificações disponíveis no Basic." → Core checks (segurança essenciais + service limits).

## 🔗 Documentação oficial

- [Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
