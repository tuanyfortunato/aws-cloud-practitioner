<!-- autoral -->

# Amazon EFS (Elastic File System)

> **Categoria:** Armazenamento de arquivos · **Domínio:** 3 · **Abrangência:** Regional (várias zonas) ou One Zone · **Ficha:** núcleo
>
> **Em uma frase:** sistema de arquivos NFS serverless e elástico, montado ao mesmo tempo por várias instâncias, containers e funções Linux.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

As instâncias do portal da escola precisam ler e gravar a mesma pasta de materiais didáticos. Um volume do [EBS](ebs.md) serve uma instância numa zona só, e copiar os arquivos para cada máquina deixa versões diferentes espalhadas.

O EFS oferece uma pasta compartilhada pelo protocolo **NFS**, comum no Linux. Ele é serverless e elástico: cresce e encolhe sozinho à medida que você adiciona e remove arquivos, até petabytes, sem provisionar capacidade. Instâncias do EC2, containers do ECS e do EKS, o Fargate e o Lambda montam o mesmo sistema de arquivos ao mesmo tempo.

O limite: o EFS **não é suportado em instâncias Windows**. Para uma pasta compartilhada Windows (SMB), a resposta é o [FSx for Windows File Server](fsx.md).

## Como funciona

1. Você cria um sistema de arquivos, regional (recomendado) ou One Zone.
2. As instâncias e containers montam o sistema de arquivos pela rede, como uma pasta comum.
3. Os arquivos novos vão para a classe EFS Standard.
4. Uma política de ciclo de vida move os arquivos pouco usados para EFS Infrequent Access e EFS Archive.

## Opções principais

| Opção | O que faz | Quando lembrar |
|---|---|---|
| Regional | Guarda os dados em várias zonas de disponibilidade | Padrão recomendado; resiste à falha de uma zona |
| One Zone | Guarda os dados numa zona só, por menos | Dados que toleram a perda da zona |
| EFS Standard | SSD, menor latência | Arquivos acessados com frequência |
| EFS Infrequent Access | Classe mais barata para poucos acessos por trimestre | Arquivos pouco usados |
| EFS Archive | Classe para poucos acessos por ano ou menos | Arquivos quase nunca lidos |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Escala máxima | Petabytes, sem provisionar capacidade | 06/10/2026 |
| Protocolo | NFS (sem suporte a instâncias Windows) | 06/10/2026 |

## Como é cobrado

Não há taxa mínima nem de instalação. Você paga pelo armazenamento **usado** (diferente do EBS, que cobra o provisionado), pelas leituras e gravações e pelo movimento entre classes; as classes Infrequent Access e Archive também cobram as leituras. O desempenho pode ser provisionado com antecedência (Provisioned Throughput), com cobrança própria.

## Não confundir com

| Serviço | Diferença para o EFS | Pista no enunciado |
|---|---|---|
| [Amazon EBS](ebs.md) | Disco de uma instância, numa zona, cobrado pelo tamanho provisionado | "Disco da instância" |
| [Amazon FSx](fsx.md) | Sistemas de arquivos conhecidos, como Windows File Server (SMB) | "Windows", "SMB", "NetApp ONTAP" |
| [Amazon S3](s3.md) | Objetos acessados por API, não uma pasta montada | "Fotos, backups, site estático" |
| [AWS Storage Gateway](storage-gateway.md) | Pasta de rede no datacenter do cliente, com os dados na AWS | "Servidores locais", "cache local" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
- [Tipos de sistema de arquivos e classes de armazenamento](https://docs.aws.amazon.com/efs/latest/ug/features.html)
- [Preços do Amazon EFS](https://aws.amazon.com/efs/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
