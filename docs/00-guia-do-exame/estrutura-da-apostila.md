<!-- autoral -->

# Como estudar com esta apostila

🏠 [Guia do exame](README.md)

---

A prova não pede que você configure serviços, e esta apostila também não. Ela foi escrita para quem está começando: cada aula parte de um problema concreto, explica a solução e mostra onde a solução para de servir. Você não precisa abrir o console da AWS, criar uma conta ou programar para acompanhar a leitura.

Esta página mostra como o material está organizado, o que esperar de cada aula e de cada ficha, e como saber se você entendeu um assunto ou só decorou o nome.

## As partes do material

O **capítulo 0** explica, para quem nunca trabalhou com tecnologia, o que é servidor, rede, dado, API e segurança básica. Os **capítulos 1 a 4** seguem os quatro domínios da prova e têm 41 aulas, numeradas de 1.1 a 4.6. As aulas são o estudo principal e devem ser lidas na ordem, porque cada uma usa o que as anteriores ensinaram.

As **fichas de serviço** aprofundam um serviço quando ele aparece numa aula. São 105, divididas em três grupos. As 67 fichas *núcleo* cobrem os serviços que a prova mais cobra e têm a versão completa. As 25 *complementares* e as 13 *de referência* são curtas: dizem o que o serviço faz, como funciona e com o que ele costuma ser confundido.

Para praticar e revisar, há 94 **questões** no formato da prova, agrupadas por domínio; **flashcards** que saem das perguntas de revisão das aulas; três **resumos** para a última semana; e um **glossário** para relembrar termos já estudados.

## Como uma aula é organizada

Toda aula dos capítulos 1 a 4 segue a mesma sequência. A abertura conta um problema de uma rede de escolas fictícia, que aparece ao longo de toda a apostila e é apresentada em [o caso da escola](caso-da-escola.md). Em seguida, cada conceito é explicado nesta ordem: o que é, como funciona, por que existe e qual é o custo ou o limite. Os termos novos são explicados no próprio texto, na primeira vez em que aparecem. Quando uma relação fica mais clara num desenho, a aula traz uma figura com legenda.

Depois dos conceitos vêm cinco seções fixas:

- **Na prova** reúne as regras que decidem as questões, em frases curtas.
- **Caso resolvido** aplica a aula a uma situação e explica por que as alternativas tentadoras falham.
- **Revisão** traz perguntas com a resposta escondida, para você tentar antes de olhar.
- **Resumo** lista as ideias principais.
- **Fontes oficiais** indica as páginas da AWS que confirmam cada informação, com a data da verificação.

O bloco **Minhas anotações**, no fim, é seu: escreva nele as dúvidas e as questões que errou.

## Como uma ficha é organizada

Uma ficha núcleo começa por uma frase que resume o serviço e pela situação dele na lista oficial da prova. Depois vêm as seções que respondem às perguntas práticas: que problema o serviço resolve, como funciona, quais opções principais ele tem, que números a prova cobra, como é cobrado e com quais serviços ele costuma ser confundido. As fichas complementares e de referência mantêm só o essencial: como funciona e com o que não confundir.

A ficha não repete a aula. Quando a aula já explicou o mecanismo, a ficha aponta para ela e se concentra nas escolhas e nos limites do serviço.

## Estudar sem o console

Você não precisa decorar telas. Para entender um serviço, basta responder a seis perguntas sobre ele. O exemplo abaixo usa o Amazon EC2, o serviço de máquinas virtuais da [aula 3.3](../03-tecnologia-e-servicos/03-ec2.md).

| Pergunta | Resposta para o EC2 |
|---|---|
| Que recurso eu crio? | Uma instância, a partir de uma imagem (AMI) e de um tipo de instância, numa sub-rede de uma zona de disponibilidade |
| O que eu configuro? | Capacidade, rede, acesso, disco e permissões |
| O que entra e o que sai? | Requisições chegam à aplicação, que processa e devolve ou grava resultados |
| Quem pode acessar? | A rede permite ou bloqueia a conexão; as permissões do IAM autorizam as ações na AWS |
| Quem cuida de cada parte? | A AWS cuida da infraestrutura; o cliente, do sistema operacional, da aplicação e dos dados |
| O que continua custando quando paro? | Os volumes EBS continuam cobrados mesmo com a instância parada |

Quando uma questão diz que algo "não funciona", vale perguntar que tipo de impedimento é esse. Às vezes o serviço simplesmente não tem a capacidade: o S3 hospeda sites estáticos, mas não executa código de servidor. Às vezes ele tem a capacidade, mas falta configuração, como uma instância sem rota para a internet. Às vezes a rede funciona, mas falta permissão, como uma função que não pode usar a chave do KMS que protege o objeto. E às vezes só certas opções têm o recurso: o EBS Multi-Attach, que liga um volume a várias instâncias, só existe para volumes Provisioned IOPS SSD (io1 e io2).

## Como saber se você entendeu

Há quatro níveis de entendimento. **Reconhecer** é identificar o serviço pelo nome. **Explicar** é descrever o que ele faz, quem cuida de cada parte e qual é o limite dele, sem copiar o texto. **Escolher** é comparar alternativas a partir do requisito do enunciado, e não de uma palavra solta. **Transferir** é mudar um detalhe do cenário e dizer se a resposta muda, e por quê.

A prova cobra principalmente os níveis de explicar e escolher. Se você só reconhece os nomes, volte à aula. Se consegue explicar a escolha e dizer que mudança no cenário levaria a outra resposta, avance.

Os exemplos, os casos e as questões desta apostila são autorais. Eles não reproduzem questões oficiais nem preveem a prova.

## Fontes oficiais

Verificadas em 06/10/2026.

- [Guia do exame CLF-C02](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html): o que se espera do candidato e as tarefas fora do escopo, como programar e implementar.
- [Ciclo de vida das instâncias EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html): volumes EBS cobrados com a instância parada.
- [Hospedar um site estático no Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html): sites estáticos, com scripts que rodam no navegador.
- [EBS Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html): disponível para volumes io1 e io2.

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações sobre como você estuda melhor. -->
<!-- notas:fim -->
