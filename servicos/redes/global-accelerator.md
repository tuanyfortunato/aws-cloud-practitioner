# AWS Global Accelerator

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Usuários de lugares diferentes precisam chegar a aplicações por caminhos de rede mais consistentes, com pontos de entrada fixos.

**Como este serviço ajuda?** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.

**Exemplo do dia a dia:** Uma aplicação distribuída usa endereços de entrada fixos e encaminha conexões para seus destinos AWS configurados.

**O que ele não resolve sozinho?** Ele encaminha tráfego; não guarda cópias de imagens ou páginas como uma CDN. Também não corrige lentidão causada pelo código ou pelo banco.

**Primeiras palavras para entender:**

- **IP:** endereço de rede.
- **Destino:** recurso que recebe o tráfego.
- **Roteamento:** escolha do caminho de uma comunicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Rede / desempenho global · **Domínio:** 3 · **Escopo:** **Global** · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** fornece **2 IPs anycast estáticos** e leva o tráfego TCP/UDP pela rede global da AWS até o endpoint saudável mais próximo.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.

**Passo 1.** Defina destinos compatíveis e o comportamento de atendimento entre eles.

**Passo 2.** Prepare os pontos de entrada e o encaminhamento pela rede AWS conforme a configuração e a saúde observada.

**Passo 3.** Observe o resultado nas conexões. O serviço encaminha tráfego; ele não mantém cópias dos arquivos da aplicação.

## 2. Recursos e opções, com significado

### Como funciona

**Antes de ler este trecho:**

- **edge location:** Local de infraestrutura usado para aproximar determinadas funções dos usuários, como entrega de conteúdo. Não é uma região completa com todos os serviços.

1. O usuário se conecta a um dos **2 IPs estáticos** anycast, que entram na rede AWS pela edge location mais próxima.

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.

2. O tráfego segue pela **backbone da AWS** (não pela internet pública) até o **endpoint group** da região.

3. Health checks redirecionam em segundos para outra região se houver falha.

### Configurações

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **TCP:** Protocolo de transporte orientado a conexão, com mecanismos de entrega e ordem. É usado por muitas aplicações; não acrescenta criptografia por si só.
- **UDP:** Protocolo de transporte por datagramas, sem as mesmas garantias de entrega e ordem do TCP. A aplicação precisa lidar com os requisitos que o protocolo não fornece.
- **ALB / NLB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.

| Item | Detalhe |
|---|---|
| **Listeners** | Portas/protocolos TCP e UDP. |
| **Endpoint groups** | Um por região; **traffic dial** controla o percentual enviado a cada região. |
| **Endpoints** | ALB, NLB, instâncias EC2, Elastic IPs; com **pesos**. |
| **Client affinity** | Mantém o mesmo usuário no mesmo endpoint. |
| **Custom routing** | Mapeia usuários para instâncias específicas (jogos, VoIP). |
| **Proteção** | Shield Standard incluso. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **CDN:** Rede de distribuição de conteúdo. Ela aproxima entrega de conteúdo dos usuários e pode manter cópias em cache conforme as regras.

Ele encaminha tráfego; não guarda cópias de imagens ou páginas como uma CDN. Também não corrige lentidão causada pelo código ou pelo banco.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.

⚠️ **Não faz cache.** Para cache → CloudFront.

**Antes de ler este trecho:**

- **Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.

IP fixo **global** → Global Accelerator; IP fixo **regional** → NLB com Elastic IP.

**Antes de ler este trecho:**

- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **failover:** Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **TTL:** Tempo de vida de uma informação. Em DNS pode orientar cache; em um banco pode indicar expiração de itens. O efeito concreto depende do serviço.

Failover regional rápido sem depender de TTL de DNS → Global Accelerator (o Route 53 depende do cache DNS dos clientes).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.

Taxa fixa por acelerador-hora + **DT-Premium** por GB transferido.

## 5. Caso resolvido: ligando as peças

Uma aplicação distribuída usa endereços de entrada fixos e encaminha conexões para seus destinos AWS configurados.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina destinos compatíveis e o comportamento de atendimento entre eles.
**Etapa 2:** Prepare os pontos de entrada e o encaminhamento pela rede AWS conforme a configuração e a saúde observada.
**Etapa 3:** Observe o resultado nas conexões. O serviço encaminha tráfego; ele não mantém cópias dos arquivos da aplicação.

**Resultado e responsabilidade:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.

**Recursos envolvidos:** Accelerator, IPs estáticos, listeners, endpoint groups e endpoints.

**Decisões que precisam ser tomadas:** Protocolo, regiões, saúde e pesos.

**Outra situação comentada:** Usuários globais precisam IPs fixos e tráfego TCP/UDP: Global Accelerator, em vez de escolher CloudFront por palavra global.

**Por que não concluir mais do que isso:** Não é cache/CDN de objetos e não substitui a aplicação

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "IPs estáticos globais e failover rápido entre regiões para TCP/UDP."

**Resposta curta:** Global Accelerator.

**Pergunta:** "Jogo multiplayer UDP com usuários no mundo todo."

**Resposta curta:** Global Accelerator.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
