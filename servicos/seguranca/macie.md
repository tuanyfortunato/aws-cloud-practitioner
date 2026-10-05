# Amazon Macie

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa guarda muitos arquivos no S3 e precisa localizar possíveis dados sensíveis, como informações pessoais, sem abrir cada arquivo manualmente.

**Como este serviço ajuda?** Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.

**Exemplo do dia a dia:** A escola avalia um bucket de documentos para identificar arquivos que podem conter informações pessoais dos alunos.

**O que ele não resolve sozinho?** Ele não anonimiza automaticamente os arquivos nem examina todos os bancos e serviços AWS. Resultados precisam ser avaliados e ações de proteção planejadas.

**Primeiras palavras para entender:**

- **Dado sensível:** informação que exige proteção especial.
- **Classificação:** identificação do tipo de conteúdo.
- **Bucket:** recipiente de objetos no S3.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Inventário de buckets, jobs, identificadores e findings |
| **O que você decide/configura?** | Buckets, escopo, formatos e identificadores suportados |
| **Em que ordem as coisas acontecem?** | Inspeciona dados elegíveis no S3 e reporta dados sensíveis/postura |
| **O que pode fazer, e em que condição?** | Pode encontrar padrões de informação pessoal ou segredos |
| **O que não pode presumir?** | Não varre genericamente RDS/EBS e não apaga conteúdo sensível sozinho |

**Caso comentado:** Encontrar dados pessoais em documentos S3: Macie; confirme elegibilidade do formato e permissões.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
