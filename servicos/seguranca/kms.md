<!-- autoral -->

# AWS KMS (Key Management Service)

> **Categoria:** Segurança e criptografia · **Domínio:** 2 · **Abrangência:** Regional (chaves multirregionais opcionais) · **Ficha:** núcleo
>
> **Em uma frase:** cria e controla as chaves usadas para cifrar dados, integradas aos serviços da AWS e com cada uso registrado no CloudTrail.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.5 Criptografia](../../docs/02-seguranca-e-conformidade/05-criptografia.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Os laudos médicos dos alunos ficam cifrados no S3, mas a criptografia move o problema para a chave: quem guarda, quem pode usar, como provar quem usou.

O KMS guarda as chaves em **módulos de segurança de hardware** (HSMs) validados pela FIPS 140-3 nível 3, e a chave nunca sai dele sem estar cifrada. Serviços como S3, EBS e RDS pedem ao KMS que cifre ou decifre, usando **criptografia de envelope**: os dados são cifrados com uma chave de dados, e ela é cifrada pela chave do KMS. Uma **política de chave** diz quem pode usar cada chave, e o CloudTrail registra todas as chamadas.

O limite: o KMS usa HSMs gerenciados e compartilhados pela AWS. Quem precisa de HSM exclusivo usa o [CloudHSM](cloudhsm.md). E a criptografia não substitui as permissões: quem pode ler o objeto e usar a chave lê o dado decifrado.

## Como funciona

1. Você usa uma chave pertencente à AWS ou gerenciada pela AWS, ou cria uma **chave gerenciada pelo cliente**.
2. A política de chave, junto com o IAM, define quem administra e quem usa a chave.
3. O serviço gera uma chave de dados, cifra os dados com ela e guarda a chave de dados cifrada ao lado.
4. Para ler, o serviço pede ao KMS que decifre a chave de dados; a chamada fica no CloudTrail.

## Opções principais

| Tipo de chave | Quem controla | Custo |
|---|---|---|
| Pertencente à AWS | O serviço da AWS, numa conta da AWS | Nenhum |
| Gerenciada pela AWS (`aws/serviço`, legada desde 2021) | A AWS, na sua conta, só para aquele serviço | Sem custo mensal; paga-se o uso |
| Gerenciada pelo cliente | Você: política, rotação, ativação e exclusão | Custo mensal por chave e por uso |
| Chave multirregional | Mesma chave em várias Regiões, para cifrar numa e decifrar noutra | Cada réplica é uma chave cobrada |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Validação dos HSMs | FIPS 140-3 nível 3 | 06/10/2026 |
| Rotação automática | Anual por padrão, ou no período definido | 06/10/2026 |
| Espera para apagar uma chave | De 7 a 30 dias (padrão de 30) | 06/10/2026 |
| Nível gratuito | 20.000 requisições por mês | 06/10/2026 |

## Como é cobrado

Cada chave gerenciada pelo cliente tem custo mensal, e as requisições são cobradas acima do nível gratuito de 20.000 por mês. As chaves pertencentes à AWS não custam nada, e as gerenciadas pela AWS cobram só o uso.

## Não confundir com

| Serviço | Diferença para o KMS | Pista no enunciado |
|---|---|---|
| [AWS CloudHSM](cloudhsm.md) | HSM exclusivo do cliente, que administra os usuários | "HSM dedicado", "controle exclusivo" |
| [AWS Certificate Manager](certificate-manager.md) | Certificados TLS para dados em trânsito | "HTTPS", "certificado" |
| [AWS Secrets Manager](secrets-manager-e-parameter-store.md) | Guarda segredos (cifrados com o KMS) e os rotaciona | "Senha do banco" |
| [AWS CloudTrail](../gerenciamento/cloudtrail.md) | Registra quem usou a chave | "Quem usou a chave e quando" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Chaves do AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
- [Criptografia de envelope](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html)
- [Rotação de chaves](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
- [Exclusão de chaves](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html)
- [Chaves multirregionais](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html)
- [Registro de chamadas no CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html)
- [Preços do AWS KMS](https://aws.amazon.com/kms/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
