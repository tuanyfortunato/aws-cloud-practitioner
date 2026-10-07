<!-- autoral -->

# Amazon Lightsail

> **Categoria:** Computação simplificada · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** o jeito mais simples de começar na AWS para criar sites e aplicações web, com servidores, bancos e rede reunidos em planos de preço mensal previsível.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Como funciona

A escola de Lisboa quer um site de eventos em WordPress, tem pouca experiência com a AWS e precisa saber quanto vai pagar por mês. O **Lightsail** reúne num só lugar o necessário para isso: instâncias (servidores privados virtuais), containers, bancos gerenciados, distribuição de conteúdo, balanceadores, armazenamento e IPs estáticos.

1. Escolhe-se uma imagem pronta, como WordPress, ou um sistema operacional.
2. Escolhe-se um plano, que já reúne processador, memória, armazenamento e uma franquia de transferência de dados.
3. O Lightsail cria a instância, e o site vai ao ar.
4. Quando precisa, a escola acrescenta banco gerenciado, balanceador ou IP estático no próprio console do Lightsail.

O limite: o Lightsail troca opções por simplicidade. Quando o projeto precisa de controle fino, os serviços completos ([EC2](ec2.md), [ELB](elastic-load-balancing.md), [RDS](../banco-de-dados/rds.md)) oferecem mais.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon EC2](ec2.md) | Servidores com todas as opções e cobrança pelo uso | "Controle total", "tipo de instância" |
| [AWS Elastic Beanstalk](elastic-beanstalk.md) | Sobe e escala uma aplicação a partir do código | "Só enviar o código" |
| [AWS Amplify](../aplicacoes/amplify-e-appsync.md) | Hospeda e cria aplicações web e móveis de front-end | "Front-end", "app móvel" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)
- [Planos de instância do Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-bundles.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
