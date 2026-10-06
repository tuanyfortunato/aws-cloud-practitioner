<!-- autoral -->

# Classes de armazenamento do S3 (incluindo S3 Glacier)

> **Categoria:** Armazenamento de objetos · **Domínio:** 3 e 4 (custos) · **Abrangência:** Por objeto · **Ficha:** núcleo
>
> **Em uma frase:** cada classe troca preço de armazenamento por custo e tempo de recuperação; escolha pelo quanto o dado é acessado.
>
> **Escopo oficial:** ✅ No escopo (S3 e S3 Glacier) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.8 Amazon S3 — armazenamento de objetos](../../docs/03-tecnologia-e-servicos/08-s3.md) · custos em [4.3 Como outros recursos são cobrados](../../docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

As fotos do sistema da escola são abertas todo dia; os boletins de anos atrás, guardados por obrigação legal, quase nunca. Pagar o mesmo preço para guardar os dois desperdiça dinheiro.

Cada objeto do [S3](s3.md) tem uma **classe de armazenamento**. Quanto menos o dado é acessado, mais barato é guardá-lo, e mais caro ou demorado é buscá-lo. Uma **configuração de ciclo de vida** muda os objetos de classe (transição) e os apaga (expiração) sozinha; o **Intelligent-Tiering** faz a troca objeto a objeto quando o padrão de acesso é desconhecido.

O limite: as classes baratas cobram por GB recuperado e têm **prazo mínimo**. Apagar ou mover o objeto antes do prazo gera cobrança pelo prazo inteiro. Nas classes Glacier Flexible Retrieval e Deep Archive, o objeto precisa ser restaurado antes de ser lido.

## Como funciona

1. Sem escolha explícita, o objeto vai para o S3 Standard.
2. Você escolhe a classe no envio ou define regras de ciclo de vida para o bucket.
3. Uma regra de **transição** muda a classe depois de um tempo (por exemplo, Standard-IA após 30 dias).
4. Uma regra de **expiração** apaga o objeto, por exemplo ao fim do prazo legal.

## Opções principais

| Classe | Para que serve | AZs | Prazo mínimo | Recuperação |
|---|---|---|---|---|
| S3 Standard | Acesso frequente | 3 ou mais | Nenhum | Milissegundos, sem taxa |
| S3 Intelligent-Tiering | Acesso desconhecido ou que muda | 3 ou mais | Nenhum | Sem taxa; taxa mensal de monitoramento por objeto |
| S3 Express One Zone | Aplicações muito sensíveis a latência | 1 | Nenhum | Milissegundos de um dígito |
| S3 Standard-IA | Pouco acesso (cerca de uma vez por mês), mas rápido | 3 ou mais | 30 dias | Milissegundos, com taxa por GB |
| S3 One Zone-IA | Pouco acesso, dado que pode ser recriado | 1 | 30 dias | Milissegundos, com taxa por GB |
| S3 Glacier Instant Retrieval | Arquivo acessado cerca de uma vez por trimestre | 3 ou mais | 90 dias | Milissegundos, com taxa por GB |
| S3 Glacier Flexible Retrieval | Arquivo acessado uma ou duas vezes por ano | 3 ou mais | 90 dias | Restauração de minutos a 12 horas |
| S3 Glacier Deep Archive | Arquivo de longo prazo, menos de uma vez por ano | 3 ou mais | 180 dias | Restauração em até 12 horas (padrão) ou 48 horas (em massa) |

"IA" quer dizer *infrequent access*. As classes de uma zona só perdem os dados se a zona for destruída.

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Durabilidade de todas as classes da tabela | 11 noves | 06/10/2026 |
| Prazo mínimo: Standard-IA e One Zone-IA | 30 dias | 06/10/2026 |
| Prazo mínimo: Glacier Instant e Flexible Retrieval | 90 dias | 06/10/2026 |
| Prazo mínimo: Glacier Deep Archive | 180 dias | 06/10/2026 |
| Tamanho mínimo cobrado nas classes IA e Glacier Instant Retrieval | 128 KB | 06/10/2026 |
| Restauração no Glacier Flexible Retrieval | Acelerada 1–5 min · padrão 3–5 h · em massa 5–12 h (gratuita) | 06/10/2026 |

## Como é cobrado

O preço por GB guardado cai a cada classe, e o custo de buscar sobe: taxa por GB recuperado nas classes IA e Glacier, prazo mínimo e tamanho mínimo cobrado. O Intelligent-Tiering não cobra recuperação, mas cobra uma pequena taxa mensal de monitoramento por objeto; objetos menores que 128 KB não são monitorados e ficam na camada de acesso frequente. As transições do ciclo de vida são cobradas por requisição. O S3 Glacier Deep Archive é a opção de armazenamento mais barata da AWS.

## Não confundir com

| Serviço | Diferença para as classes do S3 | Pista no enunciado |
|---|---|---|
| [Amazon S3](s3.md) | O serviço em si; a classe é uma propriedade de cada objeto | "Guardar arquivos" |
| [AWS Backup](aws-backup.md) | Centraliza backups de vários serviços, com armazenamento frio próprio | "Gerenciar backups num só lugar" |
| [AWS Storage Gateway](storage-gateway.md) | O Tape Gateway arquiva fitas virtuais no Glacier para o software de backup local | "Substituir fitas físicas" |
| [Amazon EFS](efs.md) | Tem classes próprias (Standard, Infrequent Access e Archive) para arquivos compartilhados | "Pasta compartilhada pouco acessada" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Classes de armazenamento do S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [Classes S3 Glacier](https://docs.aws.amazon.com/AmazonS3/latest/userguide/glacier-storage-classes.html)
- [Ciclo de vida dos objetos](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Preços do Amazon S3](https://aws.amazon.com/s3/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
