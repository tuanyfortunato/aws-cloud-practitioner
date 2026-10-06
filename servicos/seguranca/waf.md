# AWS WAF (Web Application Firewall)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um site precisa analisar pedidos web e bloquear padrões indesejados, como tentativas de explorar campos de entrada ou volumes excessivos de chamadas.

**Como este serviço ajuda?** WAF aplica regras ao tráfego web em integrações compatíveis. Você define critérios de inspeção e ações como permitir ou bloquear.

**Exemplo do dia a dia:** A escola configura regras para inspecionar pedidos ao seu site e limitar padrões de requisições suspeitos.

**O que ele não resolve sozinho?** WAF não corrige o código vulnerável nem protege automaticamente todo protocolo e recurso AWS. A regra deve estar associada ao ponto de entrada compatível.

**Primeiras palavras para entender:**

- **Requisição:** pedido feito ao site.
- **Regra:** condição e ação de inspeção.
- **Web ACL:** conjunto de regras aplicado pelo WAF.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / proteção de aplicações · **Domínio:** 2 · **Escopo:** Global (CloudFront) ou Regional · **Tópico do guia:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** firewall de **camada 7** que filtra requisições HTTP(S) maliciosas antes que cheguem à aplicação.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.

**Passo 1.** Identifique o ponto web compatível e o padrão de pedidos que deseja permitir, observar ou bloquear.

**Passo 2.** Crie regras e associe o conjunto ao recurso. Os pedidos são inspecionados conforme a configuração.

**Passo 3.** Acompanhe resultados e ajuste regras. Um bloqueio incorreto pode afetar usuários legítimos; a correção do programa também precisa ser planejada.

## 2. Recursos e opções, com significado

### Onde se associa

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **ALB / NLB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
- **REST:** Estilo de API que usa recursos e operações, frequentemente por HTTP. O código integrado continua sendo responsável pelo comportamento da aplicação.

**CloudFront, ALB, API Gateway (REST), AppSync, Cognito user pools**, App Runner, Verified Access, Amplify. ⚠️ **Não** em NLB nem diretamente em EC2.

### Conceitos e configurações

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **ACL:** ACL significa lista de controle de acesso. A NACL da VPC controla tráfego no segmento de rede; ACL de armazenamento tem outro contexto. Não trate as duas como a mesma função.
- **XSS:** Ataque que busca executar conteúdo indevido no contexto de uma página acessada pelo usuário. Regras de proteção e correções do código atendem partes desse risco.
- **SQL injection:** Tentativa de manipular comandos de banco por entradas indevidas. Proteger a entrada não dispensa corrigir como a aplicação constrói e executa consultas.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **WCU:** Capacidade provisionada de escrita e leitura no DynamoDB. Tamanho do item e condições da operação influenciam consumo; unidades não equivalem diretamente a usuários.
- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.
- **OWASP:** Organização e referências de segurança de aplicações. Listas de riscos ajudam a orientar avaliação, não garantem proteção por si só.
- **CAPTCHA:** Desafio ou mecanismo para diferenciar comportamentos humanos e automatizados. É uma opção de controle, não uma autorização universal para acessar dados.
- **ATP / ACFP:** Recursos de proteção WAF associados a tentativas de tomada de conta e criação fraudulenta de contas. Exigem configuração e contexto de uso compatíveis.

| Item | Detalhe |
|---|---|
| **Web ACL** | Conjunto de regras com ação padrão (allow/block). |
| **Rules** | Condições: IP sets, países (**geo match**), strings/regex, tamanho, cabeçalhos, **SQL injection**, **XSS**. Ações: allow, block, count, CAPTCHA, challenge. |
| **Rate-based rules** | Limitam requisições por IP (ou chave) em uma janela → mitigam *HTTP floods*, *brute force*. |
| **Managed rule groups** | Prontos da AWS (Core rule set, SQLi, IP reputation, bots conhecidos, OWASP) e do **Marketplace**. |
| **Bot Control** | Identifica e controla bots (pago). |
| **Fraud Control** | Proteção contra tomada de conta (ATP) e criação fraudulenta de contas (ACFP). |
| **Logs** | Para CloudWatch Logs, S3 ou Firehose. |
| **Capacidade (WCU)** | Cada regra consome unidades 🧊. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.

WAF não corrige o código vulnerável nem protege automaticamente todo protocolo e recurso AWS. A regra deve estar associada ao ponto de entrada compatível.

### ⚠️ Pegadinhas

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **security group:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.
- **DDoS:** Ataque distribuído que tenta sobrecarregar um serviço e impedir seu uso legítimo. É diferente de tentar explorar um campo vulnerável de um programa.

WAF (aplicação, camada 7) × Shield (DDoS, camadas 3/4) × Network Firewall (VPC, camadas 3–7) × Security group/NACL.

"Bloquear países" → WAF geo match ou geo restriction do CloudFront.

"Mesmas regras em todas as contas" → **Firewall Manager**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por Web ACL/mês + por regra/mês + por milhão de requisições; extras para Bot/Fraud Control (🧊 valores). Sem custo extra nos recursos protegidos pelo Shield Advanced.

## 5. Caso resolvido: ligando as peças

A escola configura regras para inspecionar pedidos ao seu site e limitar padrões de requisições suspeitos.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique o ponto web compatível e o padrão de pedidos que deseja permitir, observar ou bloquear.
**Etapa 2:** Crie regras e associe o conjunto ao recurso. Os pedidos são inspecionados conforme a configuração.
**Etapa 3:** Acompanhe resultados e ajuste regras. Um bloqueio incorreto pode afetar usuários legítimos; a correção do programa também precisa ser planejada.

**Resultado e responsabilidade:** WAF aplica regras ao tráfego web em integrações compatíveis. Você define critérios de inspeção e ações como permitir ou bloquear.

**Recursos envolvidos:** Web ACL, rules, rule groups e associação a recursos.

**Decisões que precisam ser tomadas:** Critérios HTTP, rate-based rules, ação e logging.

**Outra situação comentada:** SQL injection em aplicação web suportada: WAF; modo Count ajuda a avaliar regra antes de bloquear.

**Por que não concluir mais do que isso:** Não é firewall universal de toda EC2 nem corrige a causa no código

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Bloquear SQL injection e XSS."

**Resposta curta:** WAF.

**Pergunta:** "Limitar requisições por IP."

**Resposta curta:** Rate-based rule do WAF.

**Pergunta:** "Em quais serviços o WAF pode ser usado?"

**Resposta curta:** CloudFront, ALB, API Gateway, AppSync, Cognito.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
