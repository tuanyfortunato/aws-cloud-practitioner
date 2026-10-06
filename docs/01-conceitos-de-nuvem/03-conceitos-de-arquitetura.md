# 1.3 Conceitos de arquitetura que a prova cobra

## 🧠 Antes de começar

**Qual é a dificuldade?** Um sistema pode crescer, ficar lento ou perder uma máquina. A equipe precisa escolher como continuar atendendo e como recuperar dados e operação.

**A ideia em palavras simples:** Conceitos de arquitetura descrevem capacidade, disponibilidade, recuperação e dependências entre partes. Eles ajudam a explicar o objetivo antes de escolher um serviço.

**Exemplo do dia a dia:** Se uma máquina não atende mais os visitantes, você pode usar uma maior ou distribuir o trabalho entre várias. Se uma falhar, outra pode ajudar a manter o atendimento, conforme o projeto.

**O que não concluir?** Crescer não é o mesmo que suportar falhas; ter cópias também não garante recuperação imediata. Aprenda a distinguir as necessidades antes de escolher uma solução.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Alta disponibilidade** | o sistema continua acessível mesmo com falhas (em geral, usando várias AZs). |
| **Tolerância a falhas** | continuar funcionando sem que o usuário perceba a falha. |
| **RTO** | quanto tempo você aceita ficar fora do ar depois de um desastre. |
| **RPO** | quantos dados (em tempo) você aceita perder. |

---

> **Domínio 1 — Conceitos de Nuvem (24%)**

⬅️ [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) · 🏠 [Índice do domínio](README.md) · [1.4 AWS Well-Architected Framework](04-well-architected-framework.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Uma aplicação depende de várias partes. Crescer uma delas ajuda apenas se ela for o limite do atendimento. Disponibilidade trata de continuar atendendo; recuperação trata de voltar após uma interrupção. Esses objetivos podem exigir soluções diferentes.

Imagine um banco com cópias: se uma máquina falha, uma alternativa pode ajudar. Se um comando apaga dados e a exclusão chega às cópias, pode ser necessário restaurar um ponto anterior. Isso explica por que redundância, replicação e backup não são sinônimos.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

pense num **restaurante**: contratar garçons extras no sábado e dispensá-los na segunda é **elasticidade**; ter duas cozinhas para o caso de uma pegar fogo é **alta disponibilidade**; os pedidos ficarem num quadro em vez de o garçom esperar o cozinheiro é **acoplamento fraco**.

</details>

## 2. Conceitos e opções explicados

**Escalabilidade:** capacidade de crescer para atender à demanda. *Vertical* (scale up: instância maior) vs *horizontal* (scale out: mais instâncias).

**Elasticidade:** crescer e encolher automaticamente conforme a carga (ex.: Auto Scaling). A diferença para escalabilidade é o "encolher sozinho".

**Alta disponibilidade:** o sistema continua acessível com falhas, normalmente com várias AZs.

**Tolerância a falhas:** continuar funcionando sem interrupção perceptível mesmo quando um componente falha (redundância).

**Agilidade:** reduzir o tempo e o custo de experimentar.

**Recuperação de desastres (DR):** do mais barato e lento para o mais caro e rápido: Backup and Restore → Pilot Light → Warm Standby → Multi-site active/active.

**Acoplamento fraco (loose coupling):** componentes se comunicam por filas e eventos (SQS, SNS, EventBridge), e a falha de um não derruba o outro.

### ➕ Complemento

**RTO (Recovery Time Objective):** tempo máximo aceitável para restaurar o serviço após um desastre.

**RPO (Recovery Point Objective):** quantidade máxima de dados que se aceita perder, medida em tempo (ex.: "no máximo 15 minutos de dados").

Quanto menores RTO e RPO, mais cara a estratégia de DR (Multi-site é a de menor RTO/RPO; Backup and Restore, a de maior).

**Monolito vs microsserviços:** o monolito tem tudo numa única aplicação; microsserviços são serviços pequenos e independentes, que escalam e são implantados separadamente e se comunicam por APIs, filas e eventos.

**Projetar para falhas (design for failure):** assumir que componentes vão falhar e construir redundância e recuperação automática.

**Serverless:** não gerenciar servidores, escala automática, pagar só pelo uso e alta disponibilidade embutida (Lambda, Fargate, DynamoDB, S3, SQS, SNS).

**Stateless:** a aplicação não guarda estado no servidor (sessão vai para ElastiCache ou DynamoDB), o que facilita escalar horizontalmente.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** Escala vertical aumenta uma máquina; horizontal adiciona máquinas. Filas desacoplam produtores e consumidores. Redundância reduz impacto de falhas; backups permitem voltar a uma cópia anterior.

**Depois, compare as escolhas:** Separe três requisitos: crescer, continuar disponível e recuperar depois de um desastre. Para recuperação, RTO trata do tempo fora do ar; RPO trata da perda tolerável de dados.

**Por fim, verifique o limite:** Multi-AZ não recupera automaticamente uma exclusão lógica replicada. Backup não mantém, por si só, o sistema disponível durante a falha. Escalar não elimina gargalos de banco.

## 4. Caso resolvido

Uma empresa aceita ficar duas horas fora do ar e perder até dez minutos de dados. Quais objetivos deve registrar?

**Raciocínio e resposta:** RTO de duas horas e RPO de dez minutos. São metas diferentes: restaurar rapidamente uma cópia antiga pode cumprir o RTO e descumprir o RPO.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **escalabilidade** (crescer) de **elasticidade** (crescer **e encolher** sozinho).
- [ ] Diferenciar escala **vertical** (máquina maior) de **horizontal** (mais máquinas).
- [ ] Ordenar as estratégias de **DR** da mais barata para a mais rápida e explicar **RTO** e **RPO**.
- [ ] Explicar por que filas e eventos (**acoplamento fraco**) evitam que uma falha derrube tudo.

**Dica de revisão para a prova:** "Encolher sozinho" → **elasticidade**. "Mais barato" em DR → **Backup and Restore**; "menor tempo" → **Multi-site**. "Falha de um componente não afetar os outros" → **acoplamento fraco** (SQS, SNS, EventBridge).

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).
**Pergunta:** "A aplicação adiciona instâncias no pico e remove de madrugada, sozinha."

**Resposta curta:** Elasticidade.

**Pergunta:** "Como garantir que a falha de um datacenter não derrube a aplicação?"

**Resposta curta:** Implantar em várias AZs (alta disponibilidade).

**Pergunta:** "Qual estratégia de DR tem menor custo?"

**Resposta curta:** Backup and Restore. "E menor tempo de recuperação?" → Multi-site active/active.

**Pergunta:** "Como evitar que a falha de um componente afete os outros?"

**Resposta curta:** Acoplamento fraco com SQS, SNS ou EventBridge.

**Pergunta:** "O que significa RPO de 1 hora?"

**Resposta curta:** Aceita-se perder no máximo 1 hora de dados.

**Pergunta:** "Aumentar o tamanho da instância é escala..."

**Resposta curta:** Vertical. "Adicionar instâncias é..." → Horizontal.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) · 🏠 [Índice do domínio](README.md) · [1.4 AWS Well-Architected Framework](04-well-architected-framework.md) ➡️
