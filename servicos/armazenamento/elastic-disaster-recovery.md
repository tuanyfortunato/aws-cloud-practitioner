# AWS Elastic Disaster Recovery (AWS DRS)

> **Categoria:** Recuperação de desastres · **Domínio:** 1 (DR) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** replica servidores continuamente (on-premises, outra nuvem ou outra região AWS) para a AWS e permite recuperá-los em minutos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **servidor reserva sempre sincronizado** na AWS: se o principal cair, você liga a cópia em minutos.

- ✅ **Escolha quando:** precisa de **recuperação de desastres rápida** para servidores (RPO de segundos, RTO de minutos).
- 🚫 **Não é a resposta quando:** quer **backups periódicos** com retenção → [AWS Backup](aws-backup.md); quer **migrar de vez** → [Application Migration Service](../migracao/application-migration-service.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "recuperar em minutos", "replicação contínua", "recuperação de desastres", "RPO baixo".
<!-- didatico:fim -->

## Como funciona

1. Instala-se o **agente de replicação** nos servidores de origem.
2. Os discos são replicados continuamente (nível de bloco) para uma *staging area* barata na AWS (instâncias pequenas + EBS).
3. Em um desastre ou teste, o DRS **lança instâncias de recuperação** totalmente provisionadas — **RPO de segundos (normalmente subsegundo), RTO de minutos** ✔️.
4. Depois, *failback* para a origem.

## Configurações importantes

- Point-in-time recovery (útil contra ransomware), *drills* de recuperação sem afetar a produção, launch templates de recuperação.

## Cobrança

- Por servidor de origem replicado por hora + recursos da staging area e das instâncias lançadas.

## ⚠️ Pegadinhas e não confundir

- **DRS** (DR contínuo, RPO/RTO baixos) × **AWS Backup** (backups periódicos) × **Application Migration Service** (migração única — mesma tecnologia, outro objetivo).
- Estratégias de DR (Backup & Restore → Pilot Light → Warm Standby → Multi-site): DRS se aproxima de *pilot light* com custo baixo.

## ❓ Perguntas típicas

- "Recuperar servidores on-premises na AWS em minutos após um desastre." → Elastic Disaster Recovery.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Servidores origem, agente, área de staging e recovery instances |
| **O que você decide/configura?** | Rede de replicação, destino e configuração de lançamento |
| **Em que ordem as coisas acontecem?** | Replica blocos, permite testes e lança recuperação quando necessária |
| **O que pode fazer, e em que condição?** | Ajuda a reduzir perda de dados e tempo de recuperação de servidores compatíveis |
| **O que não pode presumir?** | RTO/RPO dependem do ambiente; replicação não substitui backup histórico |

**Caso comentado:** Recuperar servidores após desastre: DRS; migrar definitivamente: avalie a ferramenta de migração.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)
