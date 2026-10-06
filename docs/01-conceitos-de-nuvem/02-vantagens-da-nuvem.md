# 1.2 As 6 vantagens da computação em nuvem

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma loja não sabe quantas pessoas chegarão durante uma promoção. Comprar capacidade para o maior pico pode deixar equipamentos ociosos no resto do ano.

**A ideia em palavras simples:** Os benefícios da nuvem incluem obter recursos mais rapidamente, ajustar capacidade e mudar a forma de investir em infraestrutura. Cada benefício responde a uma dificuldade diferente.

**Exemplo do dia a dia:** A loja cria capacidade para a campanha e a reduz depois, em vez de comprar máquinas permanentes apenas para o pico.

**O que não concluir?** Nuvem não garante economia em qualquer projeto. Recursos precisam ser escolhidos e acompanhados; este tópico explica benefícios, não uma promessa de redução automática da fatura.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **CapEx** | despesa de capital: comprar equipamento antes de usar (investimento antecipado). |
| **OpEx** | despesa operacional: pagar aos poucos, conforme o uso. |

---

> **Domínio 1 — Conceitos de Nuvem (24%)**

⬅️ [1.1 O que é computação em nuvem](01-o-que-e-computacao-em-nuvem.md) · 🏠 [Índice do domínio](README.md) · [1.3 Conceitos de arquitetura que a prova cobra](03-conceitos-de-arquitetura.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.

A demanda muda, mas um equipamento comprado permanece na empresa mesmo quando não é utilizado. Obter recursos sob demanda permite aproximar capacidade e necessidade. Isso também reduz a espera para experimentar ou atender um novo projeto.

Diferencie o benefício de sua implementação. A nuvem permite ajustar capacidade, mas a equipe precisa configurar esse ajuste. Também é possível manter recursos ociosos na nuvem e pagar por eles; o benefício não acontece só por mudar o local.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como trocar o **carro próprio por aplicativo de transporte**: você não paga o carro à vista (despesa variável), a empresa compra em volume (economia de escala), chama um carro maior quando precisa (parar de adivinhar capacidade), pede em minutos (agilidade), não cuida de oficina (sem manter datacenter) e usa o app em outras cidades (global em minutos).

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **CapEx / OpEx:** Despesa de capital e despesa operacional. Comprar equipamentos antecipadamente e pagar recursos ao longo do uso têm estruturas econômicas diferentes.

1. **Trocar despesa de capital por despesa variável:** sem investimento antecipado em hardware (CapEx → OpEx).

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.

2. **Beneficiar-se de economias de escala massivas:** a AWS compra em volume e repassa preços menores.

3. **Parar de adivinhar capacidade:** escala conforme a demanda real, sem sobra nem falta.

4. **Aumentar velocidade e agilidade:** recursos em minutos, experimentação barata.

5. **Parar de gastar dinheiro mantendo datacenters:** foco no negócio, não em racks e energia.

**Antes de ler este trecho:**

- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.

6. **Tornar-se global em minutos:** implantar em várias regiões com poucos cliques.

**Cai na prova:** a questão descreve um benefício e pede o nome oficial. Ex.: "não precisa mais comprar servidores para o pico de Black Friday" = parar de adivinhar capacidade.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.
- **implantação:** Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.

**Primeiro, identifique o funcionamento:** Capacidade é disponibilizada conforme a demanda, em vez de ser comprada para um pico futuro. A escala da AWS permite compartilhar infraestrutura entre clientes com isolamento.

**Depois, compare as escolhas:** Identifique o problema: capital antecipado, preço por volume, previsão de capacidade, demora de implantação, manutenção de datacenter ou alcance geográfico.

**Por fim, verifique o limite:** A nuvem oferece meios de economizar; recursos ociosos, tráfego e configurações inadequadas ainda geram despesas. Agilidade não é sinônimo de menor preço.

## 4. Caso resolvido

Uma loja mantém servidores para a Black Friday que ficam ociosos o resto do ano. Qual vantagem resolve isso?

**Raciocínio e resposta:** Deixar de adivinhar capacidade, combinado com elasticidade: aumentar no pico e reduzir depois. Comprar uma máquina maior permanentemente continua deixando capacidade ociosa.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Citar as **6 vantagens** com o nome oficial.
- [ ] Ligar cada cenário à vantagem certa (ex.: Black Friday sem comprar servidor → parar de adivinhar capacidade).
- [ ] Explicar **CapEx × OpEx** em uma frase.

**Dica de revisão para a prova:** Procure a palavra que denuncia a vantagem: **"investimento inicial"** → despesa variável; **"não sabe quanto tráfego"** → capacidade; **"preço menor por volume"** → economia de escala; **"outro continente"** → global em minutos.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).
**Pergunta:** "Qual vantagem permite trocar investimento inicial em servidores por pagamento conforme o uso?"

**Resposta curta:** Trocar despesa de capital por despesa variável.

**Pergunta:** "Uma empresa não sabe quanto tráfego terá no lançamento. Qual vantagem ajuda?"

**Resposta curta:** Parar de adivinhar capacidade.

**Pergunta:** "Como a AWS consegue preços menores que um datacenter próprio?"

**Resposta curta:** Economias de escala massivas.

**Pergunta:** "Uma startup quer abrir operação em outro continente em um dia."

**Resposta curta:** Tornar-se global em minutos.

**Pergunta:** "Qual vantagem libera o time para focar no produto em vez de racks e energia?"

**Resposta curta:** Parar de gastar mantendo datacenters.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.1 O que é computação em nuvem](01-o-que-e-computacao-em-nuvem.md) · 🏠 [Índice do domínio](README.md) · [1.3 Conceitos de arquitetura que a prova cobra](03-conceitos-de-arquitetura.md) ➡️
