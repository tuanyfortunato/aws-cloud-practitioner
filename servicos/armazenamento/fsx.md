<!-- autoral -->

# Amazon FSx

> **Categoria:** Armazenamento de arquivos gerenciado · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** sistemas de arquivos conhecidos, totalmente gerenciados: Windows File Server, Lustre, NetApp ONTAP e OpenZFS.
>
> **Escopo oficial:** 🔀 FSx ✅ · FSx for Lustre ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

A secretaria usa uma pasta compartilhada num servidor Windows, acessada pelo protocolo **SMB**, e quer levá-la para a AWS sem mudar os programas. O **FSx for Windows File Server** oferece servidores de arquivos Windows gerenciados: as aplicações e ferramentas continuam funcionando sem mudança, e a AWS atualiza o software do Windows, trata falhas de hardware e faz backups.

1. Escolhe-se o sistema de arquivos: Windows File Server, Lustre, NetApp ONTAP ou OpenZFS.
2. Cria-se o sistema de arquivos e define-se a capacidade.
3. Os computadores e servidores se conectam pela rede com o protocolo do sistema escolhido, como SMB no Windows.
4. A AWS cuida do hardware, das atualizações e dos backups.

As quatro opções: **Windows File Server** para pastas Windows; **Lustre** para computação de alto desempenho (HPC) e IA, que está fora do escopo da prova; **NetApp ONTAP** e **OpenZFS** para quem já usa esses sistemas.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon EFS](efs.md) | Arquivos por NFS para Linux, elástico | "Linux", "NFS" |
| [Amazon EBS](ebs.md) | Disco em bloco de uma instância | "Volume", "disco da instância" |
| [Amazon S3](s3.md) | Armazenamento de objetos | "Objetos", "bucket" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)
- [Amazon FSx](https://aws.amazon.com/fsx/)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
