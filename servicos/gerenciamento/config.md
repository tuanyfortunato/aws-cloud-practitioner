# AWS Config

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe precisa acompanhar como as configurações dos recursos mudaram e verificar se elas seguem requisitos definidos.

**Como este serviço ajuda?** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.

**Exemplo do dia a dia:** A escola define uma regra para uma configuração importante e acompanha os recursos avaliados como conformes ou não conformes.

**O que ele não resolve sozinho?** Config observa e avalia configuração; não é o serviço principal para medir lentidão da aplicação. Correções automáticas dependem de remediação configurada.

**Primeiras palavras para entender:**

- **Configuração:** propriedades de um recurso.
- **Regra:** critério de avaliação.
- **Remediação:** ação para corrigir uma condição inadequada.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / governança e compliance · **Domínio:** 2 · **Escopo:** Regional (agregadores multi-conta/região) · **Tópico do guia:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) · [2.6 Compliance](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)
>
> **Em uma frase:** registra a **configuração** dos recursos e seu histórico de mudanças, e avalia continuamente se estão **conformes** com regras.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Componentes

| Componente | Detalhe |
|---|---|
| **Configuration recorder** | Registra *configuration items* (estado de cada recurso e relações) — todos os tipos ou selecionados; contínuo ou diário. |
| **Delivery channel** | Envia histórico e snapshots para **S3** e notificações para **SNS**. |
| **Resource timeline** | "Como estava este security group na terça passada e quem mudou?" (com link para o evento no CloudTrail). |
| **Config rules** | **Managed rules** (centenas prontas: `s3-bucket-public-read-prohibited`, `encrypted-volumes`, `restricted-ssh`, `root-account-mfa-enabled`…) ou **custom** (Lambda ou Guard). Avaliação por mudança ou periódica. |
| **Remediation** | Ações corretivas manuais ou **automáticas** via **Systems Manager Automation**. |
| **Conformance packs** | Pacotes de regras + remediações (ex.: boas práticas de PCI DSS, CIS) implantáveis na organização. |
| **Aggregators** | Visão consolidada de várias contas e regiões. |
| **Advanced query** | Consultas SQL sobre o inventário de configuração. |

## Cobrança

- Por **configuration item registrado** + por **avaliação de regra** + conformance packs.

## Quem depende do Config

- **Security Hub** (verificações de padrões), **Firewall Manager**, **Control Tower** (controles detectivos), **Audit Manager**.

## ⚠️ Não confundir

- Config (**estado/conformidade**) × CloudTrail (**quem fez**) × CloudWatch (**métricas**).
- Config **detecta e pode remediar**; **SCP** previne.

## ❓ Perguntas típicas

- "Histórico de configuração de um recurso e se segue as regras." → AWS Config.
- "Como estava o security group semana passada?" → Config.
- "Verificar continuamente se todos os buckets estão criptografados e corrigir automaticamente." → Config rule + remediação (SSM Automation).

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Recorder, configuration items, rules e aggregators |
| **O que você decide/configura?** | Tipos de recurso, cobertura e regras |
| **Em que ordem as coisas acontecem?** | Registra configuração e avalia conformidade com critérios |
| **O que pode fazer, e em que condição?** | Mostra mudanças de estado/configuração de recursos suportados |
| **O que não pode presumir?** | Avaliar regra não bloqueia necessariamente criação; remediação depende de integração |

**Caso comentado:** Saber se bucket atende regra e seu estado anterior: Config; quem mudou: CloudTrail.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
