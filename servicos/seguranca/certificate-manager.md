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

## 1. A sequência de funcionamento

**Passo 1.** Identifique os nomes que precisam ser cobertos pelo certificado e a integração desejada.

**Passo 2.** Solicite ou disponibilize um certificado compatível e atenda à validação prevista. Associe-o ao ponto de conexão.

**Passo 3.** Acompanhe validade e condições de renovação. Emitir o certificado e configurar o recurso para usá-lo são etapas diferentes.

## 2. Recursos e opções, com significado

### Destaques

| Item | Detalhe |
|---|---|
| **Certificados públicos** | **Gratuitos** para uso em serviços integrados: **ELB, CloudFront, API Gateway**, App Runner, Amplify… |
| **Validação** | **DNS** (recomendada, permite renovação automática; com Route 53 é um clique) ou e-mail. |
| **Renovação automática** | Para certificados validados por DNS em uso. |
| **Importar certificados** | De outras CAs (sem renovação automática). |
| **CloudFront** | Certificado precisa estar em **us-east-1**. |
| **Monitoramento** | Métricas de expiração e eventos no EventBridge. |

### AWS Private CA

Autoridade certificadora **privada** gerenciada para emitir certificados internos (serviços, dispositivos IoT, mTLS). Paga por CA/mês + certificados.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Pedir um certificado não configura HTTPS em todos os recursos automaticamente. Validação do domínio, instalação ou integração e condições de renovação dependem da modalidade.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

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

**Outra situação comentada:** HTTPS no ALB: certificado ACM; criptografar volume EBS: chave KMS.

**Por que não concluir mais do que isso:** Renovação/uso depende da modalidade; certificado não autoriza leitura de dados

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Certificados SSL/TLS gratuitos com renovação automática para o load balancer."

**Resposta curta:** ACM.

**Pergunta:** "Certificados para serviços internos, não públicos."

**Resposta curta:** AWS Private CA.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [ACM](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) · [Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
