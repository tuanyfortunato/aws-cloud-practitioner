<!-- autoral -->

# AWS Systems Manager

> **Categoria:** Gerenciamento e operações · **Domínio:** 3 · **Abrangência:** Regional (EC2, servidores locais e outras nuvens) · **Ficha:** núcleo
>
> **Em uma frase:** permite ver e operar de forma central muitas máquinas, em várias contas e Regiões: aplicar patches, rodar comandos, conectar-se sem abrir portas e guardar configurações.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A rede de escolas tem cinquenta instâncias EC2 e alguns servidores ainda no datacenter da secretaria. Uma auditoria pede que todas recebam a atualização de segurança até o fim do dia. Entrar em cada uma por SSH levaria o dia todo e exigiria deixar a porta 22 aberta.

O **Systems Manager** opera as máquinas em grupo. Cada uma, chamada de **nó**, roda o **SSM Agent** e conversa com o serviço. A partir daí, o **Patch Manager** aplica atualizações em todas de uma vez, o **Run Command** executa um comando em muitas máquinas, o **Session Manager** abre uma sessão de terminal sem porta de entrada aberta nem bastion, e o **Parameter Store** guarda configurações e segredos usados pelas aplicações.

O limite: só gerencia o nó que tem o agente funcionando e conversando com o serviço. E ele aplica os patches, mas não descobre sozinho quais falhas de segurança existem; quem encontra as CVEs é o [Inspector](../seguranca/inspector.md).

## Como funciona

1. Cada nó roda o SSM Agent, que precisa conseguir falar com o Systems Manager; aí o nó passa a ser gerenciado.
2. Os nós aparecem no console, com inventário do software instalado.
3. Você escolhe a ferramenta: aplicar patches, rodar comandos, abrir sessões ou executar automações.
4. As tarefas podem ser agendadas em janelas de manutenção.

## Opções principais

| Ferramenta | O que faz | Exemplo na escola |
|---|---|---|
| Session Manager | Terminal na máquina sem porta de entrada aberta | Acessar o servidor com a porta SSH fechada |
| Patch Manager | Aplica patches em grande escala | Atualização de segurança em todas as instâncias |
| Run Command | Executa comandos em muitas máquinas | Reiniciar um serviço em todos os servidores |
| Parameter Store | Guarda configurações e segredos | Endereço do banco usado pela aplicação |
| Automation | Executa rotinas de administração | Remediação acionada por uma regra do Config |
| Maintenance Windows | Agenda as tarefas | Patches toda madrugada de domingo |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Requisito em cada nó | SSM Agent instalado e com acesso ao serviço | 06/10/2026 |
| Session Manager, Patch Manager e Run Command no EC2 | Sem custo adicional | 06/10/2026 |
| Parameter Store, nível padrão | Sem custo adicional, até 10.000 parâmetros de 4 KB | 06/10/2026 |

## Como é cobrado

A maior parte das ferramentas não tem custo adicional para instâncias EC2. São cobrados, por exemplo, os parâmetros avançados do Parameter Store, algumas automações e o uso em servidores locais e em outras nuvens.

## Não confundir com

| Serviço | Diferença para o Systems Manager | Pista no enunciado |
|---|---|---|
| [Amazon Inspector](../seguranca/inspector.md) | Encontra as vulnerabilidades que o Patch Manager corrige | "CVE", "vulnerabilidade" |
| [AWS CloudFormation](cloudformation.md) | Cria a infraestrutura a partir de um modelo | "Infraestrutura como código" |
| [AWS Secrets Manager](../seguranca/secrets-manager-e-parameter-store.md) | Guarda segredos com rotação automática | "Rotacionar a senha do banco" |
| [AWS Config](config.md) | Avalia configurações; usa automações do Systems Manager para corrigir | "Recurso fora da regra" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
- [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
- [Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html)
- [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [Preços do AWS Systems Manager](https://aws.amazon.com/systems-manager/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
