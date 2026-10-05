# Amazon EBS (Elastic Block Store) e Instance Store

> **Categoria:** Armazenamento em bloco · **Domínio:** 3 · **Escopo:** **AZ** (volume) · Regional (snapshots) · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** discos virtuais persistentes, em rede, para instâncias EC2 — como um HD/SSD que sobrevive ao desligamento.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **HD/SSD do seu computador virtual**: fica preso a uma máquina (e a uma AZ) e guarda os dados mesmo quando ela é desligada.

- ✅ **Escolha quando:** precisa de **disco persistente para uma instância EC2** (sistema operacional, banco instalado no EC2).
- 🚫 **Não é a resposta quando:** vários servidores precisam dos **mesmos arquivos** → [EFS](efs.md); quer guardar **arquivos acessados pela internet** → [S3](s3.md); dados **temporários** e muito rápidos → *instance store*, nesta ficha.
- 🎯 **Palavras do enunciado que apontam para ele:** "armazenamento em bloco", "disco da instância", "snapshot", "IOPS", "volume".
<!-- didatico:fim -->

## Para que serve

- Volume raiz (boot) das instâncias; discos de bancos de dados instalados no EC2; aplicações que precisam de sistema de arquivos em bloco.

## Tipos de volume

| Tipo | Mídia | Uso | Destaques | Boot? |
|---|---|---|---|---|
| **gp3** | SSD uso geral | Maioria das cargas | IOPS e throughput **configuráveis independentemente do tamanho** (base 3.000 IOPS e 125 MB/s em qualquer tamanho; hoje até 64 TB e 80.000 IOPS 🧊); mais barato que gp2 | Sim |
| **gp2** | SSD uso geral | Legado | IOPS proporcional ao tamanho (3 IOPS/GB, com burst) | Sim |
| **io2 Block Express / io1** | SSD IOPS provisionado | Bancos críticos, latência sub-ms | Maior durabilidade (io2: 99,999%); **Multi-Attach** | Sim |
| **st1** | HDD otimizado p/ throughput | Big data, logs, data warehouse | Throughput alto e barato | **Não** |
| **sc1** | HDD frio | Dados raramente acessados | O mais barato | **Não** |

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Escopo** | Preso a **uma AZ**; ligado a uma instância por vez (exceto Multi-Attach). |
| **Multi-Attach** | 📌 Só **io1/io2**, até **16 instâncias Nitro** na **mesma AZ**. |
| **Durabilidade** | Replicado dentro da AZ (gp/st/sc: 99,8–99,9%; io2: 99,999%). |
| **Snapshots** | **Incrementais**, armazenados no S3 (gerenciado pela AWS), **regionais**, copiáveis entre regiões e contas. Criam volumes em qualquer AZ. |
| **Fast Snapshot Restore** | Volume criado do snapshot já com desempenho total (pago). |
| **Snapshot Archive** | Camada de arquivamento até 75% mais barata (restauração em 24–72 h). |
| **Recycle Bin** | Recupera snapshots/AMIs apagados por engano dentro do período de retenção. |
| **Data Lifecycle Manager** | Automatiza criação, retenção e cópia de snapshots (ou use AWS Backup). |
| **Criptografia** | AES-256 com KMS (volume, snapshots e tráfego para a instância). **Encryption by default** pode ser ativada por região. Volume não criptografado → copie o snapshot com criptografia. |
| **Elastic Volumes** | Aumentar tamanho, mudar tipo e IOPS **sem parar** a instância. |
| **DeleteOnTermination** | Volume raiz é apagado ao encerrar a instância (padrão); volumes adicionais, não. |

## Instance store

- Disco **físico local** do host: altíssimo desempenho, **sem custo extra** (incluso na instância).
- **Efêmero:** dados perdidos ao **parar, hibernar ou encerrar** a instância ou se o hardware falhar (sobrevivem ao reboot).
- Uso: cache, buffers, dados temporários, réplicas de dados (ex.: nós de banco NoSQL replicados).

## Limites e números

- 📌 Multi-Attach: io1/io2, 16 instâncias, mesma AZ.
- 🧊 Tamanhos máximos, IOPS e throughput por tipo — não decorar.

## Cobrança

- Pelo **volume provisionado** (GB-mês), **mesmo que esteja vazio**; gp3/io também por IOPS/throughput provisionados.
- Snapshots: GB-mês armazenado (só os blocos alterados).

## Segurança e responsabilidade compartilhada

- **AWS:** replicação e disponibilidade do volume dentro da AZ.
- **Cliente:** ativar criptografia, fazer snapshots/backup, controlar quem anexa/compartilha snapshots (⚠️ snapshot público é check do Trusted Advisor).

## ⚠️ Pegadinhas e não confundir

- Volume EBS **não** pode ser usado diretamente em outra AZ → snapshot + novo volume.
- "Muitas instâncias em várias AZs, mesmos arquivos" → **EFS**, não EBS.
- EBS × instance store: persistente × efêmero.
- "500 GB provisionados, 100 GB usados" → paga **500 GB**.

## ❓ Perguntas típicas

- "Armazenamento em bloco persistente para EC2." → EBS.
- "Mover um volume para outra AZ." → Snapshot e novo volume na AZ de destino.
- "Onde ficam os snapshots?" → No S3, incrementais, regionais.
- "Disco para banco crítico com IOPS altos." → io2.
- "Disco mais barato para dados frios." → sc1.
- "O que acontece com o instance store ao parar a instância?" → Dados perdidos.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Volume de bloco, anexação à EC2, tipos de volume e snapshots |
| **O que você decide/configura?** | AZ, capacidade, desempenho, criptografia e DeleteOnTermination |
| **Em que ordem as coisas acontecem?** | Crie na AZ compatível, anexe, formate/use; snapshots geram pontos de recuperação |
| **O que pode fazer, e em que condição?** | Pode persistir dados além da vida da EC2 se configurado para preservação |
| **O que não pode presumir?** | Não é sistema de arquivos NFS multi-AZ; Multi-Attach tem requisitos específicos |

**Caso comentado:** Disco do SO de EC2: EBS; arquivos compartilhados em AZs distintas: avalie EFS.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)
- [Tipos de volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
