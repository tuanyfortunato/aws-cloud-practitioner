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

**Antes de ler este trecho:**

- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.

**Passo 1.** Avalie os requisitos de controle criptográfico e prepare os módulos compatíveis.

**Passo 2.** Administre usuários e chaves na solução e integre o software às operações necessárias.

**Passo 3.** Planeje disponibilidade e proteção operacional. Controle dedicado exige trabalho que não deve ser confundido com a abstração de KMS.

## 2. Recursos e opções, com significado

### Destaques

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.
- **TLS / SSL:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **CA:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.
- **FIPS:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
- **PKCS / JCE / CNG / KSP:** Padrões e interfaces de integração criptográfica. Cada aplicação precisa de suporte ao mecanismo usado; o nome não concede permissão à chave.
- **TDE:** Criptografia transparente de dados em bancos compatíveis. Proteção do armazenamento não substitui autorização e segurança das consultas.

| Item | Detalhe |
|---|---|
| **Single-tenant** | Hardware dedicado a você; validação **FIPS 140 nível 3**. |
| **Controle** | **Você** gerencia usuários e chaves; a **AWS não tem acesso** às chaves. Perdeu as credenciais → perdeu as chaves. |
| **Alta disponibilidade** | Cluster com HSMs em várias AZs (responsabilidade do cliente montar). |
| **APIs padrão** | PKCS#11, JCE (Java), CNG/KSP (Windows), OpenSSL. |
| **Integração** | Custom key store do KMS; offload SSL/TLS de servidores web; Oracle TDE; assinatura de código; CA privada. |

### Responsabilidade compartilhada

**Antes de ler este trecho:**

- **HSM:** Equipamento especializado em proteger chaves e executar operações criptográficas. A forma de administração depende da solução escolhida.

**AWS:** hardware, disponibilidade do HSM, patches de firmware.

**Antes de ler este trecho:**

- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.

**Cliente:** usuários, chaves, backup das credenciais, montar cluster multi-AZ, aplicação.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **CloudHSM:** CloudHSM fornece módulos de segurança de hardware para operações e armazenamento criptográfico.

HSM dedicado não significa menos trabalho de administração. CloudHSM e KMS dividem responsabilidades de formas diferentes; a aplicação também precisa integrar-se corretamente.

### ⚠️ Pegadinhas

"Hardware dedicado", "single-tenant", "controle exclusivo das chaves", "FIPS 140 nível 3", "a AWS não pode acessar" → **CloudHSM**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.

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

**Antes de ler este trecho:**

- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.

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
