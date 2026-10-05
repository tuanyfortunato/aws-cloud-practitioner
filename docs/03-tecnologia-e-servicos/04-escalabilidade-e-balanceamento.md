# 3.4 Escalabilidade e balanceamento de carga

## 🧠 Antes de começar

**Qual é a dificuldade?** Muitos visitantes chegam ao mesmo tempo. Uma máquina pode não atender, e várias máquinas sem distribuição adequada também podem ficar desequilibradas.

**A ideia em palavras simples:** Escalabilidade ajusta a capacidade; balanceamento distribui o tráfego. Os dois podem trabalhar juntos, mas resolvem partes diferentes do atendimento.

**Exemplo do dia a dia:** Durante uma promoção, o grupo adiciona máquinas e o balanceador encaminha pedidos aos destinos disponíveis. Depois, a quantidade de máquinas pode diminuir conforme as regras.

**O que não concluir?** Balanceador não cria máquinas por si só; aumentar máquinas não resolve todo gargalo. A aplicação e o armazenamento também precisam suportar o desenho.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Health check** | verificação periódica de que o servidor está respondendo. |
| **Camada 7 / camada 4** | nível da comunicação: 7 entende HTTP (caminhos, cabeçalhos); 4 só vê conexões TCP/UDP. |
| **Launch template** | o molde usado para criar as instâncias do grupo. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon EC2 Auto Scaling](../../servicos/computacao/ec2-auto-scaling.md) · [Elastic Load Balancing (ELB)](../../servicos/computacao/elastic-load-balancing.md)

⬅️ [3.3 Amazon EC2](03-ec2.md) · 🏠 [Índice do domínio](README.md) · [3.5 Containers e serverless](05-containers-e-serverless.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **balanceador:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.


O atendimento tem duas decisões: quantos recursos existem e para qual deles cada pedido vai. A primeira é capacidade; a segunda, distribuição. Um balanceador trabalha com destinos existentes e não cria sozinho a capacidade de que eles precisam.

Ao aumentar máquinas, verifique se a aplicação pode funcionar em várias cópias e compartilhar ou acessar seus dados adequadamente. Um banco sobrecarregado pode continuar sendo o limite mesmo com mais máquinas web. Escalar exige observar o verdadeiro gargalo.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

num **supermercado**, o **Auto Scaling** é o gerente que abre ou fecha caixas conforme a fila; o **Load Balancer** é o funcionário que aponta "o caixa 3 está livre" e nunca manda ninguém para o caixa fechado.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **Amazon EC2 / EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Amazon EC2 Auto Scaling / EC2 Auto Scaling:** O EC2 Auto Scaling aumenta ou diminui a quantidade de máquinas EC2 seguindo regras que você configura.


**Amazon EC2 Auto Scaling**

**Antes de ler este trecho:**

- **launch template:** Modelo versionado de parâmetros para iniciar máquinas. Facilita repetir configurações; não contém por si só todas as regras da aplicação.
- **ASG:** Grupo de Auto Scaling: conjunto cuja quantidade e saúde são administradas conforme uma configuração e suas regras.


  - **Auto Scaling Group (ASG):** grupo de instâncias com capacidade **mínima, desejada e máxima**, criadas a partir de um **launch template**.
**Antes de ler este trecho:**

- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **métrica:** Medida observada ao longo do tempo, como utilização ou número de erros. O número precisa de unidade, período e contexto para ter significado.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.


  - **Políticas de escalonamento:** *target tracking* (manter uma métrica num alvo, ex.: CPU em 50%), *step/simple* (degraus conforme alarmes), *scheduled* (horários conhecidos) e *predictive* (prevê a demanda com ML).

  - **Health checks:** substitui automaticamente instâncias com falha.
**Antes de ler este trecho:**

- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.


  - Distribui instâncias entre AZs para alta disponibilidade.

  - O Auto Scaling em si não tem custo; você paga as instâncias.
**Antes de ler este trecho:**

- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**AWS Auto Scaling:** serviço que configura escalonamento para vários recursos de uma vez (EC2, ECS, DynamoDB, Aurora).

**Antes de ler este trecho:**

- **Elastic Load Balancing:** O Elastic Load Balancing recebe conexões e encaminha o tráfego aos destinos configurados.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


**Elastic Load Balancing (ELB):** Distribui o tráfego entre destinos saudáveis em várias AZs.


**Antes de ler este trecho:**

- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **segundo:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **TCP:** Protocolo de transporte orientado a conexão, com mecanismos de entrega e ordem. É usado por muitas aplicações; não acrescenta criptografia por si só.
- **UDP:** Protocolo de transporte por datagramas, sem as mesmas garantias de entrega e ordem do TCP. A aplicação precisa lidar com os requisitos que o protocolo não fornece.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **HTTPS / TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **ALB / NLB / GWLB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
- **IPS:** Sistema de prevenção de intrusões. Atua em condições e tráfego compatíveis; não é uma correção automática de todo software vulnerável.
- **IDS:** Sistema de detecção de intrusões. Detectar é diferente de bloquear; o efeito depende da ferramenta e da configuração.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Tipo | Camada | Uso |
| --- | --- | --- |
| Application Load Balancer (ALB) | 7 (HTTP/HTTPS) | Roteamento por caminho, host ou cabeçalho; microsserviços e containers; integra com WAF |
| Network Load Balancer (NLB) | 4 (TCP/UDP/TLS) | Altíssima performance, milhões de requisições por segundo, IP estático por AZ |
| Gateway Load Balancer (GWLB) | 3 (rede) | Encaminha tráfego para appliances virtuais de terceiros (firewalls, IDS/IPS) |
| Classic Load Balancer | 4 e 7 | Geração antiga, não recomendado |


**Antes de ler este trecho:**

- **ACM:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.


**Funções do ELB:** health checks, terminação SSL/TLS (com certificado do ACM), distribuição entre AZs.

**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.


**Cai na prova:** "rotear /api para um serviço e /imagens para outro" = ALB; "tráfego TCP com latência ultrabaixa" = NLB; "inspecionar tráfego com firewall de terceiros" = GWLB; "aumentar e diminuir instâncias conforme demanda" = Auto Scaling.

## 3. Como analisar uma situação


**Primeiro, identifique o funcionamento:** Load balancer recebe tráfego e escolhe destinos saudáveis. Auto Scaling ajusta quantidade de instâncias e substitui instâncias não saudáveis conforme configuração.

**Depois, compare as escolhas:** ALB para HTTP e regras por host/caminho; NLB para transporte e requisitos como IP estático. Auto Scaling mantém capacidade dentro dos mínimos e máximos definidos.

**Por fim, verifique o limite:** Balanceador não cria sozinho novas instâncias. Auto Scaling não compartilha automaticamente sessões gravadas no disco local. Saúde e capacidade do banco também importam.

## 4. Caso resolvido

Na Black Friday o tráfego triplica. Um load balancer sem capacidade adicional garante atendimento?

**Raciocínio e resposta:** Não. Ele distribui a capacidade existente. Auto Scaling adiciona instâncias quando suas políticas e limites permitem; a aplicação precisa suportar o crescimento.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Muitos visitantes chegam ao mesmo tempo. Uma máquina pode não atender, e várias máquinas sem distribuição adequada também podem ficar desequilibradas.

**2. O que a solução fornece?**

Escalabilidade ajusta a capacidade; balanceamento distribui o tráfego. Os dois podem trabalhar juntos, mas resolvem partes diferentes do atendimento.

**3. Que conclusão seria incorreta?**

Balanceador não cria máquinas por si só; aumentar máquinas não resolve todo gargalo. A aplicação e o armazenamento também precisam suportar o desenho.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Explicar **mínimo, desejado e máximo** de um Auto Scaling Group e os tipos de política.
- [ ] Diferenciar **ALB** (camada 7, HTTP, por caminho), **NLB** (camada 4, TCP/UDP, altíssima performance) e **GWLB** (appliances de rede).
- [ ] Saber que o Auto Scaling **não tem custo** próprio (paga-se as instâncias).

**Dica de revisão para a prova:** "Aumentar/diminuir instâncias" → **Auto Scaling**. "Distribuir tráfego" → **ELB**. "/api para um serviço, /imagens para outro" → **ALB**. "TCP, latência ultrabaixa, IP fixo" → **NLB**. "Firewall de terceiros" → **GWLB**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Como ajustar automaticamente o número de instâncias à demanda?"

**Resposta curta:** EC2 Auto Scaling.


**Fundamento explicado no capítulo:** "Como ajustar automaticamente o número de instâncias à demanda?" → EC2 Auto Scaling.

**Pergunta:** "A loja tem pico toda sexta às 18h."

**Resposta curta:** Scheduled scaling.


**Fundamento explicado no capítulo:** "A loja tem pico toda sexta às 18h." → Scheduled scaling.

**Pergunta:** "Manter a CPU média do grupo em 50%."

**Resposta curta:** Target tracking.


**Fundamento explicado no capítulo:** "Manter a CPU média do grupo em 50%." → Target tracking.

**Pergunta:** "Como distribuir tráfego entre instâncias em várias AZs?"

**Resposta curta:** Elastic Load Balancing.


**Fundamento explicado no capítulo:** "Como distribuir tráfego entre instâncias em várias AZs?" → Elastic Load Balancing.

**Pergunta:** "Qual load balancer roteia por caminho de URL?"

**Resposta curta:** ALB.

**Antes de ler este trecho:**

- **URL:** Endereço usado para acessar um recurso. Uma URL pode incluir domínio, caminho e parâmetros; possuir o endereço não significa ter autorização.


**Fundamento explicado no capítulo:** "Qual load balancer roteia por caminho de URL?" → ALB.

**Pergunta:** "Qual load balancer para milhões de conexões TCP com IP fixo?"

**Resposta curta:** NLB.


**Fundamento explicado no capítulo:** "Qual load balancer para milhões de conexões TCP com IP fixo?" → NLB.

**Pergunta:** "Qual load balancer para appliances de firewall de terceiros?"

**Resposta curta:** Gateway Load Balancer.


**Fundamento explicado no capítulo:** "Qual load balancer para appliances de firewall de terceiros?" → Gateway Load Balancer.

**Pergunta:** "Auto Scaling e ELB juntos garantem o quê?"

**Resposta curta:** Alta disponibilidade e elasticidade (instâncias com falha são substituídas e o tráfego vai só para as saudáveis).

**Antes de ler este trecho:**

- **elasticidade:** Ajuste da capacidade para crescer e reduzir conforme a necessidade, dentro das regras e dos limites da solução.


**Fundamento explicado no capítulo:** "Auto Scaling e ELB juntos garantem o quê?" → Alta disponibilidade e elasticidade (instâncias com falha são substituídas e o tráfego vai só para as saudáveis).

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.3 Amazon EC2](03-ec2.md) · 🏠 [Índice do domínio](README.md) · [3.5 Containers e serverless](05-containers-e-serverless.md) ➡️
