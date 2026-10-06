<!-- autoral -->

# AWS Outposts, Local Zones e Wavelength

> **Categoria:** Infraestrutura híbrida e de borda · **Domínio:** 3 · **Abrangência:** Extensões de uma Região · **Ficha:** complementar
>
> **Em uma frase:** formas de levar a infraestrutura da AWS para mais perto: o Outposts no local do cliente, as Local Zones perto de grandes cidades e o Wavelength na rede das operadoras.
>
> **Escopo oficial:** 🔀 Outposts ✅ · Local Zones ⚪ não listado · Wavelength ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.2 Infraestrutura global](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) · [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

O laboratório da rede processa imagens de microscópio que não podem sair do prédio e precisam de resposta em milissegundos. O **AWS Outposts** instala capacidade de computação e armazenamento da AWS **no local do cliente**, gerenciada pela AWS, com as mesmas APIs e ferramentas das Regiões. Cada Outpost é uma extensão de uma Zona de Disponibilidade e da sua Região.

1. O cliente prepara o local com os requisitos de espaço, energia e rede.
2. A AWS entrega e mantém o equipamento: racks ou servidores de 1U ou 2U, de propriedade da AWS.
3. O Outpost se liga à sua Região por um *service link*.
4. A equipe cria recursos nele com o mesmo console, APIs e ferramentas que usa na Região.

As **Local Zones** colocam computação e armazenamento perto de grandes centros, para baixa latência; não aparecem na lista do exame. O **Wavelength** coloca recursos na borda das redes das operadoras de telecomunicações, para dispositivos móveis, e está fora do escopo.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Storage Gateway](../armazenamento/storage-gateway.md) | Liga o armazenamento local ao armazenamento da AWS | "Acesso local a dados na nuvem" |
| [Amazon CloudFront](../redes/cloudfront.md) | Entrega conteúdo pelos pontos de presença | "Cache perto do usuário" |
| [AWS Direct Connect](../redes/direct-connect.md) | Conexão dedicada até a AWS, sem levar recursos ao local | "Conexão privada dedicada" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html)
- [O que são as AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html)
- [O que é o AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
