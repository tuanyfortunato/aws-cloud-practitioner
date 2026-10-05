# Amazon Cognito

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Seu aplicativo precisa que clientes criem contas, façam login e provem sua identidade sem você construir do zero todo esse mecanismo.

**Como este serviço ajuda?** Cognito oferece recursos de identidade para usuários de aplicações. User pools cuidam de cadastro e autenticação; identity pools podem fornecer credenciais AWS temporárias conforme a configuração.

**Exemplo do dia a dia:** Alunos fazem login no aplicativo da escola por um cadastro Cognito. Depois, a aplicação usa essa identidade para aplicar suas regras de acesso.

**O que ele não resolve sozinho?** Login válido não significa autorização para qualquer operação. A aplicação ainda precisa decidir quais dados e ações cada usuário pode acessar.

**Primeiras palavras para entender:**

- **Autenticação:** confirmar quem a pessoa é.
- **Autorização:** decidir o que ela pode fazer.
- **User pool:** diretório de usuários da aplicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / identidade de clientes (CIAM) · **Domínio:** 2 · **Escopo:** Regional · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** cadastro, login e controle de acesso para **usuários finais** de aplicações web e mobile.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Componentes

| Componente | O que faz |
|---|---|
| **User pools** | Diretório de usuários: **cadastro e login**, verificação de e-mail/telefone, recuperação de senha, **MFA**, **login social** (Google, Facebook, Apple, Amazon), SAML/OIDC, UI hospedada (*managed login*), tokens JWT. |
| **Identity pools** | Trocam uma identidade (user pool, social, SAML ou visitante) por **credenciais AWS temporárias** (via STS) para acessar S3, DynamoDB etc. direto do app. |

## Configurações

- Políticas de senha, MFA adaptativo e proteção contra credenciais comprometidas (*threat protection*), gatilhos Lambda (personalizar fluxos), integração com ALB e API Gateway para autenticação.
- Planos de recursos: Lite, Essentials e Plus.

## Cobrança

- Por **usuário ativo mensal (MAU)**, conforme o plano; identity pools sem custo próprio.

## ❓ Perguntas típicas

- "Permitir login com Google num app mobile." → Cognito.
- "App mobile precisa enviar fotos direto ao S3 com credenciais temporárias." → Cognito identity pool.
- "Cognito ou Identity Center para funcionários acessarem o console?" → Identity Center.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | User pools, app clients e identity pools |
| **O que você decide/configura?** | Métodos de login, federação, MFA e roles |
| **Em que ordem as coisas acontecem?** | User pool autentica; identity pool pode trocar identidades por credenciais AWS |
| **O que pode fazer, e em que condição?** | Permite login de consumidores e acesso autorizado a recursos |
| **O que não pode presumir?** | User pool e identity pool não são o mesmo recurso; login não concede toda ação AWS |

**Caso comentado:** App precisa login social e acesso limitado a recurso: combine capacidades conforme requisito.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
