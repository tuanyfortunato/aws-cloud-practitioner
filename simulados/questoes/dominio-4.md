# ❓ Questões — Domínio 4 — Cobrança, Preços e Suporte (12%)

8 questões no formato da prova, em ordem de tópico. Responda antes de abrir "Ver resposta".

⬅️ [Todas as questões por domínio](README.md) · 📝 [Simulado completo](../simulado-01.md)

---

### Questão 1

<sub>Domínio 4 · tópico [4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)</sub>

Uma empresa executa renderizações de vídeo em lote que podem ser interrompidas e retomadas depois, sem prazo rígido. Qual opção de compra do EC2 oferece o MENOR custo?

- **A)** Dedicated Hosts
- **B)** Spot Instances
- **C)** On-Demand Instances
- **D)** Reserved Instances Standard de 3 anos

<details>
<summary>Ver resposta</summary>

**Resposta: B**

As **Spot Instances** oferecem até 90% de desconto para cargas tolerantes a interrupção (aviso de 2 minutos). On-Demand é mais caro; Dedicated Hosts são os mais caros; RIs exigem compromisso de 1 ou 3 anos e fazem sentido para cargas estáveis.

</details>

### Questão 2

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

### Questão 3

<sub>Domínio 4 · tópico [4.3](../../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) · **múltipla resposta**</sub>

Quais DOIS tipos de transferência de dados são GRATUITOS na AWS? (Escolha DUAS.)

- **A)** Transferência entre regiões AWS
- **B)** Saída de dados da AWS para a internet
- **C)** Transferência entre zonas de disponibilidade da mesma região
- **D)** Entrada de dados da internet para a AWS
- **E)** Transferência de uma origem na AWS (como o S3) para o Amazon CloudFront

<details>
<summary>Ver resposta</summary>

**Resposta: D, E**

A **entrada** de dados da internet e a transferência de **origens AWS para o CloudFront** são gratuitas. A saída para a internet, a transferência entre regiões e a transferência entre AZs são cobradas.

</details>

### Questão 4

<sub>Domínio 4 · tópico [4.4](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)</sub>

Antes de migrar, uma empresa quer estimar o custo mensal de uma nova arquitetura com EC2, RDS e S3, e compartilhar a estimativa com a diretoria. Qual ferramenta deve ser usada?

- **A)** AWS Budgets
- **B)** AWS Cost and Usage Report
- **C)** AWS Pricing Calculator
- **D)** AWS Cost Explorer

<details>
<summary>Ver resposta</summary>

**Resposta: C**

A **Pricing Calculator** estima custos **antes** de criar recursos e gera estimativas compartilháveis. Cost Explorer, Budgets e CUR trabalham com gastos **reais** de recursos já em uso.

</details>

### Questão 5

<sub>Domínio 4 · tópico [4.4](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)</sub>

O gerente financeiro quer ser notificado por e-mail quando o gasto PREVISTO do mês ultrapassar US$ 5.000. Qual serviço deve ser configurado?

- **A)** AWS Trusted Advisor
- **B)** AWS Cost Explorer
- **C)** AWS Budgets
- **D)** AWS Pricing Calculator

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **Budgets** dispara alertas quando o gasto real **ou previsto** passa de um limite (e pode até executar ações). O Cost Explorer analisa e prevê, mas não alerta por limite; a Pricing Calculator estima antes de usar; o Trusted Advisor dá recomendações.

</details>

### Questão 6

<sub>Domínio 4 · tópico [4.4](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)</sub>

Uma empresa com uma única conta AWS precisa saber quanto cada departamento gasta para fazer o rateio interno dos custos. Qual é a forma recomendada?

- **A)** Abrir um caso no AWS Support pedindo o relatório
- **B)** Usar o AWS Pricing Calculator mensalmente
- **C)** Aplicar cost allocation tags aos recursos e ativá-las no console de Billing
- **D)** Criar um usuário IAM para cada departamento

<details>
<summary>Ver resposta</summary>

**Resposta: C**

As **cost allocation tags** (ex.: `departamento=marketing`), depois de **ativadas** no Billing, separam os custos no Cost Explorer e no CUR. Usuários IAM não separam custos de recursos; a calculadora estima custos futuros; o suporte não faz rateio.

</details>

### Questão 7

<sub>Domínio 4 · tópico [4.5](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)</sub>

Uma startup quer o plano de AWS Support pago de MENOR custo, que começa em US$ 29 por mês por conta e oferece resposta em até 30 minutos para casos críticos. Qual plano atende a esse requisito?

- **A)** AWS Business Support+
- **B)** AWS Enterprise Support
- **C)** AWS Unified Operations
- **D)** Basic

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Business Support+** é o plano pago de entrada do modelo atual (task 4.3 do exam guide): a partir de US$ 29/mês por conta, com resposta de 30 minutos para casos críticos. O Basic é gratuito e não tem suporte técnico; o Enterprise começa em US$ 5.000/mês (15 min); o Unified Operations, em US$ 50.000/mês (5 min).

</details>

### Questão 8

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
