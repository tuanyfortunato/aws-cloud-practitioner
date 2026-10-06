# 4.3 Como outros recursos são cobrados

## 🧠 Antes de começar

**Qual é a dificuldade?** Parar a computação ou reduzir visitas não elimina necessariamente os custos de dados armazenados e comunicações.

**A ideia em palavras simples:** A cobrança pode envolver armazenamento, requisições, endereços e transferências, além da execução. Cada recurso precisa ser analisado separadamente.

**Exemplo do dia a dia:** A escola para uma máquina de testes, mas mantém volumes e cópias de dados. Esses recursos podem continuar tendo custo.

**O que não concluir?** Não aplique a regra de um serviço a todos os outros. Identifique qual recurso permanece e qual condição gera cobrança.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Provisionado** | o tamanho que você reservou, usado ou não. |
| **Free Tier** | uso gratuito oferecido pela AWS, com limites. |

---

> **Domínio 4 — Cobrança, Preços e Suporte (12%)**

> 🔎 **Fichas detalhadas:** [Amazon S3 (Simple Storage Service)](../../servicos/armazenamento/s3.md) · [Amazon EBS (Elastic Block Store) e Instance Store](../../servicos/armazenamento/ebs.md) · [AWS Lambda](../../servicos/computacao/lambda.md)

⬅️ [4.2 Modelos de compra do EC2](02-modelos-de-compra-ec2.md) · 🏠 [Índice do domínio](README.md) · [4.4 Ferramentas de custo e faturamento](04-ferramentas-de-custo.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.
- **provisionado:** Recurso ou capacidade já disponibilizado para uso. Em algumas cobranças, a disponibilidade mantida importa mesmo sem execução de trabalho de negócio.

Veja a aplicação como um conjunto de recursos cobrados separadamente. A máquina executa, o volume conserva dados, a cópia protege recuperação e a rede move informações. Parar uma parte não necessariamente encerra as outras.

Procure o que permanece provisionado ou conservado. Isso explica por que limpar um ambiente exige revisar recursos associados, e não apenas desligar o programa. Confira as condições de cada serviço, sem aplicar uma regra universal de transferência ou armazenamento.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como um **estacionamento**: entrar é grátis, mas você paga para sair — e quanto mais carros saem, menor o preço por carro (faixas de volume).

</details>

## 2. Conceitos e opções explicados

**Transferência de dados:**

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

  - **Entrada** da internet para a AWS: **grátis**.

  - **Saída** da AWS para a internet: **cobrada**, com faixas por volume.
**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.

  - Entre **regiões**: cobrada. Entre **AZs** na mesma região: cobrada.
**Antes de ler este trecho:**

- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.

  - Dentro da mesma AZ por IP privado: grátis. Da origem AWS para o CloudFront: grátis.
**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **EFS:** O EFS oferece um sistema de arquivos compartilhado.
- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.

**Armazenamento:** S3 por GB-mês, por requisição e por recuperação (nas classes IA e Glacier); EBS pelo **volume provisionado**, mesmo que não esteja cheio; EFS pelo que é usado.

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.

**Serverless:** Lambda por requisição e duração; DynamoDB sob demanda por leitura e escrita; Athena por dado escaneado.

**Antes de ler este trecho:**

- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.

**IPv4 público:** todo endereço IPv4 público é cobrado por hora.

**Antes de ler este trecho:**

- **Elastic Beanstalk:** O Elastic Beanstalk ajuda a implantar aplicações em plataformas compatíveis, provisionando e coordenando recursos AWS para esse ambiente.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.

**Serviços sem custo próprio** (paga só os recursos que criam): CloudFormation, Elastic Beanstalk, Auto Scaling, IAM, Organizations, consolidated billing.

**Antes de ler este trecho:**

- **GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.

**AWS Free Tier:** tradicionalmente cobrado na prova em três tipos: **sempre gratuito** (ex.: cota mensal de requisições do Lambda), **12 meses gratuitos** para contas novas (ex.: horas de instância micro) e **testes gratuitos** de curto prazo (ex.: GuardDuty). Desde meados de 2025, contas novas recebem um modelo baseado em **créditos** com plano gratuito por tempo limitado; confira a página oficial do Free Tier.

**Cai na prova:** "o que é sempre grátis?" = transferência de entrada e serviços como IAM; "como reduzir custo de saída para usuários globais?" = CloudFront.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** Volume provisionado, cópias, requests e transferência geram consumo mesmo quando a aplicação principal está parada. Armazenamento arquivado pode ter permanência mínima e custo de recuperação.

**Depois, compare as escolhas:** Revise computação, armazenamento, rede, observabilidade e compromissos separadamente. Compare entrada/saída, entre AZs e entre regiões; consulte exceções por serviço.

**Por fim, verifique o limite:** Não use regras absolutas como toda transferência interna é gratuita ou parar tudo zera a conta. Free Tier depende de conta, oferta, limites e modalidade atual.

## 4. Caso resolvido

Uma equipe apaga EC2, mas mantém snapshots e objetos S3. Esses dados deixam de ser cobrados?

**Raciocínio e resposta:** Não. São recursos independentes que persistem e continuam sujeitos a cobrança. Excluir a computação não exclui necessariamente cópias e dados.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Saber o que é **grátis** e o que é **pago** na transferência de dados.
- [ ] Saber que o **EBS** cobra pelo volume **provisionado**, mesmo vazio.
- [ ] Citar serviços **sem custo próprio** (CloudFormation, Elastic Beanstalk, Auto Scaling, IAM, Organizations).
- [ ] Reconhecer os tipos de **Free Tier**.

**Dica de revisão para a prova:** "Sempre grátis" → **transferência de entrada** e serviços como **IAM**. "Reduzir custo de saída para usuários globais" → **CloudFront**. "Serviço grátis, paga os recursos" → CloudFormation/Beanstalk/Auto Scaling.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).
**Pergunta:** "Qual transferência de dados é gratuita?"

**Resposta curta:** Entrada da internet para a AWS (e dentro da mesma AZ por IP privado).

**Pergunta:** "Qual transferência é cobrada?"

**Resposta curta:** Saída para a internet, entre regiões e entre AZs.

**Pergunta:** "Um volume EBS de 500 GB com 100 GB usados é cobrado por quanto?"

**Resposta curta:** Pelos 500 GB provisionados.

**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.

**Pergunta:** "Qual serviço não tem custo próprio?"

**Resposta curta:** IAM, CloudFormation, Elastic Beanstalk, Auto Scaling, Organizations.

**Pergunta:** "O que é o Free Tier?"

**Resposta curta:** Uso gratuito limitado para experimentar serviços (sempre gratuito, por período ou testes; contas novas usam modelo de créditos).

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
