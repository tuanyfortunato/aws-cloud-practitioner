# 4.2 Modelos de compra do EC2

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma máquina usada ocasionalmente, uma aplicação estável e um trabalho que pode ser interrompido não precisam da mesma forma de compra.

**A ideia em palavras simples:** Modelos de compra EC2 trocam flexibilidade, compromisso, risco de interrupção e requisitos de capacidade por condições diferentes.

**Exemplo do dia a dia:** Um teste de curta duração pode usar On-Demand. Um trabalho tolerante a interrupções pode avaliar Spot. Uso estável pode justificar avaliar um compromisso.

**O que não concluir?** Desconto não significa que a opção atende qualquer tarefa. Compromisso, interrupção e garantia de capacidade são conceitos diferentes; escolha pelo requisito.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Upfront** | pagamento antecipado. |
| **Interrupção** | a AWS retomar a instância Spot quando precisa da capacidade. |
| **Capacity Reservation** | garantir capacidade numa AZ, mesmo sem desconto. |

---

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon EC2 (Elastic Compute Cloud)](../../servicos/computacao/ec2.md)

⬅️ [4.1 Princípios de preço da AWS](01-principios-de-preco.md) · 🏠 [Índice do domínio](README.md) · [4.3 Como outros recursos são cobrados](03-cobranca-de-outros-recursos.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **licença:** Direito de usar um software sob condições. Instalar o programa ou inventariá-lo não concede automaticamente esse direito.


Uma opção de compra combina preço com condições. Uso flexível, compromisso de gasto, possibilidade de interrupção, capacidade e dedicação física são requisitos separados. Uma opção que reduz preço pode mudar uma condição importante do trabalho.

Primeiro descreva se a tarefa pode parar, quanto uso é previsível e se precisa de uma modalidade específica de hardware ou licença. Só então compare a compra. Reserva de capacidade e desconto não são sinônimos, e um compromisso pode permanecer mesmo após reduzir recursos.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como **hospedagem**: **On-Demand** é a diária de hotel (cara, sem compromisso); **Reserved/Savings Plans** é o aluguel anual (desconto alto); **Spot** é a passagem de última hora com desconto enorme, mas você pode ser tirado do voo; **Dedicated Host** é alugar a casa inteira só para você.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **CI / CD / CI/CD:** Integração contínua e entrega ou implantação contínua: práticas para construir, verificar e disponibilizar versões por etapas repetíveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **segundo / hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.
- **compliance:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.
- **evento:** Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.
- **tenancy:** Forma de compartilhamento ou dedicação de infraestrutura física. Uma máquina virtual dedicada e um host físico dedicado têm controles e usos de licença distintos.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.
- **Reserved Instances:** Benefício e condições de reserva para configurações compatíveis. Não confunda desconto com qualquer garantia universal de capacidade.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
- **BYOL:** Trazer licença própria elegível. É necessário verificar o direito de uso e as condições do software; a AWS não cria automaticamente essa licença.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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



**Formas de pagamento de RIs e Savings Plans:** All Upfront (maior desconto), Partial Upfront e No Upfront (menor desconto).

**Antes de ler este trecho:**

- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.


**RIs regionais vs zonais:** a zonal reserva capacidade numa AZ; a regional dá flexibilidade de AZ e tamanho, sem reservar capacidade.


**Reserved Instance Marketplace:** permite revender RIs Standard que não serão mais usadas.

**Antes de ler este trecho:**

- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **ElastiCache:** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.


**Reservas em outros serviços:** RDS, ElastiCache, Redshift e OpenSearch têm instâncias ou nós reservados; DynamoDB tem capacidade reservada.


**Cai na prova:** "não pode ser interrompida e é imprevisível" = On-Demand; "vai rodar 24/7 por 3 anos" = Reserved ou Savings Plans; "desconto que cobre EC2, Fargate e Lambda" = Compute Savings Plans; "maior desconto e tolera interrupção" = Spot; "licença por núcleo físico" = Dedicated Host.

## 3. Como analisar uma situação


**Primeiro, identifique o funcionamento:** On-Demand evita compromisso longo; Spot usa capacidade disponível com possibilidade de interrupção; RIs/Savings Plans reduzem preço mediante compromisso. Reserva de capacidade atende outro objetivo.

**Depois, compare as escolhas:** Interrupção aceitável: Spot. Demanda incerta: On-Demand. Uso estável: avalie compromisso. Licença por hardware: Dedicated Host. Necessidade de capacidade em AZ: Capacity Reservation.

**Por fim, verifique o limite:** Savings Plans não reservam capacidade. RI regional e RI zonal têm comportamentos distintos. Terminar uma instância não cancela compromisso contratado.

## 4. Caso resolvido

A equipe precisa de capacidade garantida numa AZ amanhã. Um Compute Savings Plan sozinho resolve?

**Raciocínio e resposta:** Não. Ele trata desconto por compromisso de gasto. Reserva de capacidade é o mecanismo adequado para a necessidade de capacidade, conforme elegibilidade e condições.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma máquina usada ocasionalmente, uma aplicação estável e um trabalho que pode ser interrompido não precisam da mesma forma de compra.

**2. O que a solução fornece?**

Modelos de compra EC2 trocam flexibilidade, compromisso, risco de interrupção e requisitos de capacidade por condições diferentes.

**3. Que conclusão seria incorreta?**

Desconto não significa que a opção atende qualquer tarefa. Compromisso, interrupção e garantia de capacidade são conceitos diferentes; escolha pelo requisito.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Escolher o modelo pelo cenário (curto e imprevisível → On-Demand; 24/7 por anos → Reserved/Savings Plans; tolera interrupção → Spot).
- [ ] Diferenciar **Compute Savings Plans** (vale para EC2, Fargate e Lambda) de **EC2 Instance Savings Plans**.
- [ ] Diferenciar **Dedicated Host** (servidor físico inteiro, licença por núcleo) de **Dedicated Instance**.
- [ ] Lembrar o **aviso de 2 minutos** do Spot e as formas de pagamento (All, Partial, No Upfront).

**Dica de revisão para a prova:** "Não pode ser interrompida e é imprevisível" → **On-Demand**. "Maior desconto e tolera interrupção" → **Spot**. "Desconto que cobre Fargate e Lambda" → **Compute Savings Plans**. "Licença por núcleo físico" → **Dedicated Host**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).
**Pergunta:** "Aplicação nova, sem histórico de uso, que não pode ser interrompida."

**Resposta curta:** On-Demand.


**Fundamento explicado no capítulo:** "Aplicação nova, sem histórico de uso, que não pode ser interrompida." → On-Demand.

**Pergunta:** "Servidor de banco que roda 24/7 pelos próximos 3 anos."

**Resposta curta:** Reserved Instances ou Savings Plans (3 anos, All Upfront dá o maior desconto).


**Fundamento explicado no capítulo:** "Servidor de banco que roda 24/7 pelos próximos 3 anos." → Reserved Instances ou Savings Plans (3 anos, All Upfront dá o maior desconto).

**Pergunta:** "Desconto com flexibilidade entre EC2, Fargate e Lambda."

**Resposta curta:** Compute Savings Plans.


**Fundamento explicado no capítulo:** "Desconto com flexibilidade entre EC2, Fargate e Lambda." → Compute Savings Plans.

**Pergunta:** "Processamento em lote que pode ser interrompido e reiniciado."

**Resposta curta:** Spot.


**Fundamento explicado no capítulo:** "Processamento em lote que pode ser interrompido e reiniciado." → Spot.

**Pergunta:** "Qual o aviso antes de uma Spot ser interrompida?"

**Resposta curta:** 2 minutos.


**Fundamento explicado no capítulo:** "Qual o aviso antes de uma Spot ser interrompida?" → 2 minutos.

**Pergunta:** "Licença de software por núcleo físico."

**Resposta curta:** Dedicated Host.


**Fundamento explicado no capítulo:** "Licença de software por núcleo físico." → Dedicated Host.

**Pergunta:** "Garantir capacidade numa AZ para um evento, sem contrato longo."

**Resposta curta:** On-Demand Capacity Reservation.


**Fundamento explicado no capítulo:** "Garantir capacidade numa AZ para um evento, sem contrato longo." → On-Demand Capacity Reservation.

**Pergunta:** "Qual opção de pagamento dá o maior desconto?"

**Resposta curta:** All Upfront.


**Fundamento explicado no capítulo:** "Qual opção de pagamento dá o maior desconto?" → All Upfront.

**Pergunta:** "Reservas compradas podem ser revendidas?"

**Resposta curta:** Sim, RIs Standard no Reserved Instance Marketplace.


**Fundamento explicado no capítulo:** "Reservas compradas podem ser revendidas?" → Sim, RIs Standard no Reserved Instance Marketplace.

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
