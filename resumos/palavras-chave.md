<!-- autoral -->

# Palavras-chave do enunciado

O enunciado de uma questão costuma trazer uma expressão que decide a resposta. "Quem fez a chamada de API" aponta para o CloudTrail; "pode ser interrompida" aponta para instâncias Spot. Reconhecer essas expressões economiza tempo, mas não substitui a leitura: a mesma palavra pode vir acompanhada de um requisito que muda a escolha.

A prova pode ser feita em português ou em inglês, e muitos materiais oficiais só existem em inglês. Por isso a tabela traz a expressão nos dois idiomas, quando o termo em inglês é o que aparece com mais frequência.

## Como usar esta página

Leia a expressão e tente dizer o serviço antes de olhar a segunda coluna. Depois confira a aula: se você acertou o serviço mas não sabe explicar por que a alternativa vizinha não serve, a [página de pares que confundem](comparativos.md) mostra a diferença.

## Requisitos gerais

| Se o enunciado diz | Pense em | Aula |
|---|---|---|
| "Menor esforço operacional", "totalmente gerenciado" (*least operational overhead*, *fully managed*) | Um serviço gerenciado ou sem servidor, como Lambda, Fargate, DynamoDB ou Aurora | [3.5](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) |
| "Mais econômico" (*most cost-effective*) | A opção mais barata que ainda atende a todos os requisitos | [4.1](../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md) |
| "Alta disponibilidade" (*highly available*) | Recursos em mais de uma zona de disponibilidade | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| "Recuperação de desastre em outra Região" | Backups e réplicas entre Regiões | [1.3](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) |
| "Desacoplar" (*decouple*) | SQS, SNS ou EventBridge | [3.13](../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) |
| "Aumentar e diminuir com a demanda" | Elasticidade, com o EC2 Auto Scaling | [3.4](../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) |

## Segurança

| Se o enunciado diz | Pense em | Aula |
|---|---|---|
| "Quem fez a chamada de API", "trilha de auditoria" (*audit trail*) | CloudTrail | [2.7](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| "Histórico de configuração", "recurso fora da regra" | Config | [2.7](../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| "Atividade suspeita", "detecção de ameaças" | GuardDuty | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| "Vulnerabilidades", "CVE" | Inspector | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| "Dados pessoais no S3" (*PII*) | Macie | [2.9](../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) |
| "Relatórios de conformidade da AWS", "SOC", "PCI" | Artifact | [2.6](../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md) |
| "DDoS" | Shield | [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) |
| "Injeção de SQL", "cross-site scripting" | WAF | [2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) |
| "Credenciais temporárias" | Função do IAM | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| "Login único para os funcionários" (*single sign-on*) | IAM Identity Center | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| "Rotacionar segredos" | Secrets Manager | [2.3](../docs/02-seguranca-e-conformidade/03-iam.md) |
| "Impedir que qualquer conta da organização faça algo" | SCP do AWS Organizations | [2.4](../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md) |

## Serviços e infraestrutura

| Se o enunciado diz | Pense em | Aula |
|---|---|---|
| "Fluxo de dados em tempo real" (*real-time streaming*) | Kinesis | [3.11](../docs/03-tecnologia-e-servicos/11-analytics.md) |
| "Consultar com SQL os dados no S3, sem servidor" | Athena | [3.11](../docs/03-tecnologia-e-servicos/11-analytics.md) |
| "Execução de mais de 15 minutos" | Não é Lambda: Fargate, Batch ou EC2 | [3.5](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) |
| "Infraestrutura da AWS no próprio datacenter" | Outposts | [3.2](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| "Menor latência para usuários do mundo todo", "cache" | CloudFront | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| "IP estático", "TCP ou UDP global" | Global Accelerator | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| "Conexão privada e dedicada com o datacenter" | Direct Connect | [3.10](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| "Arquivos compartilhados por várias instâncias Linux" | EFS | [3.9](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| "Infraestrutura como código" | CloudFormation | [3.1](../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) |

## Custos e suporte

| Se o enunciado diz | Pense em | Aula |
|---|---|---|
| "Pode ser interrompida" | Instâncias Spot | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| "Uso constante por 1 ou 3 anos" | Savings Plans ou Reserved Instances | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| "Licença por núcleo ou por soquete" | Dedicated Host | [4.2](../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| "Estimar antes de usar" | Pricing Calculator | [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| "Analisar e projetar os gastos" | Cost Explorer | [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| "Avisar quando o gasto passar de um valor" | Budgets | [4.4](../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| "Gerente técnico de conta designado" (*TAM*) | Enterprise Support ou Unified Operations | [4.5](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) |
| "Resposta em 5 minutos para incidente crítico" | Unified Operations | [4.5](../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) |

## Fontes oficiais

Cada linha resume a aula indicada, que lista as páginas oficiais da AWS com a data da verificação. Os idiomas da prova, entre eles o português do Brasil, estão na [página da certificação](https://aws.amazon.com/certification/certified-cloud-practitioner/), conferida em 06/10/2026.

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Acrescente aqui as expressões que enganaram você. -->
<!-- notas:fim -->
