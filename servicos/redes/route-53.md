# Amazon Route 53

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma pessoa digita o nome de um site, mas o computador precisa descobrir para qual endereço enviar a comunicação.

**Como este serviço ajuda?** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde. DNS relaciona nomes a informações de endereço por registros.

**Exemplo do dia a dia:** A escola usa registros DNS para fazer seu domínio apontar para o endereço que atende o site.

**O que ele não resolve sozinho?** Route 53 indica o destino; ele não hospeda o código do site nem substitui a máquina que atende o pedido. Os tipos de registro e as políticas têm funções diferentes.

**Primeiras palavras para entender:**

- **Domínio:** nome como escola.example.
- **DNS:** sistema que resolve nomes.
- **Registro:** informação publicada para responder consultas DNS.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** DNS · **Domínio:** 3 · **Escopo:** **Global** · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** DNS gerenciado e altamente disponível (o "53" é a porta do DNS), com registro de domínios, roteamento inteligente e health checks.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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

- 📌 **SLA de 100%** para o DNS autoritativo — único serviço AWS com SLA de 100% (API/console fora). Tecnicamente, a página do SLA dá crédito de 10% quando a disponibilidade mensal fica **abaixo de 100%** (no GovCloud, abaixo de 99,995%).

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Hosted zones, records, health checks e políticas de roteamento |
| **O que você decide/configura?** | Domínio, registros, TTL e política |
| **Em que ordem as coisas acontecem?** | DNS devolve o endereço conforme registros e política |
| **O que pode fazer, e em que condição?** | Pode registrar domínios, resolver nomes e rotear respostas DNS |
| **O que não pode presumir?** | DNS não transporta nem balanceia cada pacote da sessão como um load balancer |

**Caso comentado:** Usuários encontram o endereço do site: Route 53; distribuição de conteúdo: CloudFront.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
