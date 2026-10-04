# 3.4 Escalabilidade e balanceamento de carga

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

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.3 Amazon EC2](03-ec2.md) · 🏠 [Índice do domínio](README.md) · [3.5 Containers e serverless](05-containers-e-serverless.md) ➡️
