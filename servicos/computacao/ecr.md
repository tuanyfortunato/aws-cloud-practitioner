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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.


**Passo 1.** Crie um repositório e envie uma imagem da aplicação, identificando sua versão.

**Passo 2.** Autorize os ambientes que devem baixar a imagem. O ambiente de execução obtém o pacote necessário.

**Passo 3.** Publique novas versões e administre sua conservação. O repositório guarda imagens; outro componente executa o programa.

## 2. Recursos e opções, com significado

### Conceitos e configurações

**Antes de ler este trecho:**

- **ECR:** O ECR é um repositório de imagens de containers.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **Amazon Inspector / Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.
- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **HTTPS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **SSE-S3:** Formas de criptografia no servidor do S3, que diferem na origem e administração das chaves e, no último caso, nas camadas. A tabela da seção distingue essas escolhas.
- **pull:** Em pull, o consumidor busca dados. Em push, o envio é iniciado para o destinatário. A forma de entrega não executa automaticamente a regra de negócio.
- **tag:** Par de nome e valor associado a recursos ou objetos compatíveis. Ajuda organização; usos em permissões e cobrança dependem de configuração e suporte.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.


Por GB armazenado por mês + transferência de saída. Enhanced scanning é cobrado pelo Inspector.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **durabilidade:** Capacidade de preservar os dados armazenados. É diferente de disponibilidade, que trata de conseguir acessá-los quando necessário.


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

**Antes de ler este trecho:**

- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **container:** Ambiente que executa uma aplicação a partir de uma imagem com software e dependências. É diferente de criar uma máquina virtual completa para cada pacote.


**Outra situação comentada:** Versionar imagem de API: ECR; iniciar API: serviço de execução, como ECS.

**Por que não concluir mais do que isso:** Guardar imagem não inicia container; imagem pode conter bibliotecas vulneráveis

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Sua equipe criou pacotes de uma aplicação e precisa guardá-los num lugar de onde os ambientes de execução possam baixá-los com controle de acesso.

**2. O que a solução fornece?**

O ECR é um repositório de imagens de containers. Ele guarda versões desses pacotes para que serviços de execução possam obtê-las.

**3. Que conclusão seria incorreta?**

Guardar uma imagem no ECR não executa a aplicação. Para executá-la, você precisa de outro serviço ou ambiente.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Onde guardar imagens Docker privadas na AWS?"

**Resposta curta:** ECR.


**Fundamento explicado no capítulo:** "Onde guardar imagens Docker privadas na AWS?" → ECR.

**Pergunta:** "Varrer imagens de contêiner em busca de vulnerabilidades."

**Resposta curta:** ECR scanning / Amazon Inspector.


**Fundamento explicado no capítulo:** "Varrer imagens de contêiner em busca de vulnerabilidades." → ECR scanning / Amazon Inspector.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
