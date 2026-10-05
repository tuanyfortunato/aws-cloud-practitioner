# 1.4 AWS Well-Architected Framework

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma aplicação funciona hoje, mas a equipe precisa avaliar se é segura, recuperável, eficiente e econômica, em vez de olhar apenas se está ligada.

**A ideia em palavras simples:** Well-Architected é um conjunto de orientações para revisar uma aplicação e sua operação sob seis áreas, chamadas pilares. Não é um serviço que hospeda o programa.

**Exemplo do dia a dia:** A escola revisa quem acessa os dados, como restaura um backup e se mantém recursos ociosos. Cada pergunta se relaciona a uma área da revisão.

**O que não concluir?** Seguir um checklist não certifica automaticamente a aplicação nem executa as melhorias. O objetivo é identificar decisões e oportunidades de melhoria.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Pilar** | uma das seis áreas de boas práticas do framework. |
| **Lens** | extensão do framework para um cenário específico (serverless, SaaS, ML…). |

---

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md)

⬅️ [1.3 Conceitos de arquitetura que a prova cobra](03-conceitos-de-arquitetura.md) · 🏠 [Índice do domínio](README.md) · [1.5 AWS Cloud Adoption Framework (CAF)](05-cloud-adoption-framework.md) ➡️

---

## 1. Entenda as peças e a relação entre elas


Uma revisão técnica precisa avaliar mais que velocidade. Perguntar como operar, proteger, recuperar, dimensionar, pagar e reduzir impacto ambiental revela necessidades diferentes da mesma aplicação. Os pilares organizam essas perguntas.

Uma prática pode beneficiar mais de um pilar. Para escolher na prova, identifique o objetivo destacado. Automatizar um procedimento para melhorar a rotina aponta para operação; preparar recuperação após falha destaca confiabilidade.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como a **inspeção de uma casa** em seis itens: a casa é fácil de manter (Excelência Operacional), tem tranca (Segurança), não cai (Confiabilidade), tem o tamanho certo (Eficiência de Performance), não desperdiça dinheiro (Otimização de Custos) e gasta pouca energia (Sustentabilidade).

</details>

## 2. Conceitos e opções explicados

Seis pilares, cada um com princípios de design. A prova descreve uma prática e pergunta o pilar.

**Antes de ler este trecho:**

- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **menor privilégio:** Conceder apenas o acesso necessário ao trabalho. Evita que uma tarefa simples carregue poder desnecessário sobre outros recursos.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Pilar | Foco | Princípios de design que mais caem |
| --- | --- | --- |
| Excelência Operacional | Rodar e monitorar sistemas e melhorar processos | Operações como código; mudanças pequenas, frequentes e reversíveis; refinar procedimentos com frequência; antecipar falhas; aprender com falhas operacionais; usar serviços gerenciados; implementar observabilidade |
| Segurança | Proteger dados, sistemas e ativos | Base forte de identidade (menor privilégio); rastreabilidade; segurança em todas as camadas; automatizar boas práticas; proteger dados em trânsito e em repouso; manter pessoas longe dos dados; preparar-se para incidentes |
| Confiabilidade | Executar corretamente e se recuperar de falhas | Recuperação automática de falhas; testar procedimentos de recuperação; escalar horizontalmente; parar de adivinhar capacidade; gerenciar mudanças com automação |
| Eficiência de Performance | Usar recursos de forma eficiente conforme a demanda muda | Democratizar tecnologias avançadas; ficar global em minutos; usar arquiteturas serverless; experimentar com mais frequência; considerar a afinidade mecânica (escolher a tecnologia que combina com o uso) |
| Otimização de Custos | Entregar valor pelo menor preço | Praticar gestão financeira na nuvem; adotar modelo de consumo; medir a eficiência geral; parar de gastar com trabalho pesado indiferenciado; analisar e atribuir gastos |
| Sustentabilidade | Reduzir impacto ambiental | Entender seu impacto; definir metas; maximizar a utilização; adotar hardware e software mais eficientes; usar serviços gerenciados; reduzir o impacto downstream |


**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.


**AWS Well-Architected Tool:** serviço gratuito no console para revisar uma carga de trabalho contra os pilares e gerar um plano de melhorias.

**Antes de ler este trecho:**

- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.
- **machine learning:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.


**Lenses:** extensões do framework para cenários específicos (serverless, SaaS, machine learning, serviços financeiros).

**Antes de ler este trecho:**

- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **Graviton:** Família de processadores AWS baseada em arquitetura ARM. A aplicação e sua imagem precisam ser compatíveis com essa arquitetura.


**Cai na prova:** "usar várias AZs" = Confiabilidade; "ativar MFA e criptografia" = Segurança; "escolher o tipo de instância certo" = Eficiência de Performance; "desligar recursos ociosos" = Otimização de Custos; "usar Graviton para gastar menos energia" = Sustentabilidade; "CloudFormation e runbooks" = Excelência Operacional.

### ➕ Complemento — princípios gerais de design do Well-Architected

Parar de adivinhar necessidades de capacidade.


Testar sistemas em escala de produção.


Automatizar para facilitar a experimentação.


Permitir arquiteturas evolutivas.


Guiar arquiteturas com dados.


Melhorar com "game days" (simulações de eventos em produção).

## 3. Como analisar uma situação


**Primeiro, identifique o funcionamento:** A revisão avalia uma carga nos seis pilares; a Well-Architected Tool registra respostas, riscos e melhorias. Ela ajuda a revisar decisões, sem implantar a arquitetura por você.

**Depois, compare as escolhas:** Operação e aprendizado: Excelência Operacional. Identidade e proteção: Segurança. Falhas e recuperação: Confiabilidade. Recursos adequados: Performance. Gasto: Custos. Impacto ambiental: Sustentabilidade.

**Por fim, verifique o limite:** Uma prática pode ajudar vários pilares. Escolha o pilar pelo objetivo expresso no enunciado; Graviton não significa automaticamente que a pergunta é sobre sustentabilidade.

## 4. Caso resolvido

Uma equipe automatiza procedimentos e revê incidentes para melhorar sua operação. Qual pilar é o principal?

**Raciocínio e resposta:** Excelência Operacional. Se o objetivo destacado fosse recuperar a carga após falhas, o foco seria Confiabilidade.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma aplicação funciona hoje, mas a equipe precisa avaliar se é segura, recuperável, eficiente e econômica, em vez de olhar apenas se está ligada.

**2. O que a solução fornece?**

Well-Architected é um conjunto de orientações para revisar uma aplicação e sua operação sob seis áreas, chamadas pilares. Não é um serviço que hospeda o programa.

**3. Que conclusão seria incorreta?**

Seguir um checklist não certifica automaticamente a aplicação nem executa as melhorias. O objetivo é identificar decisões e oportunidades de melhoria.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Citar os **6 pilares**.
- [ ] Ligar cada prática ao pilar (várias AZs → Confiabilidade; MFA → Segurança; desligar ocioso → Custos).
- [ ] Saber que a **Well-Architected Tool** é gratuita e revisa uma carga contra os pilares.

**Dica de revisão para a prova:** Associe palavras: **automação/runbooks** → Excelência Operacional; **identidade/criptografia** → Segurança; **recuperar de falhas/várias AZs** → Confiabilidade; **tipo de instância certo/serverless** → Performance; **gasto** → Custos; **energia/Graviton** → Sustentabilidade.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).
**Pergunta:** "Quantos e quais são os pilares?"

**Resposta curta:** Seis: Excelência Operacional, Segurança, Confiabilidade, Eficiência de Performance, Otimização de Custos e Sustentabilidade.


**Fundamento explicado no capítulo:** "Quantos e quais são os pilares?" → Seis: Excelência Operacional, Segurança, Confiabilidade, Eficiência de Performance, Otimização de Custos e Sustentabilidade.

**Pergunta:** "Qual pilar inclui recuperar automaticamente de falhas e escalar horizontalmente?"

**Resposta curta:** Confiabilidade.


**Fundamento explicado no capítulo:** "Qual pilar inclui recuperar automaticamente de falhas e escalar horizontalmente?" → Confiabilidade.

**Pergunta:** "Qual pilar inclui rastreabilidade e menor privilégio?"

**Resposta curta:** Segurança.


**Fundamento explicado no capítulo:** "Qual pilar inclui rastreabilidade e menor privilégio?" → Segurança.

**Pergunta:** "Qual pilar inclui fazer mudanças pequenas, frequentes e reversíveis?"

**Resposta curta:** Excelência Operacional.


**Fundamento explicado no capítulo:** "Qual pilar inclui fazer mudanças pequenas, frequentes e reversíveis?" → Excelência Operacional.

**Pergunta:** "Qual pilar inclui usar serverless e experimentar com frequência?"

**Resposta curta:** Eficiência de Performance.


**Fundamento explicado no capítulo:** "Qual pilar inclui usar serverless e experimentar com frequência?" → Eficiência de Performance.

**Pergunta:** "Qual pilar inclui adotar o modelo de consumo e analisar gastos?"

**Resposta curta:** Otimização de Custos.


**Fundamento explicado no capítulo:** "Qual pilar inclui adotar o modelo de consumo e analisar gastos?" → Otimização de Custos.

**Pergunta:** "Qual pilar foi o último adicionado e trata de impacto ambiental?"

**Resposta curta:** Sustentabilidade.


**Fundamento explicado no capítulo:** "Qual pilar foi o último adicionado e trata de impacto ambiental?" → Sustentabilidade.

**Pergunta:** "Qual ferramenta revisa uma carga de trabalho contra os pilares?"

**Resposta curta:** AWS Well-Architected Tool.


**Fundamento explicado no capítulo:** "Qual ferramenta revisa uma carga de trabalho contra os pilares?" → AWS Well-Architected Tool.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.3 Conceitos de arquitetura que a prova cobra](03-conceitos-de-arquitetura.md) · 🏠 [Índice do domínio](README.md) · [1.5 AWS Cloud Adoption Framework (CAF)](05-cloud-adoption-framework.md) ➡️
