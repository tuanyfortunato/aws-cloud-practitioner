# AWS Firewall Manager e AWS Network Firewall

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa precisa padronizar proteções em várias contas e também pode precisar inspecionar tráfego que passa pela rede.

**Como este serviço ajuda?** Firewall Manager coordena políticas de proteção em recursos compatíveis de uma organização. Network Firewall inspeciona tráfego de rede conforme regras e caminhos configurados.

**Exemplo do dia a dia:** A equipe central define uma política comum de proteção. Para uma necessidade de inspeção de rede, avalia separadamente Network Firewall.

**O que ele não resolve sozinho?** Administrar políticas é diferente de inspecionar cada conexão. São serviços distintos e têm escopos de prova diferentes, indicados abaixo.

**Primeiras palavras para entender:**

- **Firewall:** controle de tráfego por regras.
- **Política central:** regras administradas para vários ambientes.
- **Inspeção:** análise de comunicações.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança de rede · **Domínio:** 2 · **Escopo:** Organização (Firewall Manager) / VPC (Network Firewall) · **Tópico do guia:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** o Firewall Manager **governa** regras de firewall em todas as contas; o Network Firewall **é** um firewall gerenciado para a VPC.
>
> **Escopo oficial:** 🔀 Firewall Manager ✅ · Network Firewall ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


**Passo 1.** Separe a necessidade de administrar políticas da necessidade de inspecionar tráfego.

**Passo 2.** Use Firewall Manager para políticas compatíveis da organização; avalie Network Firewall para o caminho de rede que precisa de inspeção.

**Passo 3.** Configure escopo e verifique o efeito dos controles. As duas ferramentas não executam a mesma função.

## 2. Recursos e opções, com significado

### AWS Firewall Manager

**Antes de ler este trecho:**

- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **AWS Config:** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.
- **AWS Organizations / Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Função** | Gerenciamento **central** de políticas de segurança em todas as contas e recursos do **AWS Organizations**, aplicando-as automaticamente a novos recursos. |
| **Políticas** | **WAF**, **Shield Advanced**, **security groups** (auditoria e regras comuns), **Network Firewall**, **Route 53 Resolver DNS Firewall**, firewalls de terceiros do Marketplace. |
| **Pré-requisitos** | AWS Organizations (todos os recursos), **AWS Config** ativado, conta administradora do Firewall Manager. |
| **Cobrança** | Por política por região/mês + recursos subjacentes (WAF, Config). |

### AWS Network Firewall ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **porta:** Número que ajuda a identificar o serviço de destino de uma comunicação. Liberar uma porta autoriza tráfego segundo a regra, mas não configura a aplicação para responder.
- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.
- **TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **subnet:** Segmento de uma rede virtual. Na VPC, uma subnet pertence a uma zona de disponibilidade; suas rotas e controles ajudam a definir a conectividade.
- **stateful:** Controle que acompanha o estado da comunicação e trata respostas conforme esse estado. No security group, isso evita exigir uma regra independente para a resposta de uma conexão permitida.
- **stateless:** Controle que avalia cada direção sem manter o mesmo estado de conexão. Regras de ida e de volta precisam ser consideradas separadamente.
- **implantação:** Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.
- **IPS:** Sistema de prevenção de intrusões. Atua em condições e tráfego compatíveis; não é uma correção automática de todo software vulnerável.
- **FQDN:** Nome de domínio completo para identificar um destino. Resolver esse nome continua sendo tarefa DNS; nome não é credencial.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Função** | Firewall de rede **stateful**, gerenciado e escalável, para filtrar todo o tráfego que entra, sai ou atravessa a VPC. |
| **Regras** | Stateless e stateful; compatível com regras **Suricata** (IPS); filtragem por **domínio** (FQDN), IP, porta, protocolo; inspeção TLS. |
| **Implantação** | Endpoints numa *firewall subnet*; rotas direcionam o tráfego por ele; pode ficar centralizado com Transit Gateway. |
| **Uso** | Prevenção de intrusão (IPS), bloquear saída para domínios não autorizados, inspeção entre VPCs. |
| **Cobrança** | Por endpoint-hora + GB processado. |

### Comparação de "firewalls" da AWS

**Security group**

**Antes de ler este trecho:**

- **security group:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **ENI:** Interface de rede virtual. Ela associa endereços e configurações de comunicação a recursos compatíveis.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


**Camada:** 3/4

**Onde:** Instância/ENI (stateful)

**Network ACL**

**Antes de ler este trecho:**

- **ACL / Network ACL:** ACL significa lista de controle de acesso. A NACL da VPC controla tráfego no segmento de rede; ACL de armazenamento tem outro contexto. Não trate as duas como a mesma função.


**Camada:** 3/4

**Onde:** Subnet (stateless)

**Network Firewall**


**Camada:** 3–7

**Onde:** VPC (stateful, IPS, domínios)

**WAF**

**Antes de ler este trecho:**

- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **ALB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.


**Camada:** 7

**Onde:** CloudFront, ALB, API Gateway…

**Shield**

**Antes de ler este trecho:**

- **DDoS:** Ataque distribuído que tenta sobrecarregar um serviço e impedir seu uso legítimo. É diferente de tentar explorar um campo vulnerável de um programa.


**Camada:** 3/4 (+7 Advanced)

**Onde:** DDoS

**Firewall Manager**


**Onde:** Governança central de todos acima

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Administrar políticas é diferente de inspecionar cada conexão. São serviços distintos e têm escopos de prova diferentes, indicados abaixo.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

A equipe central define uma política comum de proteção. Para uma necessidade de inspeção de rede, avalia separadamente Network Firewall.

**Aplicando a sequência à situação:**

**Etapa 1:** Separe a necessidade de administrar políticas da necessidade de inspecionar tráfego.
**Etapa 2:** Use Firewall Manager para políticas compatíveis da organização; avalie Network Firewall para o caminho de rede que precisa de inspeção.
**Etapa 3:** Configure escopo e verifique o efeito dos controles. As duas ferramentas não executam a mesma função.

**Resultado e responsabilidade:** Firewall Manager coordena políticas de proteção em recursos compatíveis de uma organização. Network Firewall inspeciona tráfego de rede conforme regras e caminhos configurados.

**Recursos envolvidos:** Políticas centralizadas do Firewall Manager; endpoints/regras de Network Firewall.

**Decisões que precisam ser tomadas:** Escopo de contas/recursos e regras.


**Outra situação comentada:** Mesma política WAF em várias contas: Firewall Manager, com Organizations e configuração necessária.

**Por que não concluir mais do que isso:** Não são o mesmo produto; Network Firewall está fora do escopo consultado

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A empresa precisa padronizar proteções em várias contas e também pode precisar inspecionar tráfego que passa pela rede.

**2. O que a solução fornece?**

Firewall Manager coordena políticas de proteção em recursos compatíveis de uma organização. Network Firewall inspeciona tráfego de rede conforme regras e caminhos configurados.

**3. Que conclusão seria incorreta?**

Administrar políticas é diferente de inspecionar cada conexão. São serviços distintos e têm escopos de prova diferentes, indicados abaixo.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Aplicar as mesmas regras de WAF em todas as contas."

**Resposta curta:** Firewall Manager.


**Fundamento explicado no capítulo:** "Aplicar as mesmas regras de WAF em todas as contas." → Firewall Manager.

**Pergunta:** "Inspecionar e filtrar todo o tráfego que entra na VPC (IPS)."

**Resposta curta:** Network Firewall.


**Fundamento explicado no capítulo:** "Inspecionar e filtrar todo o tráfego que entra na VPC (IPS)." → Network Firewall.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) · [Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
