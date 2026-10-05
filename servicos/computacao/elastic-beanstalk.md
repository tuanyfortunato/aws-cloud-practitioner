# AWS Elastic Beanstalk

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Você tem uma aplicação pronta, mas configurar máquinas, balanceamento e acompanhamento da execução manualmente pode tomar tempo.

**Como este serviço ajuda?** O Elastic Beanstalk ajuda a implantar aplicações em plataformas compatíveis, provisionando e coordenando recursos AWS para esse ambiente. Você entrega o código e define opções do ambiente.

**Exemplo do dia a dia:** Uma equipe envia sua aplicação web para um ambiente Beanstalk. O serviço organiza a infraestrutura necessária para disponibilizá-la.

**O que ele não resolve sozinho?** Você continua responsável pelo código e por decisões de configuração. Os recursos criados continuam tendo custos; Beanstalk não torna a infraestrutura gratuita.

**Primeiras palavras para entender:**

- **Implantar:** colocar uma versão da aplicação em funcionamento.
- **Ambiente:** conjunto de recursos usado por essa aplicação.
- **Plataforma:** tecnologias compatíveis para executá-la.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Application, versions, environment e recursos provisionados |
| **O que você decide/configura?** | Plataforma, versão de código, variáveis, escala e rede |
| **Em que ordem as coisas acontecem?** | Envie versão; o ambiente implanta e acompanha recursos da aplicação |
| **O que pode fazer, e em que condição?** | Simplifica deploy sem impedir acesso aos recursos subjacentes autorizados |
| **O que não pode presumir?** | Aplicação, dependências e configurações continuam com o cliente; recursos usados são cobrados |

**Caso comentado:** Enviar aplicação web e delegar provisionamento comum: Beanstalk, sem presumir custo zero.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
