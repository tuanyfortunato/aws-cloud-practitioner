# 1.7 Economia da nuvem

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Compute Optimizer, Service Quotas, License Manager e outros](../../servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) · [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md)

⬅️ [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) · 🏠 [Índice do domínio](README.md)

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** Economia da nuvem é **comparar o custo total** de manter um datacenter com o de usar a nuvem — e conhecer as práticas que reduzem a conta (licenças, tamanho certo, serviços gerenciados, automação).
>
> 🏠 **Analogia:** é como comparar **ter carro próprio** (compra, seguro, IPVA, garagem, manutenção) com **usar aplicativo**: o preço da corrida parece maior, mas o custo total costuma ser menor quando você soma tudo (isso é o **TCO**).

**Ao terminar este tópico, você deve saber:**

- [ ] Diferenciar custos **fixos e antecipados** (on-premises) de **variáveis** (nuvem).
- [ ] Explicar **TCO** e citar as ferramentas Migration Evaluator e Pricing Calculator.
- [ ] Explicar **BYOL** e **rightsizing**.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **TCO** | custo total de propriedade: soma de todos os custos, inclusive pessoal e operação. |
| **BYOL** | trazer a sua própria licença de software. |
| **Rightsizing** | ajustar o tipo e o tamanho do recurso ao uso real. |

> 🎯 **Como não errar na prova:** "Caso de negócio da migração" → **Migration Evaluator**; "reduzir custo de licença" → **BYOL com Dedicated Hosts**; "recurso grande demais" → **rightsizing**; "custo que some ao migrar" → energia, refrigeração e espaço do datacenter.

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

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) · 🏠 [Índice do domínio](README.md)
