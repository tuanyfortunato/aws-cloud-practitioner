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

---

> **Domínio 4 — Cobrança, Preços e Suporte (12%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

🏠 [Índice do domínio](README.md) · [4.2 Modelos de compra do EC2](02-modelos-de-compra-ec2.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.


O serviço mede uma unidade de consumo ou capacidade, não necessariamente pessoas usando seu sistema. Tempo de máquina, espaço de dados, chamadas e transferência são dimensões diferentes. Uma aplicação pode reunir várias cobranças ao mesmo tempo.

Antes de calcular, identifique o recurso, a unidade e a condição. Parar computação pode manter volumes; remover uma aplicação pode manter cópias; uma chamada pode consumir unidades conforme seu tamanho. O modelo de cobrança evita suposições de custo zero.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como o **plano de celular**: pré-pago (pague pelo uso), plano anual com desconto (compromisso) e franquia que fica mais barata por GB quando você compra mais (volume).

</details>

## 2. Conceitos e opções explicados

**Pague conforme o uso (pay-as-you-go):** sem contrato nem investimento inicial.

**Antes de ler este trecho:**

- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.


**Economize ao se comprometer:** reservas e Savings Plans dão desconto em troca de compromisso de 1 ou 3 anos.

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.


**Pague menos por unidade quando usa mais:** faixas de desconto por volume (ex.: S3, transferência de dados).


**Três grandes geradores de custo:** computação, armazenamento e **transferência de dados de saída**.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.


**Primeiro, identifique o funcionamento:** A cobrança combina unidades: tempo de computação, capacidade armazenada, requisições, processamento e transferência. Recursos relacionados podem ser cobrados separadamente.

**Depois, compare as escolhas:** Pay-as-you-go dá flexibilidade; compromissos podem reduzir preço para consumo previsível; classes de armazenamento trocam custo por frequência e prazo de recuperação.

**Por fim, verifique o limite:** Grátis para um componente não significa solução inteira gratuita. Região, plataforma, volume e modalidade alteram preços; orçamento deve incluir dependências.

## 4. Caso resolvido

Uma função Lambda barata passa por NAT Gateway e grava logs. Só estimar a função basta?

**Raciocínio e resposta:** Não. Inclua rede, logs e armazenamento conforme o uso. A cobrança acompanha os recursos utilizados, não apenas o serviço principal.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Um recurso pode estar ocioso e ainda gerar cobrança. Para planejar gastos, você precisa entender pelo que está pagando, não apenas quantas pessoas usam o sistema.

**2. O que a solução fornece?**

Preço pode depender de capacidade provisionada, tempo, armazenamento, chamadas ou transferência, conforme o serviço. Diferentes componentes podem ter cobranças independentes.

**3. Que conclusão seria incorreta?**

Pagar pelo uso não significa pagar apenas por pessoas usando a aplicação. Este tópico ensina a identificar as unidades e condições de cobrança.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Citar os **3 princípios** de preço.
- [ ] Citar os **3 geradores de custo**: computação, armazenamento e **transferência de saída**.

**Dica de revisão para a prova:** "Desconto em troca de compromisso de 1 ou 3 anos" → **Reservas/Savings Plans**. "Mais barato por GB quanto mais usa" → **desconto por volume**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-4.md).
**Pergunta:** "Qual é um princípio de preço da AWS?"

**Resposta curta:** Pagar conforme o uso, economizar ao se comprometer, pagar menos por unidade ao usar mais.

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**Fundamento explicado no capítulo:** "Qual é um princípio de preço da AWS?" → Pagar conforme o uso, economizar ao se comprometer, pagar menos por unidade ao usar mais.

**Pergunta:** "Quais são os três principais geradores de custo?"

**Resposta curta:** Computação, armazenamento e transferência de dados de saída.


**Fundamento explicado no capítulo:** "Quais são os três principais geradores de custo?" → Computação, armazenamento e transferência de dados de saída.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

🏠 [Índice do domínio](README.md) · [4.2 Modelos de compra do EC2](02-modelos-de-compra-ec2.md) ➡️
