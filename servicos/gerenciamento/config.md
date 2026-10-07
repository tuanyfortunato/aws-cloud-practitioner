<!-- autoral -->

# AWS Config

> **Categoria:** Gerenciamento, governança e compliance · **Domínio:** 2 · **Abrangência:** Regional (agregadores reúnem contas e Regiões) · **Ficha:** núcleo
>
> **Em uma frase:** registra a configuração dos recursos, as relações entre eles e o histórico de mudanças, e avalia cada recurso contra regras de configuração desejada.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) · [2.6 Compliance e governança](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

A pasta de documentos dos pais ficou pública. O CloudTrail mostrou quem mudou a política do bucket, mas a diretora quer mais: como a política estava antes, desde quando o bucket está fora da regra e se existem outros buckets na mesma situação.

O **Config** guarda o estado. Ele registra a configuração de cada recurso como **itens de configuração**, com as relações entre recursos e o histórico de mudanças, de modo que dá para ver a política do bucket antes e depois. Sobre esse registro, as **regras do Config** descrevem a configuração desejada, como "todo bucket deve bloquear acesso público", e marcam cada recurso como em conformidade ou não. Recursos fora da regra podem ser corrigidos com **remediação**, que executa automações do Systems Manager.

O limite: o Config só tem o histórico do período em que estava registrando. E ele avalia configurações, não prova sozinho que a escola cumpre uma norma; as evidências para a auditoria são organizadas pelo [Audit Manager](../seguranca/audit-manager.md).

## Como funciona

1. Você liga o gravador do Config e escolhe quais tipos de recurso registrar.
2. Cada mudança gera um item de configuração; o histórico fica disponível para consulta.
3. Regras gerenciadas (prontas) ou personalizadas avaliam os recursos quando eles mudam ou periodicamente.
4. Recursos fora da regra aparecem como fora de conformidade e podem ser corrigidos com remediação; um agregador reúne os dados de várias contas e Regiões.

## Opções principais

| Recurso | O que faz | Exemplo na escola |
|---|---|---|
| Histórico de configuração | Estado de cada recurso ao longo do tempo | Política do bucket antes da mudança |
| Regras gerenciadas | Regras prontas da AWS | "Buckets devem bloquear acesso público" |
| Regras personalizadas | Regras escritas pelo cliente | Exigir uma etiqueta de setor em tudo |
| Remediação | Corrige com automações do Systems Manager | Reaplicar o bloqueio de acesso público |
| Pacote de conformidade | Conjunto de regras e remediações implantado de uma vez | O mesmo pacote em todas as contas |
| Agregador | Reúne dados de várias contas e Regiões | Uma visão para a rede inteira |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Unidade de registro | Item de configuração, um por estado registrado | 06/10/2026 |
| Base das verificações do Security Hub CSPM | A maioria usa regras do Config | 06/10/2026 |
| Controles detectivos do Control Tower | Implementados com regras do Config | 06/10/2026 |

## Como é cobrado

Paga-se pelo número de itens de configuração registrados, de avaliações de regras ativas e de avaliações de pacotes de conformidade na conta.

## Não confundir com

| Serviço | Diferença para o Config | Pista no enunciado |
|---|---|---|
| [AWS CloudTrail](cloudtrail.md) | Registra quem fez a chamada de API | "Quem alterou" |
| [Amazon CloudWatch](cloudwatch.md) | Métricas e alarmes de funcionamento | "Desempenho", "CPU" |
| [AWS Audit Manager](../seguranca/audit-manager.md) | Organiza evidências por controle de uma norma | "Evidências para o auditor" |
| [AWS Trusted Advisor](trusted-advisor.md) | Recomendações de boas práticas, sem histórico | "Recomendações para economizar" |
| [AWS Security Hub](../seguranca/security-hub.md) | Reúne achados e confere padrões de segurança | "Visão única de segurança" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
- [Regras do AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)
- [Remediação](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)
- [Pacotes de conformidade](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)
- [Agregadores](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html)
- [Preços do AWS Config](https://aws.amazon.com/config/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
