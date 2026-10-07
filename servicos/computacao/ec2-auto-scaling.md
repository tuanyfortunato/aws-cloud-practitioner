<!-- autoral -->

# Amazon EC2 Auto Scaling

> **Categoria:** Computação · **Domínio:** 1 (elasticidade) e 3 · **Abrangência:** Regional; o grupo pode usar várias zonas de disponibilidade · **Ficha:** núcleo
>
> **Em uma frase:** aumenta e reduz automaticamente o número de instâncias EC2 para acompanhar a demanda e substitui as que falham.
>
> **Escopo oficial:** ✅ No escopo (AWS Auto Scaling) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.4 Escalabilidade e balanceamento de carga](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) · base em [1.3 Conceitos de arquitetura](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

Na primeira semana de janeiro, o sistema de matrícula recebe dez vezes mais acessos que no resto do ano. Criar instâncias à mão em dezembro e apagá-las em fevereiro depende de alguém lembrar, e uma instância que trava de madrugada fica fora até alguém notar.

O EC2 Auto Scaling resolve o problema da **capacidade**: ele mantém um **grupo do Auto Scaling** com o número certo de instâncias em cada momento, criando instâncias quando a carga sobe e encerrando quando cai. Essa é a **elasticidade** da [aula 1.3](../../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md). O grupo também verifica a saúde das instâncias e substitui as que falham, e pode espalhá-las por várias zonas de disponibilidade.

O limite: o Auto Scaling cria e encerra instâncias, mas não distribui os acessos entre elas; isso é do [Elastic Load Balancing](elastic-load-balancing.md). E a aplicação precisa funcionar em várias cópias, sem guardar a sessão do usuário no disco de uma instância.

## Como funciona

1. Um **modelo de execução** (*launch template*) diz como criar cada instância: AMI, tipo de instância e demais configurações.
2. O grupo tem três números: **capacidade mínima**, **máxima** e **desejada**. O serviço cria ou encerra instâncias até chegar à desejada, sem sair do intervalo.
3. Uma **política de escalonamento** muda a capacidade desejada: por horário, por uma métrica ou por previsão.
4. As **verificações de saúde** encontram instâncias com defeito, e o grupo as substitui.
5. Com um balanceador ligado ao grupo, cada instância nova é registrada nele, e cada instância encerrada sai dele.

## Opções principais

| Forma de escalar | Como funciona | Exemplo |
|---|---|---|
| Manual | Alguém muda a capacidade desejada | Ajuste pontual |
| Programada (*scheduled*) | Ações em horários definidos | Aumentar no dia 2 de janeiro e reduzir no dia 15 |
| Rastreamento de destino (*target tracking*) | Mantém uma métrica num valor, como um termostato | Uso médio de processador em 50% |
| Em etapas (*step scaling*) | Ajustes que variam com o tamanho do desvio medido por um alarme | +2 instâncias acima de 70%, +4 acima de 90% |
| Preditiva (*predictive*) | Analisa o histórico e cria capacidade antes da carga prevista | Picos diários ou semanais que se repetem |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Cobrança própria do EC2 Auto Scaling | Nenhuma | 06/10/2026 |

## Como é cobrado

O EC2 Auto Scaling não tem cobrança adicional: você paga pelas instâncias que o grupo cria e pelos demais recursos usados, como o monitoramento do CloudWatch. Por isso ele também economiza: no resto do ano, o grupo encolhe até a capacidade mínima, e a escola não paga por instâncias paradas esperando janeiro.

## Não confundir com

| Serviço | Diferença para o EC2 Auto Scaling | Pista no enunciado |
|---|---|---|
| [Elastic Load Balancing](elastic-load-balancing.md) | Distribui os acessos entre as instâncias que existem; não cria capacidade | "Distribuir o tráfego", "um único ponto de acesso" |
| Escalar verticalmente | Trocar a instância por uma maior; o Auto Scaling escala horizontalmente, mudando a quantidade | "Aumentar o tamanho da instância" |
| [Amazon EC2](ec2.md) | Uma instância sozinha não acompanha a demanda nem se substitui quando falha | "Pico de acessos", "substituir instâncias com defeito" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [Escalar o grupo](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html)
- [Escalonamento programado](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)
- [Rastreamento de destino](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)
- [Escalonamento preditivo](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)
- [Verificações de saúde](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
