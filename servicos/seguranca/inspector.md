<!-- autoral -->

# Amazon Inspector

> **Categoria:** Segurança e gerenciamento de vulnerabilidades · **Domínio:** 2 · **Abrangência:** Regional (várias contas pelo Organizations) · **Ficha:** núcleo
>
> **Em uma frase:** descobre instâncias EC2, imagens de contêiner e funções Lambda e as examina continuamente em busca de vulnerabilidades conhecidas de software e de exposição de rede não intencional.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

O servidor do portal de notas roda há meses com a mesma versão de uma biblioteca. Na semana passada, publicaram uma falha grave nela, catalogada como **CVE** (*Common Vulnerabilities and Exposures*, o catálogo público de falhas conhecidas). Ninguém da escola ficou sabendo, e a porta de administração ainda está aberta para a internet.

O **Inspector** encontra esse tipo de problema sem agendamento. Depois de ativado, ele descobre sozinho os recursos elegíveis e os examina: pacotes do sistema operacional e das linguagens de programação, caminhos de rede abertos sem querer e, nas funções Lambda, também o código. A varredura acompanha a vida do recurso: o Inspector volta a examinar quando um pacote é instalado, quando um patch é aplicado e quando sai uma nova CVE que afeta o recurso.

O limite: o Inspector aponta a falha e recomenda a correção, mas aplicar o patch continua com o cliente, como manda a [responsabilidade compartilhada](../../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md). E ele não detecta um ataque em andamento; isso é o [GuardDuty](guardduty.md).

## Como funciona

1. Você ativa o Inspector numa conta ou, com um clique, para toda a organização.
2. Ele descobre as instâncias EC2, as imagens enviadas ao Amazon ECR e as funções Lambda e começa a examiná-las.
3. Cada vulnerabilidade ou caminho de rede aberto vira um achado com a falha, o recurso, uma pontuação de risco ajustada ao ambiente e a correção recomendada.
4. Quando a correção é aplicada, o Inspector percebe e fecha o achado; os achados seguem para o EventBridge e para o Security Hub.

## Opções principais

| Varredura | O que examina | Observação |
|---|---|---|
| Instâncias EC2 | CVEs em pacotes, exposição e alcance de rede | Pelo agente do SSM ou por snapshots do EBS, sem agente |
| Imagens no Amazon ECR | Pacotes dentro da imagem de contêiner | Ao enviar a imagem e enquanto ela continua ativa |
| Funções Lambda | Pacotes das funções e, opcionalmente, o código | A varredura de código é uma camada opcional |
| Imagens de máquina (AMIs) | Pacotes das AMIs da conta | Ativada à parte |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Teste gratuito | 15 dias para contas novas no Inspector | 06/10/2026 |
| Recursos examinados | EC2, imagens no ECR e funções Lambda | 06/10/2026 |
| Agendamento das varreduras | Nenhum: são automáticas e contínuas | 06/10/2026 |

## Como é cobrado

Sem taxa mínima nem compromisso: o valor mensal depende da média de instâncias EC2 examinadas, do número de imagens examinadas no ECR (no envio e nas novas varreduras) e das funções Lambda examinadas. Contas novas têm 15 dias de teste gratuito para estimar o custo.

## Não confundir com

| Serviço | Diferença para o Inspector | Pista no enunciado |
|---|---|---|
| [Amazon GuardDuty](guardduty.md) | Detecta atividade suspeita nos registros | "Ameaça em andamento", "mineração de criptomoeda" |
| [AWS Systems Manager](../gerenciamento/systems-manager.md) | Aplica os patches nas instâncias | "Aplicar atualizações em massa" |
| [AWS Security Hub](security-hub.md) | Reúne os achados do Inspector com os de outros serviços | "Visão única dos achados" |
| [AWS Trusted Advisor](../gerenciamento/trusted-advisor.md) | Recomendações de boas práticas da conta | "Porta liberada no security group", "custo" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
- [Tipos de varredura](https://docs.aws.amazon.com/inspector/latest/user/scanning-resources.html)
- [Preços do Amazon Inspector](https://aws.amazon.com/inspector/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
