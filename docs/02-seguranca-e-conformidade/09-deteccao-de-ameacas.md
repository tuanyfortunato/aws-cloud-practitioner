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

---

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon GuardDuty](../../servicos/seguranca/guardduty.md) · [Amazon Inspector](../../servicos/seguranca/inspector.md) · [Amazon Macie](../../servicos/seguranca/macie.md) · [Amazon Detective](../../servicos/seguranca/detective.md) · [AWS Security Hub](../../servicos/seguranca/security-hub.md) · [AWS Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md)

⬅️ [2.8 Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) · 🏠 [Índice do domínio](README.md) · [2.10 Outros pontos de segurança](10-outros-pontos-de-seguranca.md) ➡️

---

## 1. Entenda as peças e a relação entre elas


Encontrar algo suspeito começa uma análise. Vulnerabilidade descreve uma fraqueza; ameaça descreve uma possível ação prejudicial; dado sensível descreve conteúdo que exige proteção. Esses achados precisam de interpretações e respostas diferentes.

Considere a sequência detectar, avaliar e responder. Uma ferramenta pode emitir um achado, outra reunir resultados e outra fornecer contexto. Nenhuma indicação deve ser tratada automaticamente como prova completa de um incidente ou de sua correção.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é uma **equipe de segurança**: o **GuardDuty** é o alarme que dispara; o **Inspector** é o vistoriador que procura brechas; o **Macie** procura documentos sensíveis largados; o **Detective** investiga depois do alarme; o **Security Hub** é a sala de monitoramento que junta tudo; o **Trusted Advisor** é o consultor de boas práticas.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECR:** O ECR é um repositório de imagens de containers.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **Amazon GuardDuty / GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.
- **Amazon Inspector / Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.
- **Amazon Macie / Macie:** Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.
- **Amazon Detective / Detective:** Detective organiza dados compatíveis e suas relações para apoiar investigações de segurança.
- **AWS Security Hub / Security Hub:** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **AWS Trusted Advisor / Trusted Advisor:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **PII:** Informação que pode identificar uma pessoa. Sua identificação ajuda a planejar proteção de dados, mas não substitui avaliação do contexto e das regras aplicáveis.
- **CIS:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.
- **ML / machine learning:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **CPF:** Identificador pessoal brasileiro. Neste material é exemplo de dado que pode exigir proteção, não um mecanismo AWS de autenticação.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Serviço | O que faz | Detalhes de prova |
| --- | --- | --- |
| Amazon GuardDuty | Detecção inteligente de ameaças com machine learning | Analisa CloudTrail, VPC Flow Logs e logs de DNS (e outras fontes opcionais); sem agentes; ativação com um clique; período de teste gratuito |
| Amazon Inspector | Avaliação automática e contínua de **vulnerabilidades** | Varre instâncias EC2, imagens no ECR e funções Lambda; procura CVEs e exposição de rede; gera nota de risco |
| Amazon Macie | Descobre e protege **dados sensíveis** com ML | Só no **S3**; identifica PII (CPF, cartão, nomes) e buckets públicos ou sem criptografia |
| Amazon Detective | **Investiga** a causa raiz de achados de segurança | Monta gráficos de relacionamento a partir de logs e achados do GuardDuty |
| AWS Security Hub | **Painel central** de segurança | Agrega achados de GuardDuty, Inspector, Macie e parceiros; verifica padrões como AWS Foundational Security Best Practices e CIS |
| AWS Trusted Advisor | Recomendações de **boas práticas** | Categorias: otimização de custos, performance, segurança, tolerância a falhas, cotas de serviço e excelência operacional |


**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.
- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.


**Trusted Advisor por plano de suporte:** o Basic tem as verificações principais (service limits + 5 de segurança); 🔄 **Business Support+, Enterprise e Unified Operations têm todas as verificações** e acesso via API (no modelo clássico: Business, Enterprise On-Ramp e Enterprise). O **Trusted Advisor Priority** vem no Enterprise e no Unified Operations.

**Antes de ler este trecho:**

- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.


**Exemplos de verificações do Trusted Advisor:** buckets S3 com acesso público, MFA no root, security groups com portas abertas para o mundo, instâncias ociosas, cotas próximas do limite.


**Cai na prova:** detectar (GuardDuty) → investigar (Detective) → centralizar (Security Hub). Vulnerabilidade de software = Inspector; dado sensível = Macie.

## 3. Como analisar uma situação


**Primeiro, identifique o funcionamento:** GuardDuty detecta ameaças; Inspector avalia vulnerabilidades em recursos suportados; Macie descobre dados sensíveis em S3; Security Hub agrega e prioriza achados e postura.

**Depois, compare as escolhas:** Identifique a pergunta: comportamento suspeito, software vulnerável, conteúdo sensível ou visão centralizada. Detective ajuda a investigar contexto.

**Por fim, verifique o limite:** Um achado não corrige a aplicação sozinho. Resposta automática requer integração e permissões. Macie não é varredura genérica de todos os bancos e discos.

## 4. Caso resolvido

Há preocupação com credenciais expostas em objetos S3 e com biblioteca vulnerável em EC2. Qual serviço para cada parte?

**Raciocínio e resposta:** Macie para descoberta de dados sensíveis no S3; Inspector para vulnerabilidades em EC2 elegível. GuardDuty responde a outra pergunta: sinais de ameaça.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Atividade suspeita, software vulnerável e arquivos com informações pessoais são problemas distintos, mesmo que todos sejam chamados de segurança.

**2. O que a solução fornece?**

Serviços de detecção e análise têm especialidades. GuardDuty procura sinais de ameaça; Inspector avalia vulnerabilidades; Macie procura dados sensíveis no S3; outras ferramentas ajudam a reunir ou investigar achados.

**3. Que conclusão seria incorreta?**

Detectar não significa confirmar uma invasão nem corrigir tudo automaticamente. A equipe precisa avaliar os resultados e organizar a resposta.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Ligar cada serviço à sua função: ameaça → GuardDuty; vulnerabilidade → Inspector; dado sensível no S3 → Macie.
- [ ] Lembrar a sequência **detectar (GuardDuty) → investigar (Detective) → centralizar (Security Hub)**.
- [ ] Saber o que o **Trusted Advisor** verifica e o que muda conforme o plano de suporte.

**Dica de revisão para a prova:** Procure o **substantivo**: "ameaça/atividade maliciosa" → GuardDuty; "vulnerabilidade/CVE" → Inspector; "dados pessoais" → Macie; "causa raiz" → Detective; "painel central" → Security Hub; "boas práticas e custo" → Trusted Advisor.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).
**Pergunta:** "Qual serviço detecta atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS?"

**Resposta curta:** GuardDuty.


**Fundamento explicado no capítulo:** "Qual serviço detecta atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS?" → GuardDuty.

**Pergunta:** "Qual serviço varre instâncias EC2 e imagens de container em busca de vulnerabilidades?"

**Resposta curta:** Amazon Inspector.

**Antes de ler este trecho:**

- **container:** Ambiente que executa uma aplicação a partir de uma imagem com software e dependências. É diferente de criar uma máquina virtual completa para cada pacote.


**Fundamento explicado no capítulo:** "Qual serviço varre instâncias EC2 e imagens de container em busca de vulnerabilidades?" → Amazon Inspector.

**Pergunta:** "Qual serviço encontra dados pessoais em buckets S3?"

**Resposta curta:** Amazon Macie.


**Fundamento explicado no capítulo:** "Qual serviço encontra dados pessoais em buckets S3?" → Amazon Macie.

**Pergunta:** "Qual serviço ajuda a investigar a causa raiz de um achado de segurança?"

**Resposta curta:** Amazon Detective.


**Fundamento explicado no capítulo:** "Qual serviço ajuda a investigar a causa raiz de um achado de segurança?" → Amazon Detective.

**Pergunta:** "Qual serviço reúne os achados de segurança de vários serviços num só painel?"

**Resposta curta:** AWS Security Hub.


**Fundamento explicado no capítulo:** "Qual serviço reúne os achados de segurança de vários serviços num só painel?" → AWS Security Hub.

**Pergunta:** "Qual serviço recomenda melhorias de custo, segurança, performance e limites?"

**Resposta curta:** Trusted Advisor.


**Fundamento explicado no capítulo:** "Qual serviço recomenda melhorias de custo, segurança, performance e limites?" → Trusted Advisor.

**Pergunta:** "Qual plano de suporte libera todas as verificações do Trusted Advisor?"

**Resposta curta:** Business Support+ ou superior (no modelo clássico, Business).


**Fundamento explicado no capítulo:** "Qual plano de suporte libera todas as verificações do Trusted Advisor?" → Business Support+ ou superior (no modelo clássico, Business).

**Pergunta:** "Qual verificação de segurança o Trusted Advisor faz?"

**Resposta curta:** Buckets S3 públicos, MFA no root, portas abertas em security groups.


**Fundamento explicado no capítulo:** "Qual verificação de segurança o Trusted Advisor faz?" → Buckets S3 públicos, MFA no root, portas abertas em security groups.

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
