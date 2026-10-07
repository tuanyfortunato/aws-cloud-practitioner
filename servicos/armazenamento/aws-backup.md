<!-- autoral -->

# AWS Backup

> **Categoria:** Armazenamento e proteção de dados · **Domínio:** 3 · **Abrangência:** Regional (cópias entre Regiões e contas) · **Ficha:** núcleo
>
> **Em uma frase:** centraliza e automatiza os backups de vários serviços da AWS com planos aplicados aos recursos, num só lugar.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

Cada serviço tem seu próprio jeito de fazer backup: snapshots no EBS, backups automáticos no RDS, e assim por diante. A direção da escola quer saber, num só lugar, se todos os backups estão em dia, e conferir serviço por serviço não escala.

O AWS Backup centraliza e automatiza a proteção de dados entre serviços da AWS, na nuvem e no local do cliente. Você cria **planos de backup** (quando fazer, por quanto tempo guardar) e os aplica aos recursos, por exemplo pelas etiquetas (tags). Ele atende, entre outros, EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx e S3.

O limite: o AWS Backup só governa os backups feitos por ele; os criados por fora não entram no painel. E backup guarda cópias: manter um ambiente pronto para assumir é papel do [Elastic Disaster Recovery](elastic-disaster-recovery.md).

## Como funciona

1. Você cria um **plano de backup**: frequência, janela e por quanto tempo guardar.
2. Atribui recursos ao plano, por etiquetas ou escolhendo-os.
3. O AWS Backup cria os backups e os guarda num **cofre de backup** (*backup vault*), separado dos recursos de origem e criptografado com a chave do cofre.
4. Regras de ciclo de vida movem backups antigos para armazenamento frio; cópias vão para outras Regiões e contas.

## Opções principais

| Recurso | O que faz | Quando lembrar |
|---|---|---|
| Plano de backup | Define frequência e retenção e é aplicado a muitos recursos | "Política de backup para tudo com a tag X" |
| Cópia entre Regiões e contas | Guarda backups longe da produção | "Continuidade de negócio", "outra Região" |
| Armazenamento frio | Move backups antigos para um nível mais barato | "Guardar por anos com menor custo" |
| Vault Lock | Impede apagar backups ou mudar a retenção (WORM); no modo compliance, nem a AWS pode remover a trava | "Ninguém pode apagar os backups" |
| Gerenciamento entre contas | Aplica planos em todas as contas do AWS Organizations | "Várias contas da empresa" |
| Backup Audit Manager | Confere os backups contra controles e gera relatórios diários | "Provar conformidade dos backups" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Taxa mínima ou de instalação | Nenhuma | 06/10/2026 |
| Modos do Vault Lock | Governance e compliance | 06/10/2026 |

## Como é cobrado

Não há taxa mínima nem de instalação. Você paga pelo armazenamento de backup usado (média de GB-mês, com preço menor no armazenamento frio), pelos dados restaurados, pela transferência de backups entre Regiões, pelos testes de restauração e pelo Backup Audit Manager.

## Não confundir com

| Serviço | Diferença para o AWS Backup | Pista no enunciado |
|---|---|---|
| [AWS Elastic Disaster Recovery](elastic-disaster-recovery.md) | Replica servidores continuamente e os recupera na AWS em minutos | "Ambiente pronto após desastre" |
| [Amazon EBS](ebs.md) | Snapshots de um volume, feitos à mão ou pelo Data Lifecycle Manager | "Backup de um volume" |
| [Classes do S3](s3-classes-de-armazenamento.md) | Arquivamento de objetos no Glacier por regras de ciclo de vida | "Arquivar objetos antigos" |
| [AWS Audit Manager](../seguranca/audit-manager.md) | Coleta evidências de conformidade da conta toda; recebe os resultados do Backup Audit Manager | "Auditoria de conformidade geral" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Disponibilidade de recursos por serviço](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html)
- [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html)
- [Preços do AWS Backup](https://aws.amazon.com/backup/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
