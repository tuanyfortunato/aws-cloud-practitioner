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

## Para que serve

- Sites WordPress, lojas pequenas, blogs, ambientes de teste, aplicações simples.
- Usuários com pouca experiência em AWS que querem previsibilidade de custo.

## O que oferece

| Recurso | Detalhe |
|---|---|
| **Instâncias** | Linux/Windows com blueprints prontos (WordPress, LAMP, Node.js, cPanel…). |
| **Planos (bundles)** | Preço mensal fixo que inclui vCPU, memória, SSD e **cota de transferência de dados**. |
| **Bancos gerenciados** | MySQL e PostgreSQL. |
| **Outros** | Load balancer, contêineres, armazenamento em objetos e em bloco, CDN, DNS, snapshots. |
| **Upgrade** | Snapshot pode ser exportado para EC2 quando a aplicação crescer. |

## Cobrança

- Preço **mensal fixo** por plano (cobrado por hora até o teto mensal). Transferência acima da cota é cobrada.

## ⚠️ Pegadinhas e não confundir

- "Preço fixo e previsível, simples" → **Lightsail**. "Escala automática gerenciada a partir do código" → **Elastic Beanstalk**. "Controle total" → **EC2**.

## ❓ Perguntas típicas

- "Site WordPress simples com preço mensal fixo." → Lightsail.
- "Pequena empresa sem experiência quer um servidor com custo previsível." → Lightsail.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Instâncias, discos, snapshots e recursos simplificados |
| **O que você decide/configura?** | Blueprint, bundle, rede e backups |
| **Em que ordem as coisas acontecem?** | Crie pacote, instale/configure aplicação e acompanhe consumo |
| **O que pode fazer, e em que condição?** | Oferece início simples com preço de pacote e limites descritos |
| **O que não pode presumir?** | Não significa capacidade ilimitada ou proteção automática da aplicação |

**Caso comentado:** Pequeno site com requisitos simples: Lightsail; requisitos complexos pedem avaliar EC2 e serviços especializados.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)
