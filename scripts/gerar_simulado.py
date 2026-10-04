#!/usr/bin/env python3
"""Gera o simulado e os bancos de questões por domínio a partir de scripts/banco_questoes.py.

Uso: python3 scripts/gerar_simulado.py

Saídas (sobrescritas a cada execução):
  simulados/simulado-01.md            65 questões embaralhadas, como na prova, com gabarito no fim
  simulados/questoes/dominio-N.md     questões agrupadas por domínio, para estudo
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from banco_questoes import QUESTOES  # noqa: E402
from gerar_docs import ARQUIVOS, DOMINIOS, RAIZ, caminho_topico, escrever, rel  # noqa: E402

SEMENTE = 2026
LETRAS = "ABCDE"
DISTRIBUICAO = {"1": 16, "2": 20, "3": 21, "4": 8}  # 24% / 30% / 34% / 12% de 65


def validar():
    contagem = {d: 0 for d in DISTRIBUICAO}
    for i, q in enumerate(QUESTOES, 1):
        contagem[q["dominio"]] += 1
        total = len(q["corretas"]) + len(q["erradas"])
        esperado = 4 if len(q["corretas"]) == 1 else 5
        assert total == esperado, f"Questão {i}: {total} alternativas, esperado {esperado}"
        assert q["secao"] in ARQUIVOS, f"Questão {i}: seção {q['secao']} inexistente"
    assert contagem == DISTRIBUICAO, f"Distribuição por domínio {contagem} difere de {DISTRIBUICAO}"


def montar(q, rng):
    """Embaralha as alternativas e devolve (lista de (letra, texto), letras corretas)."""
    alternativas = [(t, True) for t in q["corretas"]] + [(t, False) for t in q["erradas"]]
    rng.shuffle(alternativas)
    opcoes = [(LETRAS[i], texto) for i, (texto, _) in enumerate(alternativas)]
    corretas = [LETRAS[i] for i, (_, ok) in enumerate(alternativas) if ok]
    return opcoes, corretas


def bloco_questao(numero, q, opcoes, corretas, destino):
    multipla = len(corretas) > 1
    tipo = " · **múltipla resposta**" if multipla else ""
    link = rel(destino, caminho_topico(q["secao"]))
    linhas = [f"### Questão {numero}", "",
              f"<sub>Domínio {q['dominio']} · tópico [{q['secao']}]({link}){tipo}</sub>", "",
              q["enunciado"], ""]
    linhas += [f"- **{letra})** {texto}" for letra, texto in opcoes]
    linhas += ["", "<details>", "<summary>Ver resposta</summary>", "",
               f"**Resposta: {', '.join(corretas)}**", "", q["explicacao"], "", "</details>", ""]
    return "\n".join(linhas)


def gerar_simulado():
    rng = random.Random(SEMENTE)
    ordem = list(QUESTOES)
    rng.shuffle(ordem)
    destino = "simulados/simulado-01.md"
    partes = ["# 📝 Simulado 01 — CLF-C02", "",
              "Simulado no formato da prova: **65 questões**, distribuídas como os pesos oficiais "
              "(Domínio 1: 16 · Domínio 2: 20 · Domínio 3: 21 · Domínio 4: 8), em ordem aleatória, "
              "com questões de **múltipla escolha** (1 correta) e **múltipla resposta** (2 corretas).", "",
              "## Como fazer", "",
              "1. Reserve **90 minutos** sem interrupção.",
              "2. Anote suas respostas num papel (ex.: `1-B, 2-A`) **sem abrir** o \"Ver resposta\".",
              "3. Ao terminar, confira no [gabarito](#gabarito) e preencha a folha de correção.",
              "4. Leia a explicação de **todas** as questões que errou e registre os erros num arquivo "
              "a partir do [modelo de simulado](../templates/simulado.md).", "",
              "> Na prova real, a nota mínima é 700/1000 (≈ 70%). Meta de treino: **≥ 80%**.", "", "---", ""]
    gabarito = []
    for n, q in enumerate(ordem, 1):
        opcoes, corretas = montar(q, rng)
        partes.append(bloco_questao(n, q, opcoes, corretas, destino))
        gabarito.append((n, ", ".join(corretas), q["dominio"], q["secao"]))

    partes += ["---", "", "## Gabarito", "", "| Questão | Resposta | Domínio | Tópico |", "|---|---|---|---|"]
    partes += [f"| {n} | **{r}** | {d} | [{s}]({rel(destino, caminho_topico(s))}) |" for n, r, d, s in gabarito]
    partes += ["", "## Folha de correção", "",
               "| Domínio | Peso | Questões | Acertos | % |", "|---|---|---|---|---|"]
    for d, (_, nome, peso) in DOMINIOS.items():
        partes.append(f"| {nome} | {peso} | {DISTRIBUICAO[d]} |  |  |")
    partes += ["| **Total** | 100% | 65 |  |  |", "",
               "> Domínio com menos de 70%? Volte aos tópicos dele e às [questões por domínio](questoes/README.md)."]
    escrever(destino, "\n".join(partes))


def gerar_por_dominio():
    for d, (pasta, nome, peso) in DOMINIOS.items():
        destino = f"simulados/questoes/dominio-{d}.md"
        rng = random.Random(f"{SEMENTE}-{d}")
        questoes = sorted((q for q in QUESTOES if q["dominio"] == d),
                          key=lambda q: tuple(int(x) for x in q["secao"].split(".")))
        partes = [f"# ❓ Questões — {nome} ({peso})", "",
                  f"{len(questoes)} questões no formato da prova, em ordem de tópico. "
                  "Responda antes de abrir \"Ver resposta\".", "",
                  "⬅️ [Todas as questões por domínio](README.md) · 📝 [Simulado completo](../simulado-01.md)", "", "---", ""]
        for n, q in enumerate(questoes, 1):
            opcoes, corretas = montar(q, rng)
            partes.append(bloco_questao(n, q, opcoes, corretas, destino))
        escrever(destino, "\n".join(partes))

    linhas = ["# ❓ Questões por domínio", "",
              "As mesmas questões do [simulado completo](../simulado-01.md), agrupadas por domínio e tópico "
              "para estudo direcionado (as alternativas aparecem em outra ordem).", "",
              "| Domínio | Peso | Questões |", "|---|---|---|"]
    for d, (_, nome, peso) in DOMINIOS.items():
        linhas.append(f"| [{nome}](dominio-{d}.md) | {peso} | {DISTRIBUICAO[d]} |")
    linhas += ["", "## Adicionar questões", "",
               "1. Inclua a questão em [`scripts/banco_questoes.py`](../../scripts/banco_questoes.py) "
               "(enunciado, alternativas corretas, distratores e explicação).",
               "2. Rode `python3 scripts/gerar_simulado.py`.",
               "3. Para um novo simulado completo, mantenha a distribuição 16/20/21/8 por domínio."]
    escrever("simulados/questoes/README.md", "\n".join(linhas))


def main():
    validar()
    gerar_simulado()
    gerar_por_dominio()
    multiplas = sum(1 for q in QUESTOES if len(q["corretas"]) > 1)
    print(f"{len(QUESTOES)} questões ({multiplas} de múltipla resposta): simulado e bancos por domínio gerados.")


if __name__ == "__main__":
    main()
