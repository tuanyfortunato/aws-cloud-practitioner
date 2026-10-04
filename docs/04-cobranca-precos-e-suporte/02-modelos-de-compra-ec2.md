# 4.2 Modelos de compra do EC2

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon EC2 (Elastic Compute Cloud)](../../servicos/computacao/ec2.md)

⬅️ [4.1 Princípios de preço da AWS](01-principios-de-preco.md) · 🏠 [Índice do domínio](README.md) · [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) ➡️

---

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
| Convertible RI | até **66%** (página de preços de RI; o SAP Lens cita 54%) | 1 ou 3 anos | troca família/SO |
| Database Savings Plans | até 35% | 1 ou 3 anos | 🔄 novo (RDS, Aurora, DynamoDB, ElastiCache…) |
| SageMaker AI Savings Plans | até 64% | 1 ou 3 anos | — |

- Para a prova basta: "Convertible < Standard em desconto, porém mais flexível".
- ⚠️ "Estável 24/7 por 3 anos, menor custo, sem flexibilidade" → Standard RI ou EC2 Instance SP · "EC2 + Lambda + Fargate com flexibilidade" → **Compute Savings Plans** · "tolera interrupção (batch, CI/CD, render)" → **Spot**.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [4.1 Princípios de preço da AWS](01-principios-de-preco.md) · 🏠 [Índice do domínio](README.md) · [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) ➡️
