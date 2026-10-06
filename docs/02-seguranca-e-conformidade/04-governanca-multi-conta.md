# 2.4 Governança multi-conta

## 🧠 Antes de começar

**Qual é a dificuldade?** A empresa separou testes e produção em várias contas, mas agora precisa de regras comuns e administração central.

**A ideia em palavras simples:** Governança de várias contas organiza ambientes e aplica controles. Organizations, Control Tower e ferramentas relacionadas têm papéis diferentes nesse trabalho.

**Exemplo do dia a dia:** A escola separa o ambiente experimental dos dados de produção e define regras centrais para suas contas.

**O que não concluir?** Um limite de governança não concede sozinho permissão a cada pessoa. Centralizar controles também não configura todas as aplicações automaticamente.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **OU** | unidade organizacional: uma "pasta" de contas dentro do Organizations. |
| **SCP** | política que define o máximo que uma conta ou OU pode fazer. |
| **Landing zone** | ambiente multi-conta já configurado com boas práticas. |
| **Guardrail** | regra de proteção do Control Tower (preventiva ou detectiva). |

---

> **Domínio 2 — Segurança e Conformidade (30%)**

> 🔎 **Fichas detalhadas:** [AWS Organizations](../../servicos/gerenciamento/organizations.md) · [AWS Control Tower](../../servicos/gerenciamento/control-tower.md) · [AWS Service Catalog e AWS Resource Access Manager (RAM)](../../servicos/gerenciamento/service-catalog-e-ram.md)

⬅️ [2.3 AWS IAM (Identity and Access Management)](03-iam.md) · 🏠 [Índice do domínio](README.md) · [2.5 Criptografia](05-criptografia.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

A conta separa administração e recursos. Várias contas permitem isolar contextos, enquanto a organização fornece ferramentas de gestão comum. Regras centrais limitam possibilidades, mas as identidades de cada conta ainda precisam receber suas permissões.

Não confunda quatro ações: organizar contas, limitar operações, oferecer configurações aprovadas e compartilhar recursos compatíveis. Elas podem fazer parte do mesmo projeto, mas usam objetos e ferramentas diferentes.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como uma **rede de franquias**: a matriz (Organizations) agrupa as lojas, define o que nenhuma pode fazer (SCP), paga uma fatura única e, com o Control Tower, entrega cada loja nova já montada no padrão.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **AWS Organizations / Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

**AWS Organizations:** gerencia várias contas de forma centralizada.

  - **Conta de gerenciamento (management account)** e **contas-membro**, organizadas em **OUs** (unidades organizacionais) hierárquicas.
**Antes de ler este trecho:**

- **SCP:** Política de controle de serviços usada na organização para limitar permissões disponíveis em contas às quais se aplica. Ela não concede acesso ao usuário sozinha.

  - **SCPs (Service Control Policies):** definem o limite máximo de permissões das contas ou OUs. **Cai na prova:** SCP não concede permissão, só restringe; e não afeta a conta de gerenciamento.
**Antes de ler este trecho:**

- **Reserved Instances:** Benefício e condições de reserva para configurações compatíveis. Não confunda desconto com qualquer garantia universal de capacidade.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.

  - **Consolidated billing:** uma fatura única; soma o uso de todas as contas para descontos por volume; compartilha Reserved Instances e Savings Plans entre as contas.
**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.

  - Criar contas por API e isolar ambientes (produção, desenvolvimento, segurança).
**Antes de ler este trecho:**

- **AWS Control Tower / Control Tower:** Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.
- **landing zone:** Base organizada de um ambiente AWS com várias contas e controles. Ainda é necessário definir aplicações, acessos e operação dentro dela.

**AWS Control Tower:** configura automaticamente um ambiente multi-conta seguro e padronizado (landing zone) sobre o Organizations.

**Antes de ler este trecho:**

- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.

  - **Controles (guardrails):** preventivos (bloqueiam ações, via SCP) e detectivos (detectam desvios, via Config).

  - **Account Factory:** cria contas novas já seguindo o padrão.
**Antes de ler este trecho:**

- **conformidade:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.

  - Painel com o status de conformidade de todas as contas.
**Antes de ler este trecho:**

- **RAM:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.

**AWS Resource Access Manager (RAM):** compartilha recursos entre contas (ex.: subnets, Transit Gateways, licenças).

**Antes de ler este trecho:**

- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **provisionar:** Criar ou disponibilizar capacidade e recursos. Um recurso provisionado pode ter cobrança mesmo enquanto está esperando trabalho.

**AWS Service Catalog:** catálogo de produtos aprovados (templates CloudFormation) que os times podem provisionar sozinhos, dentro das regras da empresa.

**Cai na prova:** "centralizar contas e aplicar políticas" = Organizations; "montar rapidamente um ambiente multi-conta com boas práticas" = Control Tower; "limitar o que uma conta inteira pode fazer" = SCP.

### ➕ Complemento

**Antes de ler este trecho:**

- **OU:** Unidade organizacional: agrupamento de contas na organização. Agrupar contas permite aplicar regras de governança segundo a estrutura escolhida.

SCPs são herdadas pela hierarquia: uma SCP numa OU vale para todas as contas abaixo dela.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.

A permissão efetiva é a interseção entre o que a SCP permite e o que a política IAM concede.

Estratégia multi-conta recomendada: contas separadas por ambiente e por função (produção, desenvolvimento, segurança, logs), para isolar riscos e custos.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.

**Primeiro, identifique o funcionamento:** Organizations agrupa contas em OUs; SCPs limitam permissões máximas das contas membro. Control Tower estabelece uma landing zone com controles e contas de governança.

**Depois, compare as escolhas:** Separe organização de contas, controles comuns e compartilhamento de recursos. RAM compartilha tipos de recurso suportados; Service Catalog oferece produtos aprovados.

**Por fim, verifique o limite:** SCP não concede acesso e não é firewall. Faturamento consolidado não mistura dados das contas. Control Tower não elimina a administração e conformidade do cliente.

## 4. Caso resolvido

Uma empresa quer impedir determinada operação em contas de desenvolvimento. Basta anexar uma SCP com Allow?

**Raciocínio e resposta:** Não. SCP define o teto; as identidades ainda precisam de permissões IAM. Uma restrição em nível organizacional pode impedir a operação mesmo com AdministratorAccess na conta membro.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Explicar **Organizations**, **OUs** e **consolidated billing**.
- [ ] Saber que **SCP só restringe** (não concede permissão) e não afeta a conta de gerenciamento.
- [ ] Diferenciar **Organizations** (agrupar e limitar) de **Control Tower** (ambiente multi-conta pronto, com guardrails).

**Dica de revisão para a prova:** "Limitar o que uma **conta inteira** pode fazer" → **SCP**. "Montar rapidamente ambiente multi-conta com boas práticas" → **Control Tower**. "Uma fatura e desconto por volume" → **consolidated billing**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).
**Pergunta:** "Como impedir que todas as contas de desenvolvimento usem uma região?"

**Resposta curta:** SCP no Organizations.

**Pergunta:** "Uma SCP permite S3, mas o usuário não tem política IAM para S3. Ele consegue acessar?"

**Resposta curta:** Não; a SCP só limita, não concede.

**Pergunta:** "Como obter desconto por volume somando o uso de várias contas?"

**Resposta curta:** Consolidated billing no Organizations.

**Pergunta:** "Como criar rapidamente um ambiente multi-conta seguro com guardrails?"

**Resposta curta:** AWS Control Tower.

**Pergunta:** "Como deixar times criarem só recursos aprovados pela empresa?"

**Resposta curta:** AWS Service Catalog.

**Pergunta:** "Como compartilhar uma subnet com outra conta?"

**Resposta curta:** AWS RAM.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.3 AWS IAM (Identity and Access Management)](03-iam.md) · 🏠 [Índice do domínio](README.md) · [2.5 Criptografia](05-criptografia.md) ➡️
