# AWS Trusted Advisor

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa precisa identificar oportunidades de melhoria no uso da AWS, como recursos ociosos ou configurações que merecem atenção.

**Como este serviço ajuda?** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.

**Exemplo do dia a dia:** A equipe consulta uma recomendação sobre recursos pouco usados e decide se pode ajustá-los ou removê-los sem prejudicar a aplicação.

**O que ele não resolve sozinho?** Uma recomendação não conhece sozinha todas as necessidades do negócio. Cobertura e acesso dependem das condições aplicáveis; a equipe deve avaliar antes de agir.

**Primeiras palavras para entender:**

- **Verificação:** análise segundo um critério.
- **Recomendação:** orientação de melhoria.
- **Ocioso:** recurso com pouco ou nenhum uso.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Checks, recomendações e visão de resultados |
| **O que você decide/configura?** | Conta, plano e acesso aos checks |
| **Em que ordem as coisas acontecem?** | Analise recomendações e aplique mudanças após avaliar impacto |
| **O que pode fazer, e em que condição?** | Ajuda custos, performance, segurança e outros temas de boas práticas |
| **O que não pode presumir?** | Não é garantia de aplicação perfeita nem alteração automática de toda recomendação |

**Caso comentado:** Recomendação geral de boas práticas: Trusted Advisor; tamanho por uso observado: Compute Optimizer.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
