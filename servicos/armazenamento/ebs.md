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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **sistema operacional:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.


**Passo 1.** Escolha a capacidade e o comportamento de armazenamento e crie um volume compatível com a máquina.

**Passo 2.** Conecte e prepare o disco no sistema operacional. A aplicação passa a ler e gravar arquivos nele.

**Passo 3.** Planeje cópias e exclusão. O volume pode continuar existindo e sendo cobrado mesmo quando a máquina deixa de executar.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.


Volume raiz (boot) das instâncias; discos de bancos de dados instalados no EC2; aplicações que precisam de sistema de arquivos em bloco.

### Tipos de volume

**Antes de ler este trecho:**

- **IOPS:** Quantidade de operações de leitura e escrita por segundo. Ajuda a descrever o comportamento de um armazenamento, mas não mede sozinha a quantidade de bytes transferidos.
- **throughput:** Quantidade de dados ou de trabalho processada por unidade de tempo. É diferente de latência, que mede quanto uma operação demora.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **SSD:** Tipo de armazenamento sem partes mecânicas, usado para acesso rápido a dados. A escolha de um volume também envolve sua capacidade e limites de desempenho.
- **GB / MB / TB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **data warehouse:** Ambiente de dados organizado para análise de grandes conjuntos. O modelo e as consultas são orientados a perguntas analíticas.
- **durabilidade:** Capacidade de preservar os dados armazenados. É diferente de disponibilidade, que trata de conseguir acessá-los quando necessário.
- **provisionado:** Recurso ou capacidade já disponibilizado para uso. Em algumas cobranças, a disponibilidade mantida importa mesmo sem execução de trabalho de negócio.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.
- **HDD:** Armazenamento por disco mecânico. Seu comportamento difere de SSD; a necessidade de acesso orienta a escolha.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Tipo | Mídia | Uso | Destaques | Boot? |
|---|---|---|---|---|
| **gp3** | SSD uso geral | Maioria das cargas | IOPS e throughput **configuráveis independentemente do tamanho** (base 3.000 IOPS e 125 MB/s em qualquer tamanho; hoje até 64 TB e 80.000 IOPS 🧊); mais barato que gp2 | Sim |
| **gp2** | SSD uso geral | Legado | IOPS proporcional ao tamanho (3 IOPS/GB, com burst) | Sim |
| **io2 Block Express / io1** | SSD IOPS provisionado | Bancos críticos, latência sub-ms | Maior durabilidade (io2: 99,999%); **Multi-Attach** | Sim |
| **st1** | HDD otimizado p/ throughput | Big data, logs, data warehouse | Throughput alto e barato | **Não** |
| **sc1** | HDD frio | Dados raramente acessados | O mais barato | **Não** |

### Conceitos e configurações

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **AWS Backup:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **snapshot:** Cópia de estado de um recurso em determinado momento, conforme o serviço. Restauração pode criar um novo recurso; não presuma uma máquina pronta e instantânea.
- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.
- **AES-256:** Algoritmo de criptografia com chave de 256 bits. Esse nome descreve a tecnologia de proteção; autorização e administração das chaves continuam necessárias.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **NoSQL:** Família de modelos de banco que não se limita à estrutura relacional tradicional. Não significa ausência de estrutura ou que todo produto NoSQL faz o mesmo trabalho.


Uso: cache, buffers, dados temporários, réplicas de dados (ex.: nós de banco NoSQL replicados).

### Limites e números

📌 Multi-Attach: io1/io2, 16 instâncias, mesma AZ.


🧊 Tamanhos máximos, IOPS e throughput por tipo — não decorar.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **instance store:** Armazenamento local temporário da máquina física. Não é lugar seguro para a única cópia de dados que precisam sobreviver às ações descritas no ciclo de vida.


EBS não deve ser confundido com uma pasta compartilhada para muitas máquinas. Discos locais instance store podem perder seus dados com ações do ciclo de vida da máquina.

### ⚠️ Pegadinhas e não confundir

Volume EBS **não** pode ser usado diretamente em outra AZ → snapshot + novo volume.

**Antes de ler este trecho:**

- **EFS:** O EFS oferece um sistema de arquivos compartilhado.


"Muitas instâncias em várias AZs, mesmos arquivos" → **EFS**, não EBS.


EBS × instance store: persistente × efêmero.


"500 GB provisionados, 100 GB usados" → paga **500 GB**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Pelo **volume provisionado** (GB-mês), **mesmo que esteja vazio**; gp3/io também por IOPS/throughput provisionados.


Snapshots: GB-mês armazenado (só os blocos alterados).

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.


**AWS:** replicação e disponibilidade do volume dentro da AZ.

**Antes de ler este trecho:**

- **Trusted Advisor:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.


**Cliente:** ativar criptografia, fazer snapshots/backup, controlar quem anexa/compartilha snapshots (⚠️ snapshot público é check do Trusted Advisor).

## 5. Caso resolvido: ligando as peças


Uma aplicação instalada numa máquina EC2 precisa de um disco para seu sistema e seus arquivos. O objetivo é leitura e escrita pelo sistema operacional, não operações de objetos como no S3.

A equipe escolhe um volume compatível, conecta-o à instância e prepara seu uso no sistema. Os arquivos ficam no volume. Snapshots ajudam a conservar pontos de recuperação, mas sua criação e sua restauração são operações distintas.

Parar a computação pode manter o disco e seu custo. Encerrar a instância exige examinar as políticas de exclusão dos volumes. Instance store é armazenamento local temporário com outro ciclo de vida; não deve receber a única cópia de dados essenciais que precisam sobreviver a essas ações.

**Recursos envolvidos:** Volume de bloco, anexação à EC2, tipos de volume e snapshots.

**Decisões que precisam ser tomadas:** AZ, capacidade, desempenho, criptografia e DeleteOnTermination.

**Antes de ler este trecho:**

- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **NFS:** NFS e SMB são protocolos para acesso a arquivos compartilhados. POSIX descreve interfaces e comportamentos de sistemas. Compatibilidade importa para a aplicação usar os arquivos corretamente.


**Outra situação comentada:** Disco do SO de EC2: EBS; arquivos compartilhados em AZs distintas: avalie EFS.

**Por que não concluir mais do que isso:** Não é sistema de arquivos NFS multi-AZ; Multi-Attach tem requisitos específicos

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma máquina virtual precisa de um lugar para guardar seu sistema operacional e os arquivos que seus programas usam como num disco.

**2. O que a solução fornece?**

O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis. A ficha também compara o disco local temporário chamado instance store.

**3. Que conclusão seria incorreta?**

EBS não deve ser confundido com uma pasta compartilhada para muitas máquinas. Discos locais instance store podem perder seus dados com ações do ciclo de vida da máquina.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Armazenamento em bloco persistente para EC2."

**Resposta curta:** EBS.


**Fundamento explicado no capítulo:** "Armazenamento em bloco persistente para EC2." → EBS.

**Pergunta:** "Mover um volume para outra AZ."

**Resposta curta:** Snapshot e novo volume na AZ de destino.


**Fundamento explicado no capítulo:** "Mover um volume para outra AZ." → Snapshot e novo volume na AZ de destino.

**Pergunta:** "Onde ficam os snapshots?"

**Resposta curta:** No S3, incrementais, regionais.


**Fundamento explicado no capítulo:** "Onde ficam os snapshots?" → No S3, incrementais, regionais.

**Pergunta:** "Disco para banco crítico com IOPS altos."

**Resposta curta:** io2.


**Fundamento explicado no capítulo:** "Disco para banco crítico com IOPS altos." → io2.

**Pergunta:** "Disco mais barato para dados frios."

**Resposta curta:** sc1.


**Fundamento explicado no capítulo:** "Disco mais barato para dados frios." → sc1.

**Pergunta:** "O que acontece com o instance store ao parar a instância?"

**Resposta curta:** Dados perdidos.


**Fundamento explicado no capítulo:** "O que acontece com o instance store ao parar a instância?" → Dados perdidos.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)
- [Tipos de volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
