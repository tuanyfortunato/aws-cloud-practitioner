# 1.5 AWS Cloud Adoption Framework (CAF)

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

⬅️ [1.4 AWS Well-Architected Framework](04-well-architected-framework.md) · 🏠 [Índice do domínio](README.md) · [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** O CAF é o **guia da AWS para a empresa inteira se preparar** para a nuvem — não só a TI, mas também negócio, pessoas e governança. Ele divide o trabalho em **6 perspectivas** e **4 fases**.
>
> 🏠 **Analogia:** é como **mudar a família inteira para outro país**: alguém cuida do dinheiro e do objetivo (Business), alguém prepara as pessoas e o idioma (People), alguém controla orçamento e riscos (Governance), e os outros cuidam da casa nova (Platform), da segurança (Security) e do dia a dia (Operations).

**Ao terminar este tópico, você deve saber:**

- [ ] Citar as **6 perspectivas** e separar as de **negócio** (Business, People, Governance) das **técnicas** (Platform, Security, Operations).
- [ ] Citar as **4 fases**: Envision, Align, Launch e Scale.
- [ ] Reconhecer os **benefícios** declarados (menos risco, melhor ESG, mais receita, mais eficiência).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Perspectiva** | um grupo de capacidades com um público responsável (ex.: People → RH e liderança). |
| **ESG** | ambiental, social e governança. |

> 🎯 **Como não errar na prova:** Leia **quem** está envolvido no enunciado: RH, cultura ou treinamento → **People**; orçamento e risco → **Governance**; arquitetura → **Platform**; monitoramento e incidentes → **Operations**.

## 📖 Conteúdo

Guia para organizar a transformação digital de uma empresa na AWS.

- **Benefícios declarados:** reduzir risco de negócio, melhorar desempenho ESG (ambiental, social e governança), aumentar receita e aumentar eficiência operacional.
- **6 perspectivas:**

| Perspectiva | Público principal | Exemplos de capacidades |
| --- | --- | --- |
| Business | CEO, CFO, diretores de negócio | Estratégia, gestão de portfólio, inovação, dados como produto |
| People | RH, liderança, gestores de pessoas | Cultura, treinamento, gestão da mudança, desenho organizacional |
| Governance | CFO, gestores de risco e projetos | Gestão de programas, benefícios, riscos, finanças na nuvem (FinOps) |
| Platform | CTO, arquitetos | Arquitetura, engenharia de plataforma, dados, CI/CD |
| Security | CISO, times de segurança | Identidade, detecção, proteção de infraestrutura e dados, resposta a incidentes |
| Operations | Times de operação e SRE | Observabilidade, gestão de incidentes e problemas, gestão de mudanças |

- **Domínios de transformação:** Tecnologia, Processos, Organização e Produto.
- **4 fases (ciclo iterativo):** Envision (enxergar oportunidades), Align (identificar lacunas e alinhar stakeholders), Launch (entregar pilotos em produção), Scale (expandir pilotos para a organização).
- **Cai na prova:** Business, People e Governance são perspectivas de negócio; Platform, Security e Operations são técnicas. "Treinar funcionários" = People; "gerenciar orçamento e risco do programa" = Governance.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).

- "Qual perspectiva do CAF trata de treinamento, cultura e mudança organizacional?" → People.
- "Qual perspectiva garante que a estratégia de nuvem gere valor de negócio?" → Business.
- "Qual perspectiva cuida de risco, orçamento e gestão do programa?" → Governance.
- "Qual perspectiva trata da arquitetura e da plataforma técnica?" → Platform.
- "Qual perspectiva trata de identidade, proteção de dados e resposta a incidentes?" → Security.
- "Qual perspectiva trata de monitoramento e gestão de incidentes operacionais?" → Operations.
- "Quais são as fases da jornada de transformação?" → Envision, Align, Launch e Scale.
- "Qual é um benefício do CAF?" → Reduzir risco de negócio, melhorar ESG, aumentar receita ou eficiência operacional.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** O CAF organiza capacidades da empresa nas perspectivas Business, People, Governance, Platform, Security e Operations. Envision define resultados; Align identifica lacunas; Launch testa iniciativas; Scale amplia o que funciona.

**Como escolher:** Use quem é responsável e qual mudança é necessária: treinamento e cultura pertencem a People; decisões sobre investimento e risco, a Governance; infraestrutura e padrões técnicos, a Platform.

**O que não concluir:** CAF não é um serviço que migra servidores nem substitui uma revisão técnica do Well-Architected. Adoção inclui organização, habilidades e processos.

### Exercício de decisão

A infraestrutura já funciona, mas faltam habilidades e adaptação de funções na equipe. Qual perspectiva precisa de atenção?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

People. Escolher Platform só porque o projeto usa AWS ignora que o impedimento é organizacional.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.4 AWS Well-Architected Framework](04-well-architected-framework.md) · 🏠 [Índice do domínio](README.md) · [1.6 Estratégias de migração (os 7 Rs)](06-estrategias-de-migracao.md) ➡️
