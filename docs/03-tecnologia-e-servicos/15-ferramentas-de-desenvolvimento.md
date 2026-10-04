# 3.15 Ferramentas de desenvolvimento

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact](../../servicos/desenvolvimento/code-services.md) · [AWS X-Ray](../../servicos/desenvolvimento/x-ray.md) · [Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** No escopo só ficaram **AWS CLI, CodeBuild, CodePipeline e X-Ray**. CodeDeploy, CodeArtifact e CloudShell estão **fora do escopo**; Cloud9, CodeCommit e CodeStar não aparecem. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.14 Aplicações de negócio, usuário final, front-end e IoT](14-aplicacoes-de-negocio-e-iot.md) · 🏠 [Índice do domínio](README.md) · [3.16 Gestão e governança](16-gestao-e-governanca.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** Ferramentas que ajudam a **entregar software**: compilar e testar, automatizar a esteira de entrega e encontrar onde uma aplicação está lenta.
>
> 🏠 **Analogia:** é uma **fábrica de software**: o **CodeBuild** monta e testa cada peça; o **CodePipeline** é a **esteira** que leva a peça de uma estação para a outra; o **X-Ray** é o **rastreador de encomendas** que mostra onde cada pedido atrasou.

**Ao terminar este tópico, você deve saber:**

- [ ] Diferenciar **CodeBuild** (compila e testa) de **CodePipeline** (orquestra a esteira de CI/CD).
- [ ] Saber que o **X-Ray** faz **rastreamento distribuído** entre microsserviços.
- [ ] Lembrar quais ferramentas ficaram **fora do escopo** (veja o aviso no topo).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **CI/CD** | integração e entrega contínuas: automatizar o caminho do código até a produção. |
| **Build** | transformar o código em algo executável e testá-lo. |
| **Rastreamento distribuído** | seguir uma requisição por vários serviços. |

> 🎯 **Como não errar na prova:** "Qual microsserviço deixa a requisição lenta" → **X-Ray**. "Automatizar a esteira" → **CodePipeline**. "Compilar e rodar testes" → **CodeBuild**.

## 📖 Conteúdo

- **AWS CLI:** ver [3.1](01-formas-de-acesso-e-implantacao.md).
- **AWS CodeBuild:** **compila, testa e empacota** código; serverless, cobrado por minuto de build.
- **AWS CodePipeline:** **orquestra a esteira de CI/CD** (fonte → build → teste → deploy) — o GitHub Actions é um equivalente de terceiros.
- **AWS CodeDeploy:** automatiza **deploys** em EC2, servidores on-premises, Lambda e ECS (não está na lista oficial, mas costuma aparecer com os outros).
- **AWS X-Ray:** **rastreamento distribuído**: acompanha requisições entre microsserviços para achar gargalos e erros.
- **AWS CodeArtifact:** repositório gerenciado de pacotes (npm, Maven, PyPI).
- **Cai na prova:** "descobrir qual microsserviço está deixando a requisição lenta" = X-Ray; "automatizar a esteira de entrega" = CodePipeline; "compilar e rodar testes" = CodeBuild.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Orquestrar a esteira de CI/CD na AWS." → CodePipeline.
- "Compilar e executar testes sem gerenciar servidores de build." → CodeBuild.
- "Automatizar deploy em EC2 e servidores on-premises." → CodeDeploy.
- "Encontrar gargalos de latência entre microsserviços." → X-Ray.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- 🔄 **Status das ferramentas de desenvolvedor:**
  - **CodeCommit:** voltou a **GA e aberto a novos clientes em 24/11/2025** (tinha sido fechado em 2024).
  - **Cloud9:** fechado para novos clientes desde 25/07/2024 → alternativa: **CloudShell** (shell no navegador, autenticado, com CLI).
  - **CodeStar:** descontinuado em 31/07/2024.
  - ✔️ Verificado em 04/10/2026: Cloud9, CodeStar e CodeCommit **não estão** na lista atual; no escopo ficaram **CLI, CodeBuild, CodePipeline e X-Ray**. Saiba só o propósito dos outros: Cloud9 = IDE no navegador; CodeStar = projetos de CI/CD.
- **AppConfig** = feature flags/configuração dinâmica · **X-Ray** = rastreamento distribuído · **CodeArtifact** = repositório de pacotes (npm, Maven, PyPI).
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.14 Aplicações de negócio, usuário final, front-end e IoT](14-aplicacoes-de-negocio-e-iot.md) · 🏠 [Índice do domínio](README.md) · [3.16 Gestão e governança](16-gestao-e-governanca.md) ➡️
