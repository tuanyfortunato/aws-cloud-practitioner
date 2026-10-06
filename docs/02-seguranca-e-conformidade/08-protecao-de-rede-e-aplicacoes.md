# 2.8 Proteção de rede e aplicações

## 🧠 Antes de começar

**Qual é a dificuldade?** Um recurso acessível pela rede pode receber conexões indevidas, pedidos web maliciosos ou tentativas de sobrecarga.

**A ideia em palavras simples:** Proteção de rede e aplicação usa controles em camadas. Regras de conexão, inspeção de pedidos web e proteção contra sobrecarga tratam ameaças diferentes.

**Exemplo do dia a dia:** A escola limita conexões ao banco, inspeciona pedidos ao site e avalia proteção contra ataques distribuídos. Cada medida atua numa parte do caminho.

**O que não concluir?** Uma regra de rede não corrige o código do programa; uma proteção web não inspeciona automaticamente todos os protocolos. Identifique o tipo de tráfego e o ponto de proteção.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Stateful** | lembra da conexão: se entrou, a resposta sai sem nova regra. |
| **Stateless** | não lembra: é preciso liberar entrada **e** saída. |
| **DDoS** | ataque que tenta derrubar o serviço com uma enxurrada de tráfego. |
| **SQL injection / XSS** | ataques que escondem comandos maliciosos em requisições web. |

---

> **Domínio 2 — Segurança e Conformidade (30%)**

> 🔎 **Fichas detalhadas:** [Amazon VPC (Virtual Private Cloud)](../../servicos/redes/vpc.md) · [AWS Shield](../../servicos/seguranca/shield.md) · [AWS WAF (Web Application Firewall)](../../servicos/seguranca/waf.md) · [AWS Firewall Manager e AWS Network Firewall](../../servicos/seguranca/firewall-manager-e-network-firewall.md)

⬅️ [2.7 Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) · 🏠 [Índice do domínio](README.md) · [2.9 Detecção de ameaças e postura de segurança](09-deteccao-de-ameacas.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Uma comunicação passa por camadas: caminho de rede, conexão e pedido entendido pela aplicação. Regras nessas camadas examinam informações diferentes. Bloquear uma faixa de endereços não é a mesma tarefa que detectar um padrão malicioso em um campo web.

Use proteção correspondente ao risco e ao recurso. Reduzir sobrecarga, inspecionar pedidos e corrigir código podem ser medidas complementares. Não atribua a uma ferramenta a cobertura que pertence a outra camada.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **security group** é o **porteiro do apartamento** (lembra quem entrou e deixa sair); a **NACL** é o **portão da rua** (confere entrada e saída e pode barrar alguém pelo nome); o **Shield** é um **quebra-mar** contra enxurradas de tráfego; o **WAF** é o **segurança que lê cada pedido** e barra os maliciosos.

</details>

## 2. Conceitos e opções explicados

**Security group:** Firewall virtual no nível da **instância/ENI**. **Stateful** (a resposta volta automaticamente); só tem regras de **permissão**; por padrão bloqueia toda entrada e libera toda saída.

**Network ACL (NACL):** firewall no nível da **subnet**. **Stateless** (precisa liberar entrada e saída); tem regras de **permitir e negar**, avaliadas em ordem numérica. A NACL padrão libera tudo.

**AWS Shield:** proteção contra **DDoS**.

  - **Shield Standard:** gratuito e automático para todos os clientes, protege contra ataques comuns de camada 3 e 4.

  - **Shield Advanced:** pago, com proteção ampliada (inclusive camada 7 junto com o WAF), acesso 24/7 ao **Shield Response Team (SRT)**, visibilidade dos ataques e **proteção de custo** (créditos pelo aumento de uso causado por ataque).

**AWS WAF:** firewall de **aplicação web (camada 7)**. Usa web ACLs com regras para bloquear SQL injection, XSS, IPs, países (geo) e limitar requisições (rate-based). Tem regras gerenciadas prontas. Associado a **CloudFront, ALB, API Gateway, AppSync e Cognito**.

**AWS Firewall Manager:** gerencia de forma central regras de WAF, Shield Advanced, security groups e firewalls de rede em **todas as contas** do Organizations.

**Cai na prova:** "bloquear um IP específico na subnet" = NACL (security group não nega); "ataque de SQL injection" = WAF; "ataque DDoS volumétrico" = Shield; "time especialista 24/7 durante ataque DDoS" = Shield Advanced.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** Security groups controlam tráfego em interfaces e mantêm estado; NACLs controlam tráfego de subnets e são sem estado. WAF avalia requisições web; Shield atua contra DDoS.

**Depois, compare as escolhas:** Porta de acesso de uma EC2: SG. Regra de subnet com negação: NACL. SQL injection em HTTP: WAF. Proteção distribuída contra negação de serviço: Shield.

**Por fim, verifique o limite:** Uma rota não concede permissão IAM; SG não examina SQL injection. Regras de retorno precisam ser consideradas em NACLs. Associar WAF exige recurso suportado.

## 4. Caso resolvido

Uma API recebe requisições com padrões de SQL injection. Abrir ou fechar a porta 443 no SG trata o padrão malicioso?

**Raciocínio e resposta:** Não. WAF avalia a requisição HTTP; SG só decide o tráfego de rede permitido. Fechar 443 bloquearia também os usuários legítimos.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **security group** (instância, stateful, só permite) de **NACL** (subnet, stateless, permite e nega).
- [ ] Diferenciar **Shield Standard** (grátis) de **Shield Advanced** (pago, com time 24/7 e proteção de custo).
- [ ] Saber que o **WAF** bloqueia SQL injection e XSS (camada 7) e que o **Firewall Manager** aplica regras em todas as contas.

**Dica de revisão para a prova:** "**Bloquear** um IP" → **NACL** (security group não tem regra de negar). "SQL injection" → **WAF**. "DDoS" → **Shield**; com "time especialista" ou "proteção de custo" → **Shield Advanced**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).
**Pergunta:** "Qual firewall atua no nível da instância e é stateful?"

**Resposta curta:** Security group.

**Pergunta:** "Qual firewall atua no nível da subnet e é stateless?"

**Resposta curta:** Network ACL.

**Pergunta:** "Como bloquear um endereço IP malicioso?"

**Resposta curta:** Regra de negação na NACL (ou regra no WAF para tráfego web).

**Pergunta:** "Qual proteção DDoS todo cliente tem sem custo?"

**Resposta curta:** Shield Standard.

**Pergunta:** "Qual serviço dá acesso a especialistas 24/7 e proteção de custo durante ataques DDoS?"

**Resposta curta:** Shield Advanced.

**Pergunta:** "Como bloquear SQL injection e XSS?"

**Resposta curta:** AWS WAF.

**Pergunta:** "Como bloquear acesso de certos países ao site?"

**Resposta curta:** WAF (regra geográfica) ou restrição geográfica do CloudFront.

**Pergunta:** "Em quais serviços o WAF pode ser usado?"

**Resposta curta:** CloudFront, ALB, API Gateway, AppSync e Cognito.

**Pergunta:** "Como aplicar as mesmas regras de WAF em todas as contas?"

**Resposta curta:** AWS Firewall Manager.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **Shield Advanced (📌):** **US$ 3.000/mês por organização**, compromisso mínimo de **1 ano**, mais data transfer out dos recursos protegidos. Inclui camada 7 (com WAF), **Shield Response Team 24/7**, **proteção de custo** (créditos por escalonamento causado por DDoS) e **WAF sem custo adicional** nos recursos protegidos. A taxa cobre todas as contas da Organization.
  - *Questão-modelo:* "reembolso de custos de escalonamento causados por DDoS + especialistas 24/7" → **Shield Advanced**.
- **WAF:** cobra por Web ACL, por regra e por milhão de requisições (🧊 valores). Camada 7: SQL injection, XSS, rate-based rules, geo-blocking. ⚠️ Atua em CloudFront, ALB, API Gateway, AppSync e Cognito — **não** atua em NLB.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.7 Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) · 🏠 [Índice do domínio](README.md) · [2.9 Detecção de ameaças e postura de segurança](09-deteccao-de-ameacas.md) ➡️
