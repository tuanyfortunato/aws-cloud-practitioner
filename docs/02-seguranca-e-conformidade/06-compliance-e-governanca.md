# 2.6 Compliance e governança

## 🧠 Antes de começar

**Qual é a dificuldade?** Um auditor pede que a empresa demonstre suas práticas de segurança e os controles do provedor. A equipe precisa saber onde obter evidências e como avaliar seu ambiente.

**A ideia em palavras simples:** Conformidade envolve atender requisitos e demonstrar isso. Relatórios da AWS, avaliações de configuração e evidências do cliente atendem partes diferentes desse processo.

**Exemplo do dia a dia:** A escola consulta relatórios oficiais do provedor e reúne evidências de que ela própria protege acessos e dados.

**O que não concluir?** A conformidade da AWS não torna toda aplicação do cliente automaticamente conforme. Documentos, configuração e operação precisam ser avaliados no contexto do requisito.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Compliance** | estar em conformidade com leis, normas e regulações. |
| **SOC, PCI DSS, ISO 27001** | relatórios e certificações de segurança reconhecidos no mercado. |
| **BAA** | acordo exigido para dados de saúde (HIPAA), aceito pelo Artifact. |

---

> **Domínio 2 — Segurança e Conformidade (30%)**

> 🔎 **Fichas detalhadas:** [AWS Artifact](../../servicos/seguranca/artifact.md) · [AWS Audit Manager](../../servicos/seguranca/audit-manager.md) · [AWS Config](../../servicos/gerenciamento/config.md)

⬅️ [2.5 Criptografia](05-criptografia.md) · 🏠 [Índice do domínio](README.md) · [2.7 Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **conformidade:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.

Conformidade exige um requisito definido e evidências de atendimento. O provedor demonstra sua parte; o cliente precisa demonstrar decisões e operação que continuam sob sua responsabilidade. Um documento só vale dentro do escopo que descreve.

Separe obter um relatório oficial, avaliar uma configuração e coletar evidências. Esses trabalhos se complementam. A conclusão de uma auditoria não é obtida apenas por abrir uma ferramenta ou usar um serviço certificado.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **Artifact** é a **pasta de certificados da AWS** que você entrega ao auditor; o **Audit Manager** é um **assistente que junta as provas da sua própria empresa** para a sua auditoria.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **AWS Artifact / Artifact:** Artifact disponibiliza relatórios e acordos de conformidade aplicáveis, conforme o acesso e as condições de cada documento.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **SOC / PCI DSS / HIPAA:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.
- **BAA:** Acordos com funções diferentes: confidencialidade e relacionamento associado a requisitos específicos de saúde. Aceitar um documento não torna toda operação conforme.
- **ISO:** Referências de padrões e de proteção de dados com finalidades distintas. Identifique o requisito aplicável; o material técnico não substitui uma avaliação de conformidade.

**AWS Artifact:** portal de autoatendimento para baixar **relatórios de compliance da AWS** (SOC 1/2/3, PCI DSS, ISO 27001 etc.) e aceitar **acordos** (ex.: BAA para HIPAA). Gratuito.

**Antes de ler este trecho:**

- **AWS Audit Manager / Audit Manager:** Audit Manager ajuda a coletar e organizar evidências em avaliações baseadas em estruturas de controles compatíveis.

**AWS Audit Manager:** coleta evidências **da sua conta** continuamente e mapeia para frameworks (PCI DSS, GDPR, HIPAA), para preparar as suas auditorias.

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.

**Programas de compliance:** a AWS mantém certificações e atestados, mas compliance da carga de trabalho é responsabilidade compartilhada. Nem todo serviço é elegível para todo programa e a disponibilidade varia por região.

**Residência de dados:** os dados ficam na região escolhida; a AWS não os move sem ação do cliente.

**AWS GovCloud (US):** regiões isoladas para cargas reguladas do governo americano.

**Antes de ler este trecho:**

- **AWS Config:** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.

**AWS Config** com **conformance packs:** conjuntos de regras para avaliar conformidade (ver [2.7](07-logs-monitoramento-e-auditoria.md)).

**Cai na prova:** "auditor pede o relatório SOC 2 da AWS" = Artifact; "automatizar a coleta de evidências para auditoria da empresa" = Audit Manager.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.

**Primeiro, identifique o funcionamento:** Artifact disponibiliza documentos de conformidade da AWS. Config registra configuração e avalia regras. Evidências do ambiente do cliente ajudam uma auditoria, mas exigem interpretação.

**Depois, compare as escolhas:** Relatório da infraestrutura AWS: Artifact. Histórico e avaliação de recurso: Config. Regras do setor e localização dos dados: avalie regiões, serviços e suas obrigações.

**Por fim, verifique o limite:** A certificação da AWS não certifica automaticamente a aplicação do cliente. Uma regra conforme no Config não prova que todos os requisitos legais foram atendidos.

## 4. Caso resolvido

Um auditor pede o relatório de conformidade da AWS, não o histórico do banco da empresa. Qual recurso?

**Raciocínio e resposta:** AWS Artifact. CloudTrail registra atividades da conta; Config registra configurações. Eles não substituem o documento solicitado.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **Artifact** (relatórios da AWS) de **Audit Manager** (evidências da sua conta).
- [ ] Saber que compliance também é **responsabilidade compartilhada**.
- [ ] Saber que os dados ficam na **região escolhida** (residência de dados).

**Dica de revisão para a prova:** "Auditor pede o relatório **da AWS**" → **Artifact**. "Coletar evidências **da empresa**" → **Audit Manager**. "Avaliar se os recursos seguem regras" → **AWS Config**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).
**Pergunta:** "Onde baixar o relatório SOC 2 ou o atestado PCI da AWS?"

**Resposta curta:** AWS Artifact.

**Pergunta:** "Onde aceitar um acordo como o BAA (HIPAA)?"

**Resposta curta:** AWS Artifact (Agreements).

**Pergunta:** "Como coletar evidências continuamente para a auditoria da empresa?"

**Resposta curta:** AWS Audit Manager.

**Pergunta:** "Os dados podem sair da região sem ação do cliente?"

**Resposta curta:** Não; o cliente escolhe a região e controla onde os dados ficam.

**Pergunta:** "Usar um serviço certificado garante que a aplicação está em conformidade?"

**Resposta curta:** Não; o cliente também precisa configurar e operar de forma conforme (responsabilidade compartilhada).

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.5 Criptografia](05-criptografia.md) · 🏠 [Índice do domínio](README.md) · [2.7 Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) ➡️
