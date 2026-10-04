# 2.6 Compliance e governança

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Artifact](../../servicos/seguranca/artifact.md) · [AWS Audit Manager](../../servicos/seguranca/audit-manager.md) · [AWS Config](../../servicos/gerenciamento/config.md)

⬅️ [2.5 Criptografia](05-criptografia.md) · 🏠 [Índice do domínio](README.md) · [2.7 Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) ➡️

---

## 📖 Conteúdo

- **AWS Artifact:** portal de autoatendimento para baixar **relatórios de compliance da AWS** (SOC 1/2/3, PCI DSS, ISO 27001 etc.) e aceitar **acordos** (ex.: BAA para HIPAA). Gratuito.
- **AWS Audit Manager:** coleta evidências **da sua conta** continuamente e mapeia para frameworks (PCI DSS, GDPR, HIPAA), para preparar as suas auditorias.
- **Programas de compliance:** a AWS mantém certificações e atestados, mas compliance da carga de trabalho é responsabilidade compartilhada. Nem todo serviço é elegível para todo programa e a disponibilidade varia por região.
- **Residência de dados:** os dados ficam na região escolhida; a AWS não os move sem ação do cliente.
- **AWS GovCloud (US):** regiões isoladas para cargas reguladas do governo americano.
- **AWS Config** com **conformance packs:** conjuntos de regras para avaliar conformidade (ver [2.7](07-logs-monitoramento-e-auditoria.md)).
- **Cai na prova:** "auditor pede o relatório SOC 2 da AWS" = Artifact; "automatizar a coleta de evidências para auditoria da empresa" = Audit Manager.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Onde baixar o relatório SOC 2 ou o atestado PCI da AWS?" → AWS Artifact.
- "Onde aceitar um acordo como o BAA (HIPAA)?" → AWS Artifact (Agreements).
- "Como coletar evidências continuamente para a auditoria da empresa?" → AWS Audit Manager.
- "Os dados podem sair da região sem ação do cliente?" → Não; o cliente escolhe a região e controla onde os dados ficam.
- "Usar um serviço certificado garante que a aplicação está em conformidade?" → Não; o cliente também precisa configurar e operar de forma conforme (responsabilidade compartilhada).

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.5 Criptografia](05-criptografia.md) · 🏠 [Índice do domínio](README.md) · [2.7 Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) ➡️
