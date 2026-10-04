# 3.15 Ferramentas de desenvolvimento

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact](../../servicos/desenvolvimento/code-services.md) · [AWS X-Ray](../../servicos/desenvolvimento/x-ray.md) · [Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md)

⬅️ [3.14 Aplicações de negócio, usuário final, front-end e IoT](14-aplicacoes-de-negocio-e-iot.md) · 🏠 [Índice do domínio](README.md) · [3.16 Gestão e governança](16-gestao-e-governanca.md) ➡️

---

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
  - Como o exam guide ainda lista Cloud9 e CodeStar, saiba o propósito: Cloud9 = IDE no navegador; CodeStar = gerenciar projetos de CI/CD.
- **AppConfig** = feature flags/configuração dinâmica · **X-Ray** = rastreamento distribuído · **CodeArtifact** = repositório de pacotes (npm, Maven, PyPI).
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.14 Aplicações de negócio, usuário final, front-end e IoT](14-aplicacoes-de-negocio-e-iot.md) · 🏠 [Índice do domínio](README.md) · [3.16 Gestão e governança](16-gestao-e-governanca.md) ➡️
