# Amazon ECR (Elastic Container Registry)

> **Categoria:** Computação / Contêineres · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** registro gerenciado para guardar, versionar e distribuir imagens de contêiner (Docker/OCI).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é a **estante onde ficam guardadas as imagens dos seus contêineres** — um Docker Hub privado dentro da AWS.

- ✅ **Escolha quando:** precisa guardar e versionar **imagens Docker privadas** para ECS, EKS ou Lambda.
- 🚫 **Não é a resposta quando:** quer guardar **arquivos comuns** → [S3](../armazenamento/s3.md); quer guardar **pacotes** (npm, Maven) → CodeArtifact, na ficha de [CI/CD](../desenvolvimento/code-services.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "imagens Docker privadas", "registro de contêineres", "varrer imagens em busca de vulnerabilidades".
<!-- didatico:fim -->

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Repositórios privados** | Controlados por IAM e políticas de repositório. |
| **ECR Public / Public Gallery** | Repositórios públicos para distribuir imagens. |
| **Image scanning** | *Basic* (CVEs do SO) ou *Enhanced* (contínuo, SO + pacotes de linguagem, via **Amazon Inspector**). |
| **Tag immutability** | Impede sobrescrever uma tag (ex.: `v1.2`). |
| **Lifecycle policies** | Apagam imagens antigas automaticamente (ex.: manter só as 10 últimas). |
| **Replicação** | Entre regiões e contas. |
| **Pull through cache** | Faz cache de imagens de registros públicos (Docker Hub, Quay, GitHub). |
| **Criptografia** | Em repouso (SSE-S3 ou KMS) e em trânsito (HTTPS). |

## Cobrança

- Por GB armazenado por mês + transferência de saída. Enhanced scanning é cobrado pelo Inspector.

## Segurança e responsabilidade compartilhada

- **AWS:** disponibilidade e durabilidade do registro (armazenado no S3).
- **Cliente:** quem pode fazer push/pull, conteúdo e vulnerabilidades das imagens.

## ❓ Perguntas típicas

- "Onde guardar imagens Docker privadas na AWS?" → ECR.
- "Varrer imagens de contêiner em busca de vulnerabilidades." → ECR scanning / Amazon Inspector.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Repositório, imagens, tags/digests e políticas |
| **O que você decide/configura?** | Acesso, retenção/lifecycle e opções de varredura |
| **Em que ordem as coisas acontecem?** | Faça push da imagem e autorize o ambiente de execução a fazer pull |
| **O que pode fazer, e em que condição?** | Distribui artefatos de container e pode integrar varredura |
| **O que não pode presumir?** | Guardar imagem não inicia container; imagem pode conter bibliotecas vulneráveis |

**Caso comentado:** Versionar imagem de API: ECR; iniciar API: serviço de execução, como ECS.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
