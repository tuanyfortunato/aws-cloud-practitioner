# 2.9 Detecção de ameaças e postura de segurança

## 🧠 Antes de começar

**Qual é a dificuldade?** Atividade suspeita, software vulnerável e arquivos com informações pessoais são problemas distintos, mesmo que todos sejam chamados de segurança.

**A ideia em palavras simples:** Serviços de detecção e análise têm especialidades. GuardDuty procura sinais de ameaça; Inspector avalia vulnerabilidades; Macie procura dados sensíveis no S3; outras ferramentas ajudam a reunir ou investigar achados.

**Exemplo do dia a dia:** A equipe investiga um alerta de uso suspeito de identidade, corrige software vulnerável e revisa um arquivo com dados pessoais usando ferramentas adequadas a cada caso.

**O que não concluir?** Detectar não significa confirmar uma invasão nem corrigir tudo automaticamente. A equipe precisa avaliar os resultados e organizar a resposta.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **CVE** | identificador público de uma vulnerabilidade conhecida. |
| **PII** | dados pessoais que identificam alguém (CPF, cartão, nome). |
| **Achado (finding)** | um alerta de segurança gerado por um serviço. |

**Ao terminar este tópico, você deve saber:**

- [ ] Ligar cada serviço à sua função: ameaça → GuardDuty; vulnerabilidade → Inspector; dado sensível no S3 → Macie.
- [ ] Lembrar a sequência **detectar (GuardDuty) → investigar (Detective) → centralizar (Security Hub)**.
- [ ] Saber o que o **Trusted Advisor** verifica e o que muda conforme o plano de suporte.

<details>
<summary>Uma analogia para revisar a ideia</summary>

é uma **equipe de segurança**: o **GuardDuty** é o alarme que dispara; o **Inspector** é o vistoriador que procura brechas; o **Macie** procura documentos sensíveis largados; o **Detective** investiga depois do alarme; o **Security Hub** é a sala de monitoramento que junta tudo; o **Trusted Advisor** é o consultor de boas práticas.

</details>

> 🎯 **Como não errar na prova:** Procure o **substantivo**: "ameaça/atividade maliciosa" → GuardDuty; "vulnerabilidade/CVE" → Inspector; "dados pessoais" → Macie; "causa raiz" → Detective; "painel central" → Security Hub; "boas práticas e custo" → Trusted Advisor.

---

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon GuardDuty](../../servicos/seguranca/guardduty.md) · [Amazon Inspector](../../servicos/seguranca/inspector.md) · [Amazon Macie](../../servicos/seguranca/macie.md) · [Amazon Detective](../../servicos/seguranca/detective.md) · [AWS Security Hub](../../servicos/seguranca/security-hub.md) · [AWS Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md)

⬅️ [2.8 Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) · 🏠 [Índice do domínio](README.md) · [2.10 Outros pontos de segurança](10-outros-pontos-de-seguranca.md) ➡️

---

## 📖 Conteúdo

| Serviço | O que faz | Detalhes de prova |
| --- | --- | --- |
| Amazon GuardDuty | Detecção inteligente de ameaças com machine learning | Analisa CloudTrail, VPC Flow Logs e logs de DNS (e outras fontes opcionais); sem agentes; ativação com um clique; período de teste gratuito |
| Amazon Inspector | Avaliação automática e contínua de **vulnerabilidades** | Varre instâncias EC2, imagens no ECR e funções Lambda; procura CVEs e exposição de rede; gera nota de risco |
| Amazon Macie | Descobre e protege **dados sensíveis** com ML | Só no **S3**; identifica PII (CPF, cartão, nomes) e buckets públicos ou sem criptografia |
| Amazon Detective | **Investiga** a causa raiz de achados de segurança | Monta gráficos de relacionamento a partir de logs e achados do GuardDuty |
| AWS Security Hub | **Painel central** de segurança | Agrega achados de GuardDuty, Inspector, Macie e parceiros; verifica padrões como AWS Foundational Security Best Practices e CIS |
| AWS Trusted Advisor | Recomendações de **boas práticas** | Categorias: otimização de custos, performance, segurança, tolerância a falhas, cotas de serviço e excelência operacional |

- **Trusted Advisor por plano de suporte:** o Basic tem as verificações principais (service limits + 5 de segurança); 🔄 **Business Support+, Enterprise e Unified Operations têm todas as verificações** e acesso via API (no modelo clássico: Business, Enterprise On-Ramp e Enterprise). O **Trusted Advisor Priority** vem no Enterprise e no Unified Operations.
- **Exemplos de verificações do Trusted Advisor:** buckets S3 com acesso público, MFA no root, security groups com portas abertas para o mundo, instâncias ociosas, cotas próximas do limite.
- **Cai na prova:** detectar (GuardDuty) → investigar (Detective) → centralizar (Security Hub). Vulnerabilidade de software = Inspector; dado sensível = Macie.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Qual serviço detecta atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS?" → GuardDuty.
- "Qual serviço varre instâncias EC2 e imagens de container em busca de vulnerabilidades?" → Amazon Inspector.
- "Qual serviço encontra dados pessoais em buckets S3?" → Amazon Macie.
- "Qual serviço ajuda a investigar a causa raiz de um achado de segurança?" → Amazon Detective.
- "Qual serviço reúne os achados de segurança de vários serviços num só painel?" → AWS Security Hub.
- "Qual serviço recomenda melhorias de custo, segurança, performance e limites?" → Trusted Advisor.
- "Qual plano de suporte libera todas as verificações do Trusted Advisor?" → Business Support+ ou superior (no modelo clássico, Business).
- "Qual verificação de segurança o Trusted Advisor faz?" → Buckets S3 públicos, MFA no root, portas abertas em security groups.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** GuardDuty detecta ameaças; Inspector avalia vulnerabilidades em recursos suportados; Macie descobre dados sensíveis em S3; Security Hub agrega e prioriza achados e postura.

**Como escolher:** Identifique a pergunta: comportamento suspeito, software vulnerável, conteúdo sensível ou visão centralizada. Detective ajuda a investigar contexto.

**O que não concluir:** Um achado não corrige a aplicação sozinho. Resposta automática requer integração e permissões. Macie não é varredura genérica de todos os bancos e discos.

### Exercício de decisão

Há preocupação com credenciais expostas em objetos S3 e com biblioteca vulnerável em EC2. Qual serviço para cada parte?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Macie para descoberta de dados sensíveis no S3; Inspector para vulnerabilidades em EC2 elegível. GuardDuty responde a outra pergunta: sinais de ameaça.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **Trusted Advisor — 🔄 6 categorias:** cost optimization, performance, security, fault tolerance, service limits e **operational excellence** (a mais nova). Materiais antigos listam 5; ⚠️ se a questão listar 5, escolha as 5 clássicas.
- **Basic/Developer:** todos os checks de **Service Limits** + checks selecionados de **Security** e **Fault Tolerance**, com refresh manual. 📌 ✔️ Lista oficial atual (10/2026): todos os checks de **Service Limits** + **5 de segurança** — S3 Bucket Permissions, Security Groups – Specific Ports Unrestricted, MFA on Root Account, EBS Public Snapshots e RDS Public Snapshots. (Materiais antigos citavam também "IAM Use", que saiu da lista.)
- **Business Support+/Enterprise/Unified Operations:** todos os checks, API do Trusted Advisor e **AWS Support API**, integração com **EventBridge**. ✔️ O **Trusted Advisor Priority** vem no **Enterprise** e no **Unified Operations**.
- 🧊 Contagem de checks: fontes divergem ("56 grátis / 482 no total", "500+"). Não decorar.
- **Ferramenta certa por pergunta (📌):**

| Pergunta | Serviço |
|---|---|
| Quem fez a chamada de API? | CloudTrail |
| Como estava a configuração em tal data / está conforme? | Config |
| Métrica ou alarme de desempenho | CloudWatch |
| Ameaça ativa (mineração de cripto, IP malicioso) | GuardDuty |
| Vulnerabilidade/CVE em EC2, ECR, Lambda | Inspector |
| PII no S3 | Macie |
| Investigar a causa raiz de um achado | Detective |
| Painel central de achados e padrões (CIS, AWS FSBP) | Security Hub |
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.8 Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) · 🏠 [Índice do domínio](README.md) · [2.10 Outros pontos de segurança](10-outros-pontos-de-seguranca.md) ➡️
