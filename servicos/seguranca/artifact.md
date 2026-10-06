# AWS Artifact

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um auditor pede relatórios sobre os controles e a conformidade da infraestrutura AWS. A empresa precisa localizar esses documentos oficiais.

**Como este serviço ajuda?** Artifact disponibiliza relatórios e acordos de conformidade aplicáveis, conforme o acesso e as condições de cada documento.

**Exemplo do dia a dia:** A escola consulta um relatório oficial da AWS para apoiar uma avaliação dos serviços usados por sua aplicação.

**O que ele não resolve sozinho?** Um relatório da AWS não certifica automaticamente a aplicação do cliente. A empresa precisa demonstrar também seus próprios controles e responsabilidades.

**Primeiras palavras para entender:**

- **Conformidade:** atendimento a requisitos.
- **Relatório:** documento com informações ou evidências.
- **Acordo:** condições aceitas pelas partes.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Compliance · **Domínio:** 2 · **Escopo:** Global (portal) · **Gratuito** · **Tópico do guia:** [2.6 Compliance e governança](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)
>
> **Em uma frase:** portal de autoatendimento para baixar **relatórios de conformidade da AWS** e aceitar **acordos** legais.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Identifique o relatório ou acordo que atende à avaliação pretendida.

**Passo 2.** Acesse o documento disponível sob as condições aplicáveis e examine seu escopo.

**Passo 3.** Use o documento junto às evidências do cliente. Um relatório do provedor não demonstra sozinho os controles da aplicação.

## 2. Recursos e opções, com significado

### O que oferece

| Seção | Exemplos |
|---|---|
| **Artifact Reports** | **SOC 1, SOC 2, SOC 3**, **PCI DSS** (Attestation of Compliance), certificações **ISO 27001/27017/27018/9001**, C5, relatórios de terceiros (ISVs do Marketplace). |
| **Artifact Agreements** | **BAA** (Business Associate Addendum — **HIPAA**), NDA, acordos de GDPR; aceitar por conta ou para toda a organização. |
| **Notificações** | Avisos de novos relatórios. |

Acesso controlado por IAM; alguns relatórios exigem aceitar termos de confidencialidade.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Um relatório da AWS não certifica automaticamente a aplicação do cliente. A empresa precisa demonstrar também seus próprios controles e responsabilidades.

### ⚠️ Não confundir

**Artifact** = evidências **da AWS** (o que a AWS certifica). **Audit Manager** = evidências **da sua conta** para a **sua** auditoria.

## 4. Caso resolvido: ligando as peças

A escola consulta um relatório oficial da AWS para apoiar uma avaliação dos serviços usados por sua aplicação.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique o relatório ou acordo que atende à avaliação pretendida.
**Etapa 2:** Acesse o documento disponível sob as condições aplicáveis e examine seu escopo.
**Etapa 3:** Use o documento junto às evidências do cliente. Um relatório do provedor não demonstra sozinho os controles da aplicação.

**Resultado e responsabilidade:** Artifact disponibiliza relatórios e acordos de conformidade aplicáveis, conforme o acesso e as condições de cada documento.

**Recursos envolvidos:** Relatórios e agreements.

**Decisões que precisam ser tomadas:** Documento solicitado e autorização para consulta.

**Outra situação comentada:** Auditor pede relatório AWS: Artifact; quem apagou recurso: CloudTrail.

**Por que não concluir mais do que isso:** Não registra atividade de usuários da sua conta nem certifica sua aplicação

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Auditor pede o relatório SOC 2 da AWS."

**Resposta curta:** Artifact.

**Pergunta:** "Aceitar o BAA para HIPAA."

**Resposta curta:** Artifact Agreements.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
