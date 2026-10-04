# AWS Backup

> **Categoria:** Armazenamento / Proteção de dados · **Domínio:** 3 · **Escopo:** Regional (cópias entre regiões e contas) · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** centraliza e automatiza backups de vários serviços AWS com políticas, num só lugar.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **central de backup**: em vez de configurar cópia em cada serviço, você cria uma política e ela vale para todos.

- ✅ **Escolha quando:** precisa **centralizar e padronizar backups** de vários serviços (EC2, RDS, DynamoDB, EFS…), inclusive entre contas e regiões.
- 🚫 **Não é a resposta quando:** precisa **voltar a operar em minutos** depois de um desastre → [Elastic Disaster Recovery](elastic-disaster-recovery.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "centralizar backups", "política de backup", "retenção", "backup que ninguém pode apagar" (Vault Lock).
<!-- didatico:fim -->

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

## 🔗 Documentação oficial

- [Guia do AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
