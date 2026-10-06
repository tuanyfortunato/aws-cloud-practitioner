<!-- autoral -->

# AWS X-Ray

> **Categoria:** Ferramentas de desenvolvedor / observabilidade · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** coleta dados sobre as requisições que a aplicação atende e mostra o caminho de cada uma pelos serviços, bancos e APIs, para achar lentidão e erros.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.15 Ferramentas de desenvolvimento](../../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

O sistema de matrícula virou um conjunto de peças: site, filas, funções Lambda e banco. Quando uma inscrição demora, ninguém sabe em qual peça. O **AWS X-Ray** faz **rastreamento distribuído**: acompanha uma requisição de ponta a ponta e mostra as chamadas que a aplicação fez a outros recursos da AWS, microsserviços, bancos e APIs.

1. A aplicação é instrumentada para enviar dados de rastreamento; serviços como o Lambda já se integram ao X-Ray.
2. Cada requisição rastreada gera um registro das chamadas que ela fez.
3. O X-Ray reúne esses dados.
4. A equipe visualiza e filtra os rastros para achar onde está a demora ou o erro.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon CloudWatch](../gerenciamento/cloudwatch.md) | Métricas e logs de cada recurso | "CPU", "alarme" |
| [AWS CloudTrail](../gerenciamento/cloudtrail.md) | Registra as chamadas de API da conta | "Quem fez o quê" |
| [Ferramentas de CI/CD](code-services.md) | Compilam, testam e entregam o código | "Pipeline" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
