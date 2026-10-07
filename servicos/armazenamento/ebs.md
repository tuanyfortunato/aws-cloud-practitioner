<!-- autoral -->

# Amazon EBS (Elastic Block Store) e instance store

> **Categoria:** Armazenamento em bloco · **Domínio:** 2 (responsabilidade compartilhada) e 3 · **Abrangência:** Zona de disponibilidade (volume); Regional (snapshots) · **Ficha:** núcleo
>
> **Em uma frase:** volumes de disco persistentes, ligados pela rede a instâncias do EC2, que continuam existindo quando a instância para.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) · base em [3.3 Amazon EC2](../../docs/03-tecnologia-e-servicos/03-ec2.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

O banco de dados da escola ainda roda numa instância do EC2 e precisa de um disco: um lugar para instalar programas e gravar dados que continue lá depois de parar e ligar a instância.

Um **volume do EBS** é anexado à instância e usado como um disco rígido local. Ele existe independentemente da instância e fica em **uma zona de disponibilidade**, onde os dados são replicados entre vários servidores. O backup é um **snapshot**, uma cópia incremental de um momento do volume, guardada no S3 e usada para restaurar volumes em outra zona, Região ou conta.

O limite: o volume fica numa zona só e normalmente serve uma instância por vez; para uma pasta compartilhada, o caminho é o [EFS](efs.md). E **a AWS não faz backup automático dos volumes**: criar snapshots é responsabilidade do cliente, à mão, com o Amazon Data Lifecycle Manager ou com o [AWS Backup](aws-backup.md).

## Como funciona

1. Você cria um volume na mesma zona de disponibilidade da instância, escolhendo tipo e tamanho.
2. Anexa o volume à instância, que o usa como um disco.
3. Pode aumentar a capacidade ou ajustar o desempenho sem parar a aplicação (Elastic Volumes).
4. Cria snapshots, que guardam só os blocos que mudaram desde o anterior, e os copia para outra Região ou conta quando precisar.

## Opções principais

| Tipo | O que é | Quando usar |
|---|---|---|
| SSD de uso geral (gp3, gp2) | Equilíbrio entre preço e desempenho | Volume de inicialização, aplicações e bancos médios |
| SSD de IOPS provisionadas (io2 Block Express, io1) | Desempenho alto e constante | Bancos de dados com muita leitura e gravação |
| HDD (st1, sc1) | Grande vazão sequencial, mais barato; não serve como volume de inicialização | Big data, logs, dados pouco acessados |
| Instance store | Disco ligado fisicamente ao servidor da instância, sem custo adicional | Cache e dados temporários que podem ser perdidos |

O instance store mantém os dados quando a instância é reiniciada, mas os perde quando ela é parada, hibernada ou encerrada.

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Durabilidade do io2 Block Express | 99,999% | 06/10/2026 |
| Durabilidade dos outros tipos | De 99,8% a 99,9% | 06/10/2026 |
| Desempenho incluído no gp3 | 3.000 IOPS e 125 MB/s | 06/10/2026 |
| Tamanho máximo de um volume gp3 | 64 TiB | 06/10/2026 |

## Como é cobrado

O EBS cobra por **GB-mês provisionado**: o tamanho do volume criado, cheio ou não, mesmo com a instância parada. No gp3 e no io2, o desempenho provisionado acima do incluído é cobrado à parte. Os snapshots são cobrados pelos dados guardados; como são incrementais, apagar um snapshot nem sempre reduz o custo. O instance store já está incluído no preço da instância.

## Não confundir com

| Serviço | Diferença para o EBS | Pista no enunciado |
|---|---|---|
| [Amazon EFS](efs.md) | Pasta compartilhada por várias instâncias Linux, em várias zonas | "Mesmos arquivos para várias instâncias" |
| [Amazon S3](s3.md) | Objetos acessados pela rede, sem limite de quantidade | "Fotos, backups, site estático" |
| [AWS Backup](aws-backup.md) | Automatiza os snapshots e backups de vários serviços num só lugar | "Centralizar backups" |
| [Amazon FSx](fsx.md) | Sistemas de arquivos gerenciados, como Windows File Server | "Pasta compartilhada Windows" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)
- [Tipos de volume do EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- [Snapshots do EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)
- [Instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Duração dos dados no instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-lifetime.html)
- [Preços do Amazon EBS](https://aws.amazon.com/ebs/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
