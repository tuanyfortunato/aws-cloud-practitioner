# Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Grandes quantidades de dados podem levar muito tempo para viajar por uma conexão limitada, e alguns locais quase não têm rede.

**Como este serviço ajuda?** A família Snow foi associada a dispositivos físicos para transferência e processamento local. Esta ficha explica esses conceitos e as restrições das ofertas citadas.

**Exemplo do dia a dia:** Em um cenário histórico de transferência offline, dados eram copiados para um dispositivo e transportados até a AWS, em vez de enviados todos pela internet.

**O que ele não resolve sozinho?** Não trate esse exemplo como uma oferta atual disponível a qualquer cliente. Há produtos encerrados ou restritos; confira o status e as alternativas indicadas na ficha.

**Primeiras palavras para entender:**

- **Offline:** sem depender de conexão contínua.
- **Borda:** processamento no local dos dados.
- **Dispositivo:** equipamento físico usado para executar ou armazenar.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Migração / transferência offline e borda · **Domínio:** 3 · **Escopo:** dispositivo físico vinculado a uma região · **Tópico do guia:** [3.9 Outros armazenamentos](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) · [3.17 Migração](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** dispositivos físicos robustos para **mover grandes volumes de dados** quando a rede é lenta, cara ou inexistente, e para **computação na borda** desconectada.
>
> **Escopo oficial:** ⚪ Não listado (saiu da lista atual) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Dispositivos

| Dispositivo | Capacidade | Uso | Status 🔄 |
|---|---|---|---|
| **Snowball Edge Storage Optimized** | **210 TB** utilizáveis ✔️ (antes 80 TB) | Migração de dezenas a centenas de TB / petabytes (vários dispositivos) | Só para **clientes existentes** desde 07/11/2025 |
| **Snowball Edge Compute Optimized** | Até 104 vCPUs ✔️ | Computação na borda (navios, minas, campo militar) | Só clientes existentes |
| **Snowcone** | 8–14 TB, pequeno e leve | Borda e transferência pequena | Sem novos pedidos desde 12/11/2024; suporte encerrado em 12/11/2025 |
| **Snowmobile** | Até **100 PB** (caminhão) | Exabytes | **Encerrado em 14/03/2024** ✔️ |

> 🔄 ✔️ A página do produto anuncia o **fim do suporte comercial dos Snowball Edge Storage Optimized e Compute Optimized em 31/12/2026** nas regiões comerciais (exceção para clientes GovCloud/ADC com jobs ativos).

## Como funciona (Snowball)

1. Pedido no console → AWS envia o dispositivo.
2. Copia os dados localmente (cliente OpsHub ou S3 adapter); dados **criptografados** (KMS, 256 bits); dispositivo resistente a violação, com **E Ink** de envio.
3. Devolve à AWS → dados importados no **S3** → dispositivo é **apagado** seguindo padrões NIST.

## Alternativas atuais para novos clientes

- **AWS DataSync** (online) — [ficha](datasync-e-transfer-family.md).
- **AWS Data Transfer Terminal**: locais físicos seguros da AWS onde você leva seus próprios dispositivos de armazenamento para upload em alta velocidade.
- **Parceiros** de transferência; **Outposts** para computação de borda.

## Regra prática

- Se transferir pela rede levaria **semanas**, use Snow. Ex.: 100 TB num link de 100 Mbps ≈ 100+ dias.

## ⚠️ Na prova

- 🔄 A família Snow **não aparece** na lista atual de serviços no escopo (verificação de 04/10/2026). O Snowmobile não tem página oficial de aposentadoria localizada (só imprensa citando a AWS).

- Questões antigas citam Snowball Edge/Snowmobile (a família saiu da lista atual): "migrar petabytes com banda limitada" → **Snowball Edge**; "exabytes / 100 PB" → **Snowmobile** (questões antigas). "Processar dados num navio sem conexão" → família Snow (borda).

## ❓ Perguntas típicas

- "Migrar 500 TB de um datacenter com internet lenta." → Snowball Edge.
- "Processar dados num local remoto sem conexão." → Snowball Edge Compute Optimized.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Dispositivos físicos, jobs de transferência e ferramentas locais |
| **O que você decide/configura?** | Elegibilidade/disponibilidade, volume e procedimento de transferência |
| **Em que ordem as coisas acontecem?** | Fluxo histórico copiava dados localmente para dispositivo e importava na AWS |
| **O que pode fazer, e em que condição?** | Resolve transferência física quando oferta está disponível |
| **O que não pode presumir?** | Não listado não significa exclusão formal; não recomende contratação ignorando restrições atuais |

**Caso comentado:** Pouca banda e muitos dados: avalie transferência física disponível; para novos clientes consulte alternativas atuais da ficha.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html)
