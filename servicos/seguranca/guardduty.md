# Amazon GuardDuty

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa precisa perceber sinais de atividade suspeita, como comportamento incomum de credenciais ou recursos, sem analisar manualmente todos os registros.

**Como este serviço ajuda?** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.

**Exemplo do dia a dia:** O serviço identifica um padrão suspeito associado a uma identidade ou recurso e gera um achado para a equipe investigar.

**O que ele não resolve sozinho?** Um achado não confirma sozinho uma invasão. GuardDuty não é, por si só, um bloqueador de todo tráfego; respostas automáticas exigem recursos e configurações apropriados.

**Primeiras palavras para entender:**

- **Ameaça:** possível ação prejudicial.
- **Achado:** indicação de segurança para análise.
- **Detecção:** identificação de sinais suspeitos.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / detecção de ameaças · **Domínio:** 2 · **Escopo:** Regional (multi-conta via Organizations) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** detecção inteligente e contínua de **ameaças ativas** usando machine learning, detecção de anomalias e inteligência de ameaças.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Habilite os recursos e as fontes de detecção compatíveis com seu ambiente.

**Passo 2.** O serviço analisa sinais e produz achados quando identifica condições suspeitas.

**Passo 3.** Investigue o contexto e defina uma resposta. Um achado é uma indicação para análise, não uma ação de bloqueio universal.

## 2. Recursos e opções, com significado

### Fontes de dados

| Fundamentais (ativadas ao ligar) | Planos de proteção opcionais |
|---|---|
| **CloudTrail management events** | **S3 Protection** (data events do S3) |
| **VPC Flow Logs** | **EKS Protection** (audit logs do Kubernetes) |
| **Logs de DNS** (Route 53 Resolver) | **Runtime Monitoring** (EC2, ECS, EKS — com agente) |
| | **Malware Protection** (EBS do EC2, objetos novos no S3 e recovery points do AWS Backup) |
| | **AI Protection** (cargas de IA, ex.: Bedrock) ✔️ |
| | **RDS Protection** (logins suspeitos no Aurora/RDS) |
| | **Lambda Protection** (tráfego de rede das funções) |

**Sem agentes** para as fontes fundamentais: o GuardDuty lê os logs de forma independente (não precisa ativar Flow Logs/CloudTrail você mesmo).

**Extended Threat Detection:** correlaciona eventos em **sequências de ataque** de vários estágios.

### Exemplos de achados (findings)

Mineração de criptomoeda numa instância; comunicação com IPs/domínios maliciosos (C&C); chamadas de API de locais incomuns; credenciais de instância usadas fora da AWS; *port scanning*; buckets S3 tornados públicos; malware.

### Configurações

Ativação com **um clique**; **teste gratuito de 30 dias** (no Free Tier novo, aparece vinculado ao **Paid plan**).

Severidade (baixa, média, alta, crítica); listas de IPs confiáveis/ameaças; filtros de supressão.

**Resposta automatizada:** achados vão ao **EventBridge** → Lambda/SSM para isolar a instância, notificar via SNS.

Envia achados ao **Security Hub** e permite investigar no **Detective**.

Multi-conta com **administrador delegado** no Organizations.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Um achado não confirma sozinho uma invasão. GuardDuty não é, por si só, um bloqueador de todo tráfego; respostas automáticas exigem recursos e configurações apropriados.

### ⚠️ Não confundir

GuardDuty (**ameaça em andamento**, a partir de logs) × Inspector (**vulnerabilidade** de software) × Macie (**dados sensíveis**) × Detective (**investigação**).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por volume de eventos/logs analisados e por plano de proteção.

## 5. Caso resolvido: ligando as peças

O serviço identifica um padrão suspeito associado a uma identidade ou recurso e gera um achado para a equipe investigar.

**Aplicando a sequência à situação:**

**Etapa 1:** Habilite os recursos e as fontes de detecção compatíveis com seu ambiente.
**Etapa 2:** O serviço analisa sinais e produz achados quando identifica condições suspeitas.
**Etapa 3:** Investigue o contexto e defina uma resposta. Um achado é uma indicação para análise, não uma ação de bloqueio universal.

**Resultado e responsabilidade:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.

**Recursos envolvidos:** Detector, fontes de dados/proteções e findings.

**Decisões que precisam ser tomadas:** Região, contas, proteções e destinatários de achados.

**Outra situação comentada:** Credenciais usadas de forma suspeita: GuardDuty; pacote com CVE: Inspector.

**Por que não concluir mais do que isso:** Detectar não garante bloquear ou corrigir sozinho

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Detectar atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS."

**Resposta curta:** GuardDuty.

**Pergunta:** "Instância está minerando criptomoeda."

**Resposta curta:** GuardDuty.

**Pergunta:** "Responder automaticamente a um achado."

**Resposta curta:** GuardDuty → EventBridge → Lambda.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
