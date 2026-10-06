# 2.7 Logs, monitoramento e auditoria

## 🧠 Antes de começar

**Qual é a dificuldade?** O sistema está lento, um recurso foi alterado ou uma configuração deixou de atender às regras. Cada pergunta precisa de um tipo diferente de registro.

**A ideia em palavras simples:** CloudWatch acompanha comportamento e operação; CloudTrail registra atividades AWS; Config acompanha configuração e sua avaliação. O objetivo da pergunta orienta a ferramenta.

**Exemplo do dia a dia:** Para lentidão, a equipe examina métricas e logs. Para saber quem alterou um recurso, procura o evento. Para avaliar sua configuração, usa o histórico e as regras aplicáveis.

**O que não concluir?** Nenhuma dessas ferramentas observa tudo sem configuração. Coleta, retenção, cobertura e ações de resposta variam; registrar um problema não é o mesmo que corrigi-lo.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Chamada de API** | qualquer ação feita na AWS (pelo console, CLI ou programa). |
| **Métrica** | um número medido ao longo do tempo (ex.: uso de CPU). |
| **Alarme** | aviso disparado quando uma métrica passa de um limite. |

---

> **Domínio 2 — Segurança e Conformidade (30%)**

> 🔎 **Fichas detalhadas:** [AWS CloudTrail](../../servicos/gerenciamento/cloudtrail.md) · [AWS Config](../../servicos/gerenciamento/config.md) · [Amazon CloudWatch](../../servicos/gerenciamento/cloudwatch.md) · [Amazon VPC (Virtual Private Cloud)](../../servicos/redes/vpc.md) · [AWS Health Dashboard](../../servicos/gerenciamento/health-dashboard.md)

⬅️ [2.6 Compliance e governança](06-compliance-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [2.8 Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Há três perguntas distintas: ‘como está funcionando?’, ‘quem realizou a ação?’ e ‘como estava configurado?’. Uma métrica responde a comportamento; um evento registra atividade; um histórico de configuração mostra propriedades ao longo do tempo.

Comece pela pergunta e só depois escolha a ferramenta. Se um sistema ficou lento após uma alteração, pode ser necessário correlacionar os três tipos de informação. Registrar dados também exige planejar sua coleta, conservação e acesso.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **CloudTrail** é a **câmera de segurança** (grava quem fez cada ação); o **Config** é o **álbum de fotos** da configuração ao longo do tempo; o **CloudWatch** é o **painel do carro**, com indicadores e luzes de alerta.

</details>

## 2. Conceitos e opções explicados

**AWS CloudTrail:** registra as **chamadas de API** na conta: quem fez, o quê, quando, de onde (IP) e em qual recurso.

  - **Event history:** ativado por padrão, guarda **90 dias** de eventos de gerenciamento, grátis.

  - **Trails:** para guardar por mais tempo, envia os logs para um bucket S3 (e opcionalmente CloudWatch Logs). Pode ser multi-região e para toda a organização.

  - **Management events** (criar, alterar, apagar recursos) vs **data events** (ex.: leitura de objetos no S3, invocação de Lambda), que não são registrados por padrão.

  - **CloudTrail Insights:** detecta atividade anormal de API. **CloudTrail Lake:** consultas SQL sobre os eventos.

**AWS Config:** registra a **configuração** dos recursos e o histórico de mudanças ao longo do tempo.

  - **Config rules** (gerenciadas ou customizadas): avaliam se os recursos estão conformes (ex.: "todo bucket S3 deve ser criptografado").

  - Pode disparar **remediação automática** (via Systems Manager Automation).

  - É regional e pago por item registrado e por avaliação.

**Amazon CloudWatch**: monitoramento de métricas, logs e alarmes. Pontos de prova:

  - Métricas padrão do EC2 a cada 5 minutos (monitoramento detalhado: 1 minuto, pago).

  - **Memória e disco do EC2 não vêm por padrão:** exigem o CloudWatch agent instalado (métricas customizadas).

  - **Alarmes:** disparam ações quando uma métrica passa do limite (notificar via SNS, acionar Auto Scaling, parar/reiniciar EC2). **Billing alarm:** alerta de custo baseado na métrica de cobrança.

  - **CloudWatch Logs**, **Logs Insights** (consultas) e **dashboards**.

**VPC Flow Logs:** registram o tráfego IP que entra e sai das interfaces de rede da VPC; usados em análise de segurança e pelo GuardDuty.

**AWS Health Dashboard:** status dos serviços AWS e eventos que afetam a **sua** conta (manutenções programadas, problemas). Ver também [3.16](../03-tecnologia-e-servicos/16-gestao-e-governanca.md).

**Cai na prova:** "quem apagou a instância?" = CloudTrail; "como estava configurado o security group semana passada?" = Config; "alerta quando a CPU passa de 80%" = CloudWatch alarm; "verificar continuamente se recursos seguem as regras" = Config rules.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** CloudWatch trabalha com métricas, logs e alarmes; CloudTrail registra atividades e chamadas; Config acompanha configuração e conformidade de recursos suportados.

**Depois, compare as escolhas:** CPU elevada: CloudWatch. Quem alterou a instância: CloudTrail. Qual era a configuração e se atendia uma regra: Config. Evento da infraestrutura AWS: Health.

**Por fim, verifique o limite:** Alarmes e registros precisam de configuração e retenção adequadas. CloudTrail não inclui todo evento de dados por padrão; métricas de memória da EC2 exigem coleta adicional.

## 4. Caso resolvido

Uma regra de segurança mudou e você quer saber quem mudou e como o recurso estava antes. Um único serviço resolve as duas perguntas?

**Raciocínio e resposta:** CloudTrail ajuda a identificar a ação e a identidade; Config mostra o histórico de configuração. CloudWatch complementa com o efeito operacional.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Ligar cada pergunta ao serviço: quem fez → CloudTrail; configuração e conformidade → Config; métricas e alarmes → CloudWatch.
- [ ] Lembrar que o CloudTrail guarda **90 dias** por padrão e que, para mais tempo, se cria um **trail** para o S3.
- [ ] Lembrar que **memória e disco** do EC2 exigem o **CloudWatch agent**.

**Dica de revisão para a prova:** Leia o **verbo** da pergunta: "quem **apagou**" → CloudTrail; "como **estava**" → Config; "**alertar** quando a CPU passar" → CloudWatch. "Verificar **continuamente** se segue a regra" → Config rules.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).
**Pergunta:** "Qual serviço registra quem encerrou uma instância e quando?"

**Resposta curta:** CloudTrail.

**Pergunta:** "Por quanto tempo o CloudTrail guarda eventos sem configurar nada?"

**Resposta curta:** 90 dias (event history).

**Pergunta:** "Como guardar logs do CloudTrail por anos?"

**Resposta curta:** Criar um trail que envia para o S3.

**Pergunta:** "Qual serviço mostra o histórico de configuração de um recurso e se ele segue as regras?"

**Resposta curta:** AWS Config.

**Pergunta:** "Como receber alerta quando a CPU passar de 80%?"

**Resposta curta:** Alarme do CloudWatch (com notificação pelo SNS).

**Pergunta:** "Como coletar a memória usada pelo EC2?"

**Resposta curta:** Instalar o CloudWatch agent.

**Pergunta:** "Como capturar o tráfego de rede da VPC?"

**Resposta curta:** VPC Flow Logs.

**Pergunta:** "Onde ver logs de aplicação?"

**Resposta curta:** CloudWatch Logs.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.6 Compliance e governança](06-compliance-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [2.8 Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) ➡️
