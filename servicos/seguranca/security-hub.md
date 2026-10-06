# AWS Security Hub

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa recebe achados de segurança de várias ferramentas e precisa de uma visão organizada para acompanhar prioridades e postura de segurança.

**Como este serviço ajuda?** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.

**Exemplo do dia a dia:** A equipe consulta uma visão central de achados e controles para acompanhar problemas em seus ambientes AWS.

**O que ele não resolve sozinho?** Centralizar achados não corrige todos os recursos automaticamente nem garante conformidade com qualquer norma. Integrações, controles e ações de resposta exigem configuração.

**Primeiras palavras para entender:**

- **Postura de segurança:** situação dos controles e riscos.
- **Achado:** resultado de uma avaliação.
- **Controle:** requisito ou prática verificada.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / postura (CSPM) · **Domínio:** 2 · **Escopo:** Regional com agregação entre regiões e contas · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** **painel central** de segurança que agrega achados de vários serviços e verifica a conta contra padrões de boas práticas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina os ambientes, controles e fontes compatíveis que participarão da visão de segurança.

**Passo 2.** Reúna achados e resultados de controles para acompanhar a postura dos recursos.

**Passo 3.** Priorize problemas e configure respostas quando apropriado. Centralização não significa correção automática de todo achado.

## 2. Recursos e opções, com significado

### O que faz

| Função | Detalhe |
|---|---|
| **Agregação de achados** | GuardDuty, Inspector, Macie, IAM Access Analyzer, Firewall Manager, Config, Health e **parceiros**, num formato padrão (ASFF/OCSF). |
| **Verificações de padrões** | **AWS Foundational Security Best Practices (FSBP)**, **CIS AWS Foundations**, **PCI DSS**, **NIST SP 800-53**, AWS Resource Tagging. Gera um *security score*. |
| **Automação** | Automation rules (atualizar/suprimir achados), integração com EventBridge para remediação. |
| **Multi-conta / multi-região** | Administrador delegado + região de agregação. |
| **Pré-requisito** | ✔️ A maioria dos controles usa regras do **AWS Config**. Usando o Security Hub novo junto com o CSPM, o recorder do Config é criado automaticamente; usando só o CSPM, é preciso habilitar o Config manualmente. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Centralizar achados não corrige todos os recursos automaticamente nem garante conformidade com qualquer norma. Integrações, controles e ações de resposta exigem configuração.

### ⚠️ Não confundir

Security Hub (achados de **segurança** centralizados) × **Trusted Advisor** (boas práticas de custo, desempenho, segurança, cotas).

Security Hub (painel) × **Security Lake** (data lake de logs de segurança no formato OCSF).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

A documentação oficial já usa o nome **AWS Security Hub CSPM** para as verificações de postura (o anúncio da reformulação não foi localizado na verificação de 04/10/2026). Para a prova: "painel central de achados e padrões (CIS, FSBP)" → **Security Hub**, que está no escopo.

## 5. Caso resolvido: ligando as peças

A equipe consulta uma visão central de achados e controles para acompanhar problemas em seus ambientes AWS.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina os ambientes, controles e fontes compatíveis que participarão da visão de segurança.
**Etapa 2:** Reúna achados e resultados de controles para acompanhar a postura dos recursos.
**Etapa 3:** Priorize problemas e configure respostas quando apropriado. Centralização não significa correção automática de todo achado.

**Resultado e responsabilidade:** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.

**Recursos envolvidos:** Findings, controles/standards, agregação e configuração de contas.

**Decisões que precisam ser tomadas:** Padrões, regiões, contas e integrações.

**Outra situação comentada:** Ver achados de vários serviços num lugar: Security Hub; identificar PII em S3: Macie produz o achado.

**Por que não concluir mais do que isso:** Agregação não significa correção automática de cada finding nem certificação de conformidade

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Reunir achados de segurança de vários serviços num só painel."

**Resposta curta:** Security Hub.

**Pergunta:** "Verificar a conta contra o CIS Benchmark."

**Resposta curta:** Security Hub.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
