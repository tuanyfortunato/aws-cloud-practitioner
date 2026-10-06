<!-- autoral -->

# Amazon Macie

> **Categoria:** Segurança e proteção de dados · **Domínio:** 2 · **Abrangência:** Regional (várias contas pelo Organizations) · **Ficha:** núcleo
>
> **Em uma frase:** descobre dados sensíveis no Amazon S3 com aprendizado de máquina e reconhecimento de padrões e avalia a segurança e o controle de acesso dos buckets.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A secretaria exportou uma planilha com CPF, endereço e dados de saúde dos alunos e guardou num bucket usado para arquivos públicos do site. A escola tem centenas de buckets e milhões de objetos; ninguém sabe onde mais há dados pessoais esquecidos.

O **Macie** procura. Ao ser ativado, ele monta um inventário dos buckets S3 e avalia continuamente a segurança e o controle de acesso de cada um, gerando um achado se, por exemplo, um bucket se torna público. Ele também examina o conteúdo dos objetos com **identificadores gerenciados** (critérios prontos para dados pessoais, financeiros, credenciais e outros) e **identificadores personalizados** (expressões regulares definidas pela escola, como o formato da matrícula). Cada dado sensível encontrado vira um achado com o local e o tipo do dado.

O limite é o escopo: o Macie olha o S3, não bancos de dados nem discos de instâncias. E ele não apaga nem move a planilha; a correção fica com o cliente.

## Como funciona

1. Você ativa o Macie na conta ou para a organização inteira.
2. Ele reúne os detalhes dos buckets (criptografia, acesso público, compartilhamento) e passa a avaliá-los.
3. A descoberta automática escolhe amostras representativas dos objetos e procura dados sensíveis; para uma análise mais funda, você cria um trabalho de descoberta em buckets escolhidos.
4. Os achados vão para o console, para o EventBridge e para o Security Hub.

## Opções principais

| Recurso | O que faz | Quando usar |
|---|---|---|
| Inventário e monitoramento de buckets | Avalia acesso público, criptografia e compartilhamento | Sempre ligado ao ativar |
| Descoberta automática de dados sensíveis | Amostragem contínua dos objetos de todos os buckets | Visão ampla de onde há dados sensíveis |
| Trabalhos de descoberta | Análise direcionada, uma vez ou periódica | Auditar um bucket específico a fundo |
| Identificadores gerenciados | Critérios prontos para muitos tipos de dado e países | Dados pessoais, financeiros, credenciais |
| Identificadores personalizados | Expressão regular definida pelo cliente | Formato próprio, como o número de matrícula |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Onde procura | Amazon S3 | 06/10/2026 |
| Teste gratuito | 30 dias | 06/10/2026 |
| Avaliação contínua de buckets | Até 10.000 buckets | 06/10/2026 |

## Como é cobrado

Três dimensões, depois do teste de 30 dias: o número de buckets avaliados no inventário, o número de objetos monitorados pela descoberta automática e a quantidade de dados examinados nas descobertas automática e direcionada. As cobranças são proporcionais por dia.

## Não confundir com

| Serviço | Diferença para o Macie | Pista no enunciado |
|---|---|---|
| [Amazon GuardDuty](guardduty.md) | Detecta ameaças, inclusive no S3 com o S3 Protection | "Atividade suspeita", "exfiltração" |
| [Amazon Inspector](inspector.md) | Procura vulnerabilidades no software | "CVE", "pacote desatualizado" |
| [AWS KMS](kms.md) | Cifra os dados, sem procurar onde estão | "Criptografia", "chave" |
| [Amazon S3](../armazenamento/s3.md) | Guarda os objetos; o Bloqueio de Acesso Público impede que fiquem públicos | "Bloquear acesso público" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [Descoberta automática de dados sensíveis](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html)
- [Identificadores gerenciados](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html)
- [Preços do Amazon Macie](https://aws.amazon.com/macie/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
