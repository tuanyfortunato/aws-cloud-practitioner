# AWS Certificate Manager (ACM) e AWS Private CA

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um site precisa oferecer conexão HTTPS, mas obter, instalar e acompanhar a validade dos certificados pode causar trabalho e interrupções.

**Como este serviço ajuda?** ACM ajuda a provisionar e gerenciar certificados para integrações compatíveis. Certificados participam da identificação do servidor e da proteção da conexão.

**Exemplo do dia a dia:** A escola configura um certificado compatível no balanceador que recebe conexões HTTPS para seu site.

**O que ele não resolve sozinho?** Pedir um certificado não configura HTTPS em todos os recursos automaticamente. Validação do domínio, instalação ou integração e condições de renovação dependem da modalidade.

**Primeiras palavras para entender:**

- **HTTPS:** comunicação web protegida.
- **Certificado:** documento digital que associa uma identidade a uma chave pública.
- **TLS:** tecnologia de proteção da conexão.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / criptografia em trânsito · **Domínio:** 2 · **Escopo:** Regional (para CloudFront, **us-east-1**) · **Tópico do guia:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)
>
> **Em uma frase:** emite e gerencia certificados SSL/TLS, com renovação para certificados elegíveis; públicos não exportáveis em serviços integrados são gratuitos.
>
> **Escopo oficial:** ✅ No escopo (Private CA ⚪ não listado) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.


**Passo 1.** Identifique os nomes que precisam ser cobertos pelo certificado e a integração desejada.

**Passo 2.** Solicite ou disponibilize um certificado compatível e atenda à validação prevista. Associe-o ao ponto de conexão.

**Passo 3.** Acompanhe validade e condições de renovação. Emitir o certificado e configurar o recurso para usá-lo são etapas diferentes.

## 2. Recursos e opções, com significado

### Destaques

**Antes de ler este trecho:**

- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **ELB:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Certificados públicos** | **Gratuitos** para uso em serviços integrados: **ELB, CloudFront, API Gateway**, App Runner, Amplify… |
| **Validação** | **DNS** (recomendada, permite renovação automática; com Route 53 é um clique) ou e-mail. |
| **Renovação automática** | Para certificados validados por DNS em uso. |
| **Importar certificados** | De outras CAs (sem renovação automática). |
| **CloudFront** | Certificado precisa estar em **us-east-1**. |
| **Monitoramento** | Métricas de expiração e eventos no EventBridge. |

### AWS Private CA

**Antes de ler este trecho:**

- **CA:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.


Autoridade certificadora **privada** gerenciada para emitir certificados internos (serviços, dispositivos IoT, mTLS). Paga por CA/mês + certificados.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **HTTPS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.


Pedir um certificado não configura HTTPS em todos os recursos automaticamente. Validação do domínio, instalação ou integração e condições de renovação dependem da modalidade.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **FQDN:** Nome de domínio completo para identificar um destino. Resolver esse nome continua sendo tarefa DNS; nome não é credencial.


**Certificados públicos exportáveis** (desde 17/06/2025, pagos): permitem usar certificados do ACM em servidores próprios (EC2, on-premises). Validade de 395 dias; lançados a US$ 15 (FQDN) e US$ 149 (wildcard), hoje **US$ 7 e US$ 79** na página de preços. Na prova, siga: "público, gratuito, renovação automática, ELB/CloudFront" → ACM.

## 5. Caso resolvido: ligando as peças

A escola configura um certificado compatível no balanceador que recebe conexões HTTPS para seu site.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique os nomes que precisam ser cobertos pelo certificado e a integração desejada.
**Etapa 2:** Solicite ou disponibilize um certificado compatível e atenda à validação prevista. Associe-o ao ponto de conexão.
**Etapa 3:** Acompanhe validade e condições de renovação. Emitir o certificado e configurar o recurso para usá-lo são etapas diferentes.

**Resultado e responsabilidade:** ACM ajuda a provisionar e gerenciar certificados para integrações compatíveis. Certificados participam da identificação do servidor e da proteção da conexão.

**Recursos envolvidos:** Certificados, validação de domínio e associação a serviços.

**Decisões que precisam ser tomadas:** Domínios, tipo de certificado e serviço/região.

**Antes de ler este trecho:**

- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **ALB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.
- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.


**Outra situação comentada:** HTTPS no ALB: certificado ACM; criptografar volume EBS: chave KMS.

**Por que não concluir mais do que isso:** Renovação/uso depende da modalidade; certificado não autoriza leitura de dados

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Um site precisa oferecer conexão HTTPS, mas obter, instalar e acompanhar a validade dos certificados pode causar trabalho e interrupções.

**2. O que a solução fornece?**

ACM ajuda a provisionar e gerenciar certificados para integrações compatíveis. Certificados participam da identificação do servidor e da proteção da conexão.

**3. Que conclusão seria incorreta?**

Pedir um certificado não configura HTTPS em todos os recursos automaticamente. Validação do domínio, instalação ou integração e condições de renovação dependem da modalidade.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Certificados SSL/TLS gratuitos com renovação automática para o load balancer."

**Resposta curta:** ACM.


**Fundamento explicado no capítulo:** "Certificados SSL/TLS gratuitos com renovação automática para o load balancer." → ACM.

**Pergunta:** "Certificados para serviços internos, não públicos."

**Resposta curta:** AWS Private CA.

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**Fundamento explicado no capítulo:** "Certificados para serviços internos, não públicos." → AWS Private CA.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [ACM](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) · [Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
