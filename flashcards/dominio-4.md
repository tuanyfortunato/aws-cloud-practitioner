# 🃏 Flashcards — Domínio 4 — Cobrança, Preços e Suporte

Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* de cada tópico (`python3 scripts/gerar_docs.py`).

**Total:** 40 cards


## [4.1 Princípios de preço da AWS](../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md)

<details>
<summary>O que significa pagar pelo uso?</summary>

Pagar só pelos serviços que você usa, pelo tempo em que usa, sem contrato de longo prazo e sem multa ao parar de usar.
</details>

<details>
<summary>Como funciona o princípio "economize ao se comprometer"?</summary>

Você se compromete a usar uma quantidade de serviço por 1 ou 3 anos e, em troca, paga preços menores que os sob demanda.
</details>

<details>
<summary>O que é o desconto por volume?</summary>

Preço escalonado em faixas: quanto mais você usa, menor o preço por unidade, como no S3 e na transferência de dados de saída do EC2.
</details>

<details>
<summary>A transferência de dados para dentro da AWS é cobrada?</summary>

Não: a AWS informa que a transferência de dados de entrada é gratuita.
</details>

<details>
<summary>Como funciona o plano gratuito do AWS Free Tier para contas novas?</summary>

A conta recebe US$ 100 em créditos, pode ganhar mais US$ 100 com atividades, e o plano termina em 6 meses ou quando os créditos acabam.
</details>


## [4.2 Modelos de compra do EC2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)

<details>
<summary>Quando usar instâncias Spot?</summary>

Quando a carga tolera interrupção e tem horário flexível, como processamento em lote e análise de dados; o desconto chega a 90%.
</details>

<details>
<summary>Qual é a diferença entre Compute Savings Plans e EC2 Instance Savings Plans?</summary>

O Compute Savings Plans vale para qualquer família, Região e sistema, e também para Fargate e Lambda (até 66%); o EC2 Instance Savings Plans exige uma família numa Região e dá até 72%.
</details>

<details>
<summary>Qual é a diferença entre uma RI Standard e uma RI Convertible?</summary>

A Standard dá o maior desconto, mas não pode ser trocada; a Convertible dá desconto menor e pode ser trocada por outra configuração durante o prazo.
</details>

<details>
<summary>Quando escolher um Dedicated Host?</summary>

Quando é preciso um servidor físico inteiro, com controle de onde as instâncias rodam, para usar licenças próprias cobradas por soquete, núcleo ou máquina virtual.
</details>

<details>
<summary>Como as RIs se comportam numa organização do AWS Organizations?</summary>

Com o faturamento consolidado, o desconto de uma RI comprada por uma conta pode ser aproveitado pelas instâncias de qualquer conta da organização.
</details>


## [4.3 Como outros recursos são cobrados](../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md)

<details>
<summary>Qual transferência de dados é gratuita?</summary>

Entrada da internet para a AWS (e dentro da mesma AZ por IP privado).
</details>

<details>
<summary>Qual transferência é cobrada?</summary>

Saída para a internet, entre regiões e entre AZs.
</details>

<details>
<summary>Um volume EBS de 500 GB com 100 GB usados é cobrado por quanto?</summary>

Pelos 500 GB provisionados.
</details>

<details>
<summary>Qual serviço não tem custo próprio?</summary>

IAM, CloudFormation, Elastic Beanstalk, Auto Scaling, Organizations.
</details>

<details>
<summary>O que é o Free Tier?</summary>

Uso gratuito limitado para experimentar serviços (sempre gratuito, por período ou testes; contas novas usam modelo de créditos).
</details>


## [4.4 Ferramentas de custo e faturamento](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)

<details>
<summary>Estimar o custo de uma arquitetura antes de criá-la.</summary>

Pricing Calculator.
</details>

<details>
<summary>Visualizar gastos dos últimos meses e prever o próximo.</summary>

Cost Explorer.
</details>

<details>
<summary>Receber alerta quando o gasto previsto passar do orçamento.</summary>

Budgets.
</details>

<details>
<summary>Relatório mais detalhado de custo e uso, por hora e recurso.</summary>

Cost and Usage Report.
</details>

<details>
<summary>Ser avisado de um gasto anormal.</summary>

Cost Anomaly Detection.
</details>

<details>
<summary>Separar custos por projeto ou departamento.</summary>

Cost allocation tags (ativadas no Billing).
</details>

<details>
<summary>Uma fatura para várias contas, com desconto por volume.</summary>

Consolidated billing no Organizations.
</details>

<details>
<summary>Comprar software de terceiros pago na fatura AWS.</summary>

AWS Marketplace.
</details>

<details>
<summary>Onde ver recomendações de Savings Plans?</summary>

Cost Explorer.
</details>


## [4.5 Planos de AWS Support](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)

<details>
<summary>Qual o plano mais barato com suporte técnico 24/7 por telefone?</summary>

Business Support+ (no modelo clássico, Business).
</details>

<details>
<summary>Qual o plano mais barato com todas as verificações do Trusted Advisor?</summary>

Business Support+ (no modelo clássico, Business).
</details>

<details>
<summary>Qual plano inclui TAM dedicado?</summary>

Enterprise.
</details>

<details>
<summary>Qual plano dá acesso a um pool de TAMs?</summary>

Enterprise On-Ramp (plano clássico, encerra em 01/01/2027).
</details>

<details>
<summary>Qual plano responde em menos de 15 minutos a um sistema crítico fora do ar?</summary>

Enterprise.
</details>

<details>
<summary>Qual plano responde em menos de 1 hora a produção fora do ar?</summary>

Business Support+ ou superior (no modelo clássico, Business).
</details>

<details>
<summary>Ambiente de testes que só precisa de ajuda técnica ocasional por e-mail.</summary>

Developer (plano clássico, encerra em 01/01/2027; no modelo atual, o plano pago de entrada é o Business Support+).
</details>

<details>
<summary>O plano Basic oferece suporte técnico?</summary>

Não; só atendimento de conta e faturamento, documentação e re:Post.
</details>

<details>
<summary>Quem ajuda com dúvidas de faturamento em planos Enterprise?</summary>

Concierge Support Team.
</details>

<details>
<summary>Quem pode mudar o plano de suporte?</summary>

🔄 Não é mais tarefa exclusiva do root (saiu da lista oficial em 10/2026): uma identidade IAM com as permissões necessárias.
</details>


## [4.6 Outros recursos de ajuda](../docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md)

<details>
<summary>Encontrar um parceiro certificado para implementar a migração.</summary>

AWS Partner Network.
</details>

<details>
<summary>Contratar consultoria diretamente da AWS.</summary>

AWS Professional Services.
</details>

<details>
<summary>Terceirizar a operação diária da infraestrutura para a AWS.</summary>

AWS Managed Services.
</details>

<details>
<summary>Tirar dúvidas técnicas com a comunidade.</summary>

AWS re:Post.
</details>

<details>
<summary>Respostas prontas para dúvidas comuns.</summary>

AWS Knowledge Center.
</details>

<details>
<summary>Startup busca créditos para começar na AWS.</summary>

AWS Activate.
</details>
