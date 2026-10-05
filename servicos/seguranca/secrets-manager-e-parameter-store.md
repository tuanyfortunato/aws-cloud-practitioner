# AWS Secrets Manager e Systems Manager Parameter Store

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A aplicação precisa de senhas e configurações. Colocar esses valores no código dificulta protegê-los e alterá-los sem publicar uma nova versão.

**Como este serviço ajuda?** Secrets Manager guarda segredos com recursos como rotação compatível. Parameter Store organiza parâmetros de configuração, inclusive valores protegidos conforme a modalidade.

**Exemplo do dia a dia:** O sistema lê a senha do banco por um acesso autorizado ao serviço, em vez de manter essa senha escrita no código enviado ao repositório.

**O que ele não resolve sozinho?** Guardar um segredo não autoriza qualquer programa a lê-lo. Rotação também não funciona para todo sistema sem configuração e integração.

**Primeiras palavras para entender:**

- **Segredo:** valor sensível, como uma senha.
- **Parâmetro:** valor de configuração.
- **Rotação:** troca periódica de um segredo.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

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
| Tamanho | Até 64 KB (65.536 bytes) 🧊 | Standard 4 KB (até 10.000 parâmetros, grátis) / Advanced 8 KB (até 100.000, pago) 🧊 |
| Hierarquia | — | Sim (`/app/prod/db-url`) |
| Custo | **Pago** por segredo/mês + chamadas de API | **Standard grátis**; Advanced pago |
| Integração | RDS gera e guarda a senha mestre no Secrets Manager | CloudFormation, ECS, Lambda, EC2 |

## ⚠️ Pegadinhas

- "Rotação automática" → **Secrets Manager**. "Guardar configuração barata/grátis" → **Parameter Store**.
- Nunca guarde access keys/senhas no código, em variáveis de ambiente em texto ou no user data.

## ❓ Perguntas típicas

- "Onde guardar a senha do banco com rotação automática?" → Secrets Manager.
- "Guardar URLs e flags de configuração por ambiente sem custo." → Parameter Store.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Secrets e parâmetros; versões e chaves de criptografia quando aplicável |
| **O que você decide/configura?** | Acesso, valor, rotação e integração |
| **Em que ordem as coisas acontecem?** | Aplicação busca valor com identidade autorizada; rotação depende de configuração suportada |
| **O que pode fazer, e em que condição?** | Separa segredo/configuração do código |
| **O que não pode presumir?** | Não basta criar segredo: aplicação precisa usá-lo; rotação não muda magicamente sistemas sem integração |

**Caso comentado:** Senha de banco com rotação: Secrets Manager; parâmetros comuns: avalie Parameter Store.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) · [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
