<!-- autoral -->

# AWS Artifact

> **Categoria:** Compliance · **Domínio:** 2 · **Abrangência:** Portal no console · **Ficha:** núcleo
>
> **Em uma frase:** portal de autoatendimento, gratuito, para baixar os relatórios de segurança e compliance da AWS e aceitar acordos com ela.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.6 Compliance e governança](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

A auditora contratada pela escola pede duas coisas: um relatório independente que mostre que os data centers da AWS são bem controlados e a prova de que a escola configurou bem os próprios recursos. A primeira parte é da AWS, e a escola não tem como auditar um data center dela.

O **Artifact** entrega essa parte. Nele a escola baixa, sob demanda, relatórios SOC, relatórios de conformidade com o PCI DSS e com normas ISO e certificações de órgãos de acreditação, e os entrega à auditora como evidência. O Artifact também guarda **acordos** com a AWS, como o BAA (*Business Associate Addendum*), exigido de quem trata informações de saúde protegidas pela lei americana HIPAA, e documentos de compliance de vendedores do AWS Marketplace.

O limite: o Artifact só fala da AWS. Nenhum relatório dele prova que a escola configurou bem os seus recursos; essa segunda parte é do cliente, com ferramentas como o [Audit Manager](audit-manager.md) e o [Config](../gerenciamento/config.md).

## Como funciona

1. Você abre o Artifact no console, com permissão do IAM para ver e baixar relatórios.
2. Escolhe o relatório, aceita os termos de uso dele quando houver e faz o download.
3. Em **Acordos**, revisa e aceita acordos para a conta ou, pela conta de gerenciamento, para todas as contas da organização.
4. Entrega os documentos à auditoria e usa-os como referência para avaliar os próprios controles.

## Opções principais

| Recurso | O que oferece | Exemplo na escola |
|---|---|---|
| Relatórios da AWS | SOC, PCI DSS, ISO e certificações | Relatório SOC 2 para a auditora |
| Acordos | Revisar, aceitar e acompanhar acordos | BAA para tratar dados de saúde |
| Acordos da organização | Aceite pela conta de gerenciamento para todas as contas | Contas novas já cobertas pelo acordo |
| Relatórios de terceiros | Documentos de vendedores do AWS Marketplace | Avaliar um software comprado no Marketplace |
| Assurance Assistant | Respostas geradas por IA para perguntas de compliance | Rascunho de resposta a um questionário |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Preço dos documentos e acordos | Gratuitos | 06/10/2026 |
| Acordo clássico da prova | BAA, para HIPAA | 06/10/2026 |
| Cópia de cada relatório | Gerada para quem baixa, com marca d’água única | 06/10/2026 |

## Como é cobrado

Os documentos e acordos do Artifact não têm custo.

## Não confundir com

| Serviço | Diferença para o Artifact | Pista no enunciado |
|---|---|---|
| [AWS Audit Manager](audit-manager.md) | Coleta evidências da sua conta para a sua auditoria | "Evidências dos meus controles" |
| [AWS Config](../gerenciamento/config.md) | Avalia a configuração dos seus recursos | "Recurso fora do padrão" |
| [AWS Security Hub](security-hub.md) | Confere as contas contra padrões como PCI DSS | "Verificar a conta contra o CIS" |
| [AWS Trusted Advisor](../gerenciamento/trusted-advisor.md) | Recomendações de boas práticas | "Recomendações para a conta" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)
- [Baixar relatórios](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html)
- [Acordos no AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html)
- [Programas de compliance da AWS](https://aws.amazon.com/compliance/programs/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
