# 1.3 Conceitos de arquitetura que a prova cobra

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

⬅️ [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) · 🏠 [Índice do domínio](README.md) · [1.4 AWS Well-Architected Framework](04-well-architected-framework.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** São as **palavras de arquitetura** que a AWS usa para descrever um bom sistema na nuvem: crescer, aguentar falhas, voltar de desastres e manter as partes independentes.
>
> 🏠 **Analogia:** pense num **restaurante**: contratar garçons extras no sábado e dispensá-los na segunda é **elasticidade**; ter duas cozinhas para o caso de uma pegar fogo é **alta disponibilidade**; os pedidos ficarem num quadro em vez de o garçom esperar o cozinheiro é **acoplamento fraco**.

**Ao terminar este tópico, você deve saber:**

- [ ] Diferenciar **escalabilidade** (crescer) de **elasticidade** (crescer **e encolher** sozinho).
- [ ] Diferenciar escala **vertical** (máquina maior) de **horizontal** (mais máquinas).
- [ ] Ordenar as estratégias de **DR** da mais barata para a mais rápida e explicar **RTO** e **RPO**.
- [ ] Explicar por que filas e eventos (**acoplamento fraco**) evitam que uma falha derrube tudo.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Alta disponibilidade** | o sistema continua acessível mesmo com falhas (em geral, usando várias AZs). |
| **Tolerância a falhas** | continuar funcionando sem que o usuário perceba a falha. |
| **RTO** | quanto tempo você aceita ficar fora do ar depois de um desastre. |
| **RPO** | quantos dados (em tempo) você aceita perder. |

> 🎯 **Como não errar na prova:** "Encolher sozinho" → **elasticidade**. "Mais barato" em DR → **Backup and Restore**; "menor tempo" → **Multi-site**. "Falha de um componente não afetar os outros" → **acoplamento fraco** (SQS, SNS, EventBridge).

## 📖 Conteúdo

- **Escalabilidade:** capacidade de crescer para atender à demanda. *Vertical* (scale up: instância maior) vs *horizontal* (scale out: mais instâncias).
- **Elasticidade:** crescer e encolher automaticamente conforme a carga (ex.: Auto Scaling). A diferença para escalabilidade é o "encolher sozinho".
- **Alta disponibilidade:** o sistema continua acessível com falhas, normalmente com várias AZs.
- **Tolerância a falhas:** continuar funcionando sem interrupção perceptível mesmo quando um componente falha (redundância).
- **Agilidade:** reduzir o tempo e o custo de experimentar.
- **Recuperação de desastres (DR):** do mais barato e lento para o mais caro e rápido: Backup and Restore → Pilot Light → Warm Standby → Multi-site active/active.
- **Acoplamento fraco (loose coupling):** componentes se comunicam por filas e eventos (SQS, SNS, EventBridge), e a falha de um não derruba o outro.

## ➕ Complemento

- **RTO (Recovery Time Objective):** tempo máximo aceitável para restaurar o serviço após um desastre.
- **RPO (Recovery Point Objective):** quantidade máxima de dados que se aceita perder, medida em tempo (ex.: "no máximo 15 minutos de dados").
- Quanto menores RTO e RPO, mais cara a estratégia de DR (Multi-site é a de menor RTO/RPO; Backup and Restore, a de maior).
- **Monolito vs microsserviços:** o monolito tem tudo numa única aplicação; microsserviços são serviços pequenos e independentes, que escalam e são implantados separadamente e se comunicam por APIs, filas e eventos.
- **Projetar para falhas (design for failure):** assumir que componentes vão falhar e construir redundância e recuperação automática.
- **Serverless:** não gerenciar servidores, escala automática, pagar só pelo uso e alta disponibilidade embutida (Lambda, Fargate, DynamoDB, S3, SQS, SNS).
- **Stateless:** a aplicação não guarda estado no servidor (sessão vai para ElastiCache ou DynamoDB), o que facilita escalar horizontalmente.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).

- "A aplicação adiciona instâncias no pico e remove de madrugada, sozinha." → Elasticidade.
- "Como garantir que a falha de um datacenter não derrube a aplicação?" → Implantar em várias AZs (alta disponibilidade).
- "Qual estratégia de DR tem menor custo?" → Backup and Restore. "E menor tempo de recuperação?" → Multi-site active/active.
- "Como evitar que a falha de um componente afete os outros?" → Acoplamento fraco com SQS, SNS ou EventBridge.
- "O que significa RPO de 1 hora?" → Aceita-se perder no máximo 1 hora de dados.
- "Aumentar o tamanho da instância é escala..." → Vertical. "Adicionar instâncias é..." → Horizontal.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** Escala vertical aumenta uma máquina; horizontal adiciona máquinas. Filas desacoplam produtores e consumidores. Redundância reduz impacto de falhas; backups permitem voltar a uma cópia anterior.

**Como escolher:** Separe três requisitos: crescer, continuar disponível e recuperar depois de um desastre. Para recuperação, RTO trata do tempo fora do ar; RPO trata da perda tolerável de dados.

**O que não concluir:** Multi-AZ não recupera automaticamente uma exclusão lógica replicada. Backup não mantém, por si só, o sistema disponível durante a falha. Escalar não elimina gargalos de banco.

### Exercício de decisão

Uma empresa aceita ficar duas horas fora do ar e perder até dez minutos de dados. Quais objetivos deve registrar?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

RTO de duas horas e RPO de dez minutos. São metas diferentes: restaurar rapidamente uma cópia antiga pode cumprir o RTO e descumprir o RPO.

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

⬅️ [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) · 🏠 [Índice do domínio](README.md) · [1.4 AWS Well-Architected Framework](04-well-architected-framework.md) ➡️
