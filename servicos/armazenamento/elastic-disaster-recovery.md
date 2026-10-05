# AWS Elastic Disaster Recovery (AWS DRS)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma falha grave pode interromper os servidores de uma empresa. Ela precisa de uma forma de recuperar suas aplicações na AWS, além de simplesmente guardar arquivos.

**Como este serviço ajuda?** Elastic Disaster Recovery replica dados de servidores compatíveis para preparar sua recuperação em máquinas AWS. O processo inclui configuração, testes e acionamento da recuperação.

**Exemplo do dia a dia:** Uma empresa prepara a recuperação de seu sistema interno e realiza um teste para verificar se consegue iniciar os servidores necessários na AWS.

**O que ele não resolve sozinho?** Replicar dados não garante que todas as dependências e conexões da aplicação estejam prontas. É preciso planejar a recuperação e manter os requisitos do serviço.

**Primeiras palavras para entender:**

- **Desastre:** interrupção grave do ambiente.
- **Replicação:** manter outra cópia atualizada.
- **Recuperação:** voltar a disponibilizar o sistema.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Recuperação de desastres · **Domínio:** 1 (DR) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** replica servidores continuamente (on-premises, outra nuvem ou outra região AWS) para a AWS e permite recuperá-los em minutos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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
