<!-- autoral -->

# AWS Elastic Beanstalk

> **Categoria:** Computação (PaaS) · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** você envia o código, e o Elastic Beanstalk cria e gerencia instâncias, balanceamento, escalonamento e monitoramento para rodá-lo.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) · base em [1.1 O que é computação em nuvem](../../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Um desenvolvedor terminou o site de inscrições para um evento da escola e quer vê-lo no ar. Montar o ambiente à mão exige criar instâncias, um balanceador, um grupo do Auto Scaling e o monitoramento, peças das [aulas 3.3](../../docs/03-tecnologia-e-servicos/03-ec2.md) e [3.4](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md), e ele só quer cuidar do código.

O Elastic Beanstalk é a **plataforma como serviço** (PaaS) da [aula 1.1](../../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) dentro da AWS. Você envia o pacote com o código, e ele cria e configura os recursos, monitora a saúde do ambiente e escala com a demanda. Os recursos ficam na sua conta, então você continua podendo vê-los e ajustá-los.

O limite: o Elastic Beanstalk monta recursos que continuam existindo e sendo cobrados. Ele reduz o trabalho de montar o ambiente, mas não é serverless.

## Como funciona

1. Você cria uma aplicação no Elastic Beanstalk e envia o pacote com o código.
2. Ele cria o ambiente: instâncias do EC2 (ou um cluster do EKS), balanceador de carga e escalonamento automático.
3. Ele monitora a saúde do ambiente e escala as instâncias com a demanda.
4. Para uma versão nova, você envia outro pacote, e o Elastic Beanstalk atualiza o ambiente.

## Opções principais

| Opção | O que faz | Quando lembrar |
|---|---|---|
| Modo Standard | Roda a aplicação direto em instâncias do EC2 | O caso comum |
| Modo Cluster | Roda a aplicação no Amazon EKS | Aplicações que vão para Kubernetes sem que a equipe o monte |
| Plataformas | Go, Java, .NET, Node.js, PHP, Python, Ruby e containers Docker | "Linguagem X sem administrar servidores" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Cobrança própria do Elastic Beanstalk | Nenhuma | 06/10/2026 |

## Como é cobrado

O Elastic Beanstalk não tem cobrança adicional: você paga os recursos que ele cria, como as instâncias do EC2, o balanceador e os buckets do S3, sem taxa mínima nem compromisso. Um ambiente ligado sem acessos continua pagando as instâncias e o balanceador.

## Não confundir com

| Serviço | Diferença para o Elastic Beanstalk | Pista no enunciado |
|---|---|---|
| [Amazon EC2](ec2.md) | Você monta e administra cada instância | "Controle do sistema operacional" |
| [Amazon Lightsail](lightsail.md) | Servidor e recursos prontos num plano com preço mensal previsível | "Preço fixo", "projeto simples" |
| [AWS CloudFormation](../gerenciamento/cloudformation.md) | Cria qualquer conjunto de recursos a partir de um modelo em código (infraestrutura como código) | "Modelo", "infraestrutura como código" |
| [AWS Lambda](lambda.md) | Serverless: roda funções por evento, sem instâncias | "Sem servidores", "cobrar só quando roda" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [Preços do AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
