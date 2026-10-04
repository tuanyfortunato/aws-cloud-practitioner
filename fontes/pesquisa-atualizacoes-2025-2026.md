# CLF-C02: detalhes de serviços AWS que caem na prova (atualização 2025-2026 para o guia de estudo)

A CLF-C02 cobra principalmente o **"qual serviço/opção resolve este cenário"**, e não números finos. Mesmo assim, um conjunto pequeno de limites, defaults e opções conceituais aparece com frequência. Esses itens são o que mais vale acrescentar ao guia, junto com as mudanças importantes de 2025-2026: Free Tier por créditos, novos planos de suporte, SQS de 1 MiB, objetos S3 de 50 TB, fim da família Snow para novos clientes e fim do AWS IQ. Em várias dessas mudanças a prova provavelmente ainda usa a versão antiga.

## TL;DR

- **O que decorar:** os "números-âncora" (Lambda 15 min/10 GB; SQS 4 dias padrão, até 14 dias, visibility timeout de 30 s; S3 com 11 noves de durabilidade e mínimos de 30/90/180 dias; Spot até 90% com aviso de 2 min; Savings Plans/RIs até 72%; tempos de resposta do suporte 24h/12h/4h/1h/15 min; Route 53 com SLA de 100%; DynamoDB com itens de 400 KB; Aurora com 15 réplicas; Multi-Attach do EBS só em io1/io2). Fora isso, o foco são as **diferenças entre serviços parecidos** e os **modos e tipos** (classes, tiers, políticas, gateways, endpoints).
- **O que mudou e pode confundir:** desde 15/07/2025 o Free Tier funciona com US$ 100 em créditos no cadastro mais até US$ 100 por atividades (até US$ 200), e o plano Free expira em 6 meses ou quando os créditos acabam, o que ocorrer primeiro (AWS What's New, 16/07/2025). Os planos de suporte agora são Basic, Business Support+, Enterprise e Unified Operations, e Developer/Business/Enterprise On-Ramp acabam em 01/01/2027. O SQS passou a aceitar mensagens de 1 MiB e o S3 objetos de 50 TB. O Snowball Edge ficou restrito a clientes existentes, o Snowmobile foi aposentado e o AWS IQ encerrou em 28/05/2026. O exam guide (versão 1.0) não foi reescrito por causa disso, então a prova tende a cobrar os nomes e valores "clássicos".
- **Recomendação:** no guia, registrar o valor clássico (o "da prova") com uma nota de atualização ao lado. Marcar como "não precisa decorar" quotas finas (ENIs, camadas Lambda, número de VIFs, preços por GB e por requisição, contagens exatas de checks do Trusted Advisor), porque a própria AWS declara fora de escopo codificação, design de arquitetura, troubleshooting, implementação e testes de carga.

## Key Findings

1. **Perfil da prova:** o exame avalia "explicar o valor da nuvem", "entender custos, economia e cobrança" e "identificar serviços AWS para casos de uso comuns". Codificação, design de arquitetura, troubleshooting, implementação e testes de carga ficam fora do escopo. Por isso, números aparecem quase sempre como **diferenciadores** (ex.: "15 min" separa Lambda de EC2/Batch; "2 minutos" identifica Spot), e não como cálculo.
2. **A lista oficial de serviços mudou nomes:** a página atual "In-Scope AWS Services" usa "Amazon Quick Sight" e "Amazon SageMaker AI". O exam guide em PDF continua citando AWS Cloud9, AWS CodeStar e CodeCommit na task 3.8, embora o Cloud9 esteja fechado para novos clientes (desde 25/07/2024) e o CodeStar tenha sido descontinuado (31/07/2024). O CodeCommit voltou a GA em 24/11/2025.
3. **Mudanças de 2025-2026 com risco de "resposta antiga"** (detalhes na seção de cada categoria): Free Tier, planos de suporte, Trusted Advisor (agora 6 categorias, com Operational Excellence), SQS e SNS com 1 MiB, S3 com 50 TB, Snow Family, AWS IQ, Timestream for LiveAnalytics fechado para novos clientes.
4. **Os simulados de referência** (Tutorials Dojo/Jon Bonso, Digital Cloud Training, jayendrapatil.com, que mantém material de estudo para certificação) já incorporaram Business Support+/Unified Operations e o fim da Snow Family. Isso indica que questões novas podem aparecer, mas o exame oficial não teve nova versão de guia.

---

## Details

### Domínio 1 – Conceitos de nuvem e infraestrutura global

**Detalhes que caem**
- **Números atuais:** a AWS informa **39 regiões geográficas e 124 AZs**, com planos anunciados de mais 2 regiões (Arábia Saudita e Chile) e 7 AZs. Cada região tem **no mínimo 3 AZs**, isoladas e fisicamente separadas. A prova não pede o número exato. Pede o conceito "região = várias AZs; AZ = um ou mais data centers".
- **Edge:** o CloudFront tem **750+ PoPs** em 100+ cidades de 50+ países, mais **1.140+ PoPs embarcados** em redes de ISPs e **15 Regional Edge Caches**. Simulados antigos falam em "400+" ou "450+ edge locations". Para a prova, basta saber que "edge locations são muito mais numerosas que regiões".
- **Critérios de escolha de região** (caem muito): conformidade e soberania de dados, latência/proximidade dos usuários, disponibilidade do serviço na região e preço (que varia por região).
- **Novidade conceitual:** existe uma região AWS European Sovereign Cloud (Brandenburg, eusc-de-east-1). É bom saber que existe, mas não precisa decorar.

**Pegadinhas**
- "Implantar em várias AZs" = alta disponibilidade/tolerância a falhas. "Várias regiões" = DR geográfico, latência global ou exigência legal. A resposta nunca é "várias edge locations" para alta disponibilidade de computação.
- Local Zones (baixa latência perto de cidades) × Wavelength (dentro de redes 5G de operadoras) × Outposts (hardware AWS no seu data center).

**Não precisa decorar:** contagem de AZs por região, códigos de região, lista de cidades de PoPs.

---

### Domínio 2 – Segurança e conformidade (complementos)

**Shield**
- **Shield Standard:** gratuito e automático, protege camadas 3/4.
- **Shield Advanced:** **US$ 3.000/mês por organização, com compromisso mínimo de 1 ano**, mais taxa de data transfer out nos recursos protegidos. Inclui camada 7 (com WAF), acesso 24/7 ao DDoS Response Team, **proteção de custo** (créditos por escalonamento causado por DDoS) e uso do WAF sem custo adicional nos recursos protegidos. A taxa cobre todas as contas da Organization.
- *Exemplo de questão:* "Empresa quer reembolso de custos de escalonamento causados por um ataque DDoS e acesso a especialistas 24/7" → **Shield Advanced**.

**WAF (preço conceitual):** cobra por Web ACL, por regra e por milhão de requisições. Não precisa decorar valores. Basta saber que é pago por uso e opera na camada 7 (SQL injection, XSS, rate-based rules, geo-blocking). Atua em CloudFront, ALB, API Gateway e AppSync. Não atua em NLB.

**Trusted Advisor (atualizado)**
- Hoje são **6 categorias**: cost optimization, performance, security, fault tolerance, service limits e **operational excellence**. Materiais antigos (incluindo o cheat sheet da Tutorials Dojo) ainda listam **5**. Se a questão listar 5, escolha as 5 clássicas.
- **Basic/Developer:** todos os checks de **Service Limits** e checks selecionados de **Security** e **Fault Tolerance**, com refresh manual. A lista clássica dos "7 core checks", que cai muito: S3 Bucket Permissions, Security Groups – Specific Ports Unrestricted, IAM Use, MFA on Root Account, EBS Public Snapshots, RDS Public Snapshots e Service Limits.
- **Business Support+/Enterprise/Unified Operations:** todos os checks, acesso via **AWS Support API** e integração com EventBridge. O Trusted Advisor Priority exige Enterprise ou superior.
- **Contagem de checks:** fontes de terceiros divergem (ex.: "56 checks grátis / 482 no total" ou "500+"). **Não decorar.**

**Detalhes de segurança que mais caem**
- **Ferramenta certa por pergunta:** "Quem fez a chamada de API?" → CloudTrail. "Como estava a configuração do recurso em tal data / está em conformidade?" → Config. "Métrica/alarme de desempenho" → CloudWatch. "Ameaça ativa (ex.: mineração de cripto, IP malicioso)" → GuardDuty. "Vulnerabilidade de software/CVE em EC2, ECR, Lambda" → Inspector. "PII em S3" → Macie. "Investigar a causa raiz de um achado" → Detective. "Painel central de achados e padrões (CIS, AWS FSBP)" → Security Hub.
- **Secrets Manager × Parameter Store:** a rotação automática nativa de credenciais (ex.: RDS) é do **Secrets Manager**. O Parameter Store guarda configurações e segredos simples sem rotação nativa.
- **KMS × CloudHSM:** "hardware single-tenant, controle exclusivo das chaves, FIPS 140 nível 3" → CloudHSM. "Chaves gerenciadas e integradas a vários serviços" → KMS.

**Não precisa decorar:** preços de WAF por regra, número de checks, nomes de todos os padrões do Security Hub.

---

### Domínio 3 – Computação

**Lambda – números confirmados (documentação AWS)**
- **Memória:** 128 MB (default e mínimo) a **10.240 MB**, em incrementos de 1 MB. A CPU é alocada **proporcionalmente** à memória. Não existe configuração separada de vCPU, e isso é pegadinha.
- **Timeout:** até **900 s (15 min)**.
- **/tmp (armazenamento efêmero):** de **512 MB a 10.240 MB**. Os 512 MB não têm custo adicional; paga-se só o que for configurado acima disso.
- **Imagem de contêiner:** até 10 GB. Até 5 layers por função. **Não decorar.**
- **Cobrança:** por número de requisições + duração em milissegundos × memória configurada. O exemplo oficial de preço usa US$ 0,20 por milhão de requisições e 1 milhão de requisições gratuitas.
- **Contas novas** têm quotas reduzidas de concorrência e memória, que a AWS aumenta automaticamente conforme o uso. Não cai, mas explica relatos de "limite de 3.008 MB" em contas novas.
- *Exemplo:* "Processar um arquivo por até 2 horas sem gerenciar servidores" → **não** é Lambda (limite de 15 min); a resposta é **Fargate/ECS ou AWS Batch**.

**EC2 – detalhes que agregam**
- **Cobrança por segundo**, com **mínimo de 60 segundos**, válida para todas as opções de compra (On-Demand, Spot, Savings Plans etc.).
- **Dedicated Host** = servidor físico inteiro para você, útil para **licenças vinculadas ao servidor** (BYOL por socket/core). Pode ser comprado On-Demand (por hora) ou via Savings Plans. Dedicated Instance = hardware dedicado sem visibilidade/controle de sockets.
- **Capacity Reservations:** garantem capacidade numa AZ sem dar desconto por si só, mas podem ser combinadas com Savings Plans ou RIs regionais.

**Modelos de compra – números confirmados**

| Opção | Desconto máx. vs On-Demand | Compromisso | Detalhe que cai |
|---|---|---|---|
| Spot | até **90%** | nenhum | pode ser interrompida com **aviso de 2 min**; Savings Plans **não** se aplicam a Spot |
| EC2 Instance Savings Plans | até **72%** | 1 ou 3 anos, US$/hora | preso a uma família de instância numa região (tamanho/SO flexíveis) |
| Compute Savings Plans | até **66%** | 1 ou 3 anos | vale para EC2 (qualquer família/região), **Fargate e Lambda** |
| Standard RI | até **72%** | 1 ou 3 anos | pode ser vendida no RI Marketplace |
| Convertible RI | até **66%** na página oficial de preços de RI (o Well-Architected SAP Lens diz 54%) | 1 ou 3 anos | permite trocar família/SO |
| Database Savings Plans | até 35% | 1 ou 3 anos | novo tipo (RDS, Aurora, DynamoDB, ElastiCache…) |
| SageMaker AI Savings Plans | até 64% | 1 ou 3 anos | — |

- **Conflito de fontes:** a AWS informa 66% na página de preços de RI e 54% no Well-Architected SAP Lens para Convertible RIs. Para a prova, basta "Convertible < Standard em desconto, porém mais flexível".
- **Opções de pagamento:** All Upfront (maior desconto) > Partial Upfront > No Upfront.
- **Pegadinha:** "carga estável 24/7 por 3 anos, menor custo, sem flexibilidade necessária" → Standard RI ou EC2 Instance SP. "Usa EC2 + Lambda + Fargate e quer flexibilidade" → **Compute Savings Plans**. "Carga tolerante a interrupção (batch, CI/CD, render)" → **Spot**.

**Não precisa decorar:** preços por hora, rede por tamanho de instância, número de ENIs por VPC, escalonamento de concorrência do Lambda (1.000 ambientes a cada 10 s).

---

### Domínio 3 – Armazenamento

**S3 – números confirmados**
- **Tamanho máximo de objeto: 50 TB, anunciado em 02/12/2025 no re:Invent 2025** (antes, 5 TB; aumento de 10x), em todas as classes e com todos os recursos. **Atenção:** a prova e os simulados quase certamente ainda usam **5 TB**. Se aparecer "5 TB" como opção e não houver "50 TB", marque 5 TB. Para uploads grandes, a resposta conceitual continua sendo **multipart upload** (e Transfer Acceleration quando a distância for o problema).
- **Durabilidade:** todas as classes têm **11 noves** (99,999999999%). A diferença entre elas está na **disponibilidade**, no número de AZs, na duração mínima e na taxa de recuperação.
- **Classe padrão:** se nada for especificado no upload, o objeto vai para **S3 Standard**.

| Classe | Disponibilidade (design) | AZs | Duração mínima | Observação de prova |
|---|---|---|---|---|
| Standard | 99,99% | ≥3 | nenhuma | sem taxa de recuperação |
| Intelligent-Tiering | 99,9% | ≥3 | (sem taxa de recuperação; cobra monitoramento) | padrão de acesso desconhecido/mutável |
| Standard-IA | 99,9% | ≥3 | 30 dias | objeto mínimo cobrado: 128 KB; taxa por GB recuperado |
| One Zone-IA | 99,5% | **1** | 30 dias | dados **recriáveis**; perde-se se a AZ for destruída |
| Glacier Instant Retrieval | (milissegundos) | ≥3 | 90 dias | acesso ~1x por trimestre |
| Glacier Flexible Retrieval | — | ≥3 | 90 dias | Expedited **1–5 min** (objetos < 250 MB), Standard **3–5 h**, Bulk **5–12 h** (gratuito) |
| Glacier Deep Archive | — | ≥3 | **180 dias** | Standard **até 12 h**, Bulk **até 48 h**; **sem Expedited**; o mais barato |

- **Fontes divergem** sobre a duração mínima do Intelligent-Tiering (algumas citam 30 dias, outras "nenhuma"). Não é cobrança típica de prova.
- *Exemplo:* "Arquivos de conformidade guardados por 7 anos, acessados raramente, recuperação em até 48 h aceitável, menor custo" → **Glacier Deep Archive**. "Imagens em miniatura que podem ser regeneradas, acesso pouco frequente, menor custo" → **One Zone-IA**.
- **Outras quotas:** a AWS anunciou suporte a até 1 milhão de buckets por conta. **Não decorar.**

**EBS – detalhes**
- **Multi-Attach:** só **io1/io2 (Provisioned IOPS SSD)**, até **16 instâncias Nitro na mesma AZ**. *Pegadinha:* "compartilhar um volume entre muitas instâncias em várias AZs" → **EFS**, não EBS.
- EBS fica preso a uma AZ. Para mover para outra AZ/região, usa-se **snapshot** (armazenado regionalmente no S3 e copiável entre regiões).

**Família Snow (mudança importante)**
- **Snowmobile** (100 PB): aposentado em 2024.
- **Snowcone:** descontinuado para novos pedidos em 12/11/2024; o suporte a clientes existentes terminou em 12/11/2025.
- **Snowball Edge:** segundo o aviso oficial na página do AWS Snowball, desde **07/11/2025** os dispositivos ficam disponíveis **só para clientes existentes**. Novos clientes devem usar **DataSync** (online), **AWS Data Transfer Terminal** (transferência física segura) ou parceiros; para computação de borda, **Outposts**. O dispositivo de migração restante é o **Snowball Edge Storage Optimized de 210 TB**, mais o Compute Optimized de 104 vCPUs para edge.
- **Para a prova:** a lista in-scope e o exam guide ainda mencionam Snowball Edge/Snowmobile. Em questão do tipo "migrar petabytes com banda limitada", **Snowball Edge** continua sendo a resposta esperada (e "exabytes/100 PB" → Snowmobile, em questões antigas).

**Não precisa decorar:** IOPS máximos por tipo de EBS, throughput de st1/sc1, tamanhos de Snowball antigos (80 TB), preços por GB.

---

### Domínio 3 – Bancos de dados

**Números confirmados**
- **DynamoDB:** item de no máximo **400 KB** (incluindo nomes e valores de atributos). *Pegadinha:* "armazenar vídeos/imagens grandes no DynamoDB" → guardar no **S3** e manter só a referência no DynamoDB.
- **Aurora:** até **15 Aurora Replicas** por cluster, além da instância primária. Um cluster secundário de Global Database pode ter até 16.
- **RDS read replicas:** até **15** por instância de origem para **MySQL, MariaDB e PostgreSQL**, das quais até 5 podem ser cross-region. Para Oracle e SQL Server, as páginas da AWS **se contradizem** (5 vs 15). Não decorar.
- **Read replica × Multi-AZ** (pegadinha clássica): read replica = **escalar leitura** (assíncrona, pode ser cross-region). Multi-AZ = **alta disponibilidade/failover** (standby síncrono que não atende leitura no modelo clássico).

**Diferenças sutis**
- Redshift (data warehouse/OLAP, SQL analítico em petabytes) × RDS/Aurora (OLTP) × Athena (SQL sem servidor direto no S3, paga por dados escaneados).
- ElastiCache (cache em memória, Redis/Valkey/Memcached) × MemoryDB (banco em memória **durável**, compatível com Redis) × DAX (cache **exclusivo** do DynamoDB, microssegundos).
- Neptune = grafos (redes sociais, recomendação, fraude). DocumentDB = documentos compatíveis com MongoDB. Keyspaces = Cassandra. Timestream = séries temporais. **Atenção:** o Timestream for LiveAnalytics foi fechado a novos clientes em 20/06/2025. Na prova, "séries temporais/IoT" ainda → Timestream.

**Não precisa decorar:** RCU/WCU por tamanho de item, limites de armazenamento por motor, versões de motor.

---

### Domínio 3 – Rede e entrega de conteúdo

**Direct Connect – números confirmados**
- **Dedicated:** portas de **1, 10, 100 e 400 Gbps**.
- **Hosted** (via parceiro): **50 Mbps até 25 Gbps**.
- **Criptografia:** **MACsec** disponível em conexões dedicadas de 10/100/400 Gbps em locais selecionados. Fora isso, a criptografia de ponta a ponta normalmente vem de **VPN IPsec sobre o Direct Connect**. *Pegadinha:* "Direct Connect criptografa por padrão?" → **não**.
- *Exemplo:* "Conexão privada, banda consistente, que não passa pela internet" → Direct Connect. "Conexão criptografada rápida de configurar, pela internet" → Site-to-Site VPN. "Funcionários remotos acessando a VPC" → **Client VPN**.

**Route 53**
- **SLA de 100%:** o SLA oficial prevê crédito para qualquer disponibilidade mensal "menor que 100%" do DNS autoritativo. A API e o console **não** entram no SLA. Na prova: "único serviço AWS com SLA de 100%" → Route 53.
- As políticas de roteamento já estão no guia. Reforçar: **Failover** usa health checks; **Geolocation** = conteúdo/regulação por país; **Latency** = menor latência; **Weighted** = testes A/B e migração gradual.

**CloudFront × Global Accelerator** (cai muito)
- CloudFront = **cache** de conteúdo (HTTP/HTTPS) nas edge locations.
- Global Accelerator = **sem cache**, 2 IPs anycast estáticos, roteia TCP/UDP pela rede global da AWS até o endpoint mais saudável. Indicado para jogos, VoIP e failover regional rápido.

**Não precisa decorar:** número de VIFs por conexão (51), regras de LAG, preços por GB, quotas de VPC/subnet.

---

### Domínio 3 – Integração de aplicações

**SQS – números confirmados**
- **Tamanho máximo de mensagem: 1 MiB desde 04/08/2025** (antes, 256 KiB), em filas Standard e FIFO, em todas as regiões comerciais e no GovCloud (US), segundo o anúncio AWS What's New de 04/08/2025. O SNS também passou a 1 MiB. **Atenção:** simulados e talvez a prova ainda usem **256 KB**. Se só houver 256 KB como opção, marque 256 KB.
- **Retenção:** default **4 dias**, mínimo **60 s**, máximo **14 dias**.
- **Visibility timeout:** default **30 s**, mínimo 0, máximo **12 h**.
- **Delay queue:** até 15 min.
- **Standard × FIFO:** Standard = throughput quase ilimitado, entrega "pelo menos uma vez" e ordem por melhor esforço. FIFO = ordem garantida e processamento exatamente uma vez.

**Diferenças sutis que caem**
- **SQS × SNS × EventBridge:** SQS = fila (pull, desacoplamento, buffer). SNS = pub/sub (push, fan-out para e-mail, SMS, Lambda, SQS). EventBridge = barramento de eventos com regras/filtragem, eventos de serviços AWS e SaaS, e agendamento (Scheduler).
- **Step Functions** = orquestração de workflows com estado e passos visuais. **SWF** é legado.

**Não precisa decorar:** in-flight messages, cobrança por blocos de 64 KB, throughput exato de FIFO.

---

### Domínio 3 – Analytics, IA/ML, IoT, ferramentas de desenvolvedor

**Analytics/IA (nomes atualizados)**
- A lista oficial in-scope usa "Amazon Quick Sight" (BI/dashboards) e "Amazon SageMaker AI" (construir/treinar/implantar modelos próprios). Na prova podem aparecer os nomes antigos QuickSight/SageMaker.
- **Bedrock** = modelos de fundação via API (IA generativa sem treinar do zero). **Amazon Q** = assistente de IA generativa (Q Developer para código, Q Business para dados corporativos).
- **Associações frase → serviço:** "texto → fala" = Polly; "fala → texto" = Transcribe; "chatbot" = Lex; "sentimento/entidades em texto" = Comprehend; "extrair texto/formulários de documentos digitalizados" = Textract (não Rekognition); "rostos/objetos em imagem e vídeo" = Rekognition; "busca inteligente em documentos corporativos" = Kendra; "traduzir" = Translate.

**Ferramentas de desenvolvedor – status atual**
- **CodeCommit:** voltou a **GA e aberto a novos clientes em 24/11/2025**, depois de ter sido fechado em 2024.
- **Cloud9:** **fechado para novos clientes** desde julho de 2024. A alternativa conceitual é o **CloudShell** (shell no navegador, já autenticado e com a CLI).
- **CodeStar:** **descontinuado** em 31/07/2024.
- Como o exam guide ainda lista Cloud9 e CodeStar, saiba o propósito de cada um: Cloud9 = IDE no navegador; CodeStar = gerenciar projetos de CI/CD.
- **AppConfig** = feature flags/configuração dinâmica de aplicações. **X-Ray** = rastreamento distribuído. **CodeArtifact** = repositório de pacotes (npm, Maven, PyPI).

**IoT:** IoT Core (conectar dispositivos e trocar mensagens MQTT) × IoT Greengrass (rodar Lambda e ML localmente no dispositivo de borda). O IoT Analytics e o IoT Events tiveram fim de suporte anunciado. Não estudar.

---

### Domínio 4 – Cobrança, preços e suporte (maior concentração de mudanças)

**Free Tier (mudou em 15/07/2025)**
- Contas criadas **a partir de 15/07/2025** escolhem entre o **Free plan** e o **Paid plan**. Ambos recebem **US$ 100 em créditos no cadastro + até US$ 100** ao concluir atividades de onboarding (ex.: usar EC2 e Bedrock), num total de até **US$ 200**.
- Segundo o anúncio AWS What's New de 16/07/2025, o **Free plan** expira em **6 meses após o cadastro ou quando os créditos do Free Tier acabam, o que ocorrer primeiro**. Não gera cobranças, mas bloqueia alguns serviços caros. Para continuar, é preciso fazer upgrade para o Paid plan.
- **30+ serviços "Always Free"** continuam valendo.
- Contas criadas **antes** de 15/07/2025 seguem no Free Tier legado (12 meses grátis, trials de curto prazo e Always Free).
- **Para a prova:** o guia CLF-C02 é anterior à mudança. Questões sobre os "três tipos de oferta do Free Tier (Always Free, 12 meses grátis, trials)" ainda podem aparecer. Responda pelo modelo clássico, a menos que a questão mencione créditos.

**Planos de suporte (reestruturados em dezembro/2025)**
- **Novos planos:** Basic (grátis), **Business Support+** (a partir de **US$ 29/mês por conta**, ou percentual do uso começando em 9%; segundo o AWS News Blog, isso é 71% a menos que o mínimo mensal do antigo Business Support), **Enterprise** (mínimo reduzido para **US$ 5.000/mês**, antes US$ 15.000; inclui TAM designado) e **Unified Operations** (a partir de **US$ 50.000/mês**).
- **Tempo de resposta crítico** (AWS News Blog): Business Support+ **30 min**, Enterprise **15 min**, Unified Operations **5 min**.
- **Tempos comuns aos planos pagos:** general guidance < 24 h; system impaired < 12 h; production system impaired < 4 h; production system down < 1 h.
- **Planos legados:** Developer, Business e Enterprise On-Ramp **encerram em 01/01/2027**. Os clientes de Enterprise On-Ramp estão sendo migrados automaticamente para Enterprise ao longo de 2026. Segundo o AWS Support User Guide, os três planos legados continuam disponíveis na região AWS GovCloud (US).
- **Para a prova:** o exam guide cobra os 5 planos clássicos. Tabela que ainda deve ser estudada: Developer = horário comercial, e-mail, < 24 h/< 12 h. Business = 24/7, telefone/chat, produção fora do ar < 1 h, todos os checks do Trusted Advisor, Support API. Enterprise On-Ramp = crítico < 30 min, pool de TAMs, Concierge. Enterprise = crítico < 15 min, TAM designado, IEM, Concierge.
- *Exemplo:* "Menor plano com TAM designado e resposta de 15 min" → **Enterprise** (válido no modelo antigo e no novo). "Menor custo com resposta < 1 h para produção fora do ar" → **Business** (clássico) / Business Support+ (novo).

**Outros detalhes de cobrança que agregam**
- **Per-second billing** (mínimo de 60 s) também afeta questões de "parar instâncias ociosas reduz custo".
- **Shield Advanced** (US$ 3.000/mês, 1 ano) e **Enterprise** (US$ 5.000 mínimo) aparecem como "custo fixo alto". Na prova, a resposta "mais barata" raramente é um desses.
- **AWS Marketplace:** comprar software de terceiros (AMIs, SaaS) e **serviços profissionais**. Com o fim do **AWS IQ (28/05/2026)**, o AWS IQ User Guide recomenda o **AWS Marketplace Professional Services** como substituto (o mesmo guia informa que novos cadastros de especialistas pararam em 20/05/2025). A lista in-scope e o exam guide ainda citam o AWS IQ como "contratar freelancers/consultorias certificadas AWS sob demanda". Se aparecer na prova, essa é a resposta.

---

## Recommendations

1. **Para cada mudança recente, crie no guia uma linha "Valor na prova × Valor atual":** S3 5 TB → 50 TB; SQS 256 KB → 1 MiB; Free Tier 12 meses → créditos de US$ 200/6 meses; 5 planos de suporte → Basic/Business Support+/Enterprise/Unified Operations; Trusted Advisor 5 → 6 categorias; Snowball/Snowmobile → DataSync/Data Transfer Terminal; AWS IQ → Marketplace Professional Services; Cloud9 → CloudShell. A regra prática é responder com a opção que existe entre as alternativas, priorizando o modelo do exam guide.
2. **Organize os números em "âncoras de decisão"**, não em tabelas soltas. Exemplos: "> 15 min" → não é Lambda; "2 min de aviso" → Spot; "1 AZ / recriável" → One Zone-IA; "180 dias / 48 h" → Deep Archive; "16 instâncias mesma AZ" → EBS Multi-Attach io1/io2; "100% SLA" → Route 53; "400 KB" → DynamoDB não guarda blobs; "15 réplicas" → Aurora; "US$ 3.000/mês" → Shield Advanced.
3. **Acrescente uma seção "Não precisa decorar"** com: preços unitários (US$/GB, US$/requisição, US$/regra), quotas de ENI/VIF/LAG/camadas Lambda, contagem exata de checks do Trusted Advisor, IOPS/throughput por tipo de EBS, contagem exata de regiões/AZs/PoPs, limites de Oracle/SQL Server em read replicas e detalhes de rede da Lambda.
4. **Use simulados atualizados com cautela:** quando um simulado de 2026 marcar "Business Support+" ou "Unified Operations", trate como conhecimento atual. Ainda assim, revise os 5 planos clássicos, porque o exam guide oficial continua na versão 1.0.

## Caveats

- **Defasagem entre o exame e a realidade:** a AWS não publicou nova versão do guia CLF-C02 refletindo as mudanças de 2025-2026. Não há confirmação pública de que o banco de questões foi atualizado. As recomendações de "responder pelo modelo clássico" são inferência, não regra oficial.
- **Fontes conflitantes, registradas sem escolher um lado:** desconto máximo de Convertible RIs (66% × 54%), limite de read replicas para Oracle/SQL Server (5 × 15), número de checks do Trusted Advisor (vários números em fontes de terceiros) e duração mínima do Intelligent-Tiering.
- **Contagens que mudam rápido:** regiões/AZs (39/124 em setembro de 2026) e PoPs (750+) devem ser tratadas como aproximações. Muitos artigos de terceiros sobre Free Tier, suporte e Shield são blogs comerciais. Os números citados aqui foram mantidos quando coincidem com as páginas oficiais da AWS ou com várias fontes concordantes.
- **Relatos de aprovados** (Medium, dev.to) costumam citar temas amplos (serviços e casos de uso, responsabilidade compartilhada, CAF, Well-Architected, modelos de preço do EC2, planos de suporte, VPC), e não números específicos. Isso confirma que os números são diferenciadores, não o núcleo da prova.