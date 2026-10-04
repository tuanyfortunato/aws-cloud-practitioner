# AWS Elastic Beanstalk

> **Categoria:** Computação / PaaS · **Domínio:** 1 (modelos de serviço) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)
>
> **Em uma frase:** você envia o código e o Beanstalk provisiona e gerencia capacidade, balanceamento, escalonamento e monitoramento.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Desenvolvedores que querem publicar aplicações web **sem pensar em infraestrutura**.
- Plataformas: Java, .NET (Windows e Linux), Node.js, Python, PHP, Ruby, Go, Docker, Tomcat.

## Conceitos e componentes

| Componente | O que é |
|---|---|
| **Application** | Conjunto de versões e ambientes. |
| **Application version** | Pacote de código (zip no S3). |
| **Environment** | Recursos rodando uma versão: **Web server** (com ELB + ASG) ou **Worker** (consome fila SQS). |
| **Platform** | Combinação de SO, runtime e servidor web, atualizada pela AWS (*managed platform updates*). |
| **`.ebextensions` / platform hooks** | Personalização da configuração. |

## Configurações e opções importantes

| Opção | Detalhe |
|---|---|
| **Tipo de ambiente** | Single instance (barato, dev) ou load balanced (produção). |
| **Políticas de deploy** | All at once, Rolling, Rolling with additional batch, **Immutable**, Traffic splitting (canary); **blue/green** trocando o CNAME entre ambientes. |
| **Monitoramento** | Health básico ou *enhanced health*. |
| **Acesso** | Você continua com acesso total aos recursos criados (EC2, ELB, RDS…). |

## Cobrança

- **Sem custo adicional** — paga só os recursos que ele cria (EC2, ELB, S3, RDS…).

## Segurança e responsabilidade compartilhada

- **AWS:** provisionamento, atualizações de plataforma (quando ativadas), orquestração.
- **Cliente:** código, configuração, dados, IAM, security groups.

## ⚠️ Pegadinhas e não confundir

- **Beanstalk × CloudFormation:** Beanstalk = sobe *a aplicação* sem pensar em infra; CloudFormation = descreve *qualquer infraestrutura* como código (o Beanstalk usa CloudFormation por baixo).
- **Beanstalk × Lightsail:** PaaS que escala × servidor simples de preço fixo.

## ❓ Perguntas típicas

- "Desenvolvedor quer só subir o código Java e deixar a AWS cuidar de capacidade e balanceamento." → Elastic Beanstalk.
- "O Elastic Beanstalk tem custo próprio?" → Não.
- "Qual modelo de serviço o Beanstalk representa?" → PaaS.

## 🔗 Documentação oficial

- [Guia do Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
