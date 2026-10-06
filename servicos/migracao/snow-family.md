<!-- autoral -->

# Família AWS Snow

> **Categoria:** Migração / transferência fora da rede · **Domínio:** 3 · **Abrangência:** Dispositivo físico ligado a uma Região · **Ficha:** referência
>
> **Em uma frase:** dispositivos físicos que a AWS enviava ao cliente para levar dados fora da rede e processar na borda; não estão mais disponíveis para novos clientes.
>
> **Escopo oficial:** ⚪ Não listado (saiu da lista atual) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Quando a conexão é lenta demais para enviar dezenas de terabytes, levar os dados num dispositivo físico pode ser mais rápido. Era o papel da **família AWS Snow**, como o AWS Snowball Edge. Hoje a AWS não oferece mais nenhum dispositivo da família para novos pedidos; quem já usa continua usando. A família não aparece na lista do exame.

1. Num trabalho de importação, a AWS enviava um dispositivo vazio ao cliente.
2. O cliente copiava os dados locais para o dispositivo, sem usar a internet, e o devolvia.
3. A AWS transferia os dados para o S3; havia também trabalhos de exportação, no sentido contrário.
4. Para novos clientes, a AWS indica o DataSync (pela rede), o AWS Data Transfer Terminal (um local físico seguro onde o cliente leva seus discos) ou parceiros; para computação na borda, o Outposts.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS DataSync](datasync-e-transfer-family.md) | Transferência de arquivos pela rede | "Copiar arquivos para o S3" |
| [AWS Outposts](../computacao/outposts-local-zones-wavelength.md) | Infraestrutura da AWS no local do cliente, no escopo | "AWS no meu datacenter" |
| [AWS Direct Connect](../redes/direct-connect.md) | Conexão dedicada com a AWS, no escopo | "Conexão privada" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Mudança de disponibilidade do AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html)
- [O que é o AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html)
- [Serviços no escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
