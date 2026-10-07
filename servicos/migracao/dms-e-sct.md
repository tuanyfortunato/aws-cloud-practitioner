<!-- autoral -->

# AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)

> **Categoria:** Migração de bancos de dados · **Domínio:** 3 · **Abrangência:** Regional (SCT instalada no computador) · **Ficha:** núcleo
>
> **Em uma frase:** o DMS move os dados de um banco para a AWS, uma vez ou com replicação contínua; a SCT converte o esquema quando o banco muda de motor.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

O banco do sistema financeiro da rede roda em Oracle no datacenter, e a escola quer passar para o Aurora PostgreSQL, sem licença e gerenciado pela AWS. Só que o registro das mensalidades não pode parar, e as tabelas e o código guardado no banco foram escritos para o Oracle.

São dois trabalhos. A **AWS Schema Conversion Tool** (SCT), um programa instalado no computador, **converte o esquema** (tabelas, índices, visões e o código do banco) de um motor para o outro; o próprio DMS oferece o mesmo trabalho com o recurso **DMS Schema Conversion**. Depois, o **AWS Database Migration Service** (DMS) **move os dados** e **replica continuamente as mudanças**, de modo que o Oracle segue atendendo as inscrições até a virada, e a parada fica reduzida a esse momento. O DMS migra bancos relacionais, data warehouses e bancos NoSQL.

O limite: numa **migração homogênea**, de MySQL para RDS for MySQL, não há esquema para converter, e o DMS basta. E o DMS cuida do banco, não do servidor da aplicação; levar servidores como estão é trabalho do [Application Migration Service](application-migration-service.md).

## Como funciona

1. Se o motor muda, a SCT ou o DMS Schema Conversion converte o esquema para o banco de destino.
2. Cria-se a capacidade de replicação do DMS (uma instância ou o modo sem servidor) e os pontos de origem e destino.
3. O DMS copia os dados existentes e passa a replicar as mudanças contínuas.
4. Na virada, a aplicação passa a usar o banco novo, e a replicação é encerrada.

## Opções principais

| Caso | Ferramentas | Exemplo na escola |
|---|---|---|
| Migração homogênea | Só o DMS | MySQL local para RDS for MySQL |
| Migração heterogênea | SCT (ou DMS Schema Conversion) e depois o DMS | Oracle para Aurora PostgreSQL |
| Migração única | DMS copia os dados uma vez | Banco de arquivo morto |
| Replicação contínua | DMS mantém origem e destino sincronizados | Inscrições abertas durante a migração |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| DMS | Move os dados; cobrado por hora de capacidade de replicação | 06/10/2026 |
| DMS Schema Conversion | Paga-se só o armazenamento usado | 06/10/2026 |
| Nível gratuito antigo do DMS | 750 horas de dms.t3.micro, só para contas criadas antes de 15/07/2025 | 06/10/2026 |

## Como é cobrado

No DMS, paga-se por hora da capacidade de replicação usada, com instâncias de replicação ou no modo sem servidor. A SCT é um programa baixado e instalado no computador; o DMS Schema Conversion cobra só pelo armazenamento.

## Não confundir com

| Serviço | Diferença para o DMS | Pista no enunciado |
|---|---|---|
| [AWS Application Migration Service](application-migration-service.md) | Leva o servidor inteiro como está | "Lift and shift", "servidores" |
| [AWS DataSync](datasync-e-transfer-family.md) | Copia arquivos, não bancos em funcionamento | "Arquivos", "compartilhamento de rede" |
| [Família Snow](snow-family.md) | Leva dados em dispositivo físico | "Sem conexão boa", "petabytes" |
| [Amazon RDS](../banco-de-dados/rds.md) | É o destino gerenciado, não a ferramenta de migração | "Banco gerenciado" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
- [O que é a AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
- [Preços do AWS DMS](https://aws.amazon.com/dms/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
