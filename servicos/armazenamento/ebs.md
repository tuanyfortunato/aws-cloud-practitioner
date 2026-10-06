# Amazon EBS (Elastic Block Store) e Instance Store

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma máquina virtual precisa de um lugar para guardar seu sistema operacional e os arquivos que seus programas usam como num disco.

**Como este serviço ajuda?** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis. A ficha também compara o disco local temporário chamado instance store.

**Exemplo do dia a dia:** Uma aplicação instalada em EC2 grava seus arquivos em um volume EBS. A equipe cria cópias desse volume para ajudar na recuperação.

**O que ele não resolve sozinho?** EBS não deve ser confundido com uma pasta compartilhada para muitas máquinas. Discos locais instance store podem perder seus dados com ações do ciclo de vida da máquina.

**Primeiras palavras para entender:**

- **Volume:** disco virtual.
- **Snapshot:** cópia de um volume em determinado momento.
- **Persistente:** dado que pode continuar existindo além de uma execução.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Armazenamento em bloco · **Domínio:** 3 · **Escopo:** **AZ** (volume) · Regional (snapshots) · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** discos virtuais persistentes, em rede, para instâncias EC2 — como um HD/SSD que sobrevive ao desligamento.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Escolha a capacidade e o comportamento de armazenamento e crie um volume compatível com a máquina.

**Passo 2.** Conecte e prepare o disco no sistema operacional. A aplicação passa a ler e gravar arquivos nele.

**Passo 3.** Planeje cópias e exclusão. O volume pode continuar existindo e sendo cobrado mesmo quando a máquina deixa de executar.

## 2. Recursos e opções, com significado

### Para que serve

Volume raiz (boot) das instâncias; discos de bancos de dados instalados no EC2; aplicações que precisam de sistema de arquivos em bloco.

### Tipos de volume

| Tipo | Mídia | Uso | Destaques | Boot? |
|---|---|---|---|---|
| **gp3** | SSD uso geral | Maioria das cargas | IOPS e throughput **configuráveis independentemente do tamanho** (base 3.000 IOPS e 125 MB/s em qualquer tamanho; hoje até 64 TB e 80.000 IOPS 🧊); mais barato que gp2 | Sim |
| **gp2** | SSD uso geral | Legado | IOPS proporcional ao tamanho (3 IOPS/GB, com burst) | Sim |
| **io2 Block Express / io1** | SSD IOPS provisionado | Bancos críticos, latência sub-ms | Maior durabilidade (io2: 99,999%); **Multi-Attach** | Sim |
| **st1** | HDD otimizado p/ throughput | Big data, logs, data warehouse | Throughput alto e barato | **Não** |
| **sc1** | HDD frio | Dados raramente acessados | O mais barato | **Não** |

### Conceitos e configurações

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

### Instance store

Disco **físico local** do host: altíssimo desempenho, **sem custo extra** (incluso na instância).

**Efêmero:** dados perdidos ao **parar, hibernar ou encerrar** a instância ou se o hardware falhar (sobrevivem ao reboot).

Uso: cache, buffers, dados temporários, réplicas de dados (ex.: nós de banco NoSQL replicados).

### Limites e números

📌 Multi-Attach: io1/io2, 16 instâncias, mesma AZ.

🧊 Tamanhos máximos, IOPS e throughput por tipo — não decorar.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

EBS não deve ser confundido com uma pasta compartilhada para muitas máquinas. Discos locais instance store podem perder seus dados com ações do ciclo de vida da máquina.

### ⚠️ Pegadinhas e não confundir

Volume EBS **não** pode ser usado diretamente em outra AZ → snapshot + novo volume.

"Muitas instâncias em várias AZs, mesmos arquivos" → **EFS**, não EBS.

EBS × instance store: persistente × efêmero.

"500 GB provisionados, 100 GB usados" → paga **500 GB**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Pelo **volume provisionado** (GB-mês), **mesmo que esteja vazio**; gp3/io também por IOPS/throughput provisionados.

Snapshots: GB-mês armazenado (só os blocos alterados).

### Segurança e responsabilidade compartilhada

**AWS:** replicação e disponibilidade do volume dentro da AZ.

**Cliente:** ativar criptografia, fazer snapshots/backup, controlar quem anexa/compartilha snapshots (⚠️ snapshot público é check do Trusted Advisor).

## 5. Caso resolvido: ligando as peças

Uma aplicação instalada numa máquina EC2 precisa de um disco para seu sistema e seus arquivos. O objetivo é leitura e escrita pelo sistema operacional, não operações de objetos como no S3.

A equipe escolhe um volume compatível, conecta-o à instância e prepara seu uso no sistema. Os arquivos ficam no volume. Snapshots ajudam a conservar pontos de recuperação, mas sua criação e sua restauração são operações distintas.

Parar a computação pode manter o disco e seu custo. Encerrar a instância exige examinar as políticas de exclusão dos volumes. Instance store é armazenamento local temporário com outro ciclo de vida; não deve receber a única cópia de dados essenciais que precisam sobreviver a essas ações.

**Recursos envolvidos:** Volume de bloco, anexação à EC2, tipos de volume e snapshots.

**Decisões que precisam ser tomadas:** AZ, capacidade, desempenho, criptografia e DeleteOnTermination.

**Outra situação comentada:** Disco do SO de EC2: EBS; arquivos compartilhados em AZs distintas: avalie EFS.

**Por que não concluir mais do que isso:** Não é sistema de arquivos NFS multi-AZ; Multi-Attach tem requisitos específicos

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Armazenamento em bloco persistente para EC2."

**Resposta curta:** EBS.

**Pergunta:** "Mover um volume para outra AZ."

**Resposta curta:** Snapshot e novo volume na AZ de destino.

**Pergunta:** "Onde ficam os snapshots?"

**Resposta curta:** No S3, incrementais, regionais.

**Pergunta:** "Disco para banco crítico com IOPS altos."

**Resposta curta:** io2.

**Pergunta:** "Disco mais barato para dados frios."

**Resposta curta:** sc1.

**Pergunta:** "O que acontece com o instance store ao parar a instância?"

**Resposta curta:** Dados perdidos.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)
- [Tipos de volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
