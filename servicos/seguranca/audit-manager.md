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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Defina uma avaliação e os controles que precisam de evidências.

**Passo 2.** Organize coleta de evidências compatíveis e complemente o material necessário.

**Passo 3.** Revise a avaliação para a auditoria. A ferramenta não certifica automaticamente a organização nem dispensa controles manuais.

## 2. Recursos e opções, com significado

### 🔄 Status

**Fechado a novos clientes desde 30/04/2026** e **não aparece** na lista atual de serviços da prova (versões traduzidas antigas ainda o citam).

### Como funciona

**Antes de ler este trecho:**

- **CIS / NIST / SOC / PCI DSS / HIPAA / GDPR:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.
- **ISO:** Referências de padrões e de proteção de dados com finalidades distintas. Identifique o requisito aplicável; o material técnico não substitui uma avaliação de conformidade.


**Frameworks** prontos (PCI DSS, HIPAA, GDPR, SOC 2, CIS, NIST, FedRAMP, ISO…) ou customizados.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **Security Hub:** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.


**Assessments** coletam evidências automaticamente de **Config**, **Security Hub**, **CloudTrail** e chamadas de API (snapshots de configuração), além de evidências manuais.


Gera **relatórios de avaliação** para os auditores; delegação de controles para revisão por responsáveis.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Organizar evidências não garante aprovação na auditoria nem elimina controles manuais. A ficha está identificada como não listada no escopo atual.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Artifact:** Artifact disponibiliza relatórios e acordos de conformidade aplicáveis, conforme o acesso e as condições de cada documento.
- **Audit Manager:** Audit Manager ajuda a coletar e organizar evidências em avaliações baseadas em estruturas de controles compatíveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


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

**Antes de ler este trecho:**

- **conformidade:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.


**Outra situação comentada:** Evidência da conta do cliente difere de relatório da AWS: Audit Manager e Artifact têm papéis distintos.

**Por que não concluir mais do que isso:** Não decide conformidade legal automaticamente; observe restrição a novos clientes indicada na ficha

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A organização precisa reunir evidências sobre seus controles e organizá-las para uma auditoria, sem depender apenas de coleta manual.

**2. O que a solução fornece?**

Audit Manager ajuda a coletar e organizar evidências em avaliações baseadas em estruturas de controles compatíveis.

**3. Que conclusão seria incorreta?**

Organizar evidências não garante aprovação na auditoria nem elimina controles manuais. A ficha está identificada como não listada no escopo atual.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Coletar evidências continuamente para a auditoria da empresa."

**Resposta curta:** Audit Manager.


**Fundamento explicado no capítulo:** "Coletar evidências continuamente para a auditoria da empresa." → Audit Manager.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
