# Amazon Lightsail

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Você quer hospedar um site ou uma aplicação pequena e prefere começar com opções simples, em vez de montar muitos recursos separadamente.

**Como este serviço ajuda?** O Lightsail reúne recursos como servidores virtuais, armazenamento e rede em ofertas simplificadas. Ele facilita escolher uma configuração inicial e entender o pacote contratado.

**Exemplo do dia a dia:** Uma pessoa cria um pequeno site institucional numa instância Lightsail, usando uma imagem pronta ou instalando seu software.

**O que ele não resolve sozinho?** A simplicidade não elimina manutenção do software, segurança ou limites do plano. Quando a arquitetura exige muitas opções avançadas, serviços separados podem ser mais adequados.

**Primeiras palavras para entender:**

- **Instância:** servidor virtual.
- **Plano:** pacote de capacidade e recursos.
- **Imagem:** modelo de software usado para iniciar a máquina.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação simplificada · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)
>
> **Em uma frase:** servidores virtuais e serviços prontos com **preço mensal fixo e previsível**, para quem está começando.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Escolha uma oferta e um modelo de software compatíveis com seu site ou aplicação.

**Passo 2.** Crie o recurso e prepare o conteúdo, a conexão e o domínio quando necessário.

**Passo 3.** Mantenha o software protegido e acompanhe o consumo. O pacote simplifica escolhas, mas continua tendo limites e responsabilidades.

## 2. Recursos e opções, com significado

### Para que serve

Sites WordPress, lojas pequenas, blogs, ambientes de teste, aplicações simples.

Usuários com pouca experiência em AWS que querem previsibilidade de custo.

### O que oferece

**Instâncias**

**Detalhe:** Linux/Windows com blueprints prontos (WordPress, LAMP, Node.js, cPanel…).

**Planos (bundles)**

**Detalhe:** Preço mensal fixo que inclui vCPU, memória, SSD e **cota de transferência de dados**.

**Bancos gerenciados**

**Detalhe:** MySQL e PostgreSQL.

**Outros**

**Detalhe:** Load balancer, contêineres, armazenamento em objetos e em bloco, CDN, DNS, snapshots.

**Upgrade**

**Detalhe:** Snapshot pode ser exportado para EC2 quando a aplicação crescer.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

A simplicidade não elimina manutenção do software, segurança ou limites do plano. Quando a arquitetura exige muitas opções avançadas, serviços separados podem ser mais adequados.

### ⚠️ Pegadinhas e não confundir

"Preço fixo e previsível, simples" → **Lightsail**. "Escala automática gerenciada a partir do código" → **Elastic Beanstalk**. "Controle total" → **EC2**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Preço **mensal fixo** por plano (cobrado por hora até o teto mensal). Transferência acima da cota é cobrada.

## 5. Caso resolvido: ligando as peças

Uma pessoa cria um pequeno site institucional numa instância Lightsail, usando uma imagem pronta ou instalando seu software.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha uma oferta e um modelo de software compatíveis com seu site ou aplicação.
**Etapa 2:** Crie o recurso e prepare o conteúdo, a conexão e o domínio quando necessário.
**Etapa 3:** Mantenha o software protegido e acompanhe o consumo. O pacote simplifica escolhas, mas continua tendo limites e responsabilidades.

**Resultado e responsabilidade:** O Lightsail reúne recursos como servidores virtuais, armazenamento e rede em ofertas simplificadas. Ele facilita escolher uma configuração inicial e entender o pacote contratado.

**Recursos envolvidos:** Instâncias, discos, snapshots e recursos simplificados.

**Decisões que precisam ser tomadas:** Blueprint, bundle, rede e backups.

**Outra situação comentada:** Pequeno site com requisitos simples: Lightsail; requisitos complexos pedem avaliar EC2 e serviços especializados.

**Por que não concluir mais do que isso:** Não significa capacidade ilimitada ou proteção automática da aplicação

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Site WordPress simples com preço mensal fixo."

**Resposta curta:** Lightsail.

**Pergunta:** "Pequena empresa sem experiência quer um servidor com custo previsível."

**Resposta curta:** Lightsail.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
