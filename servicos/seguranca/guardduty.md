# Amazon GuardDuty

> **Categoria:** Segurança / detecção de ameaças · **Domínio:** 2 · **Escopo:** Regional (multi-conta via Organizations) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** detecção inteligente e contínua de **ameaças ativas** usando machine learning, detecção de anomalias e inteligência de ameaças.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **alarme inteligente** que vigia os registros da conta e avisa quando algo suspeito acontece.

- ✅ **Escolha quando:** precisa **detectar ameaças ativas**: mineração de criptomoeda, acesso de IP malicioso, credenciais roubadas.
- 🚫 **Não é a resposta quando:** procura **vulnerabilidades de software** → [Inspector](inspector.md); procura **dados sensíveis** no S3 → [Macie](macie.md); quer **investigar a causa** → [Detective](detective.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "atividade maliciosa", "detecção de ameaças", "analisa CloudTrail, VPC Flow Logs e DNS".
<!-- didatico:fim -->

## Fontes de dados

| Fundamentais (ativadas ao ligar) | Planos de proteção opcionais |
|---|---|
| **CloudTrail management events** | **S3 Protection** (data events do S3) |
| **VPC Flow Logs** | **EKS Protection** (audit logs do Kubernetes) |
| **Logs de DNS** (Route 53 Resolver) | **Runtime Monitoring** (EC2, ECS, EKS — com agente) |
| | **Malware Protection** (EBS do EC2, objetos novos no S3 e recovery points do AWS Backup) |
| | **AI Protection** (cargas de IA, ex.: Bedrock) ✔️ |
| | **RDS Protection** (logins suspeitos no Aurora/RDS) |
| | **Lambda Protection** (tráfego de rede das funções) |

- **Sem agentes** para as fontes fundamentais: o GuardDuty lê os logs de forma independente (não precisa ativar Flow Logs/CloudTrail você mesmo).
- **Extended Threat Detection:** correlaciona eventos em **sequências de ataque** de vários estágios.

## Exemplos de achados (findings)

- Mineração de criptomoeda numa instância; comunicação com IPs/domínios maliciosos (C&C); chamadas de API de locais incomuns; credenciais de instância usadas fora da AWS; *port scanning*; buckets S3 tornados públicos; malware.

## Configurações

- Ativação com **um clique**; **teste gratuito de 30 dias** (no Free Tier novo, aparece vinculado ao **Paid plan**).
- Severidade (baixa, média, alta, crítica); listas de IPs confiáveis/ameaças; filtros de supressão.
- **Resposta automatizada:** achados vão ao **EventBridge** → Lambda/SSM para isolar a instância, notificar via SNS.
- Envia achados ao **Security Hub** e permite investigar no **Detective**.
- Multi-conta com **administrador delegado** no Organizations.

## Cobrança

- Por volume de eventos/logs analisados e por plano de proteção.

## ⚠️ Não confundir

- GuardDuty (**ameaça em andamento**, a partir de logs) × Inspector (**vulnerabilidade** de software) × Macie (**dados sensíveis**) × Detective (**investigação**).

## ❓ Perguntas típicas

- "Detectar atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS." → GuardDuty.
- "Instância está minerando criptomoeda." → GuardDuty.
- "Responder automaticamente a um achado." → GuardDuty → EventBridge → Lambda.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Detector, fontes de dados/proteções e findings |
| **O que você decide/configura?** | Região, contas, proteções e destinatários de achados |
| **Em que ordem as coisas acontecem?** | Analisa sinais e gera findings; resposta é operada ou automatizada à parte |
| **O que pode fazer, e em que condição?** | Identifica comportamento potencialmente malicioso |
| **O que não pode presumir?** | Detectar não garante bloquear ou corrigir sozinho |

**Caso comentado:** Credenciais usadas de forma suspeita: GuardDuty; pacote com CVE: Inspector.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
