# Auditoria de cobertura e aprofundamento — CLF-C02

<!-- didatico:inicio -->
## 🧭 Antes de ler

**Por que esta página existe?** Você precisa saber o que foi conferido no material e quais limites essa revisão tem, em vez de assumir que uma lista de arquivos prova domínio do exame.

**Como usar?** Esta página documenta a revisão realizada, sua cobertura e suas ressalvas. Ela serve para acompanhar a qualidade do material; não é uma aula sobre um serviço.

**Exemplo:** Use a auditoria para localizar a revisão de um tema e depois leia sua explicação. Um tópico coberto ainda pode precisar de estudo e confirmação de entendimento.
<!-- didatico:fim -->

Revisão iniciada em **04/10/2026**, a partir do commit `1bdfdbff098dc1648c633fb86c39ff6f968a4b85`.

A data identifica a consulta; não assegura que páginas e ofertas permanecerão iguais até sua prova.

## Resultado

O repositório tem **cobertura temática ampla dos quatro domínios e das 19 tasks oficiais**, distribuída em

41 tópicos e 105 fichas de serviços/famílias. Não foi identificado um domínio ou categoria inteira ausente.

Isso não prova que cada possibilidade de questão esteja coberta: a própria AWS declara que o guia e as listas

não são exaustivos. Não é correto prometer “100% do que cairá”.

O material original já tinha analogias, configurações, comparações e questões. A profundidade era desigual:

algumas fichas explicavam detalhadamente componentes, e outras se concentravam em associação de nome e função.

Faltava um caminho uniforme para explicar a sequência de uso, pré-requisitos e o sentido de “pode/não pode”.

## Cobertura por domínio

| Domínio oficial | Tasks | Tópicos locais | Cobertura encontrada e aprofundamento |
|---|---|---|---|
| 1 — Conceitos de nuvem | 1.1–1.4 | 7 | Benefícios, arquitetura, seis pilares, CAF, migração e economia; decisões e exemplos sobre limites de cada conceito |
| 2 — Segurança e conformidade | 2.1–2.4 | 10 | Responsabilidades, root, IAM/federação, criptografia, compliance, logs e proteção; separação de rede, autorização, detecção e correção |
| 3 — Tecnologia e serviços | 3.1–3.8 | 18 | Acesso, infraestrutura, compute, banco, rede, armazenamento, analytics/IA e outras categorias; recursos e fluxo de uso sem depender da tela |
| 4 — Cobrança, preços e suporte | 4.1–4.3 | 6 | Compras, custos, relatórios, suporte e recursos de ajuda; custo residual, compromissos, alertas e primeira resposta |

A ligação de **cada task** aos arquivos está em [Escopo oficial](escopo-oficial.md).

A numeração local é editorial: tópico local 3.7 (bancos) não é task oficial 3.7 (IA/analytics).

## Categorias da lista oficial e onde estão

| Categoria oficial | Local de estudo e observação |
|---|---|
| Analytics | [Fichas](../../servicos/README.md): Athena, EMR, Glue, Kinesis, OpenSearch, Quick Sight; Redshift está na pasta de bancos |
| Application Integration | EventBridge, SNS, SQS e Step Functions nas fichas de integração |
| Business Applications | Connect e SES nas fichas de aplicações |
| Cloud Financial Management | Budgets, Cost Explorer, CUR/Data Exports; Marketplace em recursos de ajuda |
| Compute | Batch, EC2, Beanstalk, Lightsail e Outposts em computação |
| Containers | ECR, ECS e EKS em computação |
| Customer Enablement | AWS Support em custos/suporte |
| Database | Aurora, DocumentDB, DynamoDB, ElastiCache, Neptune e RDS em bancos |
| Developer Tools | CLI, CodeBuild, CodePipeline e X-Ray em desenvolvimento |
| End User Computing | WorkSpaces, AppStream e Secure Browser na ficha conjunta |
| Frontend Web and Mobile | Amplify na ficha de aplicações |
| Internet of Things | IoT Core na ficha de IoT; separar Greengrass fora do escopo |
| Machine Learning | APIs prontas, Amazon Q e SageMaker AI em IA/ML |
| Management and Governance | Auto Scaling, CloudFormation, CloudTrail, CloudWatch, Config, Organizations e demais em computação/gerenciamento; Console na ficha de acesso; Well-Architected Tool no tópico 1.4 e ficha de utilitários |
| Migration and Transfer | Discovery, MGN, DMS, Evaluator, Hub e SCT em migração |
| Networking and Content Delivery | API Gateway, CloudFront, Direct Connect, Global Accelerator, PrivateLink, Route 53, Transit Gateway, VPC e modalidades VPN em redes |
| Security, Identity, and Compliance | Identidade, chaves, proteção, detecção e documentos em segurança; RAM em gerenciamento |
| Serverless | Fargate e Lambda em computação |
| Storage | Backup, EBS, EFS, DRS, FSx, S3/Glacier e Storage Gateway em armazenamento |

“Coberto numa ficha conjunta” não significa uma ficha independente para cada nome.

As 105 fichas incluem extras e cinco arquivos de famílias fora do escopo. Não são 105 serviços obrigatórios da prova.

## Correções e limites identificados

| Encontrado | Tratamento nesta revisão | Evidência oficial |
|---|---|---|
| “O guia atual cobra os planos novos” | Removida a certeza. Guia consultado cita Developer, Business, Enterprise On-Ramp e Enterprise; página comercial apresenta Business Support+, Enterprise e Unified Operations. Estudar os dois com contexto. **Atualização de 06/10/2026:** a task 4.3 passou a citar Basic Support, Business Support+, Enterprise Support e Unified Operations, os mesmos planos da página comercial | [Task 4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html), [planos comerciais](https://aws.amazon.com/premiumsupport/plans/) |
| “700 é cerca de 70%” | Explicada a nota escalonada; meta de acerto em simulado é editorial | [Resultados da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) |
| Escolher alternativa só porque contém um valor atual ou um serviço no escopo | Enfatizada leitura do requisito/contexto; listas não são regra universal de eliminação | [Guia](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html), [lista no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html) |
| “Lambda nunca ultrapassa 15 minutos” e “nada quando não executa” | Delimitado o caso de funções convencionais e cobrança base. Durable Functions/MicroVMs e capacidade provisionada exigem contexto próprio | [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), [Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), [preços](https://aws.amazon.com/lambda/pricing/) |
| Um único máximo do S3 como se toda forma de upload fosse igual | Diferenciados PUT simples, console e multipart; não sugerida memorização descontextualizada | [Uploads S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) |
| Risco de generalizar RDS Multi-AZ | Diferenciado standby de DB instance de modalidades de cluster que podem ter leitores | [Multi-AZ DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html) |
| “Detectar”, “permitir” e “corrigir” misturados | Fichas separam achado, autorização, configuração e ação operacional | [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html), [Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html), [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) |

Os relatórios antigos em `fontes/` permanecem como registros históricos, sem edição.

Quando houver divergência, esta revisão informa a leitura mais recente e suas fontes; um lançamento comercial

não permite deduzir a data em que uma questão de certificação será alterada.

## O que foi acrescentado

**41 aprofundamentos**, cada um com funcionamento, decisão, limite e exercício com resposta comentada.

**105 fichas práticas**, cada uma com recursos, escolhas, sequência, capacidade condicional, limite e caso comentado.

Um [roteiro sem console](estudar-sem-console.md) com modelo de raciocínio e exemplo integrado.

Cobertura obrigatória no gerador: falha se houver tópico/ficha sem aprofundamento ou registro extra sem destino.

Os exemplos não acrescentam preços voláteis nem novas promessas de SLA.

As fichas mantêm sua documentação oficial e usam seus fundamentos já descritos; esta revisão fez consultas

diretas adicionais para os pontos corrigidos e comparações centrais. Não é uma revalidação linha a linha de

todas as datas, quotas, preços e anúncios históricos presentes nas fontes.

## Lacunas que ainda exigem estudo externo

| Limite | Consequência prática |
|---|---|
| Um simulado de 65 questões, reutilizado por domínio | Repetir o mesmo banco pode medir memória da resposta; complemente com questões inéditas |
| Novos exercícios discursivos não entram no banco de múltipla escolha | Use-os para explicar decisões; o treino cronometrado continua no simulado existente |
| Sem experiência prática obrigatória | Suficiente para aprender seleção conceitual; não comprova habilidade de operar produção |
| Listas não exaustivas e páginas sujeitas a mudança | Consulte o guia antes da prova; não há garantia de cobertura de todas as questões |
| Preços, disponibilidade e limites variam | Para implantar, verifique a documentação específica da região/modalidade e a página atual de preço |

## Verificação das alterações

Geração de 41 tópicos, 302 flashcards e índice de 105 fichas concluída.

Geração do simulado de 65 questões concluída.

Cada um dos 41 tópicos e das 105 fichas contém exatamente um bloco de aprofundamento.

Repetir o gerador não altera o conteúdo produzido (idempotência verificada por hash).

Anotações e complementos foram preservados em um teste de regeneração, com restauração do arquivo ao final.

Verificador de links relativos terminou sem destinos quebrados; ele não valida conteúdo de URLs externas nem âncoras.

Diff conferido sem erros de whitespace.

## Fontes do escopo

[Guia CLF-C02](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)

[Domínio 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html)

[Domínio 2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html)

[Domínio 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html)

[Domínio 4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html)

[Serviços no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html)

[Serviços fora do escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)

[Voltar ao índice](../../README.md)
