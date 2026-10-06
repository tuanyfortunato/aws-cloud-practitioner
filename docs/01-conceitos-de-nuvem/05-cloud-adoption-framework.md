# 1.5 AWS Cloud Adoption Framework (CAF)

## 🧠 Antes de começar

**Qual é a dificuldade?** Mudar para a nuvem afeta orçamento, equipes, processos e segurança. A mudança pode fracassar mesmo que as máquinas funcionem.

**A ideia em palavras simples:** O Cloud Adoption Framework, ou CAF, ajuda a organizar a preparação da empresa em perspectivas. Cada perspectiva reúne capacidades e responsáveis por uma parte da adoção.

**Exemplo do dia a dia:** A escola planeja treinamento para a equipe, regras de orçamento e operação do sistema, além da migração técnica.

**O que não concluir?** CAF não transfere servidores nem substitui ferramentas de implantação. Ele organiza a transformação da empresa; Well-Architected se concentra na revisão de uma aplicação e sua operação.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Perspectiva** | um grupo de capacidades com um público responsável (ex.: People → RH e liderança). |
| **ESG** | ambiental, social e governança. |

---

> **Domínio 1 — Conceitos de Nuvem (24%)**

⬅️ [1.4 AWS Well-Architected Framework](04-well-architected-framework.md) · 🏠 [Índice do domínio](README.md) · [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **CAF:** Cloud Adoption Framework: orientação para preparar capacidades da organização na adoção de nuvem. Não é uma ferramenta que transfere servidores.

Tecnologia é apenas uma parte da mudança. A empresa pode ter recursos funcionando, mas faltar equipe preparada, regras de decisão ou procedimentos operacionais. O CAF organiza essas capacidades para não deixar a transformação restrita à instalação de máquinas.

Leia cada perspectiva como um grupo de perguntas e responsáveis. Quem cuida de competências e cultura não realiza a mesma tarefa de quem define padrões técnicos. As fases orientam começar com objetivos, identificar lacunas, experimentar e ampliar.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como **mudar a família inteira para outro país**: alguém cuida do dinheiro e do objetivo (Business), alguém prepara as pessoas e o idioma (People), alguém controla orçamento e riscos (Governance), e os outros cuidam da casa nova (Platform), da segurança (Security) e do dia a dia (Operations).

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

Guia para organizar a transformação digital de uma empresa na AWS.

**Antes de ler este trecho:**

- **ESG:** Conjunto de aspectos ambientais, sociais e de governança. É uma perspectiva de avaliação organizacional, não uma função de configuração de um recurso.

**Benefícios declarados:** reduzir risco de negócio, melhorar desempenho ESG (ambiental, social e governança), aumentar receita e aumentar eficiência operacional.

**6 perspectivas:**

**Antes de ler este trecho:**

- **CI / CD / CI/CD:** Integração contínua e entrega ou implantação contínua: práticas para construir, verificar e disponibilizar versões por etapas repetíveis.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **treinamento:** Ajuste de um modelo com dados. É uma etapa diferente de utilizar o modelo já treinado para responder a uma nova entrada.

| Perspectiva | Público principal | Exemplos de capacidades |
| --- | --- | --- |
| Business | CEO, CFO, diretores de negócio | Estratégia, gestão de portfólio, inovação, dados como produto |
| People | RH, liderança, gestores de pessoas | Cultura, treinamento, gestão da mudança, desenho organizacional |
| Governance | CFO, gestores de risco e projetos | Gestão de programas, benefícios, riscos, finanças na nuvem (FinOps) |
| Platform | CTO, arquitetos | Arquitetura, engenharia de plataforma, dados, CI/CD |
| Security | CISO, times de segurança | Identidade, detecção, proteção de infraestrutura e dados, resposta a incidentes |
| Operations | Times de operação e SRE | Observabilidade, gestão de incidentes e problemas, gestão de mudanças |

**Domínios de transformação:** Tecnologia, Processos, Organização e Produto.

**4 fases (ciclo iterativo):** Envision (enxergar oportunidades), Align (identificar lacunas e alinhar stakeholders), Launch (entregar pilotos em produção), Scale (expandir pilotos para a organização).

**Cai na prova:** Business, People e Governance são perspectivas de negócio; Platform, Security e Operations são técnicas. "Treinar funcionários" = People; "gerenciar orçamento e risco do programa" = Governance.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** O CAF organiza capacidades da empresa nas perspectivas Business, People, Governance, Platform, Security e Operations. Envision define resultados; Align identifica lacunas; Launch testa iniciativas; Scale amplia o que funciona.

**Depois, compare as escolhas:** Use quem é responsável e qual mudança é necessária: treinamento e cultura pertencem a People; decisões sobre investimento e risco, a Governance; infraestrutura e padrões técnicos, a Platform.

**Por fim, verifique o limite:** CAF não é um serviço que migra servidores nem substitui uma revisão técnica do Well-Architected. Adoção inclui organização, habilidades e processos.

## 4. Caso resolvido

A infraestrutura já funciona, mas faltam habilidades e adaptação de funções na equipe. Qual perspectiva precisa de atenção?

**Raciocínio e resposta:** People. Escolher Platform só porque o projeto usa AWS ignora que o impedimento é organizacional.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Citar as **6 perspectivas** e separar as de **negócio** (Business, People, Governance) das **técnicas** (Platform, Security, Operations).
- [ ] Citar as **4 fases**: Envision, Align, Launch e Scale.
- [ ] Reconhecer os **benefícios** declarados (menos risco, melhor ESG, mais receita, mais eficiência).

**Dica de revisão para a prova:** Leia **quem** está envolvido no enunciado: RH, cultura ou treinamento → **People**; orçamento e risco → **Governance**; arquitetura → **Platform**; monitoramento e incidentes → **Operations**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).
**Pergunta:** "Qual perspectiva do CAF trata de treinamento, cultura e mudança organizacional?"

**Resposta curta:** People.

**Pergunta:** "Qual perspectiva garante que a estratégia de nuvem gere valor de negócio?"

**Resposta curta:** Business.

**Pergunta:** "Qual perspectiva cuida de risco, orçamento e gestão do programa?"

**Resposta curta:** Governance.

**Pergunta:** "Qual perspectiva trata da arquitetura e da plataforma técnica?"

**Resposta curta:** Platform.

**Pergunta:** "Qual perspectiva trata de identidade, proteção de dados e resposta a incidentes?"

**Resposta curta:** Security.

**Pergunta:** "Qual perspectiva trata de monitoramento e gestão de incidentes operacionais?"

**Resposta curta:** Operations.

**Pergunta:** "Quais são as fases da jornada de transformação?"

**Resposta curta:** Envision, Align, Launch e Scale.

**Pergunta:** "Qual é um benefício do CAF?"

**Resposta curta:** Reduzir risco de negócio, melhorar ESG, aumentar receita ou eficiência operacional.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.4 AWS Well-Architected Framework](04-well-architected-framework.md) · 🏠 [Índice do domínio](README.md) · [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) ➡️
