# Amazon Route 53

> **Categoria:** DNS · **Domínio:** 3 · **Escopo:** **Global** · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** DNS gerenciado e altamente disponível (o "53" é a porta do DNS), com registro de domínios, roteamento inteligente e health checks.

## Funções

1. **Registro de domínios** (`.com`, `.com.br` etc.).
2. **DNS autoritativo** (hosted zones).
3. **Health checks** e failover.
4. **Route 53 Resolver**: DNS híbrido (endpoints inbound/outbound entre VPC e on-premises) e **DNS Firewall**.

## Conceitos

| Item | Detalhe |
|---|---|
| **Hosted zone pública** | Responde na internet. |
| **Hosted zone privada** | Responde só dentro das VPCs associadas. |
| **Registros** | **A** (IPv4), **AAAA** (IPv6), **CNAME** (alias de nome; não no apex), **MX** (e-mail), **TXT**, **NS**, **SOA**, **CAA**… |
| **Alias record** | Extensão da AWS: aponta para recursos AWS (ELB, CloudFront, S3 website, API Gateway…), **funciona no apex** (`exemplo.com`) e consultas a alias de recursos AWS são **gratuitas**. |
| **TTL** | Tempo de cache da resposta nos resolvedores. |

## Políticas de roteamento

| Política | Uso |
|---|---|
| **Simple** | Um recurso (ou vários IPs aleatórios), sem health check |
| **Weighted** | Divide tráfego por peso (**testes A/B**, migração gradual, ex.: 10% para v2) |
| **Latency-based** | Envia para a **região com menor latência** para o usuário |
| **Failover** | Ativo-passivo com **health check** |
| **Geolocation** | Por **país/continente** do usuário (idioma, conteúdo licenciado, regulação) |
| **Geoproximity** | Por distância geográfica, com *bias* ajustável (Traffic Flow) |
| **Multivalue answer** | Até 8 registros saudáveis aleatórios (balanceamento simples no DNS) |
| **IP-based** | Pelo bloco CIDR de origem do usuário |

## Limites e números

- 📌 **SLA de 100%** para o DNS autoritativo — único serviço AWS com SLA de 100% (API/console fora).

## Cobrança

- Por hosted zone por mês + por milhão de consultas (alias para recursos AWS grátis) + health checks + domínios registrados (anual).

## ⚠️ Pegadinhas e não confundir

- Route 53 decide **para onde ir** (DNS); CloudFront **entrega e faz cache** do conteúdo.
- Geolocation (fronteiras, país) × Latency (desempenho) × Geoproximity (distância ajustável).
- Route 53 é um dos serviços **globais** (com IAM, CloudFront, Organizations).

## ❓ Perguntas típicas

- "Registrar domínio e gerenciar DNS." → Route 53.
- "Mandar 10% dos usuários para a nova versão." → Weighted.
- "Usuários da Alemanha devem ver o site em alemão." → Geolocation.
- "Enviar para a região mais rápida." → Latency-based.
- "Se o site principal cair, mandar para a página de manutenção." → Failover com health check.
- "Qual serviço tem SLA de 100%?" → Route 53.

## 🔗 Documentação oficial

- [Guia do Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
