# AWS Backup

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa tem dados em vários serviços e precisa organizar cópias de segurança, prazos de retenção e recuperação sem administrar tudo de forma isolada.

**Como este serviço ajuda?** AWS Backup centraliza políticas e operações de backup para recursos compatíveis. Você define o que copiar, quando copiar e por quanto tempo manter as cópias.

**Exemplo do dia a dia:** A escola define um plano que protege recursos compatíveis do sistema de matrícula e mantém pontos de recuperação por um período determinado.

**O que ele não resolve sozinho?** Ter backup não mantém automaticamente uma aplicação disponível durante uma falha. Também é preciso planejar e testar a restauração; a cobertura depende do recurso e das opções usadas.

**Primeiras palavras para entender:**

- **Backup:** cópia de segurança.
- **Retenção:** tempo de conservação.
- **Ponto de recuperação:** cópia que pode ser usada numa restauração.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Armazenamento / Proteção de dados · **Domínio:** 3 · **Escopo:** Regional (cópias entre regiões e contas) · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** centraliza e automatiza backups de vários serviços AWS com políticas, num só lugar.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Selecione recursos compatíveis e defina periodicidade, destinos e retenção das cópias.

**Passo 2.** Atribua os recursos ao plano. O serviço executa operações conforme a agenda e as permissões.

**Passo 3.** Teste a restauração e confira se os dados recuperados servem à aplicação. Sucesso de cópia e sucesso de recuperação são verificações diferentes.

## 2. Recursos e opções, com significado

### Recursos suportados (exemplos)

EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, S3, DocumentDB, Neptune, Redshift, Storage Gateway (volumes), VMware on-premises, entre outros.

### Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Backup plan** | Frequência (cron), janela, **retenção**, transição para *cold storage*, cópia para outra região/conta. |
| **Resource assignment** | Quais recursos entram no plano (por tag, ID ou tipo). |
| **Backup vault** | Contêiner criptografado (KMS) onde ficam os *recovery points*. |
| **Vault Lock** | **WORM** para backups: ninguém (nem o root) apaga antes do prazo — modo compliance. |
| **Logically air-gapped vault** | Vault isolado e compartilhável para recuperação após ransomware. |
| **Cross-region / cross-account copy** | DR e isolamento. |
| **Backup policies (Organizations)** | Aplicam planos em todas as contas da organização. |
| **Backup Audit Manager** | Relatórios de conformidade dos backups (frameworks e controles). |
| **Restore testing** | Testes automáticos de restauração. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ter backup não mantém automaticamente uma aplicação disponível durante uma falha. Também é preciso planejar e testar a restauração; a cobertura depende do recurso e das opções usadas.

### ⚠️ Pegadinhas e não confundir

**AWS Backup** (centraliza políticas) × snapshots manuais/DLM (por serviço).

**AWS Backup** × **Elastic Disaster Recovery**: backup com RPO de horas × replicação contínua com recuperação em minutos.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

GB-mês armazenado por tipo de recurso (warm/cold), restauração, cópias entre regiões.

## 5. Caso resolvido: ligando as peças

A escola define um plano que protege recursos compatíveis do sistema de matrícula e mantém pontos de recuperação por um período determinado.

**Aplicando a sequência à situação:**

**Etapa 1:** Selecione recursos compatíveis e defina periodicidade, destinos e retenção das cópias.
**Etapa 2:** Atribua os recursos ao plano. O serviço executa operações conforme a agenda e as permissões.
**Etapa 3:** Teste a restauração e confira se os dados recuperados servem à aplicação. Sucesso de cópia e sucesso de recuperação são verificações diferentes.

**Resultado e responsabilidade:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis. Você define o que copiar, quando copiar e por quanto tempo manter as cópias.

**Recursos envolvidos:** Planos, seleções de recursos, vaults e recovery points.

**Decisões que precisam ser tomadas:** Agenda, retenção, cópias, permissões e recursos elegíveis.

**Outra situação comentada:** Políticas comuns de retenção entre serviços: AWS Backup, com seleção e proteção configuradas.

**Por que não concluir mais do que isso:** Não inclui automaticamente todo recurso e não substitui disponibilidade ou teste de recuperação

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Centralizar backups de vários serviços com políticas."

**Resposta curta:** AWS Backup.

**Pergunta:** "Impedir que backups sejam apagados, nem pelo administrador."

**Resposta curta:** Backup Vault Lock.

**Pergunta:** "Aplicar a mesma política de backup em todas as contas."

**Resposta curta:** Backup policies no Organizations.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
