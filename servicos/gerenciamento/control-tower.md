<!-- autoral -->

# AWS Control Tower

> **Categoria:** Gerenciamento e governança de várias contas · **Domínio:** 2 · **Abrangência:** Organização · **Ficha:** núcleo
>
> **Em uma frase:** monta e governa um ambiente com várias contas segundo boas práticas, orquestrando Organizations, IAM Identity Center e outros serviços, e aplicando controles às contas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A rede de escolas vai passar de três para trinta contas, uma por escola e por ambiente. Montar tudo à mão significa criar a organização, a conta de registros, o login central, escrever SCPs e conferir sempre se cada conta continua seguindo as regras. A equipe de TI tem duas pessoas.

O **Control Tower** automatiza a montagem. Ele orquestra o Organizations, o Service Catalog, o IAM Identity Center e outros serviços para criar uma **landing zone**: um ambiente com várias contas configurado segundo boas práticas de segurança e conformidade. Sobre ela, aplica **controles** (*guardrails*), regras em linguagem simples que impedem, detectam ou barram antes da criação o que foge do padrão. O **Account Factory** cria contas novas que já nascem com a configuração aprovada, e um painel mostra as contas e os controles.

O limite: o Control Tower não substitui o Organizations; ele usa o Organizations por baixo. E os serviços que ele configura, como CloudTrail, Config e S3, são cobrados normalmente.

## Como funciona

1. Na conta de gerenciamento, você configura a landing zone.
2. O Control Tower cria a estrutura de OUs e contas e, se você não preferir gerenciar o acesso por conta própria, o login central pelo IAM Identity Center.
3. Você ativa controles nas OUs: preventivos, detectivos e proativos.
4. Novas contas saem do Account Factory já dentro das regras; o painel mostra recursos fora da conformidade.

## Opções principais

| Tipo de controle | Como age | Implementado com |
|---|---|---|
| Preventivo | Impede a ação que violaria a regra | Políticas do Organizations, como SCPs e RCPs |
| Detectivo | Encontra recursos fora da regra e alerta no painel | Regras do AWS Config |
| Proativo | Verifica o recurso antes de ser criado pelo CloudFormation | Hooks do CloudFormation |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Custo do Control Tower | Sem custo adicional | 06/10/2026 |
| Tipos de controle | Preventivo, detectivo e proativo | 06/10/2026 |
| Serviços que ele orquestra | Organizations, Service Catalog, IAM Identity Center e outros | 06/10/2026 |

## Como é cobrado

O Control Tower não tem custo adicional. Ao montar a landing zone, porém, começam as cobranças dos serviços que ele configura, como Service Catalog, CloudTrail, Config, CloudWatch, SNS e S3; o Organizations e o IAM Identity Center não têm custo adicional.

## Não confundir com

| Serviço | Diferença para o Control Tower | Pista no enunciado |
|---|---|---|
| [AWS Organizations](organizations.md) | A base: organização, OUs, SCPs e fatura única | "Fatura única", "SCP" |
| [AWS Config](config.md) | Avalia a configuração dos recursos | "Regra de configuração" |
| [AWS Service Catalog](service-catalog-e-ram.md) | Catálogo de produtos aprovados | "Equipes só criam o que foi aprovado" |
| [AWS CloudFormation](cloudformation.md) | Infraestrutura como código | "Modelo", "pilha" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [Como o Control Tower funciona](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html)
- [Sobre os controles](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) e [comportamento dos controles](https://docs.aws.amazon.com/controltower/latest/controlreference/control-behavior.html)
- [Preços do AWS Control Tower](https://aws.amazon.com/controltower/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
