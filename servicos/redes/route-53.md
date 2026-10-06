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

## 1. A sequência de funcionamento

**Passo 1.** Determine o nome que os usuários consultarão e o destino que deve atender.

**Passo 2.** Configure os registros e a política de resposta pertinente. O resolvedor DNS consulta informações para localizar o destino.

**Passo 3.** Acompanhe mudanças e saúde quando aplicável. Resolver o nome não confirma que a aplicação está respondendo corretamente.

## 2. Recursos e opções, com significado

### Funções

1. **Registro de domínios** (`.com`, `.com.br` etc.).

2. **DNS autoritativo** (hosted zones).

3. **Health checks** e failover.

4. **Route 53 Resolver**: DNS híbrido (endpoints inbound/outbound entre VPC e on-premises) e **DNS Firewall**.

### Conceitos

| Item | Detalhe |
|---|---|
| **Hosted zone pública** | Responde na internet. |
| **Hosted zone privada** | Responde só dentro das VPCs associadas. |
| **Registros** | **A** (IPv4), **AAAA** (IPv6), **CNAME** (alias de nome; não no apex), **MX** (e-mail), **TXT**, **NS**, **SOA**, **CAA**… |
| **Alias record** | Extensão da AWS: aponta para recursos AWS (ELB, CloudFront, S3 website, API Gateway…), **funciona no apex** (`exemplo.com`) e consultas a alias de recursos AWS são **gratuitas**. |
| **TTL** | Tempo de cache da resposta nos resolvedores. |

### Políticas de roteamento

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

### Limites e números

📌 **SLA de 100%** para o DNS autoritativo — único serviço AWS com SLA de 100% (API/console fora). Tecnicamente, a página do SLA dá crédito de 10% quando a disponibilidade mensal fica **abaixo de 100%** (no GovCloud, abaixo de 99,995%).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Route 53 indica o destino; ele não hospeda o código do site nem substitui a máquina que atende o pedido. Os tipos de registro e as políticas têm funções diferentes.

### ⚠️ Pegadinhas e não confundir

Route 53 decide **para onde ir** (DNS); CloudFront **entrega e faz cache** do conteúdo.

Geolocation (fronteiras, país) × Latency (desempenho) × Geoproximity (distância ajustável).

Route 53 é um dos serviços **globais** (com IAM, CloudFront, Organizations).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por hosted zone por mês + por milhão de consultas (alias para recursos AWS grátis) + health checks + domínios registrados (anual).

## 5. Caso resolvido: ligando as peças

O aluno digita um nome de site e precisa chegar ao endereço que atende a escola. A primeira tarefa é resolver esse nome, antes de a aplicação atender a requisição.

A equipe configura a zona e o registro adequados ao domínio e ao destino. Uma consulta DNS obtém as informações de endereço conforme o tipo de registro e a política. O cliente então inicia a comunicação com o destino indicado.

DNS correto não garante que o servidor responde nem que os dados estão autorizados. CloudFront pode distribuir conteúdo; um balanceador pode distribuir conexões; Route 53 informa respostas de nome. Esses recursos podem cooperar, mas resolvem etapas diferentes.

**Recursos envolvidos:** Hosted zones, records, health checks e políticas de roteamento.

**Decisões que precisam ser tomadas:** Domínio, registros, TTL e política.

**Outra situação comentada:** Usuários encontram o endereço do site: Route 53; distribuição de conteúdo: CloudFront.

**Por que não concluir mais do que isso:** DNS não transporta nem balanceia cada pacote da sessão como um load balancer

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Registrar domínio e gerenciar DNS."

**Resposta curta:** Route 53.

**Pergunta:** "Mandar 10% dos usuários para a nova versão."

**Resposta curta:** Weighted.

**Pergunta:** "Usuários da Alemanha devem ver o site em alemão."

**Resposta curta:** Geolocation.

**Pergunta:** "Enviar para a região mais rápida."

**Resposta curta:** Latency-based.

**Pergunta:** "Se o site principal cair, mandar para a página de manutenção."

**Resposta curta:** Failover com health check.

**Pergunta:** "Qual serviço tem SLA de 100%?"

**Resposta curta:** Route 53.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
