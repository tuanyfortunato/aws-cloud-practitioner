# Rede e diretório (Cloud Map, VPC Lattice, Network Access Analyzer, Cloud Directory)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Aplicações podem precisar localizar outros serviços ou controlar a comunicação entre eles, além de apenas ter uma rede virtual criada.

**Como este serviço ajuda?** A ficha distingue descoberta de serviços, comunicação de aplicações, análise de caminhos e diretórios especializados. Cada ferramenta trata uma dessas necessidades.

**Exemplo do dia a dia:** Se uma parte da aplicação precisa descobrir onde está outra, descoberta de serviços é uma função pertinente. Isso é diferente de cadastrar funcionários para login.

**O que ele não resolve sozinho?** Esses produtos não substituem uns aos outros nem tornam toda rede acessível automaticamente. O conteúdo é de referência fora do escopo indicado.

**Primeiras palavras para entender:**

- **Descoberta de serviços:** localizar recursos de uma aplicação.
- **Diretório:** organização de entidades e relações.
- **Caminho de rede:** percurso de uma comunicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Redes e diretório · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** serviços de rede de aplicação e de diretório que complementam a VPC, mas não caem na prova.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Documentados aqui apenas para referência. Na prova, rede = VPC, Route 53,
> CloudFront, Global Accelerator, Direct Connect, VPN, Transit Gateway, PrivateLink e API Gateway. Veja também
> [Network Firewall](../seguranca/firewall-manager-e-network-firewall.md), que também está fora do escopo.

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Defina se precisa localizar um serviço, conectar aplicações, avaliar caminhos ou organizar entidades.

**Passo 2.** Selecione a ferramenta com aquela função e prepare o escopo de recursos e identidades.

**Passo 3.** Verifique a comunicação ou organização obtida. Descoberta de serviços não é o mesmo que cadastro de usuários.

## 2. Recursos e opções, com significado

### AWS Cloud Map

**Antes de ler este trecho:**

- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.


**Descoberta de serviços**: registra os recursos de uma aplicação (microsserviços, bancos, filas) com nomes amigáveis e o local atual, para que os serviços encontrem uns aos outros por API ou DNS. Usado pelo ECS Service Connect.

### Amazon VPC Lattice

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.


**Rede de aplicação** gerenciada: conecta, protege (políticas de autenticação com IAM) e monitora a comunicação entre serviços em várias VPCs e contas, sem gerenciar peering, rotas ou load balancers.

### Network Access Analyzer

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.


Recurso da VPC que **identifica caminhos de rede não intencionais** até seus recursos (ex.: "algum banco de dados é acessível pela internet?"), comparando com requisitos que você define.

### Amazon Cloud Directory

Banco de **diretórios hierárquicos** flexíveis (organogramas, catálogos, registros de dispositivos), com várias hierarquias sobre os mesmos dados.


🔄 Fechado a novos clientes desde 07/11/2025.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Esses produtos não substituem uns aos outros nem tornam toda rede acessível automaticamente. O conteúdo é de referência fora do escopo indicado.

### ⚠️ Como isso aparece na prova

"Ligar dezenas de VPCs" → **Transit Gateway** (no escopo). "Expor um serviço de forma privada" → **PrivateLink** (no escopo).

**Antes de ler este trecho:**

- **Directory Service:** Directory Service oferece opções para diretórios e integração com Active Directory, conforme a modalidade.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.


"Active Directory gerenciado" → **Directory Service** (no escopo), não Cloud Directory.

**Antes de ler este trecho:**

- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


"Analisar tráfego de rede" → **VPC Flow Logs**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Se uma parte da aplicação precisa descobrir onde está outra, descoberta de serviços é uma função pertinente. Isso é diferente de cadastrar funcionários para login.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina se precisa localizar um serviço, conectar aplicações, avaliar caminhos ou organizar entidades.
**Etapa 2:** Selecione a ferramenta com aquela função e prepare o escopo de recursos e identidades.
**Etapa 3:** Verifique a comunicação ou organização obtida. Descoberta de serviços não é o mesmo que cadastro de usuários.

**Resultado e responsabilidade:** A ficha distingue descoberta de serviços, comunicação de aplicações, análise de caminhos e diretórios especializados. Cada ferramenta trata uma dessas necessidades.

**Recursos envolvidos:** Descoberta de serviços, conectividade de aplicações e diretórios especializados.

**Decisões que precisam ser tomadas:** Escopo de rede, identidade e serviço.

**Antes de ler este trecho:**

- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.


**Outra situação comentada:** DNS Route 53 e identidade IAM são conceitos centrais; ferramentas especializadas pedem contexto próprio.

**Por que não concluir mais do que isso:** Fora do escopo; não são substitutos universais de VPC, DNS ou IAM

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Aplicações podem precisar localizar outros serviços ou controlar a comunicação entre eles, além de apenas ter uma rede virtual criada.

**2. O que a solução fornece?**

A ficha distingue descoberta de serviços, comunicação de aplicações, análise de caminhos e diretórios especializados. Cada ferramenta trata uma dessas necessidades.

**3. Que conclusão seria incorreta?**

Esses produtos não substituem uns aos outros nem tornam toda rede acessível automaticamente. O conteúdo é de referência fora do escopo indicado.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Cloud Map](https://aws.amazon.com/cloud-map/) · [VPC Lattice](https://aws.amazon.com/vpc/lattice/) · [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) · [Cloud Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
