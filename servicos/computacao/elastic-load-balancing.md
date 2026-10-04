# Elastic Load Balancing (ELB)

> **Categoria:** Computação / Rede · **Domínio:** 3 · **Escopo:** Regional (multi-AZ) · **Tópico do guia:** [3.4 Escalabilidade e balanceamento](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)
>
> **Em uma frase:** distribui automaticamente o tráfego entre destinos saudáveis (EC2, contêineres, IPs, Lambda) em várias AZs.
>
> **Escopo oficial:** ✅ Cobrado junto com o EC2 (não aparece como item separado na lista) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Alta disponibilidade e tolerância a falhas: só envia tráfego a destinos que passam no health check.
- Ponto único de entrada (DNS) para uma frota que escala.
- Terminação TLS centralizada com certificados do [ACM](../seguranca/certificate-manager.md).

## Conceitos e componentes

| Componente | O que é |
|---|---|
| **Listener** | Porta/protocolo que o LB escuta (ex.: HTTPS:443). |
| **Rules** (ALB) | Condições (caminho, host, cabeçalho, query string, IP de origem) → ação (encaminhar, redirecionar, resposta fixa, autenticar). |
| **Target group** | Conjunto de destinos (instâncias, IPs, Lambda, ALB) com seu health check. |
| **Health check** | Requisição periódica a um caminho/porta; define saudável/não saudável. |
| **Cross-zone load balancing** | Distribui igualmente entre todos os destinos de todas as AZs. Ativado por padrão no ALB. |
| **Sticky sessions** | Mantém o mesmo cliente no mesmo destino (cookie). |
| **Connection draining / deregistration delay** | Termina requisições em andamento antes de remover um destino. |

## Tipos

| Tipo | Camada | Protocolos | Destaques | Uso |
|---|---|---|---|---|
| **Application LB (ALB)** | 7 | HTTP, HTTPS, gRPC, WebSocket | Roteamento por caminho/host/cabeçalho; destino Lambda; autenticação com Cognito/OIDC; integra com **WAF** | Microsserviços, contêineres, web |
| **Network LB (NLB)** | 4 | TCP, UDP, TLS | Milhões de req/s, latência ultrabaixa, **IP estático por AZ** (aceita Elastic IP), preserva IP de origem | Jogos, IoT, protocolos não HTTP, PrivateLink |
| **Gateway LB (GWLB)** | 3 | IP (GENEVE) | Insere appliances de terceiros de forma transparente | Firewalls, IDS/IPS virtuais |
| **Classic LB (CLB)** | 4 e 7 | HTTP, HTTPS, TCP | Geração anterior | Legado — não recomendado |

## Configurações e opções importantes

- **Internet-facing** (IP público) × **internal** (só dentro da VPC).
- **SSL/TLS offloading:** o LB descriptografa e alivia as instâncias; certificado do ACM; política de segurança TLS.
- **Redirect HTTP → HTTPS** com regra no ALB.
- **Access logs** no S3; métricas no CloudWatch.

## Cobrança

- Por **hora** de LB + **LCU/NLCU/GLCU** (unidades de capacidade consumidas: conexões novas, ativas, bytes, avaliações de regras).

## Segurança e responsabilidade compartilhada

- **AWS:** disponibilidade, escala e patch do LB (serviço gerenciado). Inclui **Shield Standard**.
- **Cliente:** listeners, certificados, security groups do LB, regras do WAF, health checks.

## ⚠️ Pegadinhas e não confundir

- ⚠️ **WAF não se associa a NLB** (só ALB, CloudFront, API Gateway, AppSync, Cognito…).
- "Rotear `/api` e `/imagens` para serviços diferentes" → **ALB**.
- "IP fixo para clientes liberarem no firewall" → **NLB** (ou Global Accelerator para IP global).
- ELB distribui tráfego; **Auto Scaling** ajusta a quantidade. São complementares.

## ❓ Perguntas típicas

- "Qual LB roteia por caminho de URL?" → ALB.
- "Qual LB para milhões de conexões TCP com IP estático?" → NLB.
- "Qual LB para appliances de firewall de terceiros?" → GWLB.
- "Como fazer HTTPS no LB com certificado gratuito?" → ACM no listener do ALB/NLB.
- "Como garantir que o tráfego só vá para instâncias saudáveis?" → Health checks do ELB.

## 🔗 Documentação oficial

- [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
