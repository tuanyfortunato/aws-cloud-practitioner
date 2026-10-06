<!-- autoral -->

# Amazon EC2 (Elastic Compute Cloud)

> **Categoria:** Computação · **Domínio:** 3 (e 4, nas formas de compra) · **Abrangência:** Regional; cada instância fica numa zona de disponibilidade · **Ficha:** núcleo
>
> **Em uma frase:** servidores virtuais sob demanda, com controle total do sistema operacional (IaaS).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.3 Amazon EC2](../../docs/03-tecnologia-e-servicos/03-ec2.md) · formas de compra na [aula 4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

O sistema de matrícula da escola roda num servidor velho e depende de um sistema operacional específico, com configurações ajustadas ao longo dos anos. A escola quer levá-lo para a nuvem sem reescrever nada, e para isso precisa de um computador onde possa instalar e configurar o que quiser.

O EC2 entrega esse computador: uma **instância** é um servidor virtual criado em minutos, com o processamento, a memória e o disco escolhidos, cobrado enquanto está ligado. A AWS cuida do hardware e da virtualização; o cliente controla o sistema operacional e tudo o que instala nele. É o exemplo clássico de IaaS.

O limite é o outro lado do controle: atualizar o sistema operacional, configurar o firewall e proteger a aplicação são tarefas do cliente, pelo [modelo de responsabilidade compartilhada](../../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md). Para quem não quer cuidar de servidor, existem o Lambda e os containers com Fargate ([aula 3.5](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)).

## Como funciona

1. Você escolhe uma **AMI** (*Amazon Machine Image*), a imagem com o sistema operacional e o software inicial. Uma AMI pertence a uma Região.
2. Escolhe o **tipo de instância**, que define processamento, memória, rede e armazenamento.
3. Define o acesso: um **par de chaves** para entrar na instância, um **grupo de segurança** (o firewall da instância) e, se a aplicação precisar chamar outros serviços, uma função do IAM.
4. Pode passar **dados de usuário** (*user data*), comandos que configuram a instância automaticamente quando ela inicia.
5. A instância inicia e é cobrada por segundo enquanto roda. Depois ela pode ser parada e iniciada de novo, ou encerrada de vez.

## Opções principais

| Categoria de instância | Para que serve | Exemplos de uso |
|---|---|---|
| Uso geral | Equilíbrio entre processamento, memória e rede | Servidores web, repositórios de código |
| Otimizada para computação | Aplicações limitadas pelo processador | Processamento em lote, transcodificação de mídia, servidores de jogos |
| Otimizada para memória | Grandes volumes de dados na memória | Bancos de dados em memória, análise de dados |
| Computação acelerada | GPUs e outros aceleradores | Machine learning, processamento gráfico |
| Otimizada para armazenamento | Muitas leituras e gravações rápidas no disco local | Bancos de alta vazão, processamento de dados |

| Opção | O que é | Quando lembrar |
|---|---|---|
| Volume EBS | Disco durável, que existe independentemente da instância | Dados que precisam sobreviver quando a instância para |
| Instance store | Disco temporário ligado ao computador físico | Cache e arquivos temporários; os dados somem ao parar ou encerrar |
| Instâncias T | Desempenho com intermitência: base de processamento e créditos para passar dela | Cargas quase sempre tranquilas |
| AWS Graviton | Processadores da própria AWS, com a melhor relação preço e desempenho no EC2 | Economia e sustentabilidade |
| Elastic IP | IPv4 público fixo, que pode passar de uma instância para outra | Manter o mesmo endereço público |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Cobrança sob demanda | Por segundo, com mínimo de 60 segundos, para sistemas como Amazon Linux, Windows e Ubuntu | 06/10/2026 |
| Instância Spot | Até 90% de desconto, com aviso de 2 minutos antes da interrupção | 06/10/2026 |
| Savings Plans | Até 66% (Compute) e até 72% (EC2 Instance) | 06/10/2026 |

## Como é cobrado

A instância é cobrada só no estado **em execução**. Parada ou encerrada, o uso não é cobrado, mas os volumes EBS continuam cobrados enquanto existirem, e todo IPv4 público é cobrado por hora, inclusive o Elastic IP sem uso. Ao ser iniciada de novo, a instância parada recebe um novo IPv4 público.

As formas de compra mudam o preço: sob demanda, Savings Plans, instâncias reservadas, Spot, hosts e instâncias dedicadas e reservas de capacidade, todas explicadas na [aula 4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md). Grupos de segurança não têm cobrança adicional.

| Estado | Uso cobrado | EBS | Instance store |
|---|---|---|---|
| Em execução | Sim | Mantido | Mantido |
| Parada | Não | Mantido e cobrado | Apagado |
| Encerrada | Não | Volumes marcados para apagar no encerramento são apagados | Apagado |

## Não confundir com

| Serviço | Diferença para o EC2 | Pista no enunciado |
|---|---|---|
| [AWS Lambda](lambda.md) | Roda código disparado por eventos, sem servidor para administrar, por até 15 minutos | "Sem gerenciar servidores", "quando um arquivo chega" |
| [Amazon Lightsail](lightsail.md) | Servidores e recursos prontos com preço mensal previsível | "Começar simples", "preço fixo" |
| [AWS Elastic Beanstalk](elastic-beanstalk.md) | Recebe o código e cria e gerencia as instâncias e o resto do ambiente | "Só enviar o código" |
| [Amazon RDS](../banco-de-dados/rds.md) | Banco relacional gerenciado: a AWS aplica os patches do sistema e do banco | "Quem aplica patch no banco?" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [Tipos de instância](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
- [Estados da instância e cobrança](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html)
- [Instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Elastic IP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
- [Grupos de segurança](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
- [Preços do EC2](https://aws.amazon.com/ec2/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
