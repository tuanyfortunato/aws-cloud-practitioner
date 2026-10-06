# VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Duas redes privadas precisam conversar, ou uma aplicação precisa acessar um serviço AWS por conectividade privada. São necessidades diferentes.

**Como este serviço ajuda?** Peering conecta VPCs; Transit Gateway centraliza conexões entre redes; endpoints fornecem acesso a serviços compatíveis por caminhos privados. Esta ficha compara essas funções.

**Exemplo do dia a dia:** Duas VPCs podem usar peering. Uma empresa com muitas redes pode avaliar Transit Gateway. Uma aplicação pode usar um endpoint compatível para acessar um serviço AWS.

**O que ele não resolve sozinho?** Criar uma conexão não concede todas as permissões nem configura todas as rotas. Endpoints não equivalem a uma conexão geral entre todas as redes.

**Primeiras palavras para entender:**

- **Peering:** ligação entre duas VPCs.
- **Hub:** ponto central de conexões.
- **Endpoint:** ponto de acesso a um serviço.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Rede · **Domínio:** 3 · **Escopo:** Regional (peering e TGW podem ligar regiões) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** formas de conectar VPCs entre si e de acessar serviços sem passar pela internet.
>
> **Escopo oficial:** ✅ No escopo (Transit Gateway e PrivateLink listados) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Descreva quem precisa comunicar-se com quem: duas redes, muitas redes ou um serviço específico.

**Passo 2.** Escolha a conexão pertinente e configure suas associações, rotas e controles.

**Passo 3.** Teste o caminho autorizado. Não suponha trânsito entre redes ou permissão a dados apenas porque existe uma conexão.

## 2. Recursos e opções, com significado

### VPC Peering

Conexão privada **um-para-um** entre duas VPCs (mesma conta, outra conta, outra região).

⚠️ **Não é transitivo:** A↔B e B↔C não permite A↔C.

CIDRs **não podem se sobrepor**. Precisa atualizar route tables e SGs dos dois lados.

Sem custo por hora; paga transferência de dados.

### AWS Transit Gateway

**Hub regional** que conecta milhares de VPCs, VPNs, Direct Connect e outros TGWs (peering entre regiões) — modelo *hub-and-spoke*.

Route tables do TGW permitem segmentar (ex.: prod não fala com dev).

Compartilhável entre contas via **RAM**.

Pago por anexo-hora + GB processado.

### VPC Endpoints

| Tipo | Serviços | Como funciona | Custo |
|---|---|---|---|
| **Gateway endpoint** | **Só S3 e DynamoDB** | Entrada na route table | **Gratuito** |
| **Interface endpoint** (PrivateLink) | Maioria dos serviços AWS e serviços de parceiros | ENI com IP privado na sua subnet + DNS privado | Por hora + GB |
| **Gateway Load Balancer endpoint** | Appliances de segurança | Encaminha tráfego para o GWLB | Por hora + GB |

Endpoint policies restringem o que pode ser acessado pelo endpoint.

### AWS PrivateLink

Tecnologia dos interface endpoints. Também permite **expor um serviço seu** (atrás de um NLB) para outras VPCs/contas/clientes de forma privada, sem peering e sem expor a VPC inteira.

### Comparação rápida

| Necessidade | Solução |
|---|---|
| Ligar 2 VPCs | VPC Peering |
| Ligar dezenas de VPCs + on-premises | Transit Gateway |
| Acessar S3/DynamoDB sem internet | Gateway endpoint (grátis) |
| Acessar outros serviços AWS sem internet | Interface endpoint |
| Oferecer seu serviço privadamente a outras contas | PrivateLink (endpoint service) |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Criar uma conexão não concede todas as permissões nem configura todas as rotas. Endpoints não equivalem a uma conexão geral entre todas as redes.

## 4. Caso resolvido: ligando as peças

Duas VPCs podem usar peering. Uma empresa com muitas redes pode avaliar Transit Gateway. Uma aplicação pode usar um endpoint compatível para acessar um serviço AWS.

**Aplicando a sequência à situação:**

**Etapa 1:** Descreva quem precisa comunicar-se com quem: duas redes, muitas redes ou um serviço específico.
**Etapa 2:** Escolha a conexão pertinente e configure suas associações, rotas e controles.
**Etapa 3:** Teste o caminho autorizado. Não suponha trânsito entre redes ou permissão a dados apenas porque existe uma conexão.

**Resultado e responsabilidade:** Peering conecta VPCs; Transit Gateway centraliza conexões entre redes; endpoints fornecem acesso a serviços compatíveis por caminhos privados. Esta ficha compara essas funções.

**Recursos envolvidos:** Peering entre VPCs; hub Transit Gateway; endpoints e PrivateLink.

**Decisões que precisam ser tomadas:** Redes envolvidas, rotas, serviço exposto e permissões.

**Outra situação comentada:** Três redes precisam comunicação por hub: TGW; consumidor só precisa de serviço privado: PrivateLink.

**Por que não concluir mais do que isso:** Peering não é transitivo; endpoint não substitui IAM

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Conectar duas VPCs de contas diferentes."

**Resposta curta:** VPC Peering.

**Pergunta:** "A falou com B e B com C; A fala com C via peering?"

**Resposta curta:** Não, peering não é transitivo.

**Pergunta:** "Conectar 50 VPCs e o datacenter num hub."

**Resposta curta:** Transit Gateway.

**Pergunta:** "Acessar o S3 a partir da VPC sem passar pela internet."

**Resposta curta:** Gateway VPC endpoint.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) · [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) · [PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
