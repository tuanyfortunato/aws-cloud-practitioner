# AWS Security Hub

> **Categoria:** Segurança / postura (CSPM) · **Domínio:** 2 · **Escopo:** Regional com agregação entre regiões e contas · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** **painel central** de segurança que agrega achados de vários serviços e verifica a conta contra padrões de boas práticas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **painel da central de segurança**: junta os alertas de vários serviços e dá uma nota para a sua conta.

- ✅ **Escolha quando:** precisa **centralizar achados de segurança** e verificar a conta contra padrões (CIS, FSBP, PCI DSS).
- 🚫 **Não é a resposta quando:** quer **recomendações de custo, desempenho e limites** → [Trusted Advisor](../gerenciamento/trusted-advisor.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "painel central de segurança", "achados de vários serviços", "CIS Benchmark", "padrões de segurança".
<!-- didatico:fim -->

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

## 🔗 Documentação oficial

- [Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
