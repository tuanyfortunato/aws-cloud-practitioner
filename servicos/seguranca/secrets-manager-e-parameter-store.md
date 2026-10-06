<!-- autoral -->

# AWS Secrets Manager e Systems Manager Parameter Store

> **Categoria:** Segurança e gestão de segredos · **Domínio:** 2 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** guardam segredos e configurações fora do código; o Secrets Manager também faz a rotação automática dos segredos.
>
> **Escopo oficial:** ✅ No escopo (Parameter Store como parte do Systems Manager) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

O sistema de matrícula precisa da senha do banco de dados. Deixá-la no código ou num arquivo de configuração faz a senha vazar junto com o código, e ninguém a troca porque teria de mexer em todos os lugares.

O **Secrets Manager** guarda, recupera e faz a **rotação** de segredos como credenciais de banco, chaves de API e tokens. A rotação pode ser automática, num calendário, e o programa sempre busca o valor atual. O **Parameter Store**, parte do Systems Manager, guarda parâmetros de configuração em texto simples ou cifrados (`SecureString`).

O limite: a AWS recomenda o Parameter Store para configurações e o Secrets Manager para segredos, porque só ele traz rotação automática. Os dois dependem das permissões do [IAM](iam.md): quem lê o segredo precisa de permissão para isso.

## Como funciona

1. Você grava o segredo no Secrets Manager (ou o parâmetro no Parameter Store), cifrado com o [KMS](kms.md).
2. Dá à função do IAM do programa permissão para ler aquele segredo.
3. O programa busca o valor na hora de usar, em vez de guardar uma cópia.
4. No Secrets Manager, a rotação troca a senha no segredo e no banco, gerenciada pelo serviço ou por uma função Lambda.

## Opções principais

| Opção | O que faz | Pista no enunciado |
|---|---|---|
| Secrets Manager | Segredos com rotação automática | "Trocar a senha do banco periodicamente" |
| Parameter Store padrão | Até 10.000 parâmetros de até 4 KB, sem cobrança adicional | "Configurações da aplicação sem custo" |
| Parameter Store avançado | Até 100.000 parâmetros de até 8 KB, com políticas; cobrado | "Parâmetros maiores ou com expiração" |
| `SecureString` | Parâmetro cifrado com o KMS | "Guardar um valor sensível no Parameter Store" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Tamanho do parâmetro padrão e avançado | 4 KB e 8 KB | 06/10/2026 |
| Parâmetros por conta e Região (padrão e avançado) | 10.000 e 100.000 | 06/10/2026 |

## Como é cobrado

O Secrets Manager cobra por segredo por mês (cada réplica conta como um segredo) e por 10.000 chamadas de API. No Parameter Store, os parâmetros padrão não têm cobrança adicional, e os avançados são cobrados.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS KMS](kms.md) | Guarda as chaves que cifram os segredos, não os segredos | "Chave de criptografia" |
| [AWS Systems Manager](../gerenciamento/systems-manager.md) | O serviço de operação do qual o Parameter Store faz parte | "Aplicar patches", "rodar comandos" |
| [AWS IAM](iam.md) | Credenciais temporárias por funções, sem guardar senha | "Instância acessando o S3" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [Rotação de segredos](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)
- [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [Parâmetros padrão e avançados](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html)
- [Preços do AWS Secrets Manager](https://aws.amazon.com/secrets-manager/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
