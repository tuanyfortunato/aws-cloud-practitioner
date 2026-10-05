# Amazon CloudFront

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Visitantes em lugares diferentes precisam receber imagens, vídeos ou páginas sem sempre buscar tudo no servidor de origem, que pode estar distante.

**Como este serviço ajuda?** CloudFront distribui conteúdo por uma rede de pontos de presença. Pode manter cópias em cache e encaminhar solicitações à origem conforme as regras.

**Exemplo do dia a dia:** A escola distribui imagens do site pelo CloudFront. Visitantes podem obter cópias a partir de um ponto próximo, sem pedir cada arquivo ao servidor original.

**O que ele não resolve sozinho?** Ele não transforma automaticamente toda aplicação em conteúdo estático nem permite guardar qualquer resposta em cache sem cuidado. A origem, as regras e os acessos precisam ser configurados.

**Primeiras palavras para entender:**

- **CDN:** rede de distribuição de conteúdo.
- **Origem:** lugar de onde o conteúdo vem.
- **Cache:** cópia mantida para reutilização.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** CDN / entrega de conteúdo · **Domínio:** 3 (e 2: proteção na borda) · **Escopo:** **Global** (edge locations) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** rede de distribuição de conteúdo (CDN) que faz **cache** perto dos usuários, reduzindo latência e carga na origem.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.


**Passo 1.** Defina a origem e quais conteúdos ou caminhos a distribuição deve atender.

**Passo 2.** Configure regras de entrega, cache e acesso. Os pedidos podem ser atendidos por cópias ou encaminhados à origem conforme essas regras.

**Passo 3.** Planeje atualização do conteúdo e proteção da origem. Conteúdo privado ou dinâmico exige condições adequadas de acesso e cache.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **streaming:** Fluxo contínuo de dados ou mídia. É diferente de esperar um arquivo completo antes de iniciar o trabalho.


Sites e APIs globais, vídeo (streaming), downloads, sites estáticos no S3, aceleração de conteúdo dinâmico.

**Antes de ler este trecho:**

- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.


Proteção na borda: **Shield Standard incluso**, integração com **WAF**.

### Conceitos e configurações

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.
- **failover:** Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **HTTPS / TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **CDN:** Rede de distribuição de conteúdo. Ela aproxima entrega de conteúdo dos usuários e pode manter cópias em cache conforme as regras.
- **TTL:** Tempo de vida de uma informação. Em DNS pode orientar cache; em um banco pode indicar expiração de itens. O efeito concreto depende do serviço.
- **ALB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
- **policy:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.
- **ACM:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.
- **OAC:** Controle de acesso à origem em integrações CloudFront compatíveis. Ajuda a restringir acesso direto à origem conforme a configuração.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.
- **SNI:** Informação de nome enviada no estabelecimento de uma conexão TLS para ajudar a escolher o contexto ou certificado pertinente.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Distribution** | Configuração da CDN com domínio `*.cloudfront.net` (ou o seu). |
| **Origins** | S3, ALB, EC2, API Gateway, MediaPackage, qualquer servidor HTTP; *origin groups* para failover. |
| **Behaviors** | Regras por caminho (`/api/*`, `*.jpg`) com origem, cache policy, métodos permitidos, viewer protocol (redirecionar HTTP→HTTPS). |
| **Cache policy / TTL** | Quanto tempo e com quais chaves (headers, cookies, query strings) guardar. |
| **Invalidation** | Remove objetos do cache antes do TTL (pago acima da cota grátis); alternativa: versionar nomes de arquivos. |
| **Regional Edge Caches** | Camada intermediária maior entre edge e origem. **Origin Shield** adiciona mais uma camada centralizada. |
| **OAC (Origin Access Control)** | Bucket S3 privado acessível **só pelo CloudFront**. ✔️ É o método recomendado; o OAI é legado ("not recommended", ainda documentado). |
| **Signed URLs / signed cookies** | Restringem acesso a conteúdo privado (cursos pagos, assinaturas). |
| **Geo restriction** | Allow/block list de países. |
| **HTTPS** | Certificado do **ACM** (precisa estar em **us-east-1**), SNI, políticas TLS; *field-level encryption*. |
| **Edge compute** | **CloudFront Functions** (JS leve, sub-ms, manipular headers/URLs) e **Lambda@Edge** (Node/Python, mais poder, acesso à rede). |
| **Price classes** | Limitar às edge locations mais baratas para reduzir custo. |
| **Logs** | Standard logs (S3/CloudWatch) e real-time logs (Kinesis). |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não transforma automaticamente toda aplicação em conteúdo estático nem permite guardar qualquer resposta em cache sem cuidado. A origem, as regras e os acessos precisam ser configurados.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **TCP:** Protocolo de transporte orientado a conexão, com mecanismos de entrega e ordem. É usado por muitas aplicações; não acrescenta criptografia por si só.
- **UDP:** Protocolo de transporte por datagramas, sem as mesmas garantias de entrega e ordem do TCP. A aplicação precisa lidar com os requisitos que o protocolo não fornece.


CloudFront (cache, HTTP/HTTPS) × **Global Accelerator** (sem cache, TCP/UDP, IPs estáticos).


CloudFront × **S3 Transfer Acceleration** (usa a rede do CloudFront para **uploads** ao S3).


"Reduzir custo de saída para usuários globais" → CloudFront.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.


Transferência de saída para a internet (por região de edge) + requisições HTTP/HTTPS + invalidações, Functions, Lambda@Edge.

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **ELB:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.


✔️ **Transferência da origem AWS (S3, EC2, ELB) para o CloudFront é gratuita** (origin fetches).

**Antes de ler este trecho:**

- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **DDoS:** Ataque distribuído que tenta sobrecarregar um serviço e impedir seu uso legítimo. É diferente de tentar explorar um campo vulnerável de um programa.


🔄 **Planos de preço fixo** (desde 18/11/2025): um valor mensal que agrupa CDN, WAF, proteção DDoS, Route 53, CloudWatch Logs, edge compute e créditos de S3, sem cobrança por excedente — Free (US$ 0), Pro (US$ 15), Business (US$ 200) e Premium (US$ 1.000) **por distribuição**, além de Custom; o pay-as-you-go continua disponível. 🧊 Não cai na prova.

### Segurança e responsabilidade compartilhada

**AWS:** rede de borda, Shield Standard, disponibilidade.


**Cliente:** configuração de HTTPS, OAC, regras do WAF, quem acessa (signed URLs), conteúdo.

## 5. Caso resolvido: ligando as peças

A escola distribui imagens do site pelo CloudFront. Visitantes podem obter cópias a partir de um ponto próximo, sem pedir cada arquivo ao servidor original.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina a origem e quais conteúdos ou caminhos a distribuição deve atender.
**Etapa 2:** Configure regras de entrega, cache e acesso. Os pedidos podem ser atendidos por cópias ou encaminhados à origem conforme essas regras.
**Etapa 3:** Planeje atualização do conteúdo e proteção da origem. Conteúdo privado ou dinâmico exige condições adequadas de acesso e cache.

**Resultado e responsabilidade:** CloudFront distribui conteúdo por uma rede de pontos de presença. Pode manter cópias em cache e encaminhar solicitações à origem conforme as regras.

**Recursos envolvidos:** Distribution, origins, behaviors, cache e políticas.

**Decisões que precisam ser tomadas:** Origem, HTTPS, cache, acesso e caminhos.

**Antes de ler este trecho:**

- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.
- **back-end:** Parte que processa regras e dados de uma aplicação. É diferente da interface que a pessoa vê no navegador ou aplicativo.


**Outra situação comentada:** Conteúdo privado S3 com HTTPS: origem S3 apropriada e OAC, sem tornar bucket público.

**Por que não concluir mais do que isso:** Não substitui back-end; resposta pode permanecer em cache até atualização/invalidation; OAC não serve ao website endpoint S3

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Visitantes em lugares diferentes precisam receber imagens, vídeos ou páginas sem sempre buscar tudo no servidor de origem, que pode estar distante.

**2. O que a solução fornece?**

CloudFront distribui conteúdo por uma rede de pontos de presença. Pode manter cópias em cache e encaminhar solicitações à origem conforme as regras.

**3. Que conclusão seria incorreta?**

Ele não transforma automaticamente toda aplicação em conteúdo estático nem permite guardar qualquer resposta em cache sem cuidado. A origem, as regras e os acessos precisam ser configurados.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Reduzir latência de conteúdo para usuários globais."

**Resposta curta:** CloudFront.

**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.


**Fundamento explicado no capítulo:** "Reduzir latência de conteúdo para usuários globais." → CloudFront.

**Pergunta:** "Deixar o bucket S3 privado e servir só via CDN."

**Resposta curta:** CloudFront com OAC.


**Fundamento explicado no capítulo:** "Deixar o bucket S3 privado e servir só via CDN." → CloudFront com OAC.

**Pergunta:** "Conteúdo pago só para assinantes."

**Resposta curta:** Signed URLs/cookies.


**Fundamento explicado no capítulo:** "Conteúdo pago só para assinantes." → Signed URLs/cookies.

**Pergunta:** "Bloquear acesso de determinados países."

**Resposta curta:** Geo restriction (ou WAF).


**Fundamento explicado no capítulo:** "Bloquear acesso de determinados países." → Geo restriction (ou WAF).

**Pergunta:** "Rodar código leve na borda para reescrever URLs."

**Resposta curta:** CloudFront Functions.


**Fundamento explicado no capítulo:** "Rodar código leve na borda para reescrever URLs." → CloudFront Functions.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
