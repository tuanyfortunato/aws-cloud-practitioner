# 🃏 Flashcards — Domínio 4 — Cobrança, Preços e Suporte

Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* de cada tópico (`python3 scripts/gerar_docs.py`).

**Total:** 41 cards


## [4.1 Princípios de preço da AWS](../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md)

<details>
<summary>Qual é um princípio de preço da AWS?</summary>

Pagar conforme o uso, economizar ao se comprometer, pagar menos por unidade ao usar mais.
</details>

<details>
<summary>Quais são os três principais geradores de custo?</summary>

Computação, armazenamento e transferência de dados de saída.
</details>


## [4.2 Modelos de compra do EC2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)

<details>
<summary>Aplicação nova, sem histórico de uso, que não pode ser interrompida.</summary>

On-Demand.
</details>

<details>
<summary>Servidor de banco que roda 24/7 pelos próximos 3 anos.</summary>

Reserved Instances ou Savings Plans (3 anos, All Upfront dá o maior desconto).
</details>

<details>
<summary>Desconto com flexibilidade entre EC2, Fargate e Lambda.</summary>

Compute Savings Plans.
</details>

<details>
<summary>Processamento em lote que pode ser interrompido e reiniciado.</summary>

Spot.
</details>

<details>
<summary>Qual o aviso antes de uma Spot ser interrompida?</summary>

2 minutos.
</details>

<details>
<summary>Licença de software por núcleo físico.</summary>

Dedicated Host.
</details>

<details>
<summary>Garantir capacidade numa AZ para um evento, sem contrato longo.</summary>

On-Demand Capacity Reservation.
</details>

<details>
<summary>Qual opção de pagamento dá o maior desconto?</summary>

All Upfront.
</details>

<details>
<summary>Reservas compradas podem ser revendidas?</summary>

Sim, RIs Standard no Reserved Instance Marketplace.
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

Business.
</details>

<details>
<summary>Qual o plano mais barato com todas as verificações do Trusted Advisor?</summary>

Business.
</details>

<details>
<summary>Qual plano inclui TAM dedicado?</summary>

Enterprise.
</details>

<details>
<summary>Qual plano dá acesso a um pool de TAMs?</summary>

Enterprise On-Ramp.
</details>

<details>
<summary>Qual plano responde em menos de 15 minutos a um sistema crítico fora do ar?</summary>

Enterprise.
</details>

<details>
<summary>Qual plano responde em menos de 1 hora a produção fora do ar?</summary>

Business.
</details>

<details>
<summary>Ambiente de testes que só precisa de ajuda técnica ocasional por e-mail.</summary>

Developer.
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

O usuário root.
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
