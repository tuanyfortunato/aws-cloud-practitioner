<!-- autoral -->

# AWS Security Hub

> **Categoria:** Segurança e gerenciamento de postura · **Domínio:** 2 · **Abrangência:** Regional, com agregação de Regiões e contas · **Ficha:** núcleo
>
> **Em uma frase:** reúne, correlaciona e prioriza os sinais de segurança do GuardDuty, do Inspector, do Macie e das verificações de postura, e confere as contas contra padrões de boas práticas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

A equipe de TI da escola ativou o GuardDuty, o Inspector e o Macie em dez contas e três Regiões. Agora há achados em três consoles diferentes, e a pergunta da diretora é simples: "qual é o problema mais grave hoje?". Ninguém consegue responder sem abrir tudo.

O **Security Hub** é a visão única. Ele recebe os achados desses serviços e do IAM Access Analyzer, correlaciona os sinais e mostra as **exposições**: por exemplo, uma instância com uma CVE crítica que também está aberta para a internet. Sua parte de gerenciamento de postura, o **Security Hub CSPM** (*cloud security posture management*), verifica as contas contra padrões de segurança, como o AWS Foundational Security Best Practices, criado pela AWS, e padrões externos como CIS, PCI DSS e NIST.

O limite: o Security Hub depende das fontes. Sem o GuardDuty ativado, não há achados de ameaça para reunir, e a maioria das verificações do CSPM exige o [AWS Config](../gerenciamento/config.md) gravando os recursos.

## Como funciona

1. Você ativa o Security Hub numa conta ou para a organização, e escolhe uma Região principal que agrega as demais.
2. Os serviços integrados enviam achados num formato comum (OCSF), e o CSPM roda as verificações dos padrões escolhidos.
3. O Security Hub correlaciona os sinais, prioriza os riscos e mostra um painel com exposições, ameaças, cobertura e um grafo de caminhos de ataque.
4. A resposta pode ser automatizada, inclusive com a abertura de tickets em ferramentas como Jira Cloud e ServiceNow.

## Opções principais

| Peça | O que faz | Exemplo na escola |
|---|---|---|
| Achados de exposição | Correlaciona CSPM, Inspector e outros serviços | Instância vulnerável e aberta à internet |
| Security Hub CSPM | Verificações contra padrões de segurança | Bucket sem criptografia reprova numa verificação |
| Análise de acesso não usado | Papéis, usuários e chaves sem uso há 90 dias | Chave de acesso de um ex-professor |
| Agregação entre Regiões | Reúne os dados numa Região principal | Um painel para as três Regiões |
| Integrações | Tickets e soluções de parceiros | Achado crítico vira ticket no ServiceNow |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Padrões do CSPM | FSBP (AWS), CIS, PCI DSS e NIST | 06/10/2026 |
| Acesso não usado | Janela de 90 dias | 06/10/2026 |
| Teste gratuito | 30 dias | 06/10/2026 |

## Como é cobrado

Sem compromisso: o plano Essentials é cobrado por unidade de recurso por mês, com complementos opcionais e um plano Extended para soluções de parceiros selecionados. Os serviços usados pelas verificações, como os itens do AWS Config, são cobrados à parte. Há 30 dias de teste gratuito.

## Não confundir com

| Serviço | Diferença para o Security Hub | Pista no enunciado |
|---|---|---|
| [Amazon GuardDuty](guardduty.md) | Gera os achados de ameaça que o Security Hub reúne | "Detectar atividade suspeita" |
| [Amazon Detective](detective.md) | Investiga a causa raiz de um achado | "Investigar", "linha do tempo" |
| [AWS Config](../gerenciamento/config.md) | Registra configurações e avalia regras, base das verificações | "Histórico de configuração" |
| [AWS Trusted Advisor](../gerenciamento/trusted-advisor.md) | Recomendações de custo, desempenho, segurança e outras | "Economizar", "limites de serviço" |
| [AWS Audit Manager](audit-manager.md) | Coleta evidências para auditoria | "Evidências para o auditor" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Introdução ao AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html)
- [Introdução ao Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
- [Agregação entre Regiões](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html)
- [Preços do AWS Security Hub](https://aws.amazon.com/security-hub/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
