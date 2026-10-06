<!-- autoral -->

# Pares que confundem

Muitas questões da prova oferecem dois serviços vizinhos como alternativas. Os dois parecem resolver o problema, e só um atende ao requisito do enunciado. Esta página junta esses pares em uma linha cada, agrupados pelo assunto, com a aula que explica a diferença.

Use a tabela para revisar, não para aprender. Se uma linha não fizer sentido, volte à aula indicada: lá a diferença aparece com o problema que cada serviço resolve e com o limite de cada um.

## Conceitos de nuvem

| Par | Diferença | Aula |
|---|---|---|
| Escalabilidade e elasticidade | Escalabilidade é conseguir crescer; elasticidade é crescer e encolher sozinho, acompanhando a demanda | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| Escala vertical e horizontal | Vertical é trocar por uma instância maior; horizontal é acrescentar mais instâncias | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| RTO e RPO | RTO é quanto tempo o sistema pode ficar fora do ar; RPO é quantos dados, medidos em tempo, podem ser perdidos | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| Replicação e backup | A réplica copia também uma exclusão por engano; só uma cópia anterior desfaz o erro | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| Rehost, replatform e refactor | Rehost move sem mudar; replatform faz ajustes pequenos, como trocar o banco próprio pelo RDS; refactor reescreve a aplicação para a nuvem | [1.6](../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md) |
| Região, zona de disponibilidade e local de borda | A Região é uma área geográfica com três ou mais zonas; a zona é um ou mais datacenters independentes; o local de borda fica perto do usuário e atende o CloudFront e o Route 53 | [3.2](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| Outposts, Local Zones e Wavelength | Outposts leva a AWS ao local do cliente; Local Zones, para perto de grandes cidades; Wavelength, para a rede das operadoras. Na lista da prova, só o Outposts está no escopo | [3.2](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) |

## Segurança e conformidade

| Par | Diferença | Aula |
|---|---|---|
| Usuário do IAM e função do IAM | O usuário tem credencial de longo prazo; a função entrega credenciais temporárias a quem a assume | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| IAM Identity Center e Cognito | O Identity Center dá aos funcionários acesso às contas e aplicações com um único login; o Cognito cuida do login dos usuários de um aplicativo | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| Organizations e Control Tower | O Organizations agrupa contas, aplica SCPs e junta a fatura; o Control Tower monta sobre ele um ambiente de várias contas já com controles | [2.4](../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md) |
| KMS e CloudHSM | O KMS gerencia as chaves por você; o CloudHSM dá um HSM dedicado, com usuários administrados pelo cliente | [2.5](../docs/02-seguranca-e-conformidade/05-criptografia.md) |
| Secrets Manager e Parameter Store | Os dois guardam segredos fora do código; só o Secrets Manager faz rotação automática. O Parameter Store tem parâmetros padrão sem cobrança adicional | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| Artifact e Audit Manager | O Artifact entrega os relatórios de conformidade da própria AWS; o Audit Manager coleta evidências da sua conta, mas está em modo de manutenção e fora da lista da prova | [2.6](../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md) |
| CloudTrail e CloudWatch | O CloudTrail registra quem fez qual chamada de API; o CloudWatch acompanha métricas, logs e alarmes | [2.7](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| CloudTrail e Config | O CloudTrail registra as ações; o Config registra como cada recurso estava configurado ao longo do tempo e se segue as regras | [2.7](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| Security group e ACL de rede | O security group protege o recurso, só tem regras de permissão e lembra as conexões (*stateful*); a ACL protege a sub-rede, permite e nega e não lembra as conexões (*stateless*) | [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) |
| Shield e WAF | O Shield protege contra DDoS; o WAF lê cada pedido HTTP e bloqueia padrões como injeção de SQL e XSS | [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) |
| WAF e Firewall Manager | O WAF aplica regras numa aplicação; o Firewall Manager aplica as mesmas regras em todas as contas da organização | [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) |
| GuardDuty e Inspector | O GuardDuty detecta atividade suspeita nos registros; o Inspector procura vulnerabilidades de software em EC2, imagens de contêiner e Lambda | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| GuardDuty e Detective | O GuardDuty detecta; o Detective ajuda a investigar a causa raiz | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| Macie e Inspector | O Macie encontra dados sensíveis no S3; o Inspector encontra software vulnerável | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| Security Hub e Trusted Advisor | O Security Hub reúne os achados de segurança de vários serviços; o Trusted Advisor recomenda boas práticas de custo, segurança, desempenho e outras categorias | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |

## Computação

| Par | Diferença | Aula |
|---|---|---|
| Lambda e Fargate | O Lambda roda funções disparadas por eventos, por até 15 minutos; o Fargate roda contêineres sem que você administre servidores | [3.5](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) |
| ECS e EKS | O ECS é o orquestrador de contêineres da própria AWS; o EKS roda Kubernetes | [3.5](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) |
| ECS ou EKS e Fargate | O ECS e o EKS decidem onde e quantos contêineres rodam; o Fargate é onde eles rodam sem instâncias para administrar | [3.5](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) |
| Elastic Beanstalk e CloudFormation | O Beanstalk recebe o código e monta o ambiente para rodá-lo; o CloudFormation descreve qualquer infraestrutura como código | [3.1](../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) e [3.6](../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) |
| Elastic Beanstalk e Lightsail | O Beanstalk gerencia um ambiente que escala; o Lightsail reúne servidor, banco e rede em planos de preço mensal previsível | [3.6](../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) |
| Dedicated Host e Dedicated Instance | O Host dá o servidor físico inteiro, com visibilidade de soquetes e núcleos para licenças; a Instance roda em hardware exclusivo, sem esse controle | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |

## Armazenamento e bancos de dados

| Par | Diferença | Aula |
|---|---|---|
| EBS, EFS e S3 | O EBS é o disco de uma instância; o EFS é uma pasta compartilhada por várias instâncias Linux; o S3 guarda objetos acessados por API | [3.9](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| EBS e instance store | O EBS guarda os dados quando a instância para; o instance store é temporário e perde os dados quando a instância para | [3.9](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| EFS e FSx | O EFS serve arquivos por NFS para Linux; o FSx oferece sistemas de arquivos conhecidos, como o Windows File Server (SMB) e o NetApp ONTAP | [3.9](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| DataSync e família Snow | O DataSync copia dados pela rede; a família Snow levava dados em dispositivos físicos e não está mais disponível para clientes novos | [3.17](../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) |
| RDS Multi-AZ e réplica de leitura | O Multi-AZ mantém uma cópia pronta para assumir se a principal falhar; a réplica de leitura recebe consultas e alivia a principal | [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) |
| RDS e Aurora | O RDS gerencia vários motores, inclusive comerciais; o Aurora é o motor relacional da AWS que funciona com MySQL e PostgreSQL, com armazenamento copiado em três zonas | [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) |
| RDS e DynamoDB | O RDS é relacional, com SQL e junções entre tabelas; o DynamoDB é NoSQL de chave e valor e escala sem servidor para administrar | [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) |
| RDS e Redshift | O RDS atende as transações do dia a dia; o Redshift é um data warehouse para análise de grandes volumes | [3.7](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) |

## Rede, integração e análise de dados

| Par | Diferença | Aula |
|---|---|---|
| Internet Gateway e NAT Gateway | O Internet Gateway liga a sub-rede pública à internet nos dois sentidos; o NAT Gateway deixa a sub-rede privada sair sem aceitar conexões de fora | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| VPC Peering e Transit Gateway | O peering liga duas VPCs, sem passar tráfego adiante; o Transit Gateway é um ponto central para muitas VPCs e redes locais | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| Site-to-Site VPN e Direct Connect | A VPN cifra o tráfego pela internet e se monta rápido; o Direct Connect é uma conexão física dedicada, que não passa pela internet | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| Route 53 e CloudFront | O Route 53 responde para onde ir (DNS); o CloudFront entrega o conteúdo e guarda cópias perto do usuário | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| CloudFront e Global Accelerator | O CloudFront guarda conteúdo em cache; o Global Accelerator não guarda nada e dá dois IPs estáticos que levam o tráfego TCP ou UDP pela rede da AWS | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| Athena e Redshift | O Athena consulta com SQL os dados que já estão no S3 e cobra pelos dados lidos; o Redshift é um data warehouse com os dados carregados nele | [3.11](../docs/03-tecnologia-e-servicos/11-analytics.md) |
| Glue e EMR | O Glue prepara dados sem servidor e mantém o catálogo; o EMR roda clusters de ferramentas como Spark e Hadoop | [3.11](../docs/03-tecnologia-e-servicos/11-analytics.md) |
| Kinesis e SQS | O Kinesis guarda um fluxo contínuo que várias aplicações leem e releem; o SQS guarda mensagens até um consumidor processar e apagar cada uma | [3.11](../docs/03-tecnologia-e-servicos/11-analytics.md) e [3.13](../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) |
| SQS e SNS | O SQS é uma fila, e o consumidor busca as mensagens; o SNS publica num tópico e empurra para todos os assinantes | [3.13](../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) |
| SNS e EventBridge | O SNS entrega a mesma mensagem a todos os assinantes; o EventBridge encaminha cada evento por regras, inclusive eventos de aplicações SaaS | [3.13](../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) |
| EventBridge e Step Functions | O EventBridge reage a um evento e o encaminha; o Step Functions coordena as etapas de um processo em ordem | [3.13](../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) |
| SNS e SES | O SNS manda notificações curtas, inclusive por SMS; o SES envia e recebe e-mails em volume | [3.14](../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md) |
| WorkSpaces e WorkSpaces Applications (antigo AppStream 2.0) | O WorkSpaces entrega um desktop inteiro; o WorkSpaces Applications transmite só a aplicação | [3.14](../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md) |
| Application Migration Service e DMS | O MGN migra servidores inteiros; o DMS migra os dados de um banco | [3.17](../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) |
| DMS e SCT | O DMS move os dados; a SCT converte o esquema quando o banco muda de motor | [3.17](../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) |

## Custos e suporte

| Par | Diferença | Aula |
|---|---|---|
| Reserved Instances e Savings Plans | A reserva se prende a uma configuração de instância; o Savings Plan é um compromisso de gasto por hora e vale para mais de um tipo de uso | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| Pricing Calculator e Cost Explorer | A Calculator estima antes de usar; o Cost Explorer analisa e projeta o gasto real | [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| Cost Explorer e Budgets | O Cost Explorer analisa; o Budgets avisa quando o gasto passa de um limite e pode disparar ações | [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| Cost Explorer e Cost and Usage Report | O Cost Explorer mostra gráficos e filtros; o CUR entrega os dados completos de uso e custo | [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| Business Support+, Enterprise Support e Unified Operations | Resposta a casos críticos em 30, 15 e 5 minutos; o Enterprise tem gerente técnico de conta (TAM) designado, e o Unified Operations acrescenta monitoramento contínuo pela AWS | [4.5](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) |
| Professional Services e parceiros da APN | Os dois ajudam em projetos: o Professional Services é a equipe da própria AWS; a APN reúne empresas parceiras | [4.6](../docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md) |

## Fontes oficiais

Cada linha resume a aula indicada, e cada aula lista as páginas oficiais da AWS que confirmam a diferença, com a data da verificação. Os nomes e as situações dos serviços seguem o [escopo oficial](../docs/00-guia-do-exame/escopo-oficial.md) e [o que mudou em 2025 e 2026](../docs/00-guia-do-exame/atualizacoes-2025-2026.md), conferidos em 06/10/2026.

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Acrescente aqui os pares que você trocou nas questões. -->
<!-- notas:fim -->
