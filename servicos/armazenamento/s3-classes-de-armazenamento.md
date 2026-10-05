# Classes de armazenamento do S3 (incluindo S3 Glacier)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Nem todo arquivo precisa do mesmo tipo de acesso. Uma foto usada todo dia e um documento guardado por anos podem exigir custos e tempos de recuperação diferentes.

**Como este serviço ajuda?** As classes do S3 oferecem opções de armazenamento conforme frequência de acesso, disponibilidade e recuperação. Você escolhe a classe ou configura regras compatíveis para mudar objetos ao longo do tempo.

**Exemplo do dia a dia:** A escola mantém materiais atuais em uma classe de acesso frequente e avalia uma classe de arquivo para documentos que quase nunca consulta.

**O que ele não resolve sozinho?** Armazenamento mais barato por volume pode ter cobrança de recuperação, prazo mínimo e espera para obter o conteúdo. A classe deve atender ao tempo em que você precisa dos dados.

**Primeiras palavras para entender:**

- **Classe:** modalidade de armazenamento do objeto.
- **Recuperação:** obter dados arquivados.
- **Ciclo de vida:** regras para transições e outras ações ao longo do tempo.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Armazenamento de objetos · **Domínio:** 3 e 4 (custos) · **Escopo:** por objeto · **Tópico do guia:** [3.8 Amazon S3](../../docs/03-tecnologia-e-servicos/08-s3.md)
>
> **Em uma frase:** cada classe troca custo de armazenamento por custo/tempo de acesso — escolha pelo padrão de acesso.
>
> **Escopo oficial:** ✅ No escopo (S3 e S3 Glacier) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Tabela completa

| Classe | Uso | Disponibilidade (design) | AZs | Duração mínima | Tamanho mínimo cobrado | Recuperação | Taxa de recuperação |
|---|---|---|---|---|---|---|---|
| **S3 Standard** | Acesso frequente | 99,99% | ≥3 | — | — | ms | Não |
| **S3 Intelligent-Tiering** | Acesso desconhecido/mutável | 99,9% | ≥3 | — | (objetos < 128 KB não são monitorados) | ms (camadas de arquivo opcionais: horas) | Não (cobra monitoramento por objeto) |
| **S3 Express One Zone** | Latência mínima, alto desempenho | 99,95% | **1** | 1 hora | — | ms de um dígito | Não |
| **S3 Standard-IA** | Pouco acesso, mas rápido | 99,9% | ≥3 | **30 dias** | 128 KB | ms | **Sim** |
| **S3 One Zone-IA** | Pouco acesso, **dado recriável** | 99,5% | **1** | **30 dias** | 128 KB | ms | **Sim** |
| **S3 Glacier Instant Retrieval** | Arquivo acessado ~1x por trimestre | 99,9% | ≥3 | **90 dias** | 128 KB | **ms** | Sim |
| **S3 Glacier Flexible Retrieval** | Arquivo sem pressa | 99,99% | ≥3 | **90 dias** | 40 KB (metadados) | Expedited **1–5 min** para objetos < 250 MB ✔️ · Standard **3–5 h** · Bulk **5–12 h** (grátis) | Sim (Bulk grátis) |
| **S3 Glacier Deep Archive** | Retenção de longo prazo (7–10 anos) | 99,99% | ≥3 | **180 dias** | 40 KB (metadados) | Standard **até 12 h** · Bulk **até 48 h** · **sem Expedited** | Sim |

- 📌 Todas têm durabilidade de **11 noves**.
- 📌 Classe padrão do upload: **S3 Standard**.
- Objetos apagados/movidos antes da duração mínima pagam o restante do período (*early deletion*).

## SLA × disponibilidade de projeto (oficial)

| Classe | Disponibilidade de projeto | SLA |
|---|---|---|
| Standard | 99,99% | 99,9% |
| Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier Instant | 99,9% / 99,9% / 99,5% / 99,9% | 99% |
| Express One Zone | 99,95% | 99,9% |
| Glacier Flexible, Deep Archive | 99,99% | 99,9% |

## Intelligent-Tiering por dentro

| Camada | Quando o objeto vai para lá |
|---|---|
| Frequent Access | Ao entrar |
| Infrequent Access | Após **30 dias** sem acesso |
| Archive Instant Access | Após **90 dias** sem acesso |
| Archive Access (opcional) | Após 90+ dias (configurável) |
| Deep Archive Access (opcional) | Após 180+ dias (configurável) |

- Um acesso traz o objeto de volta para Frequent Access. ✔️ Cobra uma taxa mensal de **monitoramento e automação por objeto**; recuperações Standard e Bulk são **gratuitas**, mas a recuperação **Expedited** da camada opcional Archive Access é **cobrada**. Objetos < 128 KB não são monitorados (ficam em Frequent Access, sem taxa de monitoramento).

## Lifecycle: transições típicas

```
Standard ──30d──▶ Standard-IA ──60d──▶ Glacier Instant/Flexible ──180d──▶ Deep Archive ──(expiração)──▶ apagado
```

- Regras podem filtrar por prefixo ou tag e também apagar **versões antigas** e **uploads multipart incompletos**.

## Restaurar do Glacier

- Objetos em Flexible Retrieval/Deep Archive precisam de **restore** (cria uma cópia temporária por N dias) antes de serem lidos.
- 🔄 O **Amazon Glacier** original (serviço de *vaults*, com Glacier Vault Lock) é diferente das classes S3 Glacier e está **fechado a novos clientes** desde 07/11/2025. Hoje se usa o Glacier pelas classes do S3.
- O Express One Zone usa *directory buckets* e **não** suporta transições de Lifecycle.

## ⚠️ Pegadinhas

- "Acesso imprevisível" → **Intelligent-Tiering**.
- "Raro, mas precisa abrir **na hora**" → **Glacier Instant Retrieval** (não Flexible).
- "Pode ser regenerado" / "uma AZ basta" → **One Zone-IA**.
- "Compliance 7 anos, menor custo, até 48 h" → **Deep Archive**.
- "Menor latência possível" → **Express One Zone**.
- Deep Archive **não tem Expedited**.

## ❓ Perguntas típicas

- "Classe mais barata para arquivamento de longo prazo?" → Glacier Deep Archive.
- "Qual classe guarda dados em uma única AZ?" → One Zone-IA (ou Express One Zone).
- "Recuperar arquivo do Glacier em minutos." → Glacier Flexible Retrieval com Expedited.
- "Duração mínima do Deep Archive?" → 180 dias.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Classes/camadas de objeto, regras lifecycle e solicitações de restore |
| **O que você decide/configura?** | Frequência, prazo de acesso, permanência mínima e tolerância a uma AZ |
| **Em que ordem as coisas acontecem?** | Escolha classe ou lifecycle; quando necessário, restaure objeto arquivado antes do uso |
| **O que pode fazer, e em que condição?** | Reduz custo de dados pouco acessados conforme condições da classe |
| **O que não pode presumir?** | Glacier Instant Retrieval não requer espera de restore como Flexible/Deep Archive; uma AZ reduz resiliência a perda da AZ |

**Caso comentado:** Arquivo raro que deve abrir imediatamente: Glacier Instant Retrieval; espera de horas permite outras classes.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Classes de armazenamento](https://aws.amazon.com/s3/storage-classes/)
- [Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)
