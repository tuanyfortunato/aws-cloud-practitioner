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

## 1. A sequência de funcionamento

**Passo 1.** Escolha uma plataforma compatível e prepare o pacote da aplicação.

**Passo 2.** Crie um ambiente com opções de capacidade, acesso e implantação. Beanstalk organiza recursos AWS para atender essa configuração.

**Passo 3.** Envie versões e acompanhe a saúde da aplicação. Código, escolhas operacionais e recursos cobrados continuam exigindo atenção.

## 2. Recursos e opções, com significado

### Para que serve

Desenvolvedores que querem publicar aplicações web **sem pensar em infraestrutura**.

Plataformas: Java, .NET (Windows e Linux), Node.js, Python, PHP, Ruby, Go, Docker, Tomcat.

### Conceitos e componentes

**Application**

**O que é:** Conjunto de versões e ambientes.

**Application version**

**O que é:** Pacote de código (zip no S3).

**Environment**

**O que é:** Recursos rodando uma versão: **Web server** (com ELB + ASG) ou **Worker** (consome fila SQS).

**Platform**

**O que é:** Combinação de SO, runtime e servidor web, atualizada pela AWS (*managed platform updates*).

**.ebextensions / platform hooks**

**O que é:** Personalização da configuração.

### Configurações e opções importantes

**Tipo de ambiente**

**Detalhe:** Single instance (barato, dev) ou load balanced (produção).

**Políticas de deploy**

**Detalhe:** All at once, Rolling, Rolling with additional batch, **Immutable**, Traffic splitting (canary); **blue/green** trocando o CNAME entre ambientes.

**Monitoramento**

**Detalhe:** Health básico ou *enhanced health*.

**Acesso**

**Detalhe:** Você continua com acesso total aos recursos criados (EC2, ELB, RDS…).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Você continua responsável pelo código e por decisões de configuração. Os recursos criados continuam tendo custos; Beanstalk não torna a infraestrutura gratuita.

### ⚠️ Pegadinhas e não confundir

**Beanstalk × CloudFormation:** Beanstalk = sobe *a aplicação* sem pensar em infra; CloudFormation = descreve *qualquer infraestrutura* como código (o Beanstalk usa CloudFormation por baixo).

**Beanstalk × Lightsail:** PaaS que escala × servidor simples de preço fixo.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Sem custo adicional** — paga só os recursos que ele cria (EC2, ELB, S3, RDS…).

### Segurança e responsabilidade compartilhada

**AWS:** provisionamento, atualizações de plataforma (quando ativadas), orquestração.

**Cliente:** código, configuração, dados, IAM, security groups.

## 5. Caso resolvido: ligando as peças

Uma equipe envia sua aplicação web para um ambiente Beanstalk. O serviço organiza a infraestrutura necessária para disponibilizá-la.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha uma plataforma compatível e prepare o pacote da aplicação.
**Etapa 2:** Crie um ambiente com opções de capacidade, acesso e implantação. Beanstalk organiza recursos AWS para atender essa configuração.
**Etapa 3:** Envie versões e acompanhe a saúde da aplicação. Código, escolhas operacionais e recursos cobrados continuam exigindo atenção.

**Resultado e responsabilidade:** O Elastic Beanstalk ajuda a implantar aplicações em plataformas compatíveis, provisionando e coordenando recursos AWS para esse ambiente. Você entrega o código e define opções do ambiente.

**Recursos envolvidos:** Application, versions, environment e recursos provisionados.

**Decisões que precisam ser tomadas:** Plataforma, versão de código, variáveis, escala e rede.

**Outra situação comentada:** Enviar aplicação web e delegar provisionamento comum: Beanstalk, sem presumir custo zero.

**Por que não concluir mais do que isso:** Aplicação, dependências e configurações continuam com o cliente; recursos usados são cobrados

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Desenvolvedor quer só subir o código Java e deixar a AWS cuidar de capacidade e balanceamento."

**Resposta curta:** Elastic Beanstalk.

**Pergunta:** "O Elastic Beanstalk tem custo próprio?"

**Resposta curta:** Não.

**Pergunta:** "Qual modelo de serviço o Beanstalk representa?"

**Resposta curta:** PaaS.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
