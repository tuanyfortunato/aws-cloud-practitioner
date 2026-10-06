# AWS Config

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe precisa acompanhar como as configurações dos recursos mudaram e verificar se elas seguem requisitos definidos.

**Como este serviço ajuda?** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.

**Exemplo do dia a dia:** A escola define uma regra para uma configuração importante e acompanha os recursos avaliados como conformes ou não conformes.

**O que ele não resolve sozinho?** Config observa e avalia configuração; não é o serviço principal para medir lentidão da aplicação. Correções automáticas dependem de remediação configurada.

**Primeiras palavras para entender:**

- **Configuração:** propriedades de um recurso.
- **Regra:** critério de avaliação.
- **Remediação:** ação para corrigir uma condição inadequada.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / governança e compliance · **Domínio:** 2 · **Escopo:** Regional (agregadores multi-conta/região) · **Tópico do guia:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) · [2.6 Compliance](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)
>
> **Em uma frase:** registra a **configuração** dos recursos e seu histórico de mudanças, e avalia continuamente se estão **conformes** com regras.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Selecione os recursos e configurações compatíveis que precisam de acompanhamento.

**Passo 2.** Registre mudanças e aplique regras de avaliação para requisitos definidos.

**Passo 3.** Investigue não conformidades e configure remediação quando apropriado. Avaliar uma configuração e corrigi-la são operações diferentes.

## 2. Recursos e opções, com significado

### Componentes

**Configuration recorder**

**Detalhe:** Registra *configuration items* (estado de cada recurso e relações) — todos os tipos ou selecionados; contínuo ou diário.

**Delivery channel**

**Detalhe:** Envia histórico e snapshots para **S3** e notificações para **SNS**.

**Resource timeline**

**Detalhe:** "Como estava este security group na terça passada e quem mudou?" (com link para o evento no CloudTrail).

**Config rules**

**Detalhe:** **Managed rules** (centenas prontas: `s3-bucket-public-read-prohibited`, `encrypted-volumes`, `restricted-ssh`, `root-account-mfa-enabled`…) ou **custom** (Lambda ou Guard). Avaliação por mudança ou periódica.

**Remediation**

**Detalhe:** Ações corretivas manuais ou **automáticas** via **Systems Manager Automation**.

**Conformance packs**

**Detalhe:** Pacotes de regras + remediações (ex.: boas práticas de PCI DSS, CIS) implantáveis na organização.

**Aggregators**

**Detalhe:** Visão consolidada de várias contas e regiões.

**Advanced query**

**Detalhe:** Consultas SQL sobre o inventário de configuração.

### Quem depende do Config

**Security Hub** (verificações de padrões), **Firewall Manager**, **Control Tower** (controles detectivos), **Audit Manager**.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Config observa e avalia configuração; não é o serviço principal para medir lentidão da aplicação. Correções automáticas dependem de remediação configurada.

### ⚠️ Não confundir

Config (**estado/conformidade**) × CloudTrail (**quem fez**) × CloudWatch (**métricas**).

Config **detecta e pode remediar**; **SCP** previne.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por **configuration item registrado** + por **avaliação de regra** + conformance packs.

## 5. Caso resolvido: ligando as peças

A escola define uma regra para uma configuração importante e acompanha os recursos avaliados como conformes ou não conformes.

**Aplicando a sequência à situação:**

**Etapa 1:** Selecione os recursos e configurações compatíveis que precisam de acompanhamento.
**Etapa 2:** Registre mudanças e aplique regras de avaliação para requisitos definidos.
**Etapa 3:** Investigue não conformidades e configure remediação quando apropriado. Avaliar uma configuração e corrigi-la são operações diferentes.

**Resultado e responsabilidade:** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.

**Recursos envolvidos:** Recorder, configuration items, rules e aggregators.

**Decisões que precisam ser tomadas:** Tipos de recurso, cobertura e regras.

**Outra situação comentada:** Saber se bucket atende regra e seu estado anterior: Config; quem mudou: CloudTrail.

**Por que não concluir mais do que isso:** Avaliar regra não bloqueia necessariamente criação; remediação depende de integração

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Histórico de configuração de um recurso e se segue as regras."

**Resposta curta:** AWS Config.

**Pergunta:** "Como estava o security group semana passada?"

**Resposta curta:** Config.

**Pergunta:** "Verificar continuamente se todos os buckets estão criptografados e corrigir automaticamente."

**Resposta curta:** Config rule + remediação (SSM Automation).

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
