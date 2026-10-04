# Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)

> **Categoria:** Migração / transferência offline e borda · **Domínio:** 3 · **Escopo:** dispositivo físico vinculado a uma região · **Tópico do guia:** [3.9 Outros armazenamentos](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) · [3.17 Migração](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** dispositivos físicos robustos para **mover grandes volumes de dados** quando a rede é lenta, cara ou inexistente, e para **computação na borda** desconectada.
>
> **Escopo oficial:** ⚪ Não listado (saiu da lista atual) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **HD gigante e blindado que a AWS manda pelo correio**: você copia os dados e devolve.

- ✅ **Escolha quando:** precisa mover **grandes volumes sem rede boa**, ou processar dados em **locais remotos**. (A família saiu da lista atual da prova.)
- 🚫 **Não é a resposta quando:** a transferência pode ser **online** → [DataSync](datasync-e-transfer-family.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "petabytes", "internet lenta", "local remoto sem conexão".
<!-- didatico:fim -->

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

## 🔗 Documentação oficial

- [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html)
