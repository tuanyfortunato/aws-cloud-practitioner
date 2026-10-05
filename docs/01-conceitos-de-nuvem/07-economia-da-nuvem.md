# 1.7 Economia da nuvem

## 🧠 Antes de começar

**Qual é a dificuldade?** Comparar apenas o preço de uma máquina própria com o de uma máquina AWS pode esconder gastos como manutenção, energia e trabalho operacional.

**A ideia em palavras simples:** Economia da nuvem trata do conjunto de custos e do valor das escolhas. O custo total inclui mais que o preço de um recurso isolado.

**Exemplo do dia a dia:** A escola compara equipamentos, manutenção e equipe do ambiente atual com recursos e operação previstos na AWS.

**O que não concluir?** Uma estimativa depende das hipóteses usadas. Este tópico ensina o raciocínio econômico; não determina que qualquer migração sempre será mais barata.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **TCO** | custo total de propriedade: soma de todos os custos, inclusive pessoal e operação. |
| **BYOL** | trazer a sua própria licença de software. |
| **Rightsizing** | ajustar o tipo e o tamanho do recurso ao uso real. |

**Ao terminar este tópico, você deve saber:**

- [ ] Diferenciar custos **fixos e antecipados** (on-premises) de **variáveis** (nuvem).
- [ ] Explicar **TCO** e citar as ferramentas Migration Evaluator e Pricing Calculator.
- [ ] Explicar **BYOL** e **rightsizing**.

<details>
<summary>Uma analogia para revisar a ideia</summary>

é como comparar **ter carro próprio** (compra, seguro, IPVA, garagem, manutenção) com **usar aplicativo**: o preço da corrida parece maior, mas o custo total costuma ser menor quando você soma tudo (isso é o **TCO**).

</details>

> 🎯 **Como não errar na prova:** "Caso de negócio da migração" → **Migration Evaluator**; "reduzir custo de licença" → **BYOL com Dedicated Hosts**; "recurso grande demais" → **rightsizing**; "custo que some ao migrar" → energia, refrigeração e espaço do datacenter.

---

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Compute Optimizer, Service Quotas, License Manager e outros](../../servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) · [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md)

⬅️ [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) · 🏠 [Índice do domínio](README.md)

---

## 📖 Conteúdo

- **Custos on-premises:** fixos e antecipados (servidores, storage, rede, datacenter, energia, refrigeração, pessoal). Muitos são "invisíveis" num TCO mal feito.
- **Custos na nuvem:** variáveis, por uso, sem compromisso (exceto quando você escolhe reservar).
- **TCO (Total Cost of Ownership):** comparação do custo total on-premises vs nuvem, incluindo pessoal e operação. Ferramentas: Migration Evaluator e Pricing Calculator.
- **Licenciamento:** BYOL (trazer licenças próprias, ex.: Windows Server ou Oracle em Dedicated Hosts) vs licença incluída na instância. AWS License Manager controla o uso das licenças.
- **Rightsizing:** ajustar tipo e tamanho dos recursos ao uso real. Ferramentas: Compute Optimizer, Cost Explorer, Trusted Advisor.
- **Serviços gerenciados reduzem custo operacional:** a AWS cuida de patch, backup e hardware; o time foca no produto.
- **Automação reduz custo e erro:** infraestrutura como código (CloudFormation) e escalonamento automático — o Terraform é um equivalente de terceiros.
- **Cai na prova:** "pagar só pelo que usa" e "sem contratos de longo prazo" = modelo On-Demand; "reduzir custo de licença" = BYOL e Dedicated Hosts.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).

- "Qual custo deixa de existir ao migrar para a AWS?" → Custos de datacenter (energia, refrigeração, espaço físico, compra de hardware).
- "Qual custo continua sendo do cliente na nuvem?" → Gestão das aplicações e dos dados, licenças não incluídas, uso dos recursos.
- "Como reduzir custo de licenças ao migrar?" → BYOL com Dedicated Hosts, ou usar instâncias com licença incluída.
- "Qual ferramenta ajuda a montar o caso de negócio (TCO) da migração?" → Migration Evaluator.
- "Qual prática ajusta recursos ao uso real?" → Rightsizing.
- "Por que serviços gerenciados reduzem o TCO?" → Diminuem o trabalho operacional (patches, backups, hardware).

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** TCO inclui equipamento, energia, espaço, pessoal, licenças e operação. Rightsizing ajusta capacidade ao uso observado; automação reduz tarefas repetitivas.

**Como escolher:** Compare custo total e requisitos, não apenas preço de uma instância. BYOL reaproveita licenças elegíveis; licença incluída simplifica aquisição conforme o serviço e o produto.

**O que não concluir:** License Manager não concede licença comercial. Desconto por compromisso pode gerar desperdício se a carga desaparecer. Estimativas dependem das premissas informadas.

### Exercício de decisão

Uma instância está superdimensionada e a equipe quer economizar. Comprar compromisso primeiro resolve?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Primeiro avalie rightsizing e demanda. Comprometer um valor acima da necessidade pode prender a empresa a gasto desnecessário; compromisso vem depois de entender o consumo.

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

⬅️ [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) · 🏠 [Índice do domínio](README.md)
