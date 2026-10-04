# 2.7 Logs, monitoramento e auditoria

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS CloudTrail](../../servicos/gerenciamento/cloudtrail.md) · [AWS Config](../../servicos/gerenciamento/config.md) · [Amazon CloudWatch](../../servicos/gerenciamento/cloudwatch.md) · [Amazon VPC (Virtual Private Cloud)](../../servicos/redes/vpc.md) · [AWS Health Dashboard](../../servicos/gerenciamento/health-dashboard.md)

⬅️ [2.6 Compliance e governança](06-compliance-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [2.8 Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** Três serviços respondem três perguntas diferentes: **quem fez?** (CloudTrail), **como estava configurado?** (Config) e **como está o desempenho agora?** (CloudWatch).
>
> 🏠 **Analogia:** o **CloudTrail** é a **câmera de segurança** (grava quem fez cada ação); o **Config** é o **álbum de fotos** da configuração ao longo do tempo; o **CloudWatch** é o **painel do carro**, com indicadores e luzes de alerta.

**Ao terminar este tópico, você deve saber:**

- [ ] Ligar cada pergunta ao serviço: quem fez → CloudTrail; configuração e conformidade → Config; métricas e alarmes → CloudWatch.
- [ ] Lembrar que o CloudTrail guarda **90 dias** por padrão e que, para mais tempo, se cria um **trail** para o S3.
- [ ] Lembrar que **memória e disco** do EC2 exigem o **CloudWatch agent**.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Chamada de API** | qualquer ação feita na AWS (pelo console, CLI ou programa). |
| **Métrica** | um número medido ao longo do tempo (ex.: uso de CPU). |
| **Alarme** | aviso disparado quando uma métrica passa de um limite. |

> 🎯 **Como não errar na prova:** Leia o **verbo** da pergunta: "quem **apagou**" → CloudTrail; "como **estava**" → Config; "**alertar** quando a CPU passar" → CloudWatch. "Verificar **continuamente** se segue a regra" → Config rules.

## 📖 Conteúdo

- **AWS CloudTrail:** registra as **chamadas de API** na conta: quem fez, o quê, quando, de onde (IP) e em qual recurso.
  - **Event history:** ativado por padrão, guarda **90 dias** de eventos de gerenciamento, grátis.
  - **Trails:** para guardar por mais tempo, envia os logs para um bucket S3 (e opcionalmente CloudWatch Logs). Pode ser multi-região e para toda a organização.
  - **Management events** (criar, alterar, apagar recursos) vs **data events** (ex.: leitura de objetos no S3, invocação de Lambda), que não são registrados por padrão.
  - **CloudTrail Insights:** detecta atividade anormal de API. **CloudTrail Lake:** consultas SQL sobre os eventos.
- **AWS Config:** registra a **configuração** dos recursos e o histórico de mudanças ao longo do tempo.
  - **Config rules** (gerenciadas ou customizadas): avaliam se os recursos estão conformes (ex.: "todo bucket S3 deve ser criptografado").
  - Pode disparar **remediação automática** (via Systems Manager Automation).
  - É regional e pago por item registrado e por avaliação.
- **Amazon CloudWatch**: monitoramento de métricas, logs e alarmes. Pontos de prova:
  - Métricas padrão do EC2 a cada 5 minutos (monitoramento detalhado: 1 minuto, pago).
  - **Memória e disco do EC2 não vêm por padrão:** exigem o CloudWatch agent instalado (métricas customizadas).
  - **Alarmes:** disparam ações quando uma métrica passa do limite (notificar via SNS, acionar Auto Scaling, parar/reiniciar EC2). **Billing alarm:** alerta de custo baseado na métrica de cobrança.
  - **CloudWatch Logs**, **Logs Insights** (consultas) e **dashboards**.
- **VPC Flow Logs:** registram o tráfego IP que entra e sai das interfaces de rede da VPC; usados em análise de segurança e pelo GuardDuty.
- **AWS Health Dashboard:** status dos serviços AWS e eventos que afetam a **sua** conta (manutenções programadas, problemas). Ver também [3.16](../03-tecnologia-e-servicos/16-gestao-e-governanca.md).
- **Cai na prova:** "quem apagou a instância?" = CloudTrail; "como estava configurado o security group semana passada?" = Config; "alerta quando a CPU passa de 80%" = CloudWatch alarm; "verificar continuamente se recursos seguem as regras" = Config rules.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Qual serviço registra quem encerrou uma instância e quando?" → CloudTrail.
- "Por quanto tempo o CloudTrail guarda eventos sem configurar nada?" → 90 dias (event history).
- "Como guardar logs do CloudTrail por anos?" → Criar um trail que envia para o S3.
- "Qual serviço mostra o histórico de configuração de um recurso e se ele segue as regras?" → AWS Config.
- "Como receber alerta quando a CPU passar de 80%?" → Alarme do CloudWatch (com notificação pelo SNS).
- "Como coletar a memória usada pelo EC2?" → Instalar o CloudWatch agent.
- "Como capturar o tráfego de rede da VPC?" → VPC Flow Logs.
- "Onde ver logs de aplicação?" → CloudWatch Logs.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.6 Compliance e governança](06-compliance-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [2.8 Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) ➡️
