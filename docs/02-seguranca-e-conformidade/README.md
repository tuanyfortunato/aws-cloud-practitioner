# Domínio 2 — Segurança e Conformidade

## 🧠 Antes de começar

**Qual é a dificuldade?** Dados e recursos precisam de proteção, e a equipe precisa saber quem pode fazer cada ação e quem é responsável por cada camada.

**A ideia em palavras simples:** Este domínio responde **quem protege o quê** e **com qual serviço**. A base é o modelo de responsabilidade compartilhada e o IAM; depois vêm criptografia, compliance, monitoramento, firewalls e detecção de ameaças.

**Exemplo do dia a dia:** A escola permite que alunos consultem seus dados e que a equipe administre recursos, sem compartilhar uma identidade com poder sobre tudo.

Comece pelas aberturas dos tópicos para entender a situação e a solução. Depois use o vocabulário,
os objetivos de leitura e o conteúdo técnico. As fichas detalham cada serviço; o índice não substitui essa leitura.

**Peso na prova:** 30% das questões pontuadas

**Como o conteúdo está dividido:**

- **Parte 1:** O domínio mais pesado. Esta parte cobre quem é responsável pelo quê e como funciona o controle de acesso.
- **Parte 2:** Esta parte cobre como proteger dados, provar conformidade e detectar ameaças.

## 🧭 Como estudar este domínio

- 🗺️ **Ordem sugerida:** Comece por **2.1 (responsabilidade)** e **2.3 (IAM)**, que aparecem em muitas questões. Depois estude os serviços em pares que confundem: CloudTrail × Config × CloudWatch (2.7), security group × NACL (2.8), GuardDuty × Inspector × Macie (2.9).
- 🎯 **Dica:** É o domínio com mais pegadinhas de **"qual serviço"**. Para cada serviço, decore **uma palavra-chave** (ex.: Macie → dados pessoais).
- 🧠 Cada tópico começa com a seção **Antes de começar**: problema, explicação, exemplo e limite.
  Depois vêm palavras novas explicadas, objetivos de leitura e revisão para a prova.

## Tópicos

| # | Tópico | Perguntas típicas | Status |
|---|---|---|---|
| 2.1 | [Modelo de responsabilidade compartilhada](01-responsabilidade-compartilhada.md) | 6 | 🔴 |
| 2.2 | [Usuário root](02-usuario-root.md) | 4 | 🔴 |
| 2.3 | [AWS IAM (Identity and Access Management)](03-iam.md) | 10 | 🔴 |
| 2.4 | [Governança multi-conta](04-governanca-multi-conta.md) | 6 | 🔴 |
| 2.5 | [Criptografia](05-criptografia.md) | 7 | 🔴 |
| 2.6 | [Compliance e governança](06-compliance-e-governanca.md) | 5 | 🔴 |
| 2.7 | [Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) | 8 | 🔴 |
| 2.8 | [Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) | 9 | 🔴 |
| 2.9 | [Detecção de ameaças e postura de segurança](09-deteccao-de-ameacas.md) | 8 | 🔴 |
| 2.10 | [Outros pontos de segurança](10-outros-pontos-de-seguranca.md) | 4 | 🔴 |

> Legenda: 🔴 Não iniciado · 🟡 Em andamento · 🟢 Revisado

## Revisão rápida do domínio

- 🃏 [Flashcards do domínio](../../flashcards/dominio-2.md)
- ⚖️ [Pares que confundem](../../resumos/comparativos.md)
- 🔑 [Palavras-chave → serviço](../../resumos/palavras-chave.md)
- 📌 [Números-âncora](../../resumos/numeros-ancora.md)
