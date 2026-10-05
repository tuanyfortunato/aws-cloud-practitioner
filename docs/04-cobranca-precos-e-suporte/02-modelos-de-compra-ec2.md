# 4.2 Modelos de compra do EC2

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon EC2 (Elastic Compute Cloud)](../../servicos/computacao/ec2.md)

⬅️ [4.1 Princípios de preço da AWS](01-principios-de-preco.md) · 🏠 [Índice do domínio](README.md) · [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** Há várias formas de **pagar pelo EC2**: sem compromisso, com compromisso de 1 ou 3 anos, aproveitando sobras baratas (que podem ser retomadas) ou com servidor físico dedicado. A prova pede o modelo certo para o cenário.
>
> 🏠 **Analogia:** é como **hospedagem**: **On-Demand** é a diária de hotel (cara, sem compromisso); **Reserved/Savings Plans** é o aluguel anual (desconto alto); **Spot** é a passagem de última hora com desconto enorme, mas você pode ser tirado do voo; **Dedicated Host** é alugar a casa inteira só para você.

**Ao terminar este tópico, você deve saber:**

- [ ] Escolher o modelo pelo cenário (curto e imprevisível → On-Demand; 24/7 por anos → Reserved/Savings Plans; tolera interrupção → Spot).
- [ ] Diferenciar **Compute Savings Plans** (vale para EC2, Fargate e Lambda) de **EC2 Instance Savings Plans**.
- [ ] Diferenciar **Dedicated Host** (servidor físico inteiro, licença por núcleo) de **Dedicated Instance**.
- [ ] Lembrar o **aviso de 2 minutos** do Spot e as formas de pagamento (All, Partial, No Upfront).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Upfront** | pagamento antecipado. |
| **Interrupção** | a AWS retomar a instância Spot quando precisa da capacidade. |
| **Capacity Reservation** | garantir capacidade numa AZ, mesmo sem desconto. |

> 🎯 **Como não errar na prova:** "Não pode ser interrompida e é imprevisível" → **On-Demand**. "Maior desconto e tolera interrupção" → **Spot**. "Desconto que cobre Fargate e Lambda" → **Compute Savings Plans**. "Licença por núcleo físico" → **Dedicated Host**.

## 📖 Conteúdo

| Modelo | Desconto (referência AWS) | Compromisso | Quando usar |
| --- | --- | --- | --- |
| On-Demand | Nenhum | Nenhum; cobrança por segundo ou hora | Cargas curtas, imprevisíveis, que não podem ser interrompidas; testes e desenvolvimento |
| Reserved Instances (Standard) | Até cerca de 72% | 1 ou 3 anos, tipo de instância definido | Carga estável e previsível (ex.: banco de dados sempre ligado) |
| Reserved Instances (Convertible) | Menor que o Standard | 1 ou 3 anos; pode trocar família, SO e tenancy | Carga estável, mas com chance de mudar de tipo |
| Compute Savings Plans | Até cerca de 66% | Gasto fixo por hora (US$/h) por 1 ou 3 anos | Máxima flexibilidade: vale para qualquer família, tamanho, região, SO, e também para **Fargate e Lambda** |
| EC2 Instance Savings Plans | Até cerca de 72% | Gasto por hora numa família de instância numa região | Família fixa, mas com liberdade de tamanho e SO |
| Spot Instances | Até cerca de 90% | Nenhum; a AWS pode retomar com **aviso de 2 minutos** | Cargas tolerantes a interrupção e flexíveis: batch, análise de dados, CI/CD, renderização |
| Dedicated Hosts | Mais caro | On-Demand ou reserva | **Servidor físico inteiro dedicado**, com visibilidade de sockets e núcleos: licenças por socket/núcleo (BYOL) e compliance |
| Dedicated Instances | Mais caro | On-Demand ou reserva | Instâncias em hardware não compartilhado com outros clientes, sem controle do servidor físico |
| On-Demand Capacity Reservations | Nenhum por si só | Sem prazo; paga mesmo sem usar | **Garantir capacidade** numa AZ específica (ex.: evento previsto); combina com Savings Plans |

- **Formas de pagamento de RIs e Savings Plans:** All Upfront (maior desconto), Partial Upfront e No Upfront (menor desconto).
- **RIs regionais vs zonais:** a zonal reserva capacidade numa AZ; a regional dá flexibilidade de AZ e tamanho, sem reservar capacidade.
- **Reserved Instance Marketplace:** permite revender RIs Standard que não serão mais usadas.
- **Reservas em outros serviços:** RDS, ElastiCache, Redshift e OpenSearch têm instâncias ou nós reservados; DynamoDB tem capacidade reservada.
- **Cai na prova:** "não pode ser interrompida e é imprevisível" = On-Demand; "vai rodar 24/7 por 3 anos" = Reserved ou Savings Plans; "desconto que cobre EC2, Fargate e Lambda" = Compute Savings Plans; "maior desconto e tolera interrupção" = Spot; "licença por núcleo físico" = Dedicated Host.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).

- "Aplicação nova, sem histórico de uso, que não pode ser interrompida." → On-Demand.
- "Servidor de banco que roda 24/7 pelos próximos 3 anos." → Reserved Instances ou Savings Plans (3 anos, All Upfront dá o maior desconto).
- "Desconto com flexibilidade entre EC2, Fargate e Lambda." → Compute Savings Plans.
- "Processamento em lote que pode ser interrompido e reiniciado." → Spot.
- "Qual o aviso antes de uma Spot ser interrompida?" → 2 minutos.
- "Licença de software por núcleo físico." → Dedicated Host.
- "Garantir capacidade numa AZ para um evento, sem contrato longo." → On-Demand Capacity Reservation.
- "Qual opção de pagamento dá o maior desconto?" → All Upfront.
- "Reservas compradas podem ser revendidas?" → Sim, RIs Standard no Reserved Instance Marketplace.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** On-Demand evita compromisso longo; Spot usa capacidade disponível com possibilidade de interrupção; RIs/Savings Plans reduzem preço mediante compromisso. Reserva de capacidade atende outro objetivo.

**Como escolher:** Interrupção aceitável: Spot. Demanda incerta: On-Demand. Uso estável: avalie compromisso. Licença por hardware: Dedicated Host. Necessidade de capacidade em AZ: Capacity Reservation.

**O que não concluir:** Savings Plans não reservam capacidade. RI regional e RI zonal têm comportamentos distintos. Terminar uma instância não cancela compromisso contratado.

### Exercício de decisão

A equipe precisa de capacidade garantida numa AZ amanhã. Um Compute Savings Plan sozinho resolve?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Não. Ele trata desconto por compromisso de gasto. Reserva de capacidade é o mecanismo adequado para a necessidade de capacidade, conforme elegibilidade e condições.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **Descontos confirmados (📌):**

| Opção | Desconto máx. vs On-Demand | Compromisso | Detalhe que cai |
|---|---|---|---|
| Spot | até **90%** | nenhum | **aviso de 2 min**; ⚠️ Savings Plans **não** se aplicam a Spot |
| EC2 Instance Savings Plans | até **72%** | 1 ou 3 anos, US$/hora | família fixa numa região (tamanho/SO flexíveis) |
| Compute Savings Plans | até **66%** | 1 ou 3 anos | EC2 (qualquer família/região), **Fargate e Lambda** |
| Standard RI | até **72%** | 1 ou 3 anos | revendável no RI Marketplace |
| Convertible RI | até **66%** (✔️ confirmado no guia de Savings Plans/RIs) | 1 ou 3 anos | troca família/SO |
| Database Savings Plans | até 35% (serverless) / até 20% (provisionado) | **1 ano**, sem pagamento adiantado | 🔄 novo, desde 02/12/2025 (RDS, Aurora, DynamoDB, ElastiCache…) |
| SageMaker AI Savings Plans | até 64% | 1 ou 3 anos | — |

- Para a prova basta: "Convertible < Standard em desconto, porém mais flexível".
- **Flexibilidade de RIs (task 4.1):**
  - **RI regional:** vale para qualquer AZ da região e, em Linux/Unix com tenancy padrão, tem **flexibilidade de tamanho** dentro da família (ex.: uma `m5.xlarge` cobre duas `m5.large`). Não reserva capacidade.
  - **RI zonal:** presa a uma AZ e a um tamanho, mas **reserva capacidade** naquela AZ ✔️ (a regional não reserva).
  - **Convertible:** pode ser **trocada** por outra Convertible (família, SO, tenancy) de valor igual ou maior ✔️. **Standard** (regional ou zonal) pode ser **vendida** no RI Marketplace; a **Convertible não pode** ✔️.
  - Ordem de aplicação dos descontos ✔️: primeiro as **RIs**, depois os **Savings Plans** (que se aplicam primeiro ao uso com maior percentual de desconto), o restante é On-Demand. A flexibilidade de tamanho da RI regional também foi confirmada.
- **Capacity Reservations** ✔️: os descontos de **Savings Plans** e de **RIs regionais** se aplicam a elas. ✔️ A reserva é cobrada pela **tarifa On-Demand mesmo sem instância rodando**; quando ocupada, paga-se a instância, sem cobrança dupla.
- **RIs no Organizations (task 4.1):** com faturamento consolidado, RIs e Savings Plans são **compartilhados** entre as contas por padrão (o desconto vale primeiro na conta que comprou); a conta de gerenciamento pode desativar o compartilhamento por conta. Ver [Organizations](../../servicos/gerenciamento/organizations.md).
- ⚠️ "Estável 24/7 por 3 anos, menor custo, sem flexibilidade" → Standard RI ou EC2 Instance SP · "EC2 + Lambda + Fargate com flexibilidade" → **Compute Savings Plans** · "tolera interrupção (batch, CI/CD, render)" → **Spot**.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [4.1 Princípios de preço da AWS](01-principios-de-preco.md) · 🏠 [Índice do domínio](README.md) · [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) ➡️
