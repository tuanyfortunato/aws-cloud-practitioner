# 2.6 Compliance e governança

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Artifact](../../servicos/seguranca/artifact.md) · [AWS Audit Manager](../../servicos/seguranca/audit-manager.md) · [AWS Config](../../servicos/gerenciamento/config.md)

⬅️ [2.5 Criptografia](05-criptografia.md) · 🏠 [Índice do domínio](README.md) · [2.7 Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** Compliance é **provar que se segue as regras** (leis e normas). A AWS fornece os relatórios dela; o cliente cuida da conformidade do que ele mesmo constrói.
>
> 🏠 **Analogia:** o **Artifact** é a **pasta de certificados da AWS** que você entrega ao auditor; o **Audit Manager** é um **assistente que junta as provas da sua própria empresa** para a sua auditoria.

**Ao terminar este tópico, você deve saber:**

- [ ] Diferenciar **Artifact** (relatórios da AWS) de **Audit Manager** (evidências da sua conta).
- [ ] Saber que compliance também é **responsabilidade compartilhada**.
- [ ] Saber que os dados ficam na **região escolhida** (residência de dados).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Compliance** | estar em conformidade com leis, normas e regulações. |
| **SOC, PCI DSS, ISO 27001** | relatórios e certificações de segurança reconhecidos no mercado. |
| **BAA** | acordo exigido para dados de saúde (HIPAA), aceito pelo Artifact. |

> 🎯 **Como não errar na prova:** "Auditor pede o relatório **da AWS**" → **Artifact**. "Coletar evidências **da empresa**" → **Audit Manager**. "Avaliar se os recursos seguem regras" → **AWS Config**.

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
