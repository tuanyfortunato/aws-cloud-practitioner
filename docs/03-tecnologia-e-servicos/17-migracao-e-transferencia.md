# 3.17 Migração e transferência

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Migration Evaluator, Application Discovery Service e Migration Hub](../../servicos/migracao/discovery-migration-hub-e-evaluator.md) · [AWS Application Migration Service (AWS MGN)](../../servicos/migracao/application-migration-service.md) · [AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)](../../servicos/migracao/dms-e-sct.md) · [Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)](../../servicos/migracao/snow-family.md) · [AWS DataSync e AWS Transfer Family](../../servicos/migracao/datasync-e-transfer-family.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** **Migration Hub** e **Application Discovery Service** continuam no escopo, mas estão fechados a novos clientes desde 07/11/2025. **Transfer Family** está **fora do escopo**; Snow e DataSync não aparecem. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.16 Gestão e governança](16-gestao-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [3.18 Serviços menos conhecidos que podem aparecer](18-servicos-menos-conhecidos.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** As ferramentas de migração seguem a **ordem da mudança**: avaliar o custo e as dependências, acompanhar o progresso, migrar servidores e bancos e transferir dados.
>
> 🏠 **Analogia:** é uma **mudança de casa**: o **Migration Evaluator** faz o orçamento; o **Discovery Service** mede os móveis e vê o que depende do quê; o **Migration Hub** é a planilha de acompanhamento; o **MGN** é o caminhão que leva tudo como está; o **DMS** leva o banco com a loja aberta; o **SCT** traduz a estrutura de um banco para outro.

**Ao terminar este tópico, você deve saber:**

- [ ] Ligar cada ferramenta à **etapa** (avaliar, acompanhar, migrar, transferir).
- [ ] Diferenciar migração de banco **homogênea** (só DMS) de **heterogênea** (SCT + DMS).
- [ ] Diferenciar transferência **offline** (Snow) de **online** (DataSync, Transfer Family).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Homogênea** | mesmo motor de banco na origem e no destino (MySQL → MySQL). |
| **Heterogênea** | motores diferentes (Oracle → PostgreSQL). |
| **Schema** | a estrutura do banco: tabelas, colunas e relacionamentos. |

> 🎯 **Como não errar na prova:** "Dependências entre servidores" → **Application Discovery Service**. "Migrar VMs sem alterar" → **MGN**. "Banco sem parar o sistema" → **DMS**. "Oracle para PostgreSQL" → **SCT**. "Justificar custo" → **Migration Evaluator**.

## 📖 Conteúdo

As ferramentas seguem a ordem de uma migração: avaliar, planejar e migrar.

| Serviço | Etapa | O que faz |
| --- | --- | --- |
| Migration Evaluator | Avaliar | Monta o **caso de negócio**: estima o custo de rodar o ambiente atual na AWS (TCO) |
| AWS Application Discovery Service | Avaliar | Coleta dados dos servidores on-premises (configuração, uso, **dependências** entre aplicações), com ou sem agente |
| AWS Migration Hub | Acompanhar | **Painel único** para acompanhar o progresso das migrações em várias ferramentas |
| AWS Application Migration Service (MGN) | Migrar servidores | **Lift-and-shift (Rehost)**: replica servidores continuamente para a AWS e faz o corte com mínimo de indisponibilidade |
| AWS Database Migration Service (DMS) | Migrar bancos | Migra bancos com o **banco de origem funcionando** (replicação contínua), entre motores iguais ou diferentes |
| AWS Schema Conversion Tool (SCT) | Migrar bancos | **Converte o schema** e o código do banco entre motores diferentes (ex.: Oracle para Aurora PostgreSQL); usado junto com o DMS |
| Família AWS Snow | Transferir dados | Transferência **offline** de grandes volumes em dispositivo físico (ver [3.9](09-outros-armazenamentos.md)) |
| AWS DataSync | Transferir dados | Transferência **online** e automatizada de arquivos para S3, EFS ou FSx (ver [3.9](09-outros-armazenamentos.md)) |
| AWS Transfer Family | Transferir dados | SFTP, FTPS e FTP gerenciados direto para S3 ou EFS |

- **Migração homogênea** (MySQL → RDS MySQL): só o DMS. **Heterogênea** (Oracle → Aurora): SCT para converter o schema e DMS para mover os dados.
- **Cai na prova:** "descobrir dependências entre os servidores antes de migrar" = Application Discovery Service; "migrar VMs sem alterar" = Application Migration Service; "migrar banco sem parar o sistema" = DMS; "converter Oracle para PostgreSQL" = SCT; "justificar o custo da migração para a diretoria" = Migration Evaluator.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Levantar servidores e dependências antes de migrar." → Application Discovery Service.
- "Estimar quanto a empresa vai economizar ao migrar." → Migration Evaluator.
- "Acompanhar todas as migrações num painel central." → Migration Hub.
- "Migrar servidores físicos e VMs para EC2 com pouca indisponibilidade." → Application Migration Service.
- "Migrar um banco sem desligar a aplicação." → DMS.
- "Converter um banco Oracle para Aurora PostgreSQL." → SCT + DMS.
- "Transferir arquivos online de forma automatizada para o S3." → DataSync.
- "Parceiros enviam arquivos via SFTP para o S3." → Transfer Family.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.16 Gestão e governança](16-gestao-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [3.18 Serviços menos conhecidos que podem aparecer](18-servicos-menos-conhecidos.md) ➡️
