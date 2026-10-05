# 4.1 Princípios de preço da AWS

## 🧠 Antes de começar

**Qual é a dificuldade?** Um recurso pode estar ocioso e ainda gerar cobrança. Para planejar gastos, você precisa entender pelo que está pagando, não apenas quantas pessoas usam o sistema.

**A ideia em palavras simples:** Preço pode depender de capacidade provisionada, tempo, armazenamento, chamadas ou transferência, conforme o serviço. Diferentes componentes podem ter cobranças independentes.

**Exemplo do dia a dia:** Uma máquina ligada sem visitantes pode custar. Mesmo ao pará-la, discos ou outros recursos mantidos podem continuar cobrados.

**O que não concluir?** Pagar pelo uso não significa pagar apenas por pessoas usando a aplicação. Este tópico ensina a identificar as unidades e condições de cobrança.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Pay-as-you-go** | pagar conforme o uso, sem contrato. |
| **Transferência de saída** | dados que saem da AWS para a internet (é cobrada). |

**Ao terminar este tópico, você deve saber:**

- [ ] Citar os **3 princípios** de preço.
- [ ] Citar os **3 geradores de custo**: computação, armazenamento e **transferência de saída**.

<details>
<summary>Uma analogia para revisar a ideia</summary>

é como o **plano de celular**: pré-pago (pague pelo uso), plano anual com desconto (compromisso) e franquia que fica mais barata por GB quando você compra mais (volume).

</details>

> 🎯 **Como não errar na prova:** "Desconto em troca de compromisso de 1 ou 3 anos" → **Reservas/Savings Plans**. "Mais barato por GB quanto mais usa" → **desconto por volume**.

---

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

🏠 [Índice do domínio](README.md) · [4.2 Modelos de compra do EC2](02-modelos-de-compra-ec2.md) ➡️

---

## 📖 Conteúdo

- **Pague conforme o uso (pay-as-you-go):** sem contrato nem investimento inicial.
- **Economize ao se comprometer:** reservas e Savings Plans dão desconto em troca de compromisso de 1 ou 3 anos.
- **Pague menos por unidade quando usa mais:** faixas de desconto por volume (ex.: S3, transferência de dados).
- **Três grandes geradores de custo:** computação, armazenamento e **transferência de dados de saída**.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).

- "Qual é um princípio de preço da AWS?" → Pagar conforme o uso, economizar ao se comprometer, pagar menos por unidade ao usar mais.
- "Quais são os três principais geradores de custo?" → Computação, armazenamento e transferência de dados de saída.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** A cobrança combina unidades: tempo de computação, capacidade armazenada, requisições, processamento e transferência. Recursos relacionados podem ser cobrados separadamente.

**Como escolher:** Pay-as-you-go dá flexibilidade; compromissos podem reduzir preço para consumo previsível; classes de armazenamento trocam custo por frequência e prazo de recuperação.

**O que não concluir:** Grátis para um componente não significa solução inteira gratuita. Região, plataforma, volume e modalidade alteram preços; orçamento deve incluir dependências.

### Exercício de decisão

Uma função Lambda barata passa por NAT Gateway e grava logs. Só estimar a função basta?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Não. Inclua rede, logs e armazenamento conforme o uso. A cobrança acompanha os recursos utilizados, não apenas o serviço principal.

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

🏠 [Índice do domínio](README.md) · [4.2 Modelos de compra do EC2](02-modelos-de-compra-ec2.md) ➡️
