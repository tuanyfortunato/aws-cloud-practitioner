# 3.15 Ferramentas de desenvolvimento

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma equipe precisa construir versões do programa, testá-las, publicá-las e investigar o caminho das requisições quando há lentidão.

**A ideia em palavras simples:** Ferramentas de desenvolvimento e observação apoiam etapas distintas. Construção e entrega automatizada são diferentes de rastrear a execução da aplicação.

**Exemplo do dia a dia:** Uma alteração passa por construção e testes configurados. Depois da implantação, rastreamentos ajudam a examinar um pedido que ficou lento.

**O que não concluir?** Uma ferramenta não escreve os testes nem corrige o programa automaticamente. Identifique se o pedido é construir, coordenar a entrega, implantar ou investigar.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **CI/CD** | integração e entrega contínuas: automatizar o caminho do código até a produção. |
| **Build** | transformar o código em algo executável e testá-lo. |
| **Rastreamento distribuído** | seguir uma requisição por vários serviços. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact](../../servicos/desenvolvimento/code-services.md) · [AWS X-Ray](../../servicos/desenvolvimento/x-ray.md) · [Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** No escopo só ficaram **AWS CLI, CodeBuild, CodePipeline e X-Ray**. CodeDeploy, CodeArtifact e CloudShell estão **fora do escopo**; Cloud9, CodeCommit e CodeStar não aparecem. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.14 Aplicações de negócio, usuário final, front-end e IoT](14-aplicacoes-de-negocio-e-iot.md) · 🏠 [Índice do domínio](README.md) · [3.16 Gestão e governança](16-gestao-e-governanca.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Uma versão do programa passa por preparação, verificação e publicação. Um processo automatizado conecta essas etapas, mas realiza o que foi definido pela equipe. Depois, observar a execução é um trabalho diferente de construir a versão.

Testes precisam existir e verificar comportamentos relevantes. Rastreamentos ajudam a localizar etapas lentas quando a aplicação emite dados adequados. Nenhuma ferramenta de desenvolvimento substitui a definição da regra de negócio ou a validação da mudança.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é uma **fábrica de software**: o **CodeBuild** monta e testa cada peça; o **CodePipeline** é a **esteira** que leva a peça de uma estação para a outra; o **X-Ray** é o **rastreador de encomendas** que mostra onde cada pedido atrasou.

</details>

## 2. Conceitos e opções explicados

**AWS CLI:** ver [3.1](01-formas-de-acesso-e-implantacao.md).

**AWS CodeBuild:** **compila, testa e empacota** código; serverless, cobrado por minuto de build.

**AWS CodePipeline:** **orquestra a esteira de CI/CD** (fonte → build → teste → deploy) — o GitHub Actions é um equivalente de terceiros.

**AWS CodeDeploy:** automatiza **deploys** em EC2, servidores on-premises, Lambda e ECS (não está na lista oficial, mas costuma aparecer com os outros).

**AWS X-Ray:** **rastreamento distribuído**: acompanha requisições entre microsserviços para achar gargalos e erros.

**AWS CodeArtifact:** repositório gerenciado de pacotes (npm, Maven, PyPI).

**Cai na prova:** "descobrir qual microsserviço está deixando a requisição lenta" = X-Ray; "automatizar a esteira de entrega" = CodePipeline; "compilar e rodar testes" = CodeBuild.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** CodeBuild executa build/testes; CodePipeline coordena estágios e integra ferramentas; X-Ray acompanha traces de requisições; CLI/SDK operam APIs.

**Depois, compare as escolhas:** Compilar: CodeBuild. Automatizar o fluxo entre etapas: CodePipeline. Investigar latência entre serviços: X-Ray. Consultar métricas/logs: CloudWatch.

**Por fim, verifique o limite:** Criar pipeline não escreve testes nem código. Trace depende de instrumentação e amostragem. Ferramentas fora do escopo podem ser úteis em produção sem virar foco da prova.

## 4. Caso resolvido

A equipe quer descobrir em qual serviço uma requisição demorou. O histórico de deploy sozinho resolve?

**Raciocínio e resposta:** X-Ray oferece rastreamento distribuído com instrumentação apropriada. CodePipeline informa a execução da esteira, não o caminho interno da requisição.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **CodeBuild** (compila e testa) de **CodePipeline** (orquestra a esteira de CI/CD).
- [ ] Saber que o **X-Ray** faz **rastreamento distribuído** entre microsserviços.
- [ ] Lembrar quais ferramentas ficaram **fora do escopo** (veja o aviso no topo).

**Dica de revisão para a prova:** "Qual microsserviço deixa a requisição lenta" → **X-Ray**. "Automatizar a esteira" → **CodePipeline**. "Compilar e rodar testes" → **CodeBuild**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Orquestrar a esteira de CI/CD na AWS."

**Resposta curta:** CodePipeline.

**Pergunta:** "Compilar e executar testes sem gerenciar servidores de build."

**Resposta curta:** CodeBuild.

**Pergunta:** "Automatizar deploy em EC2 e servidores on-premises."

**Resposta curta:** CodeDeploy.

**Pergunta:** "Encontrar gargalos de latência entre microsserviços."

**Resposta curta:** X-Ray.

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
