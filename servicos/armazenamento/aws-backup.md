# AWS Backup

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa tem dados em vários serviços e precisa organizar cópias de segurança, prazos de retenção e recuperação sem administrar tudo de forma isolada.

**Como este serviço ajuda?** AWS Backup centraliza políticas e operações de backup para recursos compatíveis. Você define o que copiar, quando copiar e por quanto tempo manter as cópias.

**Exemplo do dia a dia:** A escola define um plano que protege recursos compatíveis do sistema de matrícula e mantém pontos de recuperação por um período determinado.

**O que ele não resolve sozinho?** Ter backup não mantém automaticamente uma aplicação disponível durante uma falha. Também é preciso planejar e testar a restauração; a cobertura depende do recurso e das opções usadas.

**Primeiras palavras para entender:**

- **Backup:** cópia de segurança.
- **Retenção:** tempo de conservação.
- **Ponto de recuperação:** cópia que pode ser usada numa restauração.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Armazenamento / Proteção de dados · **Domínio:** 3 · **Escopo:** Regional (cópias entre regiões e contas) · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** centraliza e automatiza backups de vários serviços AWS com políticas, num só lugar.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Recursos suportados (exemplos)

EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, S3, DocumentDB, Neptune, Redshift, Storage Gateway (volumes), VMware on-premises, entre outros.

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Backup plan** | Frequência (cron), janela, **retenção**, transição para *cold storage*, cópia para outra região/conta. |
| **Resource assignment** | Quais recursos entram no plano (por tag, ID ou tipo). |
| **Backup vault** | Contêiner criptografado (KMS) onde ficam os *recovery points*. |
| **Vault Lock** | **WORM** para backups: ninguém (nem o root) apaga antes do prazo — modo compliance. |
| **Logically air-gapped vault** | Vault isolado e compartilhável para recuperação após ransomware. |
| **Cross-region / cross-account copy** | DR e isolamento. |
| **Backup policies (Organizations)** | Aplicam planos em todas as contas da organização. |
| **Backup Audit Manager** | Relatórios de conformidade dos backups (frameworks e controles). |
| **Restore testing** | Testes automáticos de restauração. |

## Cobrança

- GB-mês armazenado por tipo de recurso (warm/cold), restauração, cópias entre regiões.

## ⚠️ Pegadinhas e não confundir

- **AWS Backup** (centraliza políticas) × snapshots manuais/DLM (por serviço).
- **AWS Backup** × **Elastic Disaster Recovery**: backup com RPO de horas × replicação contínua com recuperação em minutos.

## ❓ Perguntas típicas

- "Centralizar backups de vários serviços com políticas." → AWS Backup.
- "Impedir que backups sejam apagados, nem pelo administrador." → Backup Vault Lock.
- "Aplicar a mesma política de backup em todas as contas." → Backup policies no Organizations.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Planos, seleções de recursos, vaults e recovery points |
| **O que você decide/configura?** | Agenda, retenção, cópias, permissões e recursos elegíveis |
| **Em que ordem as coisas acontecem?** | Associe recursos ao plano, acompanhe jobs e teste restauração |
| **O que pode fazer, e em que condição?** | Centraliza políticas de backup para serviços suportados |
| **O que não pode presumir?** | Não inclui automaticamente todo recurso e não substitui disponibilidade ou teste de recuperação |

**Caso comentado:** Políticas comuns de retenção entre serviços: AWS Backup, com seleção e proteção configuradas.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
