# AWS CloudHSM

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Algumas organizações precisam de controle sobre um equipamento criptográfico dedicado, com requisitos diferentes dos atendidos por um serviço de chaves mais abstrato.

**Como este serviço ajuda?** CloudHSM fornece módulos de segurança de hardware para operações e armazenamento criptográfico. Você administra aspectos como usuários e chaves dentro dessa solução.

**Exemplo do dia a dia:** Uma organização com exigências específicas de controle criptográfico avalia um conjunto de HSMs para sua aplicação compatível.

**O que ele não resolve sozinho?** HSM dedicado não significa menos trabalho de administração. CloudHSM e KMS dividem responsabilidades de formas diferentes; a aplicação também precisa integrar-se corretamente.

**Primeiras palavras para entender:**

- **HSM:** equipamento especializado em proteger chaves e executar operações criptográficas.
- **Dedicado:** destinado ao cliente.
- **Cluster:** conjunto de equipamentos coordenados.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / criptografia · **Domínio:** 2 · **Escopo:** Regional (cluster multi-AZ na VPC) · **Tópico do guia:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)
>
> **Em uma frase:** HSM (hardware security module) **dedicado e exclusivo** na nuvem, em que só você controla as chaves.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Avalie os requisitos de controle criptográfico e prepare os módulos compatíveis.

**Passo 2.** Administre usuários e chaves na solução e integre o software às operações necessárias.

**Passo 3.** Planeje disponibilidade e proteção operacional. Controle dedicado exige trabalho que não deve ser confundido com a abstração de KMS.

## 2. Recursos e opções, com significado

### Destaques

| Item | Detalhe |
|---|---|
| **Single-tenant** | Hardware dedicado a você; validação **FIPS 140 nível 3**. |
| **Controle** | **Você** gerencia usuários e chaves; a **AWS não tem acesso** às chaves. Perdeu as credenciais → perdeu as chaves. |
| **Alta disponibilidade** | Cluster com HSMs em várias AZs (responsabilidade do cliente montar). |
| **APIs padrão** | PKCS#11, JCE (Java), CNG/KSP (Windows), OpenSSL. |
| **Integração** | Custom key store do KMS; offload SSL/TLS de servidores web; Oracle TDE; assinatura de código; CA privada. |

### Responsabilidade compartilhada

**AWS:** hardware, disponibilidade do HSM, patches de firmware.

**Cliente:** usuários, chaves, backup das credenciais, montar cluster multi-AZ, aplicação.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

HSM dedicado não significa menos trabalho de administração. CloudHSM e KMS dividem responsabilidades de formas diferentes; a aplicação também precisa integrar-se corretamente.

### ⚠️ Pegadinhas

"Hardware dedicado", "single-tenant", "controle exclusivo das chaves", "FIPS 140 nível 3", "a AWS não pode acessar" → **CloudHSM**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por **HSM por hora** (custo bem maior que o KMS).

## 5. Caso resolvido: ligando as peças

Uma organização com exigências específicas de controle criptográfico avalia um conjunto de HSMs para sua aplicação compatível.

**Aplicando a sequência à situação:**

**Etapa 1:** Avalie os requisitos de controle criptográfico e prepare os módulos compatíveis.
**Etapa 2:** Administre usuários e chaves na solução e integre o software às operações necessárias.
**Etapa 3:** Planeje disponibilidade e proteção operacional. Controle dedicado exige trabalho que não deve ser confundido com a abstração de KMS.

**Resultado e responsabilidade:** CloudHSM fornece módulos de segurança de hardware para operações e armazenamento criptográfico. Você administra aspectos como usuários e chaves dentro dessa solução.

**Recursos envolvidos:** Cluster HSM, usuários criptográficos e clientes.

**Decisões que precisam ser tomadas:** Quantidade/localização, usuários e gerenciamento de chaves.

**Outra situação comentada:** Requisito de HSM dedicado com controle de chaves: CloudHSM; integração simples de chave gerenciada: KMS.

**Por que não concluir mais do que isso:** Cliente mantém responsabilidades de usuários/chaves; não é simples cofre de senha

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Exigência regulatória de HSM dedicado com chaves sob controle exclusivo."

**Resposta curta:** CloudHSM.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
