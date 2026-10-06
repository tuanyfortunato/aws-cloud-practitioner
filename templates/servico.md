<!-- autoral -->

<!--
Modelo de ficha autoral (Fase 5 do plano de implementação). Ficha-piloto: servicos/integracao/sqs.md.

- A ficha é consulta rápida de uma ou duas páginas, não uma segunda aula. Quando a aula já explica o
  mecanismo, a ficha resume e remete a ela.
- O marcador autoral na primeira linha faz o gerar_docs.py preservar a ficha. O índice de servicos/README.md
  lê o título (primeira linha "# ") e a linha "**Em uma frase:**" do cabeçalho; mantenha as duas.
- A ficha continua registrada em FICHAS, CATEGORIA e ESCOPO do gerar_docs.py e nas bases editoriais
  (conteudo_servicos, introducoes_servicos, sequencias_servicos, aprofundamento), porque o gerador exige
  cobertura completa; essas entradas não são mais usadas para escrever a ficha.
- Ficha núcleo (serviço central de uma aula): todas as seções. Ficha complementar (no escopo, mas periférica):
  só "Em uma frase", "Como funciona", "Não confundir com" e "Fontes oficiais".
- Toda informação sobre a AWS precisa estar confirmada na documentação oficial e listada em "Fontes oficiais".
  O que não for confirmado vai para docs/00-guia-do-exame/pendencias-de-verificacao.md, não para a ficha.
- Explique cada termo em prosa no primeiro uso, sem frases defensivas. Apague estes comentários ao escrever.
-->

# Nome do serviço

> **Categoria:** Categoria · **Domínio:** N · **Abrangência:** Global, Regional ou por zona · **Ficha:** núcleo ou complementar
>
> **Em uma frase:** o que o serviço é e para que serve, sem exigir conhecimento prévio.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [x.y Título da aula](../../docs/pasta-do-dominio/arquivo-da-aula.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

<!-- Dois ou três parágrafos: o problema, contado pelo caso da escola; como o serviço resolve; e o limite
     (o que ele não faz sozinho). Termine remetendo à aula que explica o mecanismo. -->

## Como funciona

<!-- De três a cinco passos numerados, do pedido ao resultado. -->

1. Primeiro passo.
2. Segundo passo.
3. Terceiro passo.

## Opções principais

<!-- Tabela com as escolhas que mudam o comportamento ou o preço e quando usar cada uma. -->

| Opção | O que faz | Quando usar |
|---|---|---|

## Números que a prova cobra

<!-- Só números citados em fonte oficial, com unidade, condição e data de verificação. -->

| O quê | Valor | Verificado em |
|---|---|---|

## Como é cobrado

<!-- A unidade de cobrança, o que é grátis e o que continua cobrando quando o trabalho termina. -->

## Não confundir com

<!-- Serviços parecidos, comparados pelo problema que resolvem, e a pista do enunciado que leva a cada um. -->

| Serviço | Diferença | Pista no enunciado |
|---|---|---|

## Fontes oficiais

Verificadas em DD/MM/AAAA.

- [Página da documentação](https://docs.aws.amazon.com/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
