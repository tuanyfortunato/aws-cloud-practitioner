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

## 🔗 Documentação oficial

- [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
