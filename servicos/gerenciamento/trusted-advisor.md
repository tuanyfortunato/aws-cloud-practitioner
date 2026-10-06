# AWS Trusted Advisor

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa precisa identificar oportunidades de melhoria no uso da AWS, como recursos ociosos ou configurações que merecem atenção.

**Como este serviço ajuda?** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.

**Exemplo do dia a dia:** A equipe consulta uma recomendação sobre recursos pouco usados e decide se pode ajustá-los ou removê-los sem prejudicar a aplicação.

**O que ele não resolve sozinho?** Uma recomendação não conhece sozinha todas as necessidades do negócio. Cobertura e acesso dependem das condições aplicáveis; a equipe deve avaliar antes de agir.

**Primeiras palavras para entender:**

- **Verificação:** análise segundo um critério.
- **Recomendação:** orientação de melhoria.
- **Ocioso:** recurso com pouco ou nenhum uso.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / boas práticas · **Domínio:** 2, 3 e 4 · **Escopo:** Global (conta e organização) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) · [4.5 Planos de suporte](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)
>
> **Em uma frase:** inspeciona sua conta e recomenda melhorias com base nas boas práticas da AWS.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Consulte verificações compatíveis com seu ambiente e seu nível de acesso.

**Passo 2.** Leia o problema e a recomendação associados ao recurso. Compare-os com os requisitos reais da aplicação.

**Passo 3.** Faça a mudança adequada e acompanhe o resultado. Não remova um recurso apenas por uma recomendação sem avaliar seu papel.

## 2. Recursos e opções, com significado

### Categorias

1. **Cost optimization** — instâncias ociosas, volumes EBS sem uso, Elastic IPs não associados, RIs/SPs subutilizados.

2. **Performance** — instâncias sobrecarregadas, configuração do CloudFront.

3. **Security** — buckets S3 abertos, SGs com portas irrestritas, **MFA no root**, uso do IAM, snapshots públicos, access keys expostas.

4. **Fault tolerance** — EBS sem snapshot, instâncias numa só AZ, RDS sem Multi-AZ, backups.

5. **Service limits (quotas)** — uso acima de 80% da cota.

6. 🔄 **Operational excellence** — práticas operacionais (logs, monitoramento). *(confirmado na documentação oficial; materiais antigos listam só as 5 primeiras)*

Status das verificações: 🟢 sem problema · 🟡 investigação recomendada · 🔴 ação recomendada.

### Por plano de suporte

| Plano | Verificações | Extras |
|---|---|---|
| **Basic / Developer** | 📌 **Core checks**: todos de **Service Limits** + **5 de segurança**: S3 Bucket Permissions, Security Groups – Specific Ports Unrestricted, MFA on Root Account, EBS Public Snapshots, RDS Public Snapshots (✔️ lista oficial de 10/2026; "IAM Use" não aparece mais) | Refresh manual |
| **Business Support+ / Enterprise / Unified Operations** (e os clássicos Business / Enterprise On-Ramp) | **Todas** as verificações | **AWS Support API**, integração com **EventBridge**, notificações semanais, visão organizacional |
| **Enterprise e superior** | + **Trusted Advisor Priority** (recomendações priorizadas pelo time de conta) | — |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Uma recomendação não conhece sozinha todas as necessidades do negócio. Cobertura e acesso dependem das condições aplicáveis; a equipe deve avaliar antes de agir.

### ⚠️ Não confundir

Trusted Advisor (boas práticas amplas: custo, desempenho, segurança, cotas) × **Security Hub** (achados de segurança) × **Compute Optimizer** (rightsizing com ML) × **Well-Architected Tool** (revisão de uma carga contra os pilares).

## 4. Caso resolvido: ligando as peças

A equipe consulta uma recomendação sobre recursos pouco usados e decide se pode ajustá-los ou removê-los sem prejudicar a aplicação.

**Aplicando a sequência à situação:**

**Etapa 1:** Consulte verificações compatíveis com seu ambiente e seu nível de acesso.
**Etapa 2:** Leia o problema e a recomendação associados ao recurso. Compare-os com os requisitos reais da aplicação.
**Etapa 3:** Faça a mudança adequada e acompanhe o resultado. Não remova um recurso apenas por uma recomendação sem avaliar seu papel.

**Resultado e responsabilidade:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.

**Recursos envolvidos:** Checks, recomendações e visão de resultados.

**Decisões que precisam ser tomadas:** Conta, plano e acesso aos checks.

**Outra situação comentada:** Recomendação geral de boas práticas: Trusted Advisor; tamanho por uso observado: Compute Optimizer.

**Por que não concluir mais do que isso:** Não é garantia de aplicação perfeita nem alteração automática de toda recomendação

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Recomendar melhorias de custo, segurança, desempenho e limites."

**Resposta curta:** Trusted Advisor.

**Pergunta:** "Menor plano com todas as verificações do Trusted Advisor."

**Resposta curta:** Business Support+ (no modelo clássico, Business).

**Pergunta:** "Menor plano com Trusted Advisor Priority."

**Resposta curta:** Enterprise.

**Pergunta:** "Verificações disponíveis no Basic."

**Resposta curta:** Core checks (segurança essenciais + service limits).

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
