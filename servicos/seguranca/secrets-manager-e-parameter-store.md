# AWS Secrets Manager e Systems Manager Parameter Store

> **Categoria:** Segurança / gestão de segredos · **Domínio:** 2 · **Escopo:** Regional · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** guardam segredos e configurações fora do código, criptografados com KMS — o Secrets Manager também os **rotaciona automaticamente**.
>
> **Escopo oficial:** ✅ No escopo (Parameter Store como parte do Systems Manager) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Comparação

| | **Secrets Manager** | **Parameter Store** |
|---|---|---|
| Foco | Segredos (senhas de banco, chaves de API, tokens) | Configurações e segredos simples |
| **Rotação automática** | ✅ **Nativa** (RDS, Aurora, Redshift, DocumentDB) ou via Lambda; *managed rotation* | ❌ (só com automação própria) |
| Criptografia | Sempre (KMS) | Opcional (`SecureString` com KMS) |
| Replicação entre regiões | ✅ | ❌ |
| Versionamento | Estágios `AWSCURRENT` / `AWSPREVIOUS` | Histórico de versões |
| Tamanho | Até 64 KB 🧊 | Standard 4 KB / Advanced 8 KB 🧊 |
| Hierarquia | — | Sim (`/app/prod/db-url`) |
| Custo | **Pago** por segredo/mês + chamadas de API | **Standard grátis**; Advanced pago |
| Integração | RDS gera e guarda a senha mestre no Secrets Manager | CloudFormation, ECS, Lambda, EC2 |

## ⚠️ Pegadinhas

- "Rotação automática" → **Secrets Manager**. "Guardar configuração barata/grátis" → **Parameter Store**.
- Nunca guarde access keys/senhas no código, em variáveis de ambiente em texto ou no user data.

## ❓ Perguntas típicas

- "Onde guardar a senha do banco com rotação automática?" → Secrets Manager.
- "Guardar URLs e flags de configuração por ambiente sem custo." → Parameter Store.

## 🔗 Documentação oficial

- [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) · [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
