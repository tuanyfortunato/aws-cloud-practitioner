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

---

> **Domínio 1 — Conceitos de Nuvem (24%)**

> 🔎 **Fichas detalhadas:** [AWS Compute Optimizer, Service Quotas, License Manager e outros](../../servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) · [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md)

⬅️ [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) · 🏠 [Índice do domínio](README.md)

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.

Um preço isolado não representa toda a operação. Manter tecnologia inclui pessoas, espaço, energia, licenças, capacidade e tarefas de manutenção. Compare cenários completos com hipóteses equivalentes, em vez de misturar necessidades diferentes.

Depois de observar o uso, ajuste capacidade e desperdícios antes de assumir compromissos. Um desconto sobre capacidade desnecessária ainda pode ser gasto desnecessário. Licenças próprias exigem elegibilidade; uma ferramenta de inventário não concede esse direito.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como comparar **ter carro próprio** (compra, seguro, IPVA, garagem, manutenção) com **usar aplicativo**: o preço da corrida parece maior, mas o custo total costuma ser menor quando você soma tudo (isso é o **TCO**).

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **TCO:** Custo total de propriedade: inclui infraestrutura e operação, não apenas o preço de uma máquina. A comparação depende das hipóteses adotadas.

**Custos on-premises:** fixos e antecipados (servidores, storage, rede, datacenter, energia, refrigeração, pessoal). Muitos são "invisíveis" num TCO mal feito.

**Custos na nuvem:** variáveis, por uso, sem compromisso (exceto quando você escolhe reservar).

**TCO (Total Cost of Ownership):** comparação do custo total on-premises vs nuvem, incluindo pessoal e operação. Ferramentas: Migration Evaluator e Pricing Calculator.

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **BYOL:** Trazer licença própria elegível. É necessário verificar o direito de uso e as condições do software; a AWS não cria automaticamente essa licença.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **licença:** Direito de usar um software sob condições. Instalar o programa ou inventariá-lo não concede automaticamente esse direito.

**Licenciamento:** BYOL (trazer licenças próprias, ex.: Windows Server ou Oracle em Dedicated Hosts) vs licença incluída na instância. AWS License Manager controla o uso das licenças.

**Antes de ler este trecho:**

- **Trusted Advisor:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.
- **Cost Explorer:** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.
- **rightsizing:** Ajustar capacidade à necessidade observada. Reduzir demais pode prejudicar a aplicação; a recomendação precisa ser avaliada pelo uso real.

**Rightsizing:** ajustar tipo e tamanho dos recursos ao uso real. Ferramentas: Compute Optimizer, Cost Explorer, Trusted Advisor.

**Antes de ler este trecho:**

- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.

**Serviços gerenciados reduzem custo operacional:** a AWS cuida de patch, backup e hardware; o time foca no produto.

**Antes de ler este trecho:**

- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.

**Automação reduz custo e erro:** infraestrutura como código (CloudFormation) e escalonamento automático — o Terraform é um equivalente de terceiros.

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.

**Cai na prova:** "pagar só pelo que usa" e "sem contratos de longo prazo" = modelo On-Demand; "reduzir custo de licença" = BYOL e Dedicated Hosts.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.

**Primeiro, identifique o funcionamento:** TCO inclui equipamento, energia, espaço, pessoal, licenças e operação. Rightsizing ajusta capacidade ao uso observado; automação reduz tarefas repetitivas.

**Depois, compare as escolhas:** Compare custo total e requisitos, não apenas preço de uma instância. BYOL reaproveita licenças elegíveis; licença incluída simplifica aquisição conforme o serviço e o produto.

**Por fim, verifique o limite:** License Manager não concede licença comercial. Desconto por compromisso pode gerar desperdício se a carga desaparecer. Estimativas dependem das premissas informadas.

## 4. Caso resolvido

Uma instância está superdimensionada e a equipe quer economizar. Comprar compromisso primeiro resolve?

**Raciocínio e resposta:** Primeiro avalie rightsizing e demanda. Comprometer um valor acima da necessidade pode prender a empresa a gasto desnecessário; compromisso vem depois de entender o consumo.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar custos **fixos e antecipados** (on-premises) de **variáveis** (nuvem).
- [ ] Explicar **TCO** e citar as ferramentas Migration Evaluator e Pricing Calculator.
- [ ] Explicar **BYOL** e **rightsizing**.

**Dica de revisão para a prova:** "Caso de negócio da migração" → **Migration Evaluator**; "reduzir custo de licença" → **BYOL com Dedicated Hosts**; "recurso grande demais" → **rightsizing**; "custo que some ao migrar" → energia, refrigeração e espaço do datacenter.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).
**Pergunta:** "Qual custo deixa de existir ao migrar para a AWS?"

**Resposta curta:** Custos de datacenter (energia, refrigeração, espaço físico, compra de hardware).

**Pergunta:** "Qual custo continua sendo do cliente na nuvem?"

**Resposta curta:** Gestão das aplicações e dos dados, licenças não incluídas, uso dos recursos.

**Pergunta:** "Como reduzir custo de licenças ao migrar?"

**Resposta curta:** BYOL com Dedicated Hosts, ou usar instâncias com licença incluída.

**Pergunta:** "Qual ferramenta ajuda a montar o caso de negócio (TCO) da migração?"

**Resposta curta:** Migration Evaluator.

**Pergunta:** "Qual prática ajusta recursos ao uso real?"

**Resposta curta:** Rightsizing.

**Pergunta:** "Por que serviços gerenciados reduzem o TCO?"

**Resposta curta:** Diminuem o trabalho operacional (patches, backups, hardware).

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) · 🏠 [Índice do domínio](README.md)
