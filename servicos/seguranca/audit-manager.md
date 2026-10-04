# AWS Audit Manager

> **Categoria:** Compliance · **Domínio:** 2 · **Escopo:** Regional (multi-conta) · **Tópico do guia:** [2.6 Compliance e governança](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)
>
> **Em uma frase:** coleta **evidências da sua conta** continuamente e as mapeia para frameworks, para preparar as suas auditorias.
>
> **Escopo oficial:** ⚪ Não listado (saiu da lista atual) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **assistente que junta sozinho as provas** de que a sua conta segue as regras, para a sua auditoria.

- ✅ **Escolha quando:** precisa coletar **evidências contínuas da sua conta** para frameworks de auditoria. (Saiu da lista atual da prova.)
- 🚫 **Não é a resposta quando:** precisa dos **relatórios da AWS** → [Artifact](artifact.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "coletar evidências", "preparar auditoria", "frameworks de compliance".
<!-- didatico:fim -->

## 🔄 Status

- **Fechado a novos clientes desde 30/04/2026** e **não aparece** na lista atual de serviços da prova (versões traduzidas antigas ainda o citam).

## Como funciona

- **Frameworks** prontos (PCI DSS, HIPAA, GDPR, SOC 2, CIS, NIST, FedRAMP, ISO…) ou customizados.
- **Assessments** coletam evidências automaticamente de **Config**, **Security Hub**, **CloudTrail** e chamadas de API (snapshots de configuração), além de evidências manuais.
- Gera **relatórios de avaliação** para os auditores; delegação de controles para revisão por responsáveis.

## Cobrança

- Por evidência coletada.

## ⚠️ Não confundir

- Artifact (relatórios da AWS) × Audit Manager (evidências do cliente) × Config (avalia regras dos recursos).

## ❓ Perguntas típicas

- "Coletar evidências continuamente para a auditoria da empresa." → Audit Manager.

## 🔗 Documentação oficial

- [Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)
