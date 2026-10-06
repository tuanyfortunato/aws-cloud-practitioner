# Amazon ECR (Elastic Container Registry)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Sua equipe criou pacotes de uma aplicação e precisa guardá-los num lugar de onde os ambientes de execução possam baixá-los com controle de acesso.

**Como este serviço ajuda?** O ECR é um repositório de imagens de containers. Ele guarda versões desses pacotes para que serviços de execução possam obtê-las.

**Exemplo do dia a dia:** A equipe publica a imagem do serviço de pedidos no ECR. Depois, o ECS baixa essa imagem para iniciar os containers.

**O que ele não resolve sozinho?** Guardar uma imagem no ECR não executa a aplicação. Para executá-la, você precisa de outro serviço ou ambiente.

**Primeiras palavras para entender:**

- **Imagem:** pacote usado para iniciar um container.
- **Repositório:** lugar organizado para guardar imagens.
- **Tag:** identificação de uma versão do pacote.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação / Contêineres · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** registro gerenciado para guardar, versionar e distribuir imagens de contêiner (Docker/OCI).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Crie um repositório e envie uma imagem da aplicação, identificando sua versão.

**Passo 2.** Autorize os ambientes que devem baixar a imagem. O ambiente de execução obtém o pacote necessário.

**Passo 3.** Publique novas versões e administre sua conservação. O repositório guarda imagens; outro componente executa o programa.

## 2. Recursos e opções, com significado

### Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Repositórios privados** | Controlados por IAM e políticas de repositório. |
| **ECR Public / Public Gallery** | Repositórios públicos para distribuir imagens. |
| **Image scanning** | *Basic* (CVEs do SO) ou *Enhanced* (contínuo, SO + pacotes de linguagem, via **Amazon Inspector**). |
| **Tag immutability** | Impede sobrescrever uma tag (ex.: `v1.2`). |
| **Lifecycle policies** | Apagam imagens antigas automaticamente (ex.: manter só as 10 últimas). |
| **Replicação** | Entre regiões e contas. |
| **Pull through cache** | Faz cache de imagens de registros públicos (Docker Hub, Quay, GitHub). |
| **Criptografia** | Em repouso (SSE-S3 ou KMS) e em trânsito (HTTPS). |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Guardar uma imagem no ECR não executa a aplicação. Para executá-la, você precisa de outro serviço ou ambiente.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por GB armazenado por mês + transferência de saída. Enhanced scanning é cobrado pelo Inspector.

### Segurança e responsabilidade compartilhada

**AWS:** disponibilidade e durabilidade do registro (armazenado no S3).

**Cliente:** quem pode fazer push/pull, conteúdo e vulnerabilidades das imagens.

## 5. Caso resolvido: ligando as peças

A equipe publica a imagem do serviço de pedidos no ECR. Depois, o ECS baixa essa imagem para iniciar os containers.

**Aplicando a sequência à situação:**

**Etapa 1:** Crie um repositório e envie uma imagem da aplicação, identificando sua versão.
**Etapa 2:** Autorize os ambientes que devem baixar a imagem. O ambiente de execução obtém o pacote necessário.
**Etapa 3:** Publique novas versões e administre sua conservação. O repositório guarda imagens; outro componente executa o programa.

**Resultado e responsabilidade:** O ECR é um repositório de imagens de containers. Ele guarda versões desses pacotes para que serviços de execução possam obtê-las.

**Recursos envolvidos:** Repositório, imagens, tags/digests e políticas.

**Decisões que precisam ser tomadas:** Acesso, retenção/lifecycle e opções de varredura.

**Outra situação comentada:** Versionar imagem de API: ECR; iniciar API: serviço de execução, como ECS.

**Por que não concluir mais do que isso:** Guardar imagem não inicia container; imagem pode conter bibliotecas vulneráveis

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Onde guardar imagens Docker privadas na AWS?"

**Resposta curta:** ECR.

**Pergunta:** "Varrer imagens de contêiner em busca de vulnerabilidades."

**Resposta curta:** ECR scanning / Amazon Inspector.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
