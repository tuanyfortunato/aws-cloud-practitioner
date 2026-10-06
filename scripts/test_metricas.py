#!/usr/bin/env python3
"""Garante que cada métrica mede o problema que diz medir."""
import os
import tempfile
import unittest

import metricas_apostila as m

AULA = """# 2.9 Aula de exemplo

## 🧠 Antes de começar

**Qual é a dificuldade?** A equipe não sabe quem protege cada parte.

**A ideia em palavras simples:** A divisão muda com o tipo de serviço.

## 1. Conteúdo

**Antes de ler este trecho:**

- **Patch:** atualização de correção de software.

O serviço é compatível com as opções conforme a configuração.

## 2. Promessa vazia

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua
sendo administrado pelo cliente.

## 3. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A equipe não sabe quem protege cada parte.

**2. O que a solução fornece?**

Resposta escrita à mão, que não repete a abertura.
"""


class Metricas(unittest.TestCase):
    def medir(self, texto):
        with tempfile.TemporaryDirectory() as tmp:
            caminho = os.path.join(tmp, "aula.md")
            with open(caminho, "w") as f:
                f.write(texto)
            return m.medir(caminho)

    def test_conta_vocabulario_defensivas_e_revisao_circular(self):
        r = self.medir(AULA)
        self.assertEqual(r["vocabulario"], 1)
        self.assertEqual(r["defensivas"], 2)  # "compatível" e "conforme"
        self.assertEqual(r["circular"], 1)    # só a primeira resposta repete a abertura
        self.assertFalse(r["autoral"])

    def test_secao_so_com_texto_padrao(self):
        r = self.medir(AULA)
        self.assertEqual(r["titulos_padrao"], ["## 2. Promessa vazia"])

    def test_titulo_com_subtitulos_nao_conta_como_vazio(self):
        texto = ("# Ficha\n\n## 4. Operação, segurança e custo\n\n"
                 "Ter o recurso disponível é diferente de operá-lo corretamente.\n\n"
                 "### Cobrança\n\nTaxa fixa por hora.\n")
        self.assertEqual(self.medir(texto)["titulos_padrao"], [])

    def test_reconhece_arquivo_autoral(self):
        r = self.medir("<!-- autoral -->\n\n# 2.1 Aula à mão\n\nTexto.\n")
        self.assertTrue(r["autoral"])
        self.assertEqual(r["vocabulario"], 0)

    def test_relatorio_cobre_todo_o_material(self):
        linhas = m.coletar()
        self.assertGreater(len(linhas), 100)
        grupos = {g for g, _, _ in linhas}
        self.assertIn("aulas", grupos)
        self.assertIn("fichas", grupos)
        self.assertEqual(len([1 for g, _, _ in linhas if g == "aulas"]), 41)
        self.assertEqual(m.main(["--markdown"]), 0)


if __name__ == "__main__":
    unittest.main()
