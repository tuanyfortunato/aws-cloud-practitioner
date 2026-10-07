# ❓ Questões — Domínio 1 — Conceitos de Nuvem (24%)

16 questões no formato da prova, em ordem de tópico. Responda antes de abrir "Ver resposta".

⬅️ [Todas as questões por domínio](README.md)

---

### Questão 1

<sub>Domínio 1 · tópico [1.1](../../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md)</sub>

Uma empresa precisa manter dados de clientes em seu datacenter por exigência regulatória, mas quer usar a AWS para o restante das aplicações, com as duas partes conectadas. Qual modelo de implantação atende a esse cenário?

- **A)** Software como serviço (SaaS)
- **B)** Nuvem pública (all-in)
- **C)** On-premises (nuvem privada)
- **D)** Híbrido

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: D**

Parte on-premises e parte na nuvem, conectadas (VPN, Direct Connect, Outposts), é o modelo **híbrido**. SaaS é um modelo de *serviço*, não de implantação.

</details>

### Questão 2

<sub>Domínio 1 · tópico [1.1](../../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md)</sub>

Um desenvolvedor quer apenas enviar o código da sua aplicação web Java e deixar a AWS cuidar de provisionamento, balanceamento de carga e escalonamento. Qual modelo de serviço e qual serviço AWS atendem a esse cenário?

- **A)** PaaS, com o AWS Elastic Beanstalk
- **B)** IaaS, com o Amazon VPC
- **C)** IaaS, com o Amazon EC2
- **D)** SaaS, com o Amazon WorkSpaces

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: A**

No **PaaS** o cliente entrega o código e a plataforma gerencia o resto; o **Elastic Beanstalk** é o exemplo clássico. EC2 e VPC são IaaS (o cliente gerencia o SO e a rede); WorkSpaces é um desktop virtual pronto.

</details>

### Questão 3

<sub>Domínio 1 · tópico [1.2](../../docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md)</sub>

Uma varejista comprava servidores extras todo ano para aguentar a Black Friday, e eles ficavam ociosos no resto do tempo. Ao migrar para a AWS, a empresa passou a provisionar capacidade conforme a demanda real. Qual vantagem da computação em nuvem descreve esse ganho?

- **A)** Beneficiar-se de economias de escala massivas
- **B)** Parar de adivinhar a capacidade
- **C)** Tornar-se global em minutos
- **D)** Trocar despesa variável por despesa de capital

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: B**

Dimensionar pela demanda real, sem comprar para o pico, é **parar de adivinhar a capacidade**. Economias de escala tratam de preços menores pelo volume da AWS; ficar global trata de várias regiões; e a troca correta é de despesa de **capital** por despesa **variável** (a alternativa inverte a ordem).

</details>

### Questão 4

<sub>Domínio 1 · tópico [1.2](../../docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) · **múltipla resposta**</sub>

Quais DUAS opções são vantagens da computação em nuvem segundo a AWS? (Escolha DUAS.)

- **A)** Trocar despesa de capital por despesa variável
- **B)** Ter acesso físico aos servidores do datacenter da AWS
- **C)** Pagar antecipadamente pelas licenças de todos os serviços
- **D)** Beneficiar-se de economias de escala massivas
- **E)** Eliminar toda a responsabilidade do cliente pela segurança

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: A, D**

As duas fazem parte das 6 vantagens oficiais. Clientes **não** têm acesso físico aos datacenters; a segurança é **compartilhada** (o cliente continua responsável pela segurança *na* nuvem); e o modelo é pagar conforme o uso, não antecipadamente.

</details>

### Questão 5

<sub>Domínio 1 · tópico [1.3](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)</sub>

Uma aplicação adiciona instâncias automaticamente quando o tráfego aumenta à noite e as remove de madrugada, quando o tráfego cai. Qual conceito isso demonstra?

- **A)** Escalabilidade vertical
- **B)** Elasticidade
- **C)** Alta disponibilidade
- **D)** Tolerância a falhas

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: B**

**Elasticidade** é crescer **e encolher** automaticamente conforme a carga. Escalabilidade vertical é aumentar o tamanho de uma instância; tolerância a falhas e alta disponibilidade tratam de continuar funcionando quando algo falha, não de acompanhar a demanda.

</details>

### Questão 6

<sub>Domínio 1 · tópico [1.3](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)</sub>

Uma empresa aceita perder no máximo 15 minutos de dados em caso de desastre. Esse requisito define qual métrica?

- **A)** Recovery Point Objective (RPO)
- **B)** Recovery Time Objective (RTO)
- **C)** Acordo de nível de serviço (SLA)
- **D)** Tempo médio entre falhas (MTBF)

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: A**

O **RPO** mede a perda máxima aceitável de dados, expressa em tempo. O **RTO** é o tempo máximo para restaurar o serviço; SLA é o compromisso de disponibilidade do provedor; MTBF mede a confiabilidade de um componente.

</details>

### Questão 7

<sub>Domínio 1 · tópico [1.3](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)</sub>

Qual estratégia de recuperação de desastres tem o MENOR custo, aceitando o maior tempo de recuperação?

- **A)** Multi-site active/active
- **B)** Warm Standby
- **C)** Pilot Light
- **D)** Backup and Restore

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: D**

Do mais barato e lento ao mais caro e rápido: **Backup and Restore** → Pilot Light → Warm Standby → Multi-site active/active.

</details>

### Questão 8

<sub>Domínio 1 · tópico [1.3](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)</sub>

Um time quer que a falha no serviço de processamento de pedidos não derrube o site da loja, e que picos de pedidos sejam absorvidos sem perda. Qual abordagem de arquitetura atende melhor a esse objetivo?

- **A)** Colocar o site e o processamento na mesma instância EC2
- **B)** Usar um único banco de dados para guardar sessões e pedidos
- **C)** Aumentar o tamanho da instância do site (escala vertical)
- **D)** Desacoplar os componentes com uma fila do Amazon SQS

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: D**

**Acoplamento fraco** com uma fila (SQS) faz o site apenas enfileirar pedidos; se o processamento falhar ou ficar lento, as mensagens esperam na fila. As demais opções aumentam o acoplamento ou não resolvem a falha de um componente.

</details>

### Questão 9

<sub>Domínio 1 · tópico [1.4](../../docs/01-conceitos-de-nuvem/04-well-architected-framework.md)</sub>

Uma empresa implanta sua aplicação em várias zonas de disponibilidade e configura recuperação automática de falhas. Qual pilar do AWS Well-Architected Framework ela está aplicando?

- **A)** Excelência operacional
- **B)** Otimização de custos
- **C)** Eficiência de performance
- **D)** Confiabilidade

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: D**

Recuperar-se automaticamente de falhas e usar várias AZs são princípios do pilar **Confiabilidade**. Excelência operacional trata de operar e melhorar processos; eficiência de performance, de usar os recursos certos; otimização de custos, de evitar gastos desnecessários.

</details>

### Questão 10

<sub>Domínio 1 · tópico [1.4](../../docs/01-conceitos-de-nuvem/04-well-architected-framework.md)</sub>

Uma empresa passou a usar instâncias com processadores AWS Graviton e a desligar recursos ociosos com o objetivo de reduzir o impacto ambiental das suas cargas. Qual pilar do Well-Architected Framework orienta essas práticas?

- **A)** Sustentabilidade
- **B)** Excelência operacional
- **C)** Confiabilidade
- **D)** Segurança

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: A**

Reduzir impacto ambiental (maximizar utilização, hardware mais eficiente como Graviton) é o pilar **Sustentabilidade**, o sexto e mais recente pilar. O objetivo declarado na questão é ambiental, não de segurança, resiliência ou operação.

</details>

### Questão 11

<sub>Domínio 1 · tópico [1.4](../../docs/01-conceitos-de-nuvem/04-well-architected-framework.md)</sub>

Um arquiteto quer revisar uma carga de trabalho existente contra as boas práticas dos pilares da AWS e gerar um plano de melhorias, sem custo. Qual serviço ele deve usar?

- **A)** AWS Trusted Advisor
- **B)** AWS Config
- **C)** AWS Well-Architected Tool
- **D)** AWS Security Hub

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: C**

A **Well-Architected Tool** revisa uma carga de trabalho contra os 6 pilares e gera um plano de melhorias. O Trusted Advisor faz verificações automáticas da conta; o Config avalia a configuração de recursos contra regras; o Security Hub centraliza achados de segurança.

</details>

### Questão 12

<sub>Domínio 1 · tópico [1.5](../../docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md)</sub>

Na adoção de nuvem de uma empresa, um grupo cuida de treinar os funcionários, gerenciar a mudança cultural e redesenhar a estrutura organizacional. Qual perspectiva do AWS Cloud Adoption Framework (CAF) cobre essas atividades?

- **A)** Governance
- **B)** People
- **C)** Business
- **D)** Operations

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: B**

**People** trata de cultura, treinamento, gestão da mudança e desenho organizacional. Business cuida do valor de negócio; Governance, de risco, orçamento e gestão do programa; Operations, de monitoramento e gestão de incidentes.

</details>

### Questão 13

<sub>Domínio 1 · tópico [1.5](../../docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md)</sub>

Qual é a ordem correta das fases da jornada de transformação na nuvem descritas no AWS CAF?

- **A)** Plan, Build, Run, Optimize
- **B)** Assess, Mobilize, Migrate, Modernize
- **C)** Envision, Align, Launch, Scale
- **D)** Align, Envision, Scale, Launch

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: C**

As quatro fases do CAF são **Envision** (enxergar oportunidades), **Align** (alinhar stakeholders e lacunas), **Launch** (pilotos em produção) e **Scale** (expandir). *Assess, Mobilize, Migrate* são fases de um programa de migração, não do CAF.

</details>

### Questão 14

<sub>Domínio 1 · tópico [1.6](../../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)</sub>

Uma empresa quer migrar seu banco de dados MySQL de um servidor próprio para o Amazon RDS, reduzindo a administração, sem alterar o código da aplicação. Qual estratégia de migração é essa?

- **A)** Replatform
- **B)** Repurchase
- **C)** Rehost
- **D)** Refactor

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: A**

**Replatform** (lift-tinker-and-shift) faz pequenas otimizações, como trocar o banco autogerenciado por um serviço gerenciado, sem reescrever a aplicação. Rehost move sem mudanças; Refactor reescreve para cloud-native; Repurchase troca por outro produto (geralmente SaaS).

</details>

### Questão 15

<sub>Domínio 1 · tópico [1.6](../../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)</sub>

Uma empresa precisa sair do datacenter em 3 meses e quer mover centenas de VMs para o Amazon EC2 sem nenhuma alteração. Qual estratégia de migração é a mais adequada?

- **A)** Rehost
- **B)** Refactor
- **C)** Retain
- **D)** Replatform

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: A**

**Rehost** (lift-and-shift) é a estratégia mais rápida e move as VMs sem mudanças, normalmente com o AWS Application Migration Service. Retain manteria as aplicações on-premises; Replatform e Refactor exigem alterações.

</details>

### Questão 16

<sub>Domínio 1 · tópico [1.7](../../docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md)</sub>

A diretoria de uma empresa pede uma estimativa do custo total de propriedade (TCO) de mover todo o ambiente on-premises para a AWS, para montar o caso de negócio da migração. Qual serviço ajuda nisso?

- **A)** AWS Cost Explorer
- **B)** Migration Evaluator
- **C)** AWS Migration Hub
- **D)** AWS Budgets

<details markdown="1">
<summary>Ver resposta</summary>

**Resposta: B**

O **Migration Evaluator** analisa o ambiente atual e monta o caso de negócio (TCO) da migração. Cost Explorer e Budgets trabalham com gastos de recursos que já estão na AWS; o Migration Hub acompanha o progresso das migrações.

</details>
