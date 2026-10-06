<!-- autoral -->

# Amazon GuardDuty

> **Categoria:** Segurança e detecção de ameaças · **Domínio:** 2 · **Abrangência:** Regional (várias contas pelo Organizations) · **Ficha:** núcleo
>
> **Em uma frase:** analisa continuamente os registros da conta com inteligência de ameaças e aprendizado de máquina e gera achados quando vê atividade suspeita.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Numa madrugada, uma instância EC2 da escola começa a conversar com um servidor de mineração de criptomoeda, e chamadas de API chegam de um endereço desconhecido usando a chave de acesso de um professor. Os registros que mostram isso existem, mas ninguém lê milhões de linhas de log por dia.

O **GuardDuty** lê. Ao ser ativado, ele passa a analisar as **fontes básicas** (eventos de gerenciamento do CloudTrail, VPC Flow Logs e consultas DNS do Route 53 Resolver) sem que você precise ligar esses registros à parte. Ele compara a atividade com listas de endereços e domínios maliciosos e com o comportamento habitual da conta, e gera um **achado** (*finding*) com o recurso afetado e a gravidade.

O limite: o GuardDuty detecta e avisa, mas não bloqueia nada sozinho. A resposta fica com o cliente, que pode automatizá-la, por exemplo com o EventBridge chamando uma função Lambda. E ele não procura falhas no software instalado; isso é o [Inspector](inspector.md).

## Como funciona

1. Você ativa o GuardDuty em cada Região (ou para toda a organização, por uma conta administradora delegada).
2. Ele analisa as fontes básicas e, se ativados, os planos de proteção para S3, EKS, RDS, Lambda, malware e outros.
3. Atividade suspeita vira um achado com tipo, recurso, gravidade e detalhes.
4. Os achados seguem para o console, para o EventBridge e para o [Security Hub](security-hub.md); o [Detective](detective.md) ajuda a investigar a causa.

## Opções principais

| Cobertura | O que vigia | Exemplo de achado |
|---|---|---|
| Fontes básicas | CloudTrail (gerenciamento), VPC Flow Logs, DNS | Instância falando com servidor de criptomoeda |
| S3 Protection | Eventos de dados nos buckets | Tentativa de copiar ou apagar dados em massa |
| Runtime Monitoring | Eventos do sistema operacional em EC2, EKS e ECS | Processo suspeito dentro do contêiner |
| Malware Protection | Volumes EBS, objetos novos no S3, backups | Arquivo com malware enviado ao bucket |
| RDS e Lambda Protection | Logins no banco, rede das funções | Tentativas de login anômalas no Aurora |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Teste gratuito | 30 dias por conta e por Região | 06/10/2026 |
| Fontes básicas | CloudTrail, VPC Flow Logs e DNS do Route 53 Resolver | 06/10/2026 |
| Ativação das fontes básicas | Sem configurar os registros à parte | 06/10/2026 |
| Retenção dos achados | 90 dias (para guardar mais, envie pelo EventBridge) | 06/10/2026 |

## Como é cobrado

Paga-se pelo volume de registros, eventos, cargas de trabalho ou dados analisados, com preço próprio para cada plano de proteção. Na primeira ativação numa Região há 30 dias de teste gratuito com todos os planos (exceto Runtime Monitoring, que não é ligado automaticamente), e o console mostra a estimativa de custo.

## Não confundir com

| Serviço | Diferença para o GuardDuty | Pista no enunciado |
|---|---|---|
| [Amazon Inspector](inspector.md) | Procura vulnerabilidades conhecidas (CVEs) no software | "Pacote desatualizado", "CVE" |
| [Amazon Macie](macie.md) | Procura dados sensíveis no S3 | "Dados pessoais no bucket" |
| [Amazon Detective](detective.md) | Investiga a causa raiz de um achado | "Investigar", "o que mais foi afetado" |
| [AWS CloudTrail](../gerenciamento/cloudtrail.md) | Registra as chamadas, sem analisá-las | "Quem fez a chamada" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Fontes de dados básicas](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html)
- [Achados no EventBridge](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_eventbridge.html) e [várias contas no Organizations](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html)
- [Tipos de achado para EC2](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html)
- [Preços do Amazon GuardDuty](https://aws.amazon.com/guardduty/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
