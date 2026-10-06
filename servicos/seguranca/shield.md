# AWS Shield

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Muitos pedidos maliciosos podem tentar sobrecarregar um serviço e impedir que pessoas legítimas o utilizem.

**Como este serviço ajuda?** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.

**Exemplo do dia a dia:** Um site público usa os recursos de proteção aplicáveis à sua arquitetura para reduzir o impacto de tentativas de sobrecarga.

**O que ele não resolve sozinho?** Shield não elimina todos os riscos de segurança nem substitui regras de acesso, proteção da aplicação ou planejamento de capacidade. Standard e Advanced têm condições diferentes.

**Primeiras palavras para entender:**

- **DDoS:** ataque distribuído para sobrecarregar um serviço.
- **Disponibilidade:** conseguir usar o sistema quando necessário.
- **Mitigação:** reduzir o impacto de um ataque.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / proteção DDoS · **Domínio:** 2 · **Escopo:** Global (borda) e regional · **Tópico do guia:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** proteção gerenciada contra ataques de negação de serviço distribuída (DDoS).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **DDoS:** Ataque distribuído que tenta sobrecarregar um serviço e impedir seu uso legítimo. É diferente de tentar explorar um campo vulnerável de um programa.

**Passo 1.** Identifique os recursos e o tipo de exposição que precisam de proteção contra sobrecarga.

**Passo 2.** Avalie a modalidade e sua cobertura para a arquitetura. Os mecanismos de proteção atuam conforme suas condições.

**Passo 3.** Observe eventos e prepare resposta. Proteção contra DDoS não corrige vulnerabilidades do código nem substitui todos os controles de aplicação.

## 2. Recursos e opções, com significado

### Standard × Advanced

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **UDP:** Protocolo de transporte por datagramas, sem as mesmas garantias de entrega e ordem do TCP. A aplicação precisa lidar com os requisitos que o protocolo não fornece.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.
- **ELB:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.
- **SRT:** Protocolo de transporte de mídia. Compatibilidade de transmissão depende do produto e da configuração; não é uma classe de armazenamento.
- **SYN:** Sinalização do início de conexão TCP. Ataques que exploram esse fluxo são diferentes de uma consulta de aplicação autorizada.

| | **Shield Standard** | **Shield Advanced** |
|---|---|---|
| Custo | **Gratuito**, automático para todos | 📌 **US$ 3.000/mês por organização**, compromisso de **1 ano** + data transfer out dos recursos protegidos |
| Camadas | 3 e 4 (SYN flood, UDP reflection…) | 3, 4 e **7** (com WAF) |
| Recursos | Todos (melhor em CloudFront e Route 53) | EC2 (Elastic IP), ELB, CloudFront, Route 53, Global Accelerator |
| Time de resposta | — | **Shield Response Team (SRT) 24/7** |
| **Proteção de custo** | — | **Créditos** pelo aumento de uso (escalonamento) causado por DDoS |
| Visibilidade | Básica | Métricas, relatórios e diagnóstico de ataques em tempo quase real |
| WAF | Pago à parte | **Sem custo adicional** nos recursos protegidos |
| Outros | — | Detecção e mitigação automática na camada 7, health-based detection, proteção de grupos, integração com Firewall Manager |

A assinatura do Advanced cobre **todas as contas** da Organization.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **AWS CloudFormation:** CloudFormation usa um arquivo de descrição para criar e atualizar conjuntos de recursos AWS compatíveis, com suas dependências.
- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **role:** Papel que fornece permissões a uma sessão que o assume. O termo função IAM não significa um trecho de código como uma função Lambda.
- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.

✔️ Para acionar o SRT é preciso plano **Business Support+, Enterprise ou Unified Operations** (a fonte cita "Business Support") (documentação do AWS CloudFormation, 10/2026) e uma IAM role que autorize o SRT (política gerenciada `AWSShieldDRTAccessPolicy`).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.

Shield não elimina todos os riscos de segurança nem substitui regras de acesso, proteção da aplicação ou planejamento de capacidade. Standard e Advanced têm condições diferentes.

### ⚠️ Pegadinhas

**Antes de ler este trecho:**

- **XSS:** Ataque que busca executar conteúdo indevido no contexto de uma página acessada pelo usuário. Regras de proteção e correções do código atendem partes desse risco.
- **SQL injection:** Tentativa de manipular comandos de banco por entradas indevidas. Proteger a entrada não dispensa corrigir como a aplicação constrói e executa consultas.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.

"DDoS volumétrico" → Shield. "SQL injection/XSS" → WAF.

"Reembolso do custo de escalonamento + especialistas 24/7" → **Shield Advanced**.

"Proteção DDoS que todo cliente tem sem custo" → **Shield Standard**.

## 4. Caso resolvido: ligando as peças

Um site público usa os recursos de proteção aplicáveis à sua arquitetura para reduzir o impacto de tentativas de sobrecarga.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique os recursos e o tipo de exposição que precisam de proteção contra sobrecarga.
**Etapa 2:** Avalie a modalidade e sua cobertura para a arquitetura. Os mecanismos de proteção atuam conforme suas condições.
**Etapa 3:** Observe eventos e prepare resposta. Proteção contra DDoS não corrige vulnerabilidades do código nem substitui todos os controles de aplicação.

**Resultado e responsabilidade:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.

**Recursos envolvidos:** Proteção Standard e assinatura Advanced para recursos elegíveis.

**Decisões que precisam ser tomadas:** Recursos protegidos e recursos extras contratados.

**Antes de ler este trecho:**

- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.

**Outra situação comentada:** Ataque volumétrico: Shield; requisição HTTP maliciosa: WAF pode complementar.

**Por que não concluir mais do que isso:** Não equivale a filtro de SQL injection nem corrige vulnerabilidades no código

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Qual proteção DDoS todo cliente tem sem custo?"

**Resposta curta:** Shield Standard.

**Pergunta:** "Acesso a especialistas 24/7 e proteção de custo durante ataques."

**Resposta curta:** Shield Advanced.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
