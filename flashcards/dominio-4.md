# 🃏 Flashcards — Domínio 4 — Cobrança, Preços e Suporte

Clique na pergunta para ver a resposta. Gerado a partir da seção *Revisão* de cada aula (`python3 scripts/gerar_docs.py`).

**Total:** 30 cards


## [4.1 Princípios de preço da AWS](../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md)

<details markdown="1">
<summary>O que significa pagar pelo uso?</summary>

Pagar só pelos serviços que você usa, pelo tempo em que usa, sem contrato de longo prazo e sem multa ao parar de usar.
</details>

<details markdown="1">
<summary>Como funciona o princípio "economize ao se comprometer"?</summary>

Você se compromete a usar uma quantidade de serviço por 1 ou 3 anos e, em troca, paga preços menores que os sob demanda.
</details>

<details markdown="1">
<summary>O que é o desconto por volume?</summary>

Preço escalonado em faixas: quanto mais você usa, menor o preço por unidade, como no S3 e na transferência de dados de saída do EC2.
</details>

<details markdown="1">
<summary>A transferência de dados para dentro da AWS é cobrada?</summary>

Não: a AWS informa que a transferência de dados de entrada é gratuita.
</details>

<details markdown="1">
<summary>Como funciona o plano gratuito do AWS Free Tier para contas novas?</summary>

A conta recebe US$ 100 em créditos, pode ganhar mais US$ 100 com atividades, e o plano termina em 6 meses ou quando os créditos acabam.
</details>


## [4.2 Modelos de compra do EC2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)

<details markdown="1">
<summary>Quando usar instâncias Spot?</summary>

Quando a carga tolera interrupção e tem horário flexível, como processamento em lote e análise de dados; o desconto chega a 90%.
</details>

<details markdown="1">
<summary>Qual é a diferença entre Compute Savings Plans e EC2 Instance Savings Plans?</summary>

O Compute Savings Plans vale para qualquer família, Região e sistema, e também para Fargate e Lambda (até 66%); o EC2 Instance Savings Plans exige uma família numa Região e dá até 72%.
</details>

<details markdown="1">
<summary>Qual é a diferença entre uma RI Standard e uma RI Convertible?</summary>

A Standard dá o maior desconto, mas não pode ser trocada; a Convertible dá desconto menor e pode ser trocada por outra configuração durante o prazo.
</details>

<details markdown="1">
<summary>Quando escolher um Dedicated Host?</summary>

Quando é preciso um servidor físico inteiro, com controle de onde as instâncias rodam, para usar licenças próprias cobradas por soquete, núcleo ou máquina virtual.
</details>

<details markdown="1">
<summary>Como as RIs se comportam numa organização do AWS Organizations?</summary>

Com o faturamento consolidado, o desconto de uma RI comprada por uma conta pode ser aproveitado pelas instâncias de qualquer conta da organização.
</details>


## [4.3 Como outros recursos são cobrados](../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md)

<details markdown="1">
<summary>Qual transferência de dados é gratuita: entrada ou saída?</summary>

A entrada, da internet para a AWS. A saída para a internet é cobrada, com 100 GB gratuitos por mês somando todos os serviços e Regiões.
</details>

<details markdown="1">
<summary>A transferência entre zonas de disponibilidade da mesma Região é cobrada?</summary>

Sim, para recursos como EC2, RDS, Redshift e ElastiCache, nos dois sentidos; dentro da mesma zona é gratuita, salvo o tráfego por IPv4 público.
</details>

<details markdown="1">
<summary>Como o Amazon EBS é cobrado?</summary>

Por GB-mês provisionado: paga-se o tamanho do volume criado, cheio ou não.
</details>

<details markdown="1">
<summary>Qual é o preço da economia nas classes mais baratas do S3?</summary>

Taxa por GB recuperado, prazo mínimo de armazenamento e, nas classes Glacier Flexible Retrieval e Deep Archive, restauração demorada antes da leitura.
</details>

<details markdown="1">
<summary>Cite serviços que não cobram nada por si.</summary>

IAM, faturamento consolidado do Organizations, Elastic Beanstalk, EC2 Auto Scaling e CloudFormation com recursos da AWS.
</details>


## [4.4 Ferramentas de custo e faturamento](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)

<details markdown="1">
<summary>Para que serve a AWS Pricing Calculator?</summary>

Para estimar o custo de usar serviços da AWS antes de criá-los; é uma ferramenta web gratuita.
</details>

<details markdown="1">
<summary>Qual é a diferença entre o Cost Explorer e o Budgets?</summary>

O Cost Explorer analisa os gastos passados e faz previsões; o Budgets define limites e avisa (ou age) quando o custo ou o uso se aproxima deles.
</details>

<details markdown="1">
<summary>Quais são os dois tipos de tags de alocação de custos?</summary>

As definidas pelo usuário (prefixo `user:`) e as geradas pela AWS (prefixo `aws:`), e as duas precisam ser ativadas no console de Billing para aparecer nos relatórios.
</details>

<details markdown="1">
<summary>O que o AWS Cost and Usage Report oferece?</summary>

O conjunto mais completo de dados de custo e uso, entregue num bucket do S3, por hora, dia ou mês, por recurso e por tag.
</details>

<details markdown="1">
<summary>O que o faturamento consolidado do Organizations traz?</summary>

Uma fatura única para várias contas e a soma do uso de todas, o que compartilha descontos por volume, de instâncias reservadas e de Savings Plans, sem custo adicional.
</details>


## [4.5 Planos de AWS Support](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)

<details markdown="1">
<summary>O que o Basic Support oferece?</summary>

Atendimento ao cliente 24/7 para conta e faturamento, pedidos de aumento de cota, documentação, re:Post, as verificações principais do Trusted Advisor e o AWS Health.
</details>

<details markdown="1">
<summary>Qual é o plano mínimo recomendado pela AWS para cargas de produção?</summary>

O AWS Business Support+.
</details>

<details markdown="1">
<summary>O que o Enterprise Support acrescenta ao Business Support+?</summary>

Um Technical Account Manager (TAM) designado, resposta de até 15 minutos para casos críticos e revisões estratégicas com especialistas da AWS.
</details>

<details markdown="1">
<summary>Quais tipos de caso existem no AWS Support Center?</summary>

Conta e faturamento, aumento de limite de serviço e técnico; os dois primeiros estão disponíveis para todos, e o técnico exige um plano pago.
</details>

<details markdown="1">
<summary>O que acontece com os planos Developer, Business e Enterprise On-Ramp?</summary>

Serão descontinuados em 01/01/2027; a AWS indica o Business Support+ no lugar dos dois primeiros e migra o Enterprise On-Ramp para o Enterprise Support.
</details>


## [4.6 Outros recursos de ajuda](../docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md)

<details markdown="1">
<summary>Qual é a diferença entre o AWS re:Post e o AWS Knowledge Center?</summary>

O re:Post é a comunidade de perguntas e respostas da AWS; o Knowledge Center, dentro do re:Post, reúne artigos e vídeos oficiais com as perguntas mais comuns dos clientes.
</details>

<details markdown="1">
<summary>O que é o AWS Professional Services?</summary>

A equipe de consultoria da própria AWS, que ajuda a projetar, construir, migrar e gerenciar cargas de trabalho na AWS.
</details>

<details markdown="1">
<summary>Qual é a diferença entre um ISV e um integrador de sistemas na APN?</summary>

O ISV (fornecedor independente de software) cria produtos de software; o integrador de sistemas implementa projetos para os clientes.
</details>

<details markdown="1">
<summary>Quais serviços o AWS Marketplace oferece além da compra de software?</summary>

Gestão de custos, governança e controle (como o Private Marketplace) e gestão de direitos de uso das licenças (Managed Entitlements).
</details>

<details markdown="1">
<summary>A quem denunciar spam ou ataques vindos de recursos da AWS?</summary>

À equipe AWS Trust and Safety, pelo formulário de abuso da AWS.
</details>
