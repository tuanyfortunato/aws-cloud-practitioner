# Amazon Macie

> **Categoria:** Segurança / proteção de dados · **Domínio:** 2 · **Escopo:** Regional (multi-conta) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** usa machine learning e padrões para **descobrir e proteger dados sensíveis (PII) no Amazon S3**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## O que faz

| Função | Detalhe |
|---|---|
| **Inventário e postura dos buckets** | Buckets **públicos**, sem criptografia, compartilhados com outras contas ou replicados. |
| **Descoberta de dados sensíveis** | *Managed data identifiers* (CPF, cartão de crédito, passaporte, credenciais, dados de saúde, nomes, endereços) e **custom data identifiers** (regex + palavras-chave). |
| **Automated sensitive data discovery** | Amostragem contínua e econômica de todos os buckets. |
| **Jobs** | Varreduras completas sob demanda ou agendadas. |
| **Integrações** | Achados no Security Hub e EventBridge. |

- Teste gratuito de 30 dias. Cobrança por bucket monitorado e por GB inspecionado.

## ⚠️ Pegadinha

- Macie atua **só no S3**. "PII", "dados sensíveis", "LGPD/GDPR no S3" → Macie.

## ❓ Perguntas típicas

- "Encontrar dados pessoais em buckets S3." → Macie.

## 🔗 Documentação oficial

- [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
