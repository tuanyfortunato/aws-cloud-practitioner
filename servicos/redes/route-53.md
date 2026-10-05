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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.


**Passo 1.** Determine o nome que os usuários consultarão e o destino que deve atender.

**Passo 2.** Configure os registros e a política de resposta pertinente. O resolvedor DNS consulta informações para localizar o destino.

**Passo 3.** Acompanhe mudanças e saúde quando aplicável. Resolver o nome não confirma que a aplicação está respondendo corretamente.

## 2. Recursos e opções, com significado

### Funções

1. **Registro de domínios** (`.com`, `.com.br` etc.).


2. **DNS autoritativo** (hosted zones).

**Antes de ler este trecho:**

- **failover:** Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.


3. **Health checks** e failover.

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **híbrido:** Combinação de ambiente próprio e nuvem. É necessário definir quais partes ficam em cada lado e como se comunicam.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.


4. **Route 53 Resolver**: DNS híbrido (endpoints inbound/outbound entre VPC e on-premises) e **DNS Firewall**.

### Conceitos

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **IPv4 / IPv6:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **TTL:** Tempo de vida de uma informação. Em DNS pode orientar cache; em um banco pode indicar expiração de itens. O efeito concreto depende do serviço.
- **ELB:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.
- **CNAME / AAAA / TXT / MX / CAA / SOA:** Tipos de registro DNS. A e AAAA indicam endereços, CNAME indica outro nome, MX indica e-mail, TXT texto, CAA emissão de certificados e SOA informações da zona.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Hosted zone pública** | Responde na internet. |
| **Hosted zone privada** | Responde só dentro das VPCs associadas. |
| **Registros** | **A** (IPv4), **AAAA** (IPv6), **CNAME** (alias de nome; não no apex), **MX** (e-mail), **TXT**, **NS**, **SOA**, **CAA**… |
| **Alias record** | Extensão da AWS: aponta para recursos AWS (ELB, CloudFront, S3 website, API Gateway…), **funciona no apex** (`exemplo.com`) e consultas a alias de recursos AWS são **gratuitas**. |
| **TTL** | Tempo de cache da resposta nos resolvedores. |

### Políticas de roteamento

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **ativo-passivo:** Um ambiente atende normalmente e outro fica preparado para assumir. O preparo da alternativa pode variar bastante.
- **CIDR:** Notação de faixa de endereços de rede, como um endereço acompanhado de /24. A faixa define um conjunto de endereços, não uma senha ou uma permissão.
- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.
- **health check:** Teste de resposta usado para avaliar um destino. O teste e os limites precisam refletir a função observada; não equivale a uma investigação completa da aplicação.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **SLA:** Acordo de nível de serviço com condições e medidas próprias. Não é garantia de que a aplicação do cliente nunca falhará.


📌 **SLA de 100%** para o DNS autoritativo — único serviço AWS com SLA de 100% (API/console fora). Tecnicamente, a página do SLA dá crédito de 10% quando a disponibilidade mensal fica **abaixo de 100%** (no GovCloud, abaixo de 99,995%).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Route 53 indica o destino; ele não hospeda o código do site nem substitui a máquina que atende o pedido. Os tipos de registro e as políticas têm funções diferentes.

### ⚠️ Pegadinhas e não confundir

Route 53 decide **para onde ir** (DNS); CloudFront **entrega e faz cache** do conteúdo.


Geolocation (fronteiras, país) × Latency (desempenho) × Geoproximity (distância ajustável).

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.


Route 53 é um dos serviços **globais** (com IAM, CloudFront, Organizations).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por hosted zone por mês + por milhão de consultas (alias para recursos AWS grátis) + health checks + domínios registrados (anual).

## 5. Caso resolvido: ligando as peças

**Antes de ler este trecho:**

- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.


O aluno digita um nome de site e precisa chegar ao endereço que atende a escola. A primeira tarefa é resolver esse nome, antes de a aplicação atender a requisição.

A equipe configura a zona e o registro adequados ao domínio e ao destino. Uma consulta DNS obtém as informações de endereço conforme o tipo de registro e a política. O cliente então inicia a comunicação com o destino indicado.

DNS correto não garante que o servidor responde nem que os dados estão autorizados. CloudFront pode distribuir conteúdo; um balanceador pode distribuir conexões; Route 53 informa respostas de nome. Esses recursos podem cooperar, mas resolvem etapas diferentes.

**Recursos envolvidos:** Hosted zones, records, health checks e políticas de roteamento.

**Decisões que precisam ser tomadas:** Domínio, registros, TTL e política.


**Outra situação comentada:** Usuários encontram o endereço do site: Route 53; distribuição de conteúdo: CloudFront.

**Por que não concluir mais do que isso:** DNS não transporta nem balanceia cada pacote da sessão como um load balancer

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma pessoa digita o nome de um site, mas o computador precisa descobrir para qual endereço enviar a comunicação.

**2. O que a solução fornece?**

Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde. DNS relaciona nomes a informações de endereço por registros.

**3. Que conclusão seria incorreta?**

Route 53 indica o destino; ele não hospeda o código do site nem substitui a máquina que atende o pedido. Os tipos de registro e as políticas têm funções diferentes.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Registrar domínio e gerenciar DNS."

**Resposta curta:** Route 53.


**Fundamento explicado no capítulo:** "Registrar domínio e gerenciar DNS." → Route 53.

**Pergunta:** "Mandar 10% dos usuários para a nova versão."

**Resposta curta:** Weighted.


**Fundamento explicado no capítulo:** "Mandar 10% dos usuários para a nova versão." → Weighted.

**Pergunta:** "Usuários da Alemanha devem ver o site em alemão."

**Resposta curta:** Geolocation.


**Fundamento explicado no capítulo:** "Usuários da Alemanha devem ver o site em alemão." → Geolocation.

**Pergunta:** "Enviar para a região mais rápida."

**Resposta curta:** Latency-based.


**Fundamento explicado no capítulo:** "Enviar para a região mais rápida." → Latency-based.

**Pergunta:** "Se o site principal cair, mandar para a página de manutenção."

**Resposta curta:** Failover com health check.


**Fundamento explicado no capítulo:** "Se o site principal cair, mandar para a página de manutenção." → Failover com health check.

**Pergunta:** "Qual serviço tem SLA de 100%?"

**Resposta curta:** Route 53.


**Fundamento explicado no capítulo:** "Qual serviço tem SLA de 100%?" → Route 53.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
