# AWS Audit Manager

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A organização precisa reunir evidências sobre seus controles e organizá-las para uma auditoria, sem depender apenas de coleta manual.

**Como este serviço ajuda?** Audit Manager ajuda a coletar e organizar evidências em avaliações baseadas em estruturas de controles compatíveis.

**Exemplo do dia a dia:** Uma equipe reúne evidências de seu ambiente AWS e complementa o material com documentos necessários para uma avaliação.

**O que ele não resolve sozinho?** Organizar evidências não garante aprovação na auditoria nem elimina controles manuais. A ficha está identificada como não listada no escopo atual.

**Primeiras palavras para entender:**

- **Evidência:** material que demonstra uma prática.
- **Controle:** requisito avaliado.
- **Avaliação:** conjunto organizado de controles e evidências.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Compliance · **Domínio:** 2 · **Escopo:** Regional (multi-conta) · **Tópico do guia:** [2.6 Compliance e governança](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)
>
> **Em uma frase:** coleta **evidências da sua conta** continuamente e as mapeia para frameworks, para preparar as suas auditorias.
>
> **Escopo oficial:** ⚪ Não listado (saiu da lista atual) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina uma avaliação e os controles que precisam de evidências.

**Passo 2.** Organize coleta de evidências compatíveis e complemente o material necessário.

**Passo 3.** Revise a avaliação para a auditoria. A ferramenta não certifica automaticamente a organização nem dispensa controles manuais.

## 2. Recursos e opções, com significado

### 🔄 Status

**Fechado a novos clientes desde 30/04/2026** e **não aparece** na lista atual de serviços da prova (versões traduzidas antigas ainda o citam).

### Como funciona

**Frameworks** prontos (PCI DSS, HIPAA, GDPR, SOC 2, CIS, NIST, FedRAMP, ISO…) ou customizados.

**Assessments** coletam evidências automaticamente de **Config**, **Security Hub**, **CloudTrail** e chamadas de API (snapshots de configuração), além de evidências manuais.

Gera **relatórios de avaliação** para os auditores; delegação de controles para revisão por responsáveis.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Organizar evidências não garante aprovação na auditoria nem elimina controles manuais. A ficha está identificada como não listada no escopo atual.

### ⚠️ Não confundir

Artifact (relatórios da AWS) × Audit Manager (evidências do cliente) × Config (avalia regras dos recursos).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por evidência coletada.

## 5. Caso resolvido: ligando as peças

Uma equipe reúne evidências de seu ambiente AWS e complementa o material com documentos necessários para uma avaliação.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina uma avaliação e os controles que precisam de evidências.
**Etapa 2:** Organize coleta de evidências compatíveis e complemente o material necessário.
**Etapa 3:** Revise a avaliação para a auditoria. A ferramenta não certifica automaticamente a organização nem dispensa controles manuais.

**Resultado e responsabilidade:** Audit Manager ajuda a coletar e organizar evidências em avaliações baseadas em estruturas de controles compatíveis.

**Recursos envolvidos:** Frameworks, assessments, controls e evidências.

**Decisões que precisam ser tomadas:** Escopo de avaliação e responsáveis.

**Outra situação comentada:** Evidência da conta do cliente difere de relatório da AWS: Audit Manager e Artifact têm papéis distintos.

**Por que não concluir mais do que isso:** Não decide conformidade legal automaticamente; observe restrição a novos clientes indicada na ficha

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Coletar evidências continuamente para a auditoria da empresa."

**Resposta curta:** Audit Manager.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
