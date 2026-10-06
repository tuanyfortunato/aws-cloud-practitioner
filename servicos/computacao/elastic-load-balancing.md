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

## 1. A sequência de funcionamento

**Passo 1.** Defina os recursos que podem atender pedidos e como verificar sua saúde.

**Passo 2.** Configure a entrada de tráfego e seu encaminhamento aos destinos. O balanceador escolhe destinos conforme suas regras e condições.

**Passo 3.** Uma verificação malsucedida pode retirar um destino do atendimento. Corrija a causa e acompanhe a capacidade dos recursos restantes.

## 2. Recursos e opções, com significado

### Para que serve

Alta disponibilidade e tolerância a falhas: só envia tráfego a destinos que passam no health check.

Ponto único de entrada (DNS) para uma frota que escala.

Terminação TLS centralizada com certificados do [ACM](../seguranca/certificate-manager.md).

### Conceitos e componentes

**Listener**

**O que é:** Porta/protocolo que o LB escuta (ex.: HTTPS:443).

**Rules (ALB)**

**O que é:** Condições (caminho, host, cabeçalho, query string, IP de origem) → ação (encaminhar, redirecionar, resposta fixa, autenticar).

**Target group**

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

| Tipo | Camada | Protocolos | Destaques | Uso |
|---|---|---|---|---|
| **Application LB (ALB)** | 7 | HTTP, HTTPS, gRPC, WebSocket | Roteamento por caminho/host/cabeçalho; destino Lambda; autenticação com Cognito/OIDC; integra com **WAF** | Microsserviços, contêineres, web |
| **Network LB (NLB)** | 4 | TCP, UDP, TLS | Milhões de req/s, latência ultrabaixa, **IP estático por AZ** (aceita Elastic IP), preserva IP de origem | Jogos, IoT, protocolos não HTTP, PrivateLink |
| **Gateway LB (GWLB)** | 3 | IP (GENEVE) | Insere appliances de terceiros de forma transparente | Firewalls, IDS/IPS virtuais |
| **Classic LB (CLB)** | 4 e 7 | HTTP, HTTPS, TCP | Geração anterior | Legado — não recomendado |

### Configurações e opções importantes

**Internet-facing** (IP público) × **internal** (só dentro da VPC).

**SSL/TLS offloading:** o LB descriptografa e alivia as instâncias; certificado do ACM; política de segurança TLS.

**Redirect HTTP → HTTPS** com regra no ALB.

**Access logs** no S3; métricas no CloudWatch.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele distribui tráfego; não cria mais máquinas por conta própria nem corrige erros do programa. Os tipos de balanceador atendem protocolos e necessidades diferentes.

### ⚠️ Pegadinhas e não confundir

⚠️ **WAF não se associa a NLB** (só ALB, CloudFront, API Gateway, AppSync, Cognito…).

"Rotear `/api` e `/imagens` para serviços diferentes" → **ALB**.

"IP fixo para clientes liberarem no firewall" → **NLB** (ou Global Accelerator para IP global).

ELB distribui tráfego; **Auto Scaling** ajusta a quantidade. São complementares.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por **hora** de LB + **LCU/NLCU/GLCU** (unidades de capacidade consumidas: conexões novas, ativas, bytes, avaliações de regras).

### Segurança e responsabilidade compartilhada

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

### ❓ Perguntas típicas

**Pergunta:** "Qual LB roteia por caminho de URL?"

**Resposta curta:** ALB.

**Pergunta:** "Qual LB para milhões de conexões TCP com IP estático?"

**Resposta curta:** NLB.

**Pergunta:** "Qual LB para appliances de firewall de terceiros?"

**Resposta curta:** GWLB.

**Pergunta:** "Como fazer HTTPS no LB com certificado gratuito?"

**Resposta curta:** ACM no listener do ALB/NLB.

**Pergunta:** "Como garantir que o tráfego só vá para instâncias saudáveis?"

**Resposta curta:** Health checks do ELB.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
