# AWS Application Migration Service (AWS MGN)

> **Categoria:** Migração de servidores · **Domínio:** 1 (Rehost) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** migração **lift-and-shift (Rehost)** de servidores físicos, virtuais ou de outras nuvens para EC2, com mínima indisponibilidade.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Como funciona

1. Instala o **agente de replicação** no servidor de origem (Windows/Linux).
2. Replicação **contínua em nível de bloco** para uma *staging area* na AWS.
3. **Instâncias de teste** sem afetar a origem.
4. **Cutover**: lança as instâncias finais em minutos; a origem pode ser desligada.
5. Ações pós-lançamento automatizam ajustes (instalar agentes, converter licenças, modernizar).

## 🔄 Nome atual

- O serviço hoje se chama **AWS Transform MGN**. O exam guide e a lista de serviços ainda usam **AWS Application Migration Service** — é esse o nome que aparece na prova.

## Destaques

- Suporta qualquer aplicação/banco que rode no servidor; converte automaticamente para rodar em EC2.
- **Gratuito por 2.160 horas (90 dias de uso contínuo) por servidor de origem** (paga só os recursos de staging e as instâncias).
- Substitui o antigo CloudEndure Migration e o Server Migration Service (SMS).

## ⚠️ Não confundir

- **MGN** (servidores inteiros) × **DMS** (bancos de dados) × **Elastic Disaster Recovery** (mesma tecnologia, objetivo de DR contínuo).

## ❓ Perguntas típicas

- "Migrar servidores físicos e VMs para EC2 sem mudar nada, com pouca indisponibilidade." → Application Migration Service.
- "Ferramenta da estratégia Rehost." → Application Migration Service.

## 🔗 Documentação oficial

- [Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
