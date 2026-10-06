<!-- autoral -->

# AWS DataSync e AWS Transfer Family

> **Categoria:** Migração / transferência pela rede · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** referência
>
> **Em uma frase:** o DataSync copia arquivos e objetos pela rede para S3, EFS e FSx; o Transfer Family recebe e envia arquivos por SFTP, FTPS, FTP e AS2.
>
> **Escopo oficial:** 🔀 DataSync ⚪ não listado · Transfer Family ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

A secretaria quer levar dez anos de arquivos digitalizados do servidor local para o S3, e uma empresa parceira envia relatórios todo mês por SFTP. O **AWS DataSync** transfere arquivos e objetos pela rede, com criptografia e conferência de integridade. O **AWS Transfer Family** oferece transferência gerenciada por SFTP, AS2, FTPS, FTP e pelo navegador, direto para o armazenamento da AWS.

1. **DataSync:** liga-se a origem (compartilhamentos NFS e SMB, HDFS, armazenamento de objetos ou outra nuvem) ao destino (S3, EFS ou FSx).
2. O DataSync automatiza a cópia, criptografa os dados e confere a integridade na chegada; serve para migrar, arquivar e replicar.
3. **Transfer Family:** cria-se um servidor gerenciado no protocolo que os parceiros já usam.
4. Os parceiros enviam e recebem arquivos sem mudar a configuração deles, e os arquivos ficam no armazenamento da AWS.

O DataSync não aparece na lista do exame, e o Transfer Family está fora do escopo.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Storage Gateway](../armazenamento/storage-gateway.md) | Acesso local contínuo a armazenamento na AWS, no escopo | "Cache local", "híbrido" |
| [AWS DMS](dms-e-sct.md) | Migra bancos de dados, no escopo | "Migrar o banco" |
| [Família Snow](snow-family.md) | Transferência fora da rede, sem novos pedidos | "Dispositivo físico" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
- [O que é o AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
