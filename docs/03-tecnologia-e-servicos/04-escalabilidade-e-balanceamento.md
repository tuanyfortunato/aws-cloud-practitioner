# 3.4 Escalabilidade e balanceamento de carga

## 🧠 Antes de começar

**Qual é a dificuldade?** Muitos visitantes chegam ao mesmo tempo. Uma máquina pode não atender, e várias máquinas sem distribuição adequada também podem ficar desequilibradas.

**A ideia em palavras simples:** Escalabilidade ajusta a capacidade; balanceamento distribui o tráfego. Os dois podem trabalhar juntos, mas resolvem partes diferentes do atendimento.

**Exemplo do dia a dia:** Durante uma promoção, o grupo adiciona máquinas e o balanceador encaminha pedidos aos destinos disponíveis. Depois, a quantidade de máquinas pode diminuir conforme as regras.

**O que não concluir?** Balanceador não cria máquinas por si só; aumentar máquinas não resolve todo gargalo. A aplicação e o armazenamento também precisam suportar o desenho.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Health check** | verificação periódica de que o servidor está respondendo. |
| **Camada 7 / camada 4** | nível da comunicação: 7 entende HTTP (caminhos, cabeçalhos); 4 só vê conexões TCP/UDP. |
| **Launch template** | o molde usado para criar as instâncias do grupo. |

**Ao terminar este tópico, você deve saber:**

- [ ] Explicar **mínimo, desejado e máximo** de um Auto Scaling Group e os tipos de política.
- [ ] Diferenciar **ALB** (camada 7, HTTP, por caminho), **NLB** (camada 4, TCP/UDP, altíssima performance) e **GWLB** (appliances de rede).
- [ ] Saber que o Auto Scaling **não tem custo** próprio (paga-se as instâncias).

<details>
<summary>Uma analogia para revisar a ideia</summary>

num **supermercado**, o **Auto Scaling** é o gerente que abre ou fecha caixas conforme a fila; o **Load Balancer** é o funcionário que aponta "o caixa 3 está livre" e nunca manda ninguém para o caixa fechado.

</details>

> 🎯 **Como não errar na prova:** "Aumentar/diminuir instâncias" → **Auto Scaling**. "Distribuir tráfego" → **ELB**. "/api para um serviço, /imagens para outro" → **ALB**. "TCP, latência ultrabaixa, IP fixo" → **NLB**. "Firewall de terceiros" → **GWLB**.

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon EC2 Auto Scaling](../../servicos/computacao/ec2-auto-scaling.md) · [Elastic Load Balancing (ELB)](../../servicos/computacao/elastic-load-balancing.md)

⬅️ [3.3 Amazon EC2](03-ec2.md) · 🏠 [Índice do domínio](README.md) · [3.5 Containers e serverless](05-containers-e-serverless.md) ➡️

---

## 📖 Conteúdo

- **Amazon EC2 Auto Scaling**
  - **Auto Scaling Group (ASG):** grupo de instâncias com capacidade **mínima, desejada e máxima**, criadas a partir de um **launch template**.
  - **Políticas de escalonamento:** *target tracking* (manter uma métrica num alvo, ex.: CPU em 50%), *step/simple* (degraus conforme alarmes), *scheduled* (horários conhecidos) e *predictive* (prevê a demanda com ML).
  - **Health checks:** substitui automaticamente instâncias com falha.
  - Distribui instâncias entre AZs para alta disponibilidade.
  - O Auto Scaling em si não tem custo; você paga as instâncias.
- **AWS Auto Scaling:** serviço que configura escalonamento para vários recursos de uma vez (EC2, ECS, DynamoDB, Aurora).
- **Elastic Load Balancing (ELB):** Distribui o tráfego entre destinos saudáveis em várias AZs.

| Tipo | Camada | Uso |
| --- | --- | --- |
| Application Load Balancer (ALB) | 7 (HTTP/HTTPS) | Roteamento por caminho, host ou cabeçalho; microsserviços e containers; integra com WAF |
| Network Load Balancer (NLB) | 4 (TCP/UDP/TLS) | Altíssima performance, milhões de requisições por segundo, IP estático por AZ |
| Gateway Load Balancer (GWLB) | 3 (rede) | Encaminha tráfego para appliances virtuais de terceiros (firewalls, IDS/IPS) |
| Classic Load Balancer | 4 e 7 | Geração antiga, não recomendado |

- **Funções do ELB:** health checks, terminação SSL/TLS (com certificado do ACM), distribuição entre AZs.
- **Cai na prova:** "rotear /api para um serviço e /imagens para outro" = ALB; "tráfego TCP com latência ultrabaixa" = NLB; "inspecionar tráfego com firewall de terceiros" = GWLB; "aumentar e diminuir instâncias conforme demanda" = Auto Scaling.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Como ajustar automaticamente o número de instâncias à demanda?" → EC2 Auto Scaling.
- "A loja tem pico toda sexta às 18h." → Scheduled scaling.
- "Manter a CPU média do grupo em 50%." → Target tracking.
- "Como distribuir tráfego entre instâncias em várias AZs?" → Elastic Load Balancing.
- "Qual load balancer roteia por caminho de URL?" → ALB.
- "Qual load balancer para milhões de conexões TCP com IP fixo?" → NLB.
- "Qual load balancer para appliances de firewall de terceiros?" → Gateway Load Balancer.
- "Auto Scaling e ELB juntos garantem o quê?" → Alta disponibilidade e elasticidade (instâncias com falha são substituídas e o tráfego vai só para as saudáveis).

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** Load balancer recebe tráfego e escolhe destinos saudáveis. Auto Scaling ajusta quantidade de instâncias e substitui instâncias não saudáveis conforme configuração.

**Como escolher:** ALB para HTTP e regras por host/caminho; NLB para transporte e requisitos como IP estático. Auto Scaling mantém capacidade dentro dos mínimos e máximos definidos.

**O que não concluir:** Balanceador não cria sozinho novas instâncias. Auto Scaling não compartilha automaticamente sessões gravadas no disco local. Saúde e capacidade do banco também importam.

### Exercício de decisão

Na Black Friday o tráfego triplica. Um load balancer sem capacidade adicional garante atendimento?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Não. Ele distribui a capacidade existente. Auto Scaling adiciona instâncias quando suas políticas e limites permitem; a aplicação precisa suportar o crescimento.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.3 Amazon EC2](03-ec2.md) · 🏠 [Índice do domínio](README.md) · [3.5 Containers e serverless](05-containers-e-serverless.md) ➡️
