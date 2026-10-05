# Elastic Load Balancing (ELB)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Várias máquinas podem atender o mesmo site. Se todos os visitantes chegarem a uma só, ela pode ficar sobrecarregada enquanto as outras estão ociosas.

**Como este serviço ajuda?** O Elastic Load Balancing recebe conexões e encaminha o tráfego aos destinos configurados. Verificações de saúde ajudam a evitar destinos considerados indisponíveis.

**Exemplo do dia a dia:** A loja coloca um balanceador na entrada do site. Os pedidos dos visitantes são encaminhados às máquinas que atendem a aplicação.

**O que ele não resolve sozinho?** Ele distribui tráfego; não cria mais máquinas por conta própria nem corrige erros do programa. Os tipos de balanceador atendem protocolos e necessidades diferentes.

**Primeiras palavras para entender:**

- **Tráfego:** comunicações recebidas e enviadas.
- **Destino:** recurso que atende o pedido.
- **Verificação de saúde:** teste para saber se o destino responde adequadamente.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação / Rede · **Domínio:** 3 · **Escopo:** Regional (multi-AZ) · **Tópico do guia:** [3.4 Escalabilidade e balanceamento](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)
>
> **Em uma frase:** distribui automaticamente o tráfego entre destinos saudáveis (EC2, contêineres, IPs, Lambda) em várias AZs.
>
> **Escopo oficial:** ✅ Cobrado junto com o EC2 (não aparece como item separado na lista) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **balanceador:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


**Passo 1.** Defina os recursos que podem atender pedidos e como verificar sua saúde.

**Passo 2.** Configure a entrada de tráfego e seu encaminhamento aos destinos. O balanceador escolhe destinos conforme suas regras e condições.

**Passo 3.** Uma verificação malsucedida pode retirar um destino do atendimento. Corrija a causa e acompanhe a capacidade dos recursos restantes.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.
- **health check:** Teste de resposta usado para avaliar um destino. O teste e os limites precisam refletir a função observada; não equivale a uma investigação completa da aplicação.


Alta disponibilidade e tolerância a falhas: só envia tráfego a destinos que passam no health check.

**Antes de ler este trecho:**

- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.


Ponto único de entrada (DNS) para uma frota que escala.

**Antes de ler este trecho:**

- **TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **ACM:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.


Terminação TLS centralizada com certificados do [ACM](../seguranca/certificate-manager.md).

### Conceitos e componentes

**Listener**

**Antes de ler este trecho:**

- **porta:** Número que ajuda a identificar o serviço de destino de uma comunicação. Liberar uma porta autoriza tráfego segundo a regra, mas não configura a aplicação para responder.
- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.
- **listener:** Configuração que recebe conexões em uma porta e protocolo. No balanceador, ela participa da decisão de encaminhamento para destinos.


**O que é:** Porta/protocolo que o LB escuta (ex.: HTTPS:443).

**Rules (ALB)**

**Antes de ler este trecho:**

- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.
- **ALB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.


**O que é:** Condições (caminho, host, cabeçalho, query string, IP de origem) → ação (encaminhar, redirecionar, resposta fixa, autenticar).

**Target group**

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **target group:** Grupo de destinos do balanceamento, com configurações como verificações de saúde. Destino saudável não significa que toda regra de negócio está correta.


**O que é:** Conjunto de destinos (instâncias, IPs, Lambda, ALB) com seu health check.

**Health check**


**O que é:** Requisição periódica a um caminho/porta; define saudável/não saudável.

**Cross-zone load balancing**


**O que é:** Distribui igualmente entre todos os destinos de todas as AZs. Ativado por padrão no ALB.

**Sticky sessions**


**O que é:** Mantém o mesmo cliente no mesmo destino (cookie).

**Connection draining / deregistration delay**


**O que é:** Termina requisições em andamento antes de remover um destino.

### Tipos

**Antes de ler este trecho:**

- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **TCP:** Protocolo de transporte orientado a conexão, com mecanismos de entrega e ordem. É usado por muitas aplicações; não acrescenta criptografia por si só.
- **UDP:** Protocolo de transporte por datagramas, sem as mesmas garantias de entrega e ordem do TCP. A aplicação precisa lidar com os requisitos que o protocolo não fornece.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **WebSocket:** Comunicação que mantém uma conexão para troca de mensagens entre cliente e servidor. É diferente de uma sequência de pedidos web independentes.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.
- **OIDC:** Padrões de integração de identidade entre sistemas. Permitem que uma aplicação ou serviço confie em informações fornecidas por um provedor de identidade compatível.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.
- **IPS:** Sistema de prevenção de intrusões. Atua em condições e tráfego compatíveis; não é uma correção automática de todo software vulnerável.
- **IDS:** Sistema de detecção de intrusões. Detectar é diferente de bloquear; o efeito depende da ferramenta e da configuração.
- **GENEVE:** Protocolo de encapsulamento de rede usado em integrações compatíveis, como equipamentos com Gateway Load Balancer. Não é uma aplicação de proteção por si só.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Tipo | Camada | Protocolos | Destaques | Uso |
|---|---|---|---|---|
| **Application LB (ALB)** | 7 | HTTP, HTTPS, gRPC, WebSocket | Roteamento por caminho/host/cabeçalho; destino Lambda; autenticação com Cognito/OIDC; integra com **WAF** | Microsserviços, contêineres, web |
| **Network LB (NLB)** | 4 | TCP, UDP, TLS | Milhões de req/s, latência ultrabaixa, **IP estático por AZ** (aceita Elastic IP), preserva IP de origem | Jogos, IoT, protocolos não HTTP, PrivateLink |
| **Gateway LB (GWLB)** | 3 | IP (GENEVE) | Insere appliances de terceiros de forma transparente | Firewalls, IDS/IPS virtuais |
| **Classic LB (CLB)** | 4 e 7 | HTTP, HTTPS, TCP | Geração anterior | Legado — não recomendado |

### Configurações e opções importantes

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.


**Internet-facing** (IP público) × **internal** (só dentro da VPC).

**Antes de ler este trecho:**

- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.


**SSL/TLS offloading:** o LB descriptografa e alivia as instâncias; certificado do ACM; política de segurança TLS.


**Redirect HTTP → HTTPS** com regra no ALB.

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.


**Access logs** no S3; métricas no CloudWatch.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele distribui tráfego; não cria mais máquinas por conta própria nem corrige erros do programa. Os tipos de balanceador atendem protocolos e necessidades diferentes.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.


⚠️ **WAF não se associa a NLB** (só ALB, CloudFront, API Gateway, AppSync, Cognito…).


"Rotear `/api` e `/imagens` para serviços diferentes" → **ALB**.

**Antes de ler este trecho:**

- **Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.


"IP fixo para clientes liberarem no firewall" → **NLB** (ou Global Accelerator para IP global).


ELB distribui tráfego; **Auto Scaling** ajusta a quantidade. São complementares.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **LCU / NLCU / GLCU:** Unidades de capacidade usadas por modalidades de balanceadores. A unidade representa dimensões de consumo definidas pela oferta, não uma contagem direta de usuários.


Por **hora** de LB + **LCU/NLCU/GLCU** (unidades de capacidade consumidas: conexões novas, ativas, bytes, avaliações de regras).

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.


**AWS:** disponibilidade, escala e patch do LB (serviço gerenciado). Inclui **Shield Standard**.


**Cliente:** listeners, certificados, security groups do LB, regras do WAF, health checks.

## 5. Caso resolvido: ligando as peças

A loja coloca um balanceador na entrada do site. Os pedidos dos visitantes são encaminhados às máquinas que atendem a aplicação.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina os recursos que podem atender pedidos e como verificar sua saúde.
**Etapa 2:** Configure a entrada de tráfego e seu encaminhamento aos destinos. O balanceador escolhe destinos conforme suas regras e condições.
**Etapa 3:** Uma verificação malsucedida pode retirar um destino do atendimento. Corrija a causa e acompanhe a capacidade dos recursos restantes.

**Resultado e responsabilidade:** O Elastic Load Balancing recebe conexões e encaminha o tráfego aos destinos configurados. Verificações de saúde ajudam a evitar destinos considerados indisponíveis.

**Recursos envolvidos:** Load balancer, listeners, target groups, destinos e health checks.

**Decisões que precisam ser tomadas:** Tipo, protocolo, portas, certificados e destinos.


**Outra situação comentada:** Dois caminhos de uma aplicação web vão para serviços diferentes: regras por caminho no ALB.

**Por que não concluir mais do que isso:** Não executa aplicação nem aumenta capacidade sozinho

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Várias máquinas podem atender o mesmo site. Se todos os visitantes chegarem a uma só, ela pode ficar sobrecarregada enquanto as outras estão ociosas.

**2. O que a solução fornece?**

O Elastic Load Balancing recebe conexões e encaminha o tráfego aos destinos configurados. Verificações de saúde ajudam a evitar destinos considerados indisponíveis.

**3. Que conclusão seria incorreta?**

Ele distribui tráfego; não cria mais máquinas por conta própria nem corrige erros do programa. Os tipos de balanceador atendem protocolos e necessidades diferentes.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Qual LB roteia por caminho de URL?"

**Resposta curta:** ALB.

**Antes de ler este trecho:**

- **URL:** Endereço usado para acessar um recurso. Uma URL pode incluir domínio, caminho e parâmetros; possuir o endereço não significa ter autorização.


**Fundamento explicado no capítulo:** "Qual LB roteia por caminho de URL?" → ALB.

**Pergunta:** "Qual LB para milhões de conexões TCP com IP estático?"

**Resposta curta:** NLB.


**Fundamento explicado no capítulo:** "Qual LB para milhões de conexões TCP com IP estático?" → NLB.

**Pergunta:** "Qual LB para appliances de firewall de terceiros?"

**Resposta curta:** GWLB.


**Fundamento explicado no capítulo:** "Qual LB para appliances de firewall de terceiros?" → GWLB.

**Pergunta:** "Como fazer HTTPS no LB com certificado gratuito?"

**Resposta curta:** ACM no listener do ALB/NLB.


**Fundamento explicado no capítulo:** "Como fazer HTTPS no LB com certificado gratuito?" → ACM no listener do ALB/NLB.

**Pergunta:** "Como garantir que o tráfego só vá para instâncias saudáveis?"

**Resposta curta:** Health checks do ELB.


**Fundamento explicado no capítulo:** "Como garantir que o tráfego só vá para instâncias saudáveis?" → Health checks do ELB.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
