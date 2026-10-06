<!-- autoral -->

# AWS Elastic Disaster Recovery (AWS DRS)

> **Categoria:** Recuperação de desastres · **Domínio:** 1 e 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** replica continuamente servidores locais ou na nuvem para uma área de preparação barata na AWS e, num desastre, lança instâncias de recuperação em minutos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) · [1.3 Conceitos de arquitetura](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Se o datacenter da secretaria pegar fogo, a rede precisa voltar a funcionar em minutos, não em dias. Backup guarda cópias; o **Elastic Disaster Recovery** mantém um ambiente pronto para assumir, usando armazenamento barato e o mínimo de computação enquanto nada acontece.

1. Instala-se o agente nos servidores de origem, que passam a replicar os dados para uma sub-rede de preparação na Região escolhida.
2. A equipe faz testes de recuperação periódicos, sem interromper a produção.
3. Num desastre, o DRS lança instâncias de recuperação na AWS em minutos, com o estado mais recente ou de um momento anterior.
4. Resolvido o problema, os dados podem voltar para o local de origem (*failback*).

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Backup](aws-backup.md) | Centraliza cópias de segurança, sem ambiente pronto | "Plano de backup", "retenção" |
| [AWS Application Migration Service](../migracao/application-migration-service.md) | Mesma ideia de replicação, mas para migrar de vez | "Migrar servidores" |
| [Amazon EBS (snapshots)](ebs.md) | Cópias de um volume | "Snapshot do volume" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
