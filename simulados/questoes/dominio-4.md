# ❓ Questões — Domínio 4 — Cobrança, Preços e Suporte (12%)

15 questões no formato da prova, em ordem de tópico. Responda antes de abrir "Ver resposta".

⬅️ [Todas as questões por domínio](README.md)

---

### Questão 1

<sub>Domínio 4 · tópico [4.1](../../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md)</sub>

Uma escola parou uma instância Amazon EC2 que só usa no período de matrículas e a deixou parada durante o mês inteiro, com um volume Amazon EBS anexado. O que continua sendo cobrado nesse mês?

- **A)** As horas de uso da instância, com desconto
- **B)** O armazenamento do volume EBS
- **C)** Nada, porque a instância está parada
- **D)** A transferência de dados de entrada da instância

<details>
<summary>Ver resposta</summary>

**Resposta: B**

Instância **parada** não cobra uso do EC2 nem transferência de dados, mas os **volumes EBS** continuam cobrados pelo armazenamento, em qualquer estado da instância (assim como endereços Elastic IP). Por isso "nada" está errado, a instância parada não gera horas de uso, e a entrada de dados na AWS já é gratuita.

</details>

### Questão 2

<sub>Domínio 4 · tópico [4.1](../../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md)</sub>

Uma empresa notou que, no Amazon S3, o preço por GB armazenado fica menor à medida que o volume total cresce. Qual princípio de preço da AWS esse comportamento ilustra?

- **A)** Economizar ao se comprometer
- **B)** Preço fixo
- **C)** Pagar menos usando mais (desconto por volume)
- **D)** Pagar pelo uso (pay-as-you-go)

<details>
<summary>Ver resposta</summary>

**Resposta: C**

**Pagar menos usando mais** é o desconto por volume: em serviços como o S3 e a transferência de saída, o preço por unidade cai em faixas conforme o uso cresce. Pagar pelo uso é cobrar só o que se consome, sem contrato; economizar ao se comprometer exige compromisso de 1 ou 3 anos (Savings Plans, instâncias reservadas); preço fixo é um valor definido por um pacote.

</details>

### Questão 3

<sub>Domínio 4 · tópico [4.1](../../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md)</sub>

Uma startup ainda não sabe quanto o seu novo produto vai crescer e quer começar sem contrato de longo prazo, pagando só pelo que usar e podendo parar a qualquer momento sem multa. Qual modelo de preço da AWS atende a essa necessidade?

- **A)** Pagar menos usando mais (desconto por volume)
- **B)** Pagar pelo uso (pay-as-you-go)
- **C)** Instâncias reservadas com pagamento antecipado total
- **D)** Savings Plans com compromisso de 3 anos

<details>
<summary>Ver resposta</summary>

**Resposta: B**

**Pagar pelo uso** cobra só o que se consome, sem contrato, sem compromisso e sem multa ao parar, o que combina com uma demanda ainda desconhecida. Savings Plans e instâncias reservadas trocam desconto por compromisso de 1 ou 3 anos; o desconto por volume depende de um uso grande que a startup ainda não tem.

</details>

### Questão 4

<sub>Domínio 4 · tópico [4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)</sub>

Uma empresa executa renderizações de vídeo em lote que podem ser interrompidas e retomadas depois, sem prazo rígido. Qual opção de compra do EC2 oferece o MENOR custo?

- **A)** Spot Instances
- **B)** On-Demand Instances
- **C)** Dedicated Hosts
- **D)** Reserved Instances Standard de 3 anos

<details>
<summary>Ver resposta</summary>

**Resposta: A**

As **Spot Instances** oferecem até 90% de desconto para cargas tolerantes a interrupção (aviso de 2 minutos). On-Demand é mais caro; Dedicated Hosts são os mais caros; RIs exigem compromisso de 1 ou 3 anos e fazem sentido para cargas estáveis.

</details>

### Questão 5

<sub>Domínio 4 · tópico [4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)</sub>

Uma empresa usa Amazon EC2 em várias regiões, AWS Fargate e AWS Lambda, e quer um desconto com compromisso de 1 ano que se aplique automaticamente a todos esses serviços, mesmo se mudar a família de instâncias. Qual opção atende a esse requisito?

- **A)** Reserved Instances Standard
- **B)** Spot Instances
- **C)** Compute Savings Plans
- **D)** EC2 Instance Savings Plans

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **Compute Savings Plans** vale para EC2 de qualquer família e região, Fargate e Lambda. O EC2 Instance Savings Plans fica preso a uma família numa região; RIs Standard ficam presas a um tipo de instância; Spot não tem compromisso nem cobre Lambda.

</details>

### Questão 6

<sub>Domínio 4 · tópico [4.3](../../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) · **múltipla resposta**</sub>

Quais DOIS tipos de transferência de dados são GRATUITOS na AWS? (Escolha DUAS.)

- **A)** Transferência entre zonas de disponibilidade da mesma região
- **B)** Transferência entre regiões AWS
- **C)** Transferência de uma origem na AWS (como o S3) para o Amazon CloudFront
- **D)** Entrada de dados da internet para a AWS
- **E)** Saída de dados da AWS para a internet

<details>
<summary>Ver resposta</summary>

**Resposta: C, D**

A **entrada** de dados da internet e a transferência de **origens AWS para o CloudFront** são gratuitas. A saída para a internet, a transferência entre regiões e a transferência entre AZs são cobradas.

</details>

### Questão 7

<sub>Domínio 4 · tópico [4.4](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)</sub>

Antes de migrar, uma empresa quer estimar o custo mensal de uma nova arquitetura com EC2, RDS e S3, e compartilhar a estimativa com a diretoria. Qual ferramenta deve ser usada?

- **A)** AWS Cost Explorer
- **B)** AWS Cost and Usage Report
- **C)** AWS Budgets
- **D)** AWS Pricing Calculator

<details>
<summary>Ver resposta</summary>

**Resposta: D**

A **Pricing Calculator** estima custos **antes** de criar recursos e gera estimativas compartilháveis. Cost Explorer, Budgets e CUR trabalham com gastos **reais** de recursos já em uso.

</details>

### Questão 8

<sub>Domínio 4 · tópico [4.4](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)</sub>

O gerente financeiro quer ser notificado por e-mail quando o gasto PREVISTO do mês ultrapassar US$ 5.000. Qual serviço deve ser configurado?

- **A)** AWS Budgets
- **B)** AWS Pricing Calculator
- **C)** AWS Trusted Advisor
- **D)** AWS Cost Explorer

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Budgets** dispara alertas quando o gasto real **ou previsto** passa de um limite (e pode até executar ações). O Cost Explorer analisa e prevê, mas não alerta por limite; a Pricing Calculator estima antes de usar; o Trusted Advisor dá recomendações.

</details>

### Questão 9

<sub>Domínio 4 · tópico [4.4](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)</sub>

Uma empresa com uma única conta AWS precisa saber quanto cada departamento gasta para fazer o rateio interno dos custos. Qual é a forma recomendada?

- **A)** Abrir um caso no AWS Support pedindo o relatório
- **B)** Criar um usuário IAM para cada departamento
- **C)** Usar o AWS Pricing Calculator mensalmente
- **D)** Aplicar cost allocation tags aos recursos e ativá-las no console de Billing

<details>
<summary>Ver resposta</summary>

**Resposta: D**

As **cost allocation tags** (ex.: `departamento=marketing`), depois de **ativadas** no Billing, separam os custos no Cost Explorer e no CUR. Usuários IAM não separam custos de recursos; a calculadora estima custos futuros; o suporte não faz rateio.

</details>

### Questão 10

<sub>Domínio 4 · tópico [4.5](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)</sub>

Uma startup quer o plano de AWS Support pago de MENOR custo, que começa em US$ 29 por mês por conta e oferece resposta em até 30 minutos para casos críticos. Qual plano atende a esse requisito?

- **A)** AWS Enterprise Support
- **B)** AWS Unified Operations
- **C)** Basic
- **D)** AWS Business Support+

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Business Support+** é o plano pago de entrada entre os planos atuais, os mesmos que a task 4.3 do guia do exame cita: a partir de US$ 29/mês por conta, com resposta de 30 minutos para casos críticos. O Basic é gratuito e não tem suporte técnico; o Enterprise começa em US$ 5.000/mês (15 min); o Unified Operations, em US$ 50.000/mês (5 min).

</details>

### Questão 11

<sub>Domínio 4 · tópico [4.5](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)</sub>

Uma grande empresa precisa de um Technical Account Manager (TAM) designado e de resposta em até 15 minutos quando um sistema crítico estiver fora do ar, pelo MENOR custo. Qual plano de suporte atende a esses requisitos?

- **A)** AWS Unified Operations
- **B)** AWS Business Support+
- **C)** Basic
- **D)** AWS Enterprise Support

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Enterprise Support** inclui TAM **designado** e resposta em 15 minutos para casos críticos, a partir de US$ 5.000/mês — atende ao requisito com o menor custo. O Business Support+ responde em 30 minutos e não tem TAM designado; o Basic não tem suporte técnico; o Unified Operations (5 min) também atenderia, mas custa a partir de US$ 50.000/mês.

</details>

### Questão 12

<sub>Domínio 4 · tópico [4.6](../../docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md)</sub>

Uma empresa quer contratar especialistas da própria AWS para ajudar a planejar e executar a migração de suas cargas de trabalho para a nuvem. Qual opção atende a esse pedido?

- **A)** AWS Trust & Safety
- **B)** AWS Support Basic
- **C)** AWS Professional Services
- **D)** AWS Marketplace

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **AWS Professional Services** é a equipe de consultoria da própria AWS, que ajuda a projetar, construir, migrar e gerenciar cargas. A Trust & Safety recebe denúncias de abuso; o Marketplace vende software e serviços de terceiros; o plano Basic não inclui suporte técnico. Se o pedido fosse uma empresa parceira, a resposta seria um parceiro da APN.

</details>

### Questão 13

<sub>Domínio 4 · tópico [4.6](../../docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md)</sub>

Uma rede de escolas quer contratar uma empresa de consultoria parceira da AWS, com profissionais certificados, para implementar seu novo portal na nuvem. Onde ela encontra esse tipo de empresa?

- **A)** No AWS Trust & Safety
- **B)** No AWS Health Dashboard
- **C)** Na AWS Partner Network (APN)
- **D)** No AWS Artifact

<details>
<summary>Ver resposta</summary>

**Resposta: C**

A **AWS Partner Network** é a comunidade global de parceiros: consultorias e integradores de sistemas, que implementam projetos, e ISVs, que criam software. A Trust & Safety recebe denúncias de abuso; o Artifact entrega relatórios de conformidade; o Health Dashboard mostra eventos que afetam os serviços.

</details>

### Questão 14

<sub>Domínio 4 · tópico [4.6](../../docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md)</sub>

O setor de compras de uma empresa quer que os funcionários só consigam comprar, no AWS Marketplace, produtos de uma lista previamente aprovada. Qual recurso atende a esse controle?

- **A)** AWS Trusted Advisor
- **B)** AWS Artifact
- **C)** Private Marketplace
- **D)** AWS Budgets

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **Private Marketplace** cria um catálogo personalizado de produtos pré-aprovados que os usuários da organização podem comprar, mantendo o controle das compras. O Artifact entrega relatórios de conformidade; o Budgets alerta sobre gastos, mas não restringe produtos; o Trusted Advisor dá recomendações.

</details>

### Questão 15

<sub>Domínio 4 · tópico [4.6](../../docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md)</sub>

Uma equipe busca guias e padrões (*patterns*) de especialistas da AWS para acelerar a adoção da nuvem e a modernização das suas aplicações. Qual recurso da AWS reúne esse material?

- **A)** AWS Health Dashboard
- **B)** AWS Prescriptive Guidance
- **C)** AWS Trusted Advisor
- **D)** AWS Artifact

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **AWS Prescriptive Guidance** reúne recursos de especialistas da AWS para acelerar a adoção da nuvem e a modernização: guias de planejamento e implementação e padrões com passos, arquiteturas e código para cenários de migração e modernização. O Artifact entrega relatórios de conformidade; o Health Dashboard mostra eventos dos serviços; o Trusted Advisor verifica a conta e recomenda boas práticas.

</details>
