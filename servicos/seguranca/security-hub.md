# AWS Security Hub

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa recebe achados de segurança de várias ferramentas e precisa de uma visão organizada para acompanhar prioridades e postura de segurança.

**Como este serviço ajuda?** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.

**Exemplo do dia a dia:** A equipe consulta uma visão central de achados e controles para acompanhar problemas em seus ambientes AWS.

**O que ele não resolve sozinho?** Centralizar achados não corrige todos os recursos automaticamente nem garante conformidade com qualquer norma. Integrações, controles e ações de resposta exigem configuração.

**Primeiras palavras para entender:**

- **Postura de segurança:** situação dos controles e riscos.
- **Achado:** resultado de uma avaliação.
- **Controle:** requisito ou prática verificada.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / postura (CSPM) · **Domínio:** 2 · **Escopo:** Regional com agregação entre regiões e contas · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** **painel central** de segurança que agrega achados de vários serviços e verifica a conta contra padrões de boas práticas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## O que faz

| Função | Detalhe |
|---|---|
| **Agregação de achados** | GuardDuty, Inspector, Macie, IAM Access Analyzer, Firewall Manager, Config, Health e **parceiros**, num formato padrão (ASFF/OCSF). |
| **Verificações de padrões** | **AWS Foundational Security Best Practices (FSBP)**, **CIS AWS Foundations**, **PCI DSS**, **NIST SP 800-53**, AWS Resource Tagging. Gera um *security score*. |
| **Automação** | Automation rules (atualizar/suprimir achados), integração com EventBridge para remediação. |
| **Multi-conta / multi-região** | Administrador delegado + região de agregação. |
| **Pré-requisito** | ✔️ A maioria dos controles usa regras do **AWS Config**. Usando o Security Hub novo junto com o CSPM, o recorder do Config é criado automaticamente; usando só o CSPM, é preciso habilitar o Config manualmente. |

## 🔄 Atualizações 2025-2026

- A documentação oficial já usa o nome **AWS Security Hub CSPM** para as verificações de postura (o anúncio da reformulação não foi localizado na verificação de 04/10/2026). Para a prova: "painel central de achados e padrões (CIS, FSBP)" → **Security Hub**, que está no escopo.

## ⚠️ Não confundir

- Security Hub (achados de **segurança** centralizados) × **Trusted Advisor** (boas práticas de custo, desempenho, segurança, cotas).
- Security Hub (painel) × **Security Lake** (data lake de logs de segurança no formato OCSF).

## ❓ Perguntas típicas

- "Reunir achados de segurança de vários serviços num só painel." → Security Hub.
- "Verificar a conta contra o CIS Benchmark." → Security Hub.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Findings, controles/standards, agregação e configuração de contas |
| **O que você decide/configura?** | Padrões, regiões, contas e integrações |
| **Em que ordem as coisas acontecem?** | Recebe achados e avalia controles compatíveis; equipe prioriza resposta |
| **O que pode fazer, e em que condição?** | Centraliza visão de postura e problemas |
| **O que não pode presumir?** | Agregação não significa correção automática de cada finding nem certificação de conformidade |

**Caso comentado:** Ver achados de vários serviços num lugar: Security Hub; identificar PII em S3: Macie produz o achado.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
