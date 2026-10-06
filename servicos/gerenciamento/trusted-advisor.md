<!-- autoral -->

# AWS Trusted Advisor

> **Categoria:** Gerenciamento e boas práticas · **Domínio:** 2, 3 e 4 · **Abrangência:** Conta e organização · **Ficha:** núcleo
>
> **Em uma frase:** examina o ambiente da AWS e recomenda onde economizar, melhorar desempenho e disponibilidade, fechar brechas de segurança e respeitar os limites de serviço.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) · [4.5 Planos de suporte](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A conta da escola cresceu sem revisão: load balancers sem uso, um security group com a porta de administração aberta para qualquer endereço, a conta root sem MFA e o número de instâncias perto do limite da conta. Ninguém tem tempo de procurar esses problemas um por um.

O **Trusted Advisor** procura por você. Ele roda **verificações** em seis categorias (otimização de custos, desempenho, segurança, tolerância a falhas, limites de serviço e excelência operacional) e mostra cada resultado com a recomendação. Entre as verificações de segurança estão permissões de buckets S3, security groups com portas liberadas sem restrição e MFA na conta root.

O limite: quantas verificações você vê depende do plano de suporte. No Basic, são todas as de limites de serviço e algumas de segurança e tolerância a falhas, atualizadas à mão. E o Trusted Advisor aponta configurações fora das boas práticas, não ataques em andamento; isso é o [GuardDuty](../seguranca/guardduty.md).

## Como funciona

1. O Trusted Advisor examina os recursos da conta.
2. Cada verificação mostra o resultado, os recursos afetados e a recomendação.
3. Nos planos Business Support+, Enterprise e Unified Operations, todas as verificações ficam disponíveis, com atualização automática e acesso pela API.
4. Com o AWS Organizations, a **visão organizacional** reúne os resultados de todas as contas num relatório.

## Opções principais

| Categoria | O que verifica | Exemplo na escola |
|---|---|---|
| Otimização de custos | Recursos ociosos ou subutilizados | Load balancer ocioso, NAT gateway sem uso |
| Desempenho | Configurações que limitam o desempenho | Volume EBS subdimensionado para o uso |
| Segurança | Brechas de configuração | Porta aberta para qualquer endereço, root sem MFA |
| Tolerância a falhas | Pontos únicos de falha | Banco RDS com todas as instâncias na mesma zona |
| Limites de serviço | Uso perto das cotas da conta | Instâncias perto do limite da Região |
| Excelência operacional | Boas práticas de operação | VPC sem Flow Logs |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Categorias de verificação | 6 | 06/10/2026 |
| Plano Basic | Todas as de limites de serviço e algumas de segurança e tolerância a falhas, sem atualização automática | 06/10/2026 |
| Todas as verificações e a API | Business Support+, Enterprise ou Unified Operations | 06/10/2026 |
| Trusted Advisor Priority | Enterprise ou Unified Operations, na conta de gerenciamento | 06/10/2026 |

## Como é cobrado

O Trusted Advisor não tem cobrança própria: o acesso vem com o plano de suporte. O Basic, gratuito, dá as verificações principais; os planos pagos liberam todas.

## Não confundir com

| Serviço | Diferença para o Trusted Advisor | Pista no enunciado |
|---|---|---|
| [AWS Compute Optimizer](compute-optimizer-service-quotas-e-license-manager.md) | Recomenda o tamanho certo a partir das métricas de uso | "Tamanho certo da instância" |
| [Service Quotas](compute-optimizer-service-quotas-e-license-manager.md) | Mostra as cotas e recebe o pedido de aumento | "Pedir aumento de limite" |
| [AWS Config](config.md) | Avalia regras definidas pelo cliente e guarda histórico | "Histórico de configuração" |
| [AWS Security Hub](../seguranca/security-hub.md) | Reúne achados de segurança e confere padrões | "Visão única de segurança" |
| [Amazon GuardDuty](../seguranca/guardduty.md) | Detecta ameaças em andamento | "Atividade suspeita" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
- [Referência das verificações](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html)
- [Visão organizacional](https://docs.aws.amazon.com/awssupport/latest/user/organizational-view.html)
- [Trusted Advisor Priority](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-priority.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
