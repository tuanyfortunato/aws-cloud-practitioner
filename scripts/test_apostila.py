#!/usr/bin/env python3
"""Testes do gerador de índices e flashcards e do glossário."""
import os
import re
import shutil
import tempfile
import unittest
import gerar_docs
from gerar_docs import AUTORAL, caminho_topico, eh_autoral, extrair_cards_revisao


class Autoral(unittest.TestCase):
    """Aulas e fichas com <!-- autoral --> são a fonte da verdade e não são reescritas."""

    AULA = """<!-- autoral -->

# 2.1 Aula escrita à mão

Texto autoral que o gerador não deve tocar.

## Revisão

### Quem protege o hipervisor?

A AWS. Ela opera o hardware e a camada de virtualização.

Parágrafo extra que fica só na aula.

### Quem aplica patches no sistema operacional do EC2?

O cliente, porque a instância é dele.
"""

    def test_marcador_vale_so_no_topo(self):
        with tempfile.TemporaryDirectory() as tmp:
            topo = os.path.join(tmp, 'topo.md')
            fundo = os.path.join(tmp, 'fundo.md')
            with open(topo, 'w') as f:
                f.write(self.AULA)
            with open(fundo, 'w') as f:
                f.write('# Aula gerada\n' + '\nlinha\n' * 20 + AUTORAL + '\n')
            self.assertTrue(eh_autoral(topo))
            self.assertFalse(eh_autoral(fundo))
            self.assertFalse(eh_autoral(os.path.join(tmp, 'inexistente.md')))

    def test_todo_conteudo_e_autoral(self):
        gerar_docs.conferir_autorais()

    def test_gerador_falha_se_aula_perde_o_marcador(self):
        raiz_real = gerar_docs.RAIZ
        with tempfile.TemporaryDirectory() as tmp:
            for pasta in ('docs', 'servicos', 'resumos'):
                shutil.copytree(os.path.join(raiz_real, pasta), os.path.join(tmp, pasta))
            shutil.copy(os.path.join(raiz_real, 'glossario.md'), tmp)
            caminho = os.path.join(tmp, caminho_topico('2.1'))
            with open(caminho) as f:
                texto = f.read().replace(AUTORAL, '', 1)
            with open(caminho, 'w') as f:
                f.write(texto)
            gerar_docs.RAIZ = tmp
            try:
                with self.assertRaises(AssertionError):
                    gerar_docs.conferir_autorais()
            finally:
                gerar_docs.RAIZ = raiz_real

    def test_flashcards_da_aula_autoral_vem_da_revisao(self):
        cards = extrair_cards_revisao(self.AULA)
        self.assertEqual(len(cards), 2)
        self.assertEqual(cards[0][0], 'Quem protege o hipervisor?')
        self.assertEqual(cards[0][1], 'A AWS. Ela opera o hardware e a camada de virtualização.')
        self.assertNotIn('Parágrafo extra', cards[0][1])
        self.assertEqual(extrair_cards_revisao('# Aula sem revisão\n\nTexto.\n'), [])
        recolhida = ('## Revisão\n\n### O que é IP?\n\n<details>\n<summary>Ver resposta</summary>\n\n'
                     'O endereço de uma máquina na rede.\n\nComentário longo.\n\n</details>\n')
        self.assertEqual(extrair_cards_revisao(recolhida), [('O que é IP?', 'O endereço de uma máquina na rede.')])

    def test_flashcards_do_capitulo_zero_cobrem_todas_as_aulas(self):
        aulas = gerar_docs.aulas_fundamentos()
        self.assertTrue(aulas)
        esperado = 0
        for numero, _, caminho in aulas:
            with open(os.path.join(gerar_docs.RAIZ, caminho), encoding='utf-8') as f:
                cards = extrair_cards_revisao(f.read())
            self.assertGreaterEqual(len(cards), 3, caminho)
            esperado += len(cards)
        todas = []
        with tempfile.TemporaryDirectory() as tmp:
            raiz = gerar_docs.RAIZ
            os.makedirs(os.path.join(tmp, 'flashcards'))
            shutil.copytree(os.path.join(raiz, 'docs', 'fundamentos'), os.path.join(tmp, 'docs', 'fundamentos'))
            gerar_docs.RAIZ = tmp
            try:
                gerar_docs.escrever_flashcards('flashcards/capitulo-0.md', 'Capítulo 0', aulas, todas,
                                               lambda n: f'CLF-C02 capitulo-0 aula-{n}')
                with open(os.path.join(tmp, 'flashcards', 'capitulo-0.md'), encoding='utf-8') as f:
                    texto = f.read()
            finally:
                gerar_docs.RAIZ = raiz
        self.assertEqual(len(todas), esperado)
        self.assertEqual(texto.count('<details markdown="1">'), esperado)
        self.assertTrue(all('capitulo-0' in tags for _, _, tags in todas))


class Glossario(unittest.TestCase):
    def termos(self):
        with open(os.path.join(gerar_docs.RAIZ, 'glossario.md'), encoding='utf-8') as f:
            texto = f.read()
        return re.findall(r'^\| \*\*(.+?)\*\* \| (.+) \|$', texto, re.M)

    def test_glossario_em_ordem_alfabetica_e_sem_repeticao(self):
        import unicodedata
        def chave(nome):
            s = unicodedata.normalize('NFKD', nome).encode('ascii', 'ignore').decode().casefold()
            return (not s[0].isalpha(), s)
        nomes = [n for n, _ in self.termos()]
        self.assertEqual(len(nomes), len({chave(n) for n in nomes}))
        self.assertEqual(nomes, sorted(nomes, key=chave))

    def test_glossario_nao_usa_definicoes_defensivas(self):
        for nome, definicao in self.termos():
            self.assertNotRegex(definicao, r'compatíve|conforme', nome)


class Site(unittest.TestCase):
    """Páginas publicadas no GitHub Pages (_config.yml)."""

    def test_respostas_recolhidas_interpretam_markdown(self):
        # Sem markdown="1", o site mostra o Markdown da resposta como texto cru.
        raiz = gerar_docs.RAIZ
        for pasta, _, arquivos in os.walk(raiz):
            if os.path.relpath(pasta, raiz).split(os.sep)[0] in ('.git', 'fontes', 'pendencias', 'build'):
                continue
            for nome in arquivos:
                if nome.endswith('.md'):
                    with open(os.path.join(pasta, nome), encoding='utf-8') as f:
                        self.assertNotIn('<details>', f.read(), os.path.join(pasta, nome))

    def test_menu_do_site_aponta_para_paginas_existentes(self):
        import json
        with open(os.path.join(gerar_docs.RAIZ, '_data', 'navegacao.json'), encoding='utf-8') as f:
            grupos = json.load(f)
        urls = [i['url'] for g in grupos for i in g['itens']]
        self.assertIn('/docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.html', urls)
        self.assertEqual(len(urls), len(set(urls)))


if __name__=='__main__':
    unittest.main()
