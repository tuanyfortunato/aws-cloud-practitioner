# 🧭 Rastreabilidade: task oficial → aula → questões

Cada linha liga uma *task statement* do [guia oficial do exame](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) às aulas que a ensinam e às questões que a praticam. As tasks foram conferidas em 06/10/2026.

A numeração das aulas (1.1 a 4.6) não é a mesma das tasks oficiais. Uma aula pode servir a mais de uma task, como a 3.2 (benefícios da nuvem e infraestrutura global) e a 3.17 (migração e serviços de banco de dados); nesse caso, as questões dela aparecem nas duas linhas.

⬅️ [Todas as questões por domínio](README.md)

---

## Resumo

| Task oficial | Aulas | Questões |
|---|---|---|
| [1.1](#task-11) | [1.1](../../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) · [1.2](../../docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) · [3.2](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) | 6 |
| [1.2](#task-12) | [1.3](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) · [1.4](../../docs/01-conceitos-de-nuvem/04-well-architected-framework.md) | 7 |
| [1.3](#task-13) | [1.5](../../docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md) · [1.6](../../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md) · [3.17](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) | 5 |
| [1.4](#task-14) | [1.7](../../docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md) | 1 |
| [2.1](#task-21) | [2.1](../../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) | 3 |
| [2.2](#task-22) | [2.5](../../docs/02-seguranca-e-conformidade/05-criptografia.md) · [2.6](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md) · [2.7](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) | 4 |
| [2.3](#task-23) | [2.2](../../docs/02-seguranca-e-conformidade/02-usuario-root.md) · [2.3](../../docs/02-seguranca-e-conformidade/03-iam.md) · [2.4](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md) | 7 |
| [2.4](#task-24) | [2.8](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) · [2.9](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) · [2.10](../../docs/02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) | 9 |
| [3.1](#task-31) | [3.1](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) · [3.16](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md) | 6 |
| [3.2](#task-32) | [3.2](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) | 2 |
| [3.3](#task-33) | [3.3](../../docs/03-tecnologia-e-servicos/03-ec2.md) · [3.4](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) · [3.5](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) · [3.6](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) | 8 |
| [3.4](#task-34) | [3.7](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · [3.17](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) | 4 |
| [3.5](#task-35) | [3.10](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) | 3 |
| [3.6](#task-36) | [3.8](../../docs/03-tecnologia-e-servicos/08-s3.md) · [3.9](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) | 4 |
| [3.7](#task-37) | [3.11](../../docs/03-tecnologia-e-servicos/11-analytics.md) · [3.12](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md) | 2 |
| [3.8](#task-38) | [3.13](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) · [3.14](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md) · [3.15](../../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md) · [3.18](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md) | 11 |
| [4.1](#task-41) | [4.1](../../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md) · [4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) · [4.3](../../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) | 6 |
| [4.2](#task-42) | [4.4](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) | 3 |
| [4.3](#task-43) | [4.5](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) · [4.6](../../docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md) | 6 |

<a id="task-11"></a>

## Task 1.1: Define the benefits of the AWS Cloud

Fonte: [Content Domain 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1)

| Aula | Questões |
|---|---|
| [1.1 O que é computação em nuvem](../../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) | [D1 Q1](dominio-1.md#questão-1) · [D1 Q2](dominio-1.md#questão-2) |
| [1.2 As 6 vantagens da computação em nuvem](../../docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) | [D1 Q3](dominio-1.md#questão-3) · [D1 Q4](dominio-1.md#questão-4) |
| [3.2 Infraestrutura global](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) | [D3 Q3](dominio-3.md#questão-3) · [D3 Q4](dominio-3.md#questão-4) |

<a id="task-12"></a>

## Task 1.2: Identify design principles of the AWS Cloud

Fonte: [Content Domain 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2)

| Aula | Questões |
|---|---|
| [1.3 Conceitos de arquitetura que a prova cobra](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) | [D1 Q5](dominio-1.md#questão-5) · [D1 Q6](dominio-1.md#questão-6) · [D1 Q7](dominio-1.md#questão-7) · [D1 Q8](dominio-1.md#questão-8) |
| [1.4 AWS Well-Architected Framework](../../docs/01-conceitos-de-nuvem/04-well-architected-framework.md) | [D1 Q9](dominio-1.md#questão-9) · [D1 Q10](dominio-1.md#questão-10) · [D1 Q11](dominio-1.md#questão-11) |

<a id="task-13"></a>

## Task 1.3: Understand the benefits of and strategies for migration to the AWS Cloud

Fonte: [Content Domain 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3)

| Aula | Questões |
|---|---|
| [1.5 AWS Cloud Adoption Framework (CAF)](../../docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md) | [D1 Q12](dominio-1.md#questão-12) · [D1 Q13](dominio-1.md#questão-13) |
| [1.6 Estratégias de migração (os 7 Rs)](../../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md) | [D1 Q14](dominio-1.md#questão-14) · [D1 Q15](dominio-1.md#questão-15) |
| [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) | [D3 Q37](dominio-3.md#questão-37) |

<a id="task-14"></a>

## Task 1.4: Understand concepts of cloud economics

Fonte: [Content Domain 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4)

| Aula | Questões |
|---|---|
| [1.7 Economia da nuvem](../../docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md) | [D1 Q16](dominio-1.md#questão-16) |

<a id="task-21"></a>

## Task 2.1: Understand the AWS shared responsibility model

Fonte: [Content Domain 2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1)

| Aula | Questões |
|---|---|
| [2.1 Modelo de responsabilidade compartilhada](../../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) | [D2 Q1](dominio-2.md#questão-1) · [D2 Q2](dominio-2.md#questão-2) · [D2 Q3](dominio-2.md#questão-3) |

<a id="task-22"></a>

## Task 2.2: Understand AWS Cloud security, governance, and compliance concepts

Fonte: [Content Domain 2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2)

| Aula | Questões |
|---|---|
| [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md) | [D2 Q11](dominio-2.md#questão-11) |
| [2.6 Compliance e governança](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md) | [D2 Q12](dominio-2.md#questão-12) |
| [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) | [D2 Q13](dominio-2.md#questão-13) · [D2 Q14](dominio-2.md#questão-14) |

<a id="task-23"></a>

## Task 2.3: Identify AWS access management capabilities

Fonte: [Content Domain 2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3)

| Aula | Questões |
|---|---|
| [2.2 Usuário root](../../docs/02-seguranca-e-conformidade/02-usuario-root.md) | [D2 Q4](dominio-2.md#questão-4) |
| [2.3 AWS IAM (Identity and Access Management)](../../docs/02-seguranca-e-conformidade/03-iam.md) | [D2 Q5](dominio-2.md#questão-5) · [D2 Q6](dominio-2.md#questão-6) · [D2 Q7](dominio-2.md#questão-7) · [D2 Q8](dominio-2.md#questão-8) · [D2 Q9](dominio-2.md#questão-9) |
| [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md) | [D2 Q10](dominio-2.md#questão-10) |

<a id="task-24"></a>

## Task 2.4: Identify components and resources for security

Fonte: [Content Domain 2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4)

| Aula | Questões |
|---|---|
| [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) | [D2 Q15](dominio-2.md#questão-15) · [D2 Q16](dominio-2.md#questão-16) · [D2 Q17](dominio-2.md#questão-17) |
| [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) | [D2 Q18](dominio-2.md#questão-18) · [D2 Q19](dominio-2.md#questão-19) · [D2 Q20](dominio-2.md#questão-20) |
| [2.10 Outros pontos de segurança](../../docs/02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) | [D2 Q21](dominio-2.md#questão-21) · [D2 Q22](dominio-2.md#questão-22) · [D2 Q23](dominio-2.md#questão-23) |

<a id="task-31"></a>

## Task 3.1: Define methods of deploying and operating in the AWS Cloud

Fonte: [Content Domain 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1)

| Aula | Questões |
|---|---|
| [3.1 Formas de acessar e implantar na AWS](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) | [D3 Q1](dominio-3.md#questão-1) · [D3 Q2](dominio-3.md#questão-2) |
| [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md) | [D3 Q33](dominio-3.md#questão-33) · [D3 Q34](dominio-3.md#questão-34) · [D3 Q35](dominio-3.md#questão-35) · [D3 Q36](dominio-3.md#questão-36) |

<a id="task-32"></a>

## Task 3.2: Define the AWS global infrastructure

Fonte: [Content Domain 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2)

| Aula | Questões |
|---|---|
| [3.2 Infraestrutura global](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) | [D3 Q3](dominio-3.md#questão-3) · [D3 Q4](dominio-3.md#questão-4) |

<a id="task-33"></a>

## Task 3.3: Identify AWS compute services

Fonte: [Content Domain 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3)

| Aula | Questões |
|---|---|
| [3.3 Amazon EC2](../../docs/03-tecnologia-e-servicos/03-ec2.md) | [D3 Q5](dominio-3.md#questão-5) · [D3 Q6](dominio-3.md#questão-6) |
| [3.4 Escalabilidade e balanceamento de carga](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) | [D3 Q7](dominio-3.md#questão-7) |
| [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) | [D3 Q8](dominio-3.md#questão-8) · [D3 Q9](dominio-3.md#questão-9) |
| [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) | [D3 Q10](dominio-3.md#questão-10) · [D3 Q11](dominio-3.md#questão-11) · [D3 Q12](dominio-3.md#questão-12) |

<a id="task-34"></a>

## Task 3.4: Identify AWS database services

Fonte: [Content Domain 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4)

| Aula | Questões |
|---|---|
| [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) | [D3 Q13](dominio-3.md#questão-13) · [D3 Q14](dominio-3.md#questão-14) · [D3 Q15](dominio-3.md#questão-15) |
| [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) | [D3 Q37](dominio-3.md#questão-37) |

<a id="task-35"></a>

## Task 3.5: Identify AWS network services

Fonte: [Content Domain 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5)

| Aula | Questões |
|---|---|
| [3.10 Redes e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) | [D3 Q20](dominio-3.md#questão-20) · [D3 Q21](dominio-3.md#questão-21) · [D3 Q22](dominio-3.md#questão-22) |

<a id="task-36"></a>

## Task 3.6: Identify AWS storage services

Fonte: [Content Domain 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6)

| Aula | Questões |
|---|---|
| [3.8 Amazon S3 — armazenamento de objetos](../../docs/03-tecnologia-e-servicos/08-s3.md) | [D3 Q16](dominio-3.md#questão-16) · [D3 Q17](dominio-3.md#questão-17) |
| [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) | [D3 Q18](dominio-3.md#questão-18) · [D3 Q19](dominio-3.md#questão-19) |

<a id="task-37"></a>

## Task 3.7: Identify AWS artificial intelligence and machine learning (AI/ML) services and analytics services

Fonte: [Content Domain 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7)

| Aula | Questões |
|---|---|
| [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md) | [D3 Q23](dominio-3.md#questão-23) |
| [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md) | [D3 Q24](dominio-3.md#questão-24) |

<a id="task-38"></a>

## Task 3.8: Identify services from other in-scope AWS service categories

Fonte: [Content Domain 3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8)

| Aula | Questões |
|---|---|
| [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) | [D3 Q25](dominio-3.md#questão-25) |
| [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md) | [D3 Q26](dominio-3.md#questão-26) · [D3 Q27](dominio-3.md#questão-27) · [D3 Q28](dominio-3.md#questão-28) · [D3 Q29](dominio-3.md#questão-29) |
| [3.15 Ferramentas de desenvolvimento](../../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md) | [D3 Q30](dominio-3.md#questão-30) · [D3 Q31](dominio-3.md#questão-31) · [D3 Q32](dominio-3.md#questão-32) |
| [3.18 Serviços menos conhecidos que podem aparecer](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md) | [D3 Q38](dominio-3.md#questão-38) · [D3 Q39](dominio-3.md#questão-39) · [D3 Q40](dominio-3.md#questão-40) |

<a id="task-41"></a>

## Task 4.1: Compare AWS pricing models

Fonte: [Content Domain 4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1)

| Aula | Questões |
|---|---|
| [4.1 Princípios de preço da AWS](../../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md) | [D4 Q1](dominio-4.md#questão-1) · [D4 Q2](dominio-4.md#questão-2) · [D4 Q3](dominio-4.md#questão-3) |
| [4.2 Modelos de compra do EC2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) | [D4 Q4](dominio-4.md#questão-4) · [D4 Q5](dominio-4.md#questão-5) |
| [4.3 Como outros recursos são cobrados](../../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) | [D4 Q6](dominio-4.md#questão-6) |

<a id="task-42"></a>

## Task 4.2: Understand resources for billing, budget, and cost management

Fonte: [Content Domain 4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2)

| Aula | Questões |
|---|---|
| [4.4 Ferramentas de custo e faturamento](../../docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) | [D4 Q7](dominio-4.md#questão-7) · [D4 Q8](dominio-4.md#questão-8) · [D4 Q9](dominio-4.md#questão-9) |

<a id="task-43"></a>

## Task 4.3: Identify AWS technical resources and AWS Support options

Fonte: [Content Domain 4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3)

| Aula | Questões |
|---|---|
| [4.5 Planos de AWS Support](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) | [D4 Q10](dominio-4.md#questão-10) · [D4 Q11](dominio-4.md#questão-11) |
| [4.6 Outros recursos de ajuda](../../docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md) | [D4 Q12](dominio-4.md#questão-12) · [D4 Q13](dominio-4.md#questão-13) · [D4 Q14](dominio-4.md#questão-14) · [D4 Q15](dominio-4.md#questão-15) |

## Como manter

- A lista de tasks e de aulas fica em `TAREFAS` de [`scripts/gerar_simulado.py`](../../scripts/gerar_simulado.py); a tabela de tasks do [escopo oficial](../../docs/00-guia-do-exame/escopo-oficial.md) deve dizer o mesmo.
- O gerador falha se uma aula não estiver ligada a nenhuma task ou se uma task ficar sem questão.
- Ao dividir, renumerar ou reordenar aulas, atualize `TAREFAS` e rode `python3 scripts/gerar_simulado.py`.
- Reabra as páginas do guia oficial antes de cada revisão: a AWS muda o conteúdo sem trocar o código da prova.

## Limites

- A tabela mostra que cada task tem aula e questões; ela não mede se as questões cobrem todos os itens de "Knowledge of" e "Skills in" de cada task.
- As fontes de cada afirmação ficam na seção "Fontes oficiais" de cada aula e ficha, com a data da verificação; o que não foi confirmado fica nas [pendências de verificação](../../docs/00-guia-do-exame/pendencias-de-verificacao.md).
