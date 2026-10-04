# 1.4 AWS Well-Architected Framework

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md)

⬅️ [1.3 Conceitos de arquitetura que a prova cobra](03-conceitos-de-arquitetura.md) · 🏠 [Índice do domínio](README.md) · [1.5 AWS Cloud Adoption Framework (CAF)](05-cloud-adoption-framework.md) ➡️

---

## 📖 Conteúdo

Seis pilares, cada um com princípios de design. A prova descreve uma prática e pergunta o pilar.

| Pilar | Foco | Princípios de design que mais caem |
| --- | --- | --- |
| Excelência Operacional | Rodar e monitorar sistemas e melhorar processos | Operações como código; mudanças pequenas, frequentes e reversíveis; refinar procedimentos com frequência; antecipar falhas; aprender com falhas operacionais; usar serviços gerenciados; implementar observabilidade |
| Segurança | Proteger dados, sistemas e ativos | Base forte de identidade (menor privilégio); rastreabilidade; segurança em todas as camadas; automatizar boas práticas; proteger dados em trânsito e em repouso; manter pessoas longe dos dados; preparar-se para incidentes |
| Confiabilidade | Executar corretamente e se recuperar de falhas | Recuperação automática de falhas; testar procedimentos de recuperação; escalar horizontalmente; parar de adivinhar capacidade; gerenciar mudanças com automação |
| Eficiência de Performance | Usar recursos de forma eficiente conforme a demanda muda | Democratizar tecnologias avançadas; ficar global em minutos; usar arquiteturas serverless; experimentar com mais frequência; considerar a afinidade mecânica (escolher a tecnologia que combina com o uso) |
| Otimização de Custos | Entregar valor pelo menor preço | Praticar gestão financeira na nuvem; adotar modelo de consumo; medir a eficiência geral; parar de gastar com trabalho pesado indiferenciado; analisar e atribuir gastos |
| Sustentabilidade | Reduzir impacto ambiental | Entender seu impacto; definir metas; maximizar a utilização; adotar hardware e software mais eficientes; usar serviços gerenciados; reduzir o impacto downstream |

- **AWS Well-Architected Tool:** serviço gratuito no console para revisar uma carga de trabalho contra os pilares e gerar um plano de melhorias.
- **Lenses:** extensões do framework para cenários específicos (serverless, SaaS, machine learning, serviços financeiros).
- **Cai na prova:** "usar várias AZs" = Confiabilidade; "ativar MFA e criptografia" = Segurança; "escolher o tipo de instância certo" = Eficiência de Performance; "desligar recursos ociosos" = Otimização de Custos; "usar Graviton para gastar menos energia" = Sustentabilidade; "CloudFormation e runbooks" = Excelência Operacional.

## ➕ Complemento — princípios gerais de design do Well-Architected

- Parar de adivinhar necessidades de capacidade.
- Testar sistemas em escala de produção.
- Automatizar para facilitar a experimentação.
- Permitir arquiteturas evolutivas.
- Guiar arquiteturas com dados.
- Melhorar com "game days" (simulações de eventos em produção).

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).

- "Quantos e quais são os pilares?" → Seis: Excelência Operacional, Segurança, Confiabilidade, Eficiência de Performance, Otimização de Custos e Sustentabilidade.
- "Qual pilar inclui recuperar automaticamente de falhas e escalar horizontalmente?" → Confiabilidade.
- "Qual pilar inclui rastreabilidade e menor privilégio?" → Segurança.
- "Qual pilar inclui fazer mudanças pequenas, frequentes e reversíveis?" → Excelência Operacional.
- "Qual pilar inclui usar serverless e experimentar com frequência?" → Eficiência de Performance.
- "Qual pilar inclui adotar o modelo de consumo e analisar gastos?" → Otimização de Custos.
- "Qual pilar foi o último adicionado e trata de impacto ambiental?" → Sustentabilidade.
- "Qual ferramenta revisa uma carga de trabalho contra os pilares?" → AWS Well-Architected Tool.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [1.3 Conceitos de arquitetura que a prova cobra](03-conceitos-de-arquitetura.md) · 🏠 [Índice do domínio](README.md) · [1.5 AWS Cloud Adoption Framework (CAF)](05-cloud-adoption-framework.md) ➡️
