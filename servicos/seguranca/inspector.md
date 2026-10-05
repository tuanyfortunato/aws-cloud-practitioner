# Amazon Inspector

> **Categoria:** Segurança / gestão de vulnerabilidades · **Domínio:** 2 · **Escopo:** Regional (multi-conta) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** varre continuamente cargas de trabalho em busca de **vulnerabilidades de software (CVEs)** e exposição de rede não intencional.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **vistoria automática** que procura brechas conhecidas (CVEs) nos seus servidores, imagens e funções.

- ✅ **Escolha quando:** precisa **varrer EC2, imagens do ECR e Lambda** em busca de **vulnerabilidades**.
- 🚫 **Não é a resposta quando:** a ameaça está **em andamento** → [GuardDuty](guardduty.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "vulnerabilidades", "CVE", "patches faltando", "avaliação contínua".
<!-- didatico:fim -->

## O que varre

| Recurso | Como | O que encontra |
|---|---|---|
| **EC2** | Agente do **SSM** ou *agentless* (snapshots EBS) | CVEs de pacotes do SO e de aplicações; **alcance de rede** (portas expostas); CIS benchmarks |
| **Imagens no ECR** | Ao fazer push e continuamente | CVEs no SO e em pacotes de linguagem |
| **Funções Lambda** | Código e dependências | CVEs e falhas no código (*code scanning*) |
| **Repositórios de código / CI-CD** | Integração com pipelines | Vulnerabilidades antes do deploy |

## Destaques

- **Contínuo e automático:** reavalia quando surge um novo CVE ou o recurso muda.
- **Inspector risk score** contextualizado (CVSS + exposição de rede + exploit conhecido).
- Exporta **SBOM** (lista de componentes de software).
- Integra com Security Hub e EventBridge; **teste gratuito de 15 dias**.

## Cobrança

- Por instância EC2 escaneada/mês, por imagem do ECR, por função Lambda.

## ⚠️ Não confundir

- **Inspector** (vulnerabilidades/CVE) × **GuardDuty** (ameaças ativas) × **Macie** (PII no S3).

## ❓ Perguntas típicas

- "Varrer EC2 e imagens de contêiner em busca de vulnerabilidades." → Inspector.
- "Descobrir instâncias com portas acessíveis da internet sem necessidade." → Inspector (alcance de rede).

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Recursos elegíveis, cobertura de varredura e findings |
| **O que você decide/configura?** | Cobertura, acesso e pré-requisitos conforme recurso |
| **Em que ordem as coisas acontecem?** | Inspeção identifica vulnerabilidades e exposição conforme modalidade |
| **O que pode fazer, e em que condição?** | Ajuda a priorizar correções de software em EC2/ECR/Lambda suportados |
| **O que não pode presumir?** | Não substitui patch nem cobre automaticamente qualquer recurso da conta |

**Caso comentado:** Dependência vulnerável numa imagem: Inspector integrado à varredura adequada; equipe corrige e republica.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
