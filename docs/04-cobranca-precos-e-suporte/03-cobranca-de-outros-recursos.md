# 4.3 Como outros recursos são cobrados

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon S3 (Simple Storage Service)](../../servicos/armazenamento/s3.md) · [Amazon EBS (Elastic Block Store) e Instance Store](../../servicos/armazenamento/ebs.md) · [AWS Lambda](../../servicos/computacao/lambda.md)

⬅️ [4.2 Modelos de compra do EC2](02-modelos-de-compra-ec2.md) · 🏠 [Índice do domínio](README.md) · [4.4 Ferramentas de custo e faturamento](04-ferramentas-de-custo.md) ➡️

---

## 📖 Conteúdo

- **Transferência de dados:**
  - **Entrada** da internet para a AWS: **grátis**.
  - **Saída** da AWS para a internet: **cobrada**, com faixas por volume.
  - Entre **regiões**: cobrada. Entre **AZs** na mesma região: cobrada.
  - Dentro da mesma AZ por IP privado: grátis. Da origem AWS para o CloudFront: grátis.
- **Armazenamento:** S3 por GB-mês, por requisição e por recuperação (nas classes IA e Glacier); EBS pelo **volume provisionado**, mesmo que não esteja cheio; EFS pelo que é usado.
- **Serverless:** Lambda por requisição e duração; DynamoDB sob demanda por leitura e escrita; Athena por dado escaneado.
- **IPv4 público:** todo endereço IPv4 público é cobrado por hora.
- **Serviços sem custo próprio** (paga só os recursos que criam): CloudFormation, Elastic Beanstalk, Auto Scaling, IAM, Organizations, consolidated billing.
- **AWS Free Tier:** tradicionalmente cobrado na prova em três tipos: **sempre gratuito** (ex.: cota mensal de requisições do Lambda), **12 meses gratuitos** para contas novas (ex.: horas de instância micro) e **testes gratuitos** de curto prazo (ex.: GuardDuty). Desde meados de 2025, contas novas recebem um modelo baseado em **créditos** com plano gratuito por tempo limitado; confira a página oficial do Free Tier.
- **Cai na prova:** "o que é sempre grátis?" = transferência de entrada e serviços como IAM; "como reduzir custo de saída para usuários globais?" = CloudFront.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).

- "Qual transferência de dados é gratuita?" → Entrada da internet para a AWS (e dentro da mesma AZ por IP privado).
- "Qual transferência é cobrada?" → Saída para a internet, entre regiões e entre AZs.
- "Um volume EBS de 500 GB com 100 GB usados é cobrado por quanto?" → Pelos 500 GB provisionados.
- "Qual serviço não tem custo próprio?" → IAM, CloudFormation, Elastic Beanstalk, Auto Scaling, Organizations.
- "O que é o Free Tier?" → Uso gratuito limitado para experimentar serviços (sempre gratuito, por período ou testes; contas novas usam modelo de créditos).

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- 🔄 **Free Tier (mudou em 15/07/2025):**
  - Contas novas escolhem **Free plan** ou **Paid plan**. Ambas recebem **US$ 100 em créditos no cadastro + até US$ 100** por atividades de onboarding (total até **US$ 200**).
  - O **Free plan** expira em **6 meses ou quando os créditos acabam** (o que vier primeiro); não gera cobrança, mas bloqueia alguns serviços caros. Para continuar, upgrade para o Paid plan.
  - **30+ serviços Always Free** continuam valendo, independentemente da idade da conta ✔️ — ex.: Lambda, DynamoDB, SQS (1 milhão de requisições), SNS (1 milhão de publicações), Step Functions, Cognito, KMS, CloudTrail, CloudFormation, Systems Manager, X-Ray, Organizations, Shield Standard.
  - ⚠️ O **Free plan** dura até 6 meses ou até acabar o crédito; os **créditos** em si podem valer por 12 meses — são coisas diferentes. Contas anteriores a 15/07/2025 seguem no modelo legado (12 meses, trials, Always Free).
  - ✔️ Confirmado em fonte oficial; atividades que liberam créditos incluem EC2, RDS, Lambda, Bedrock e Budgets.
  - ⚠️ **Na prova:** questões antigas descrevem o modelo clássico (**Always Free, 12 meses grátis, trials**); se a questão falar em créditos ou em Free plan, use o modelo novo.
- **Transferência de dados** ✔️ (AWS Architecture Blog, 10/2026): entrada da internet **grátis**; dentro da mesma AZ por IP privado (inclusive VPC Peering) **grátis**; saída para a internet, **entre regiões** e **entre AZs** **cobradas** (entre AZs, cobrada nos dois sentidos); **gateway endpoints** (S3 e DynamoDB) sem custo na mesma região. ✔️ Da origem AWS (S3, EC2, ELB) para o **CloudFront** (origin fetches): **grátis**.
- **Per-second billing** (mínimo de 60 s) também explica questões de "parar instâncias ociosas reduz custo".
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [4.2 Modelos de compra do EC2](02-modelos-de-compra-ec2.md) · 🏠 [Índice do domínio](README.md) · [4.4 Ferramentas de custo e faturamento](04-ferramentas-de-custo.md) ➡️
