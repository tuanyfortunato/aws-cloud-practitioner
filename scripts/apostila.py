"""Estrutura de capítulos: conceitos antes de opções, explicação antes de revisão.

Conteúdo-base das fichas: conteudo_servicos/*.json. Regras e valores são preservados
nessa fonte editorial; a apresentação expande vocabulário e organiza a leitura.
"""
import json
import re
from pathlib import Path
from aprofundamento import FICHAS as PRATICAS, TOPICOS as CASOS
from introducoes_servicos import FICHAS as ABERTURAS
from didatica_docs import TOPICOS
from sequencias_servicos import PASSOS
from licoes_topicos import LICOES
from casos_apostila import CASOS as CASOS_ESTENDIDOS
from vocabulario_apostila import TERMOS, simples, termos_locais

PASTA = Path(__file__).parent / 'conteudo_servicos'
BASE = {}
for arquivo in sorted(PASTA.glob('*.json')):
    categoria = json.loads(arquivo.read_text())
    assert not set(BASE) & set(categoria), f'Fichas duplicadas em {arquivo}'
    BASE.update(categoria)
assert set(BASE) == set(ABERTURAS) == set(PASSOS) == set(PRATICAS), 'Cobertura de capítulos de serviço incompleta'
assert set(LICOES) == set(TOPICOS) == set(CASOS), 'Cobertura de capítulos de tópico incompleta'

# Termos que as aberturas já explicam e nomes de serviços também ficam disponíveis
# em capítulos que os mencionam. Fontes específicas continuam ao fim das fichas.
EXTRAS = {}
for nome, d in ABERTURAS.items():
    titulo = BASE[nome].splitlines()[0].removeprefix('# ')
    servico = titulo.split(' (')[0]
    definicao = d['explicacao'].split('. ')[0].rstrip('.') + '.'
    aliases = [servico, re.sub(r'^(?:Amazon|AWS) ', '', servico)]
    aliases += re.findall(r'\b[A-Z][A-Z0-9-]+\b', servico)
    for alias in aliases:
        if alias in ('AWS', 'Amazon'):
            continue
        EXTRAS.setdefault(alias.casefold(), (alias, definicao))


class Leitura:
    """Explica cada definição uma vez no arquivo, antes do trecho que a usa."""
    def __init__(self):
        self.explicados = set()

    def vocabulario(self, texto):
        pares = termos_locais(simples(texto), EXTRAS)
        novos = [(nome, d) for nome, d in pares if d not in self.explicados]
        self.explicados.update(d for _, d in novos)
        if not novos:
            return ''
        return '\n'.join(['**Antes de ler este trecho:**', '',
                         *[f'- **{nome}:** {d}' for nome, d in novos], '']) + '\n'

    def trecho(self, texto, nivel=3):
        """Abre tabelas de definições em textos por item; conserva comparações."""
        saida = []
        linhas = texto.strip().splitlines()
        i = 0
        while i < len(linhas):
            linha = linhas[i]
            if linha.lstrip().startswith(('```', '~~~')):
                delimitador = re.match(r'\s*(`{3,}|~{3,})', linha).group(1)
                bloco = [linha]
                i += 1
                while i < len(linhas):
                    bloco.append(linhas[i])
                    i += 1
                    if re.fullmatch(r'\s*' + re.escape(delimitador) + r'\s*', bloco[-1]):
                        break
                else:
                    raise ValueError('Bloco de código sem fechamento')
                codigo = '\n'.join(bloco)
                saida += [self.vocabulario(codigo), codigo, '']
                continue
            if linha.startswith('|') and i + 1 < len(linhas) and re.match(r'^\|[\s:|-]+\|?$', linhas[i+1]):
                tabela = [linha, linhas[i+1]]
                i += 2
                while i < len(linhas) and linhas[i].startswith('|'):
                    tabela.append(linhas[i]); i += 1
                texto_tabela = '\n'.join(tabela)
                colunas = [p.strip() for p in tabela[0].strip('|').split('|')]
                # Comparar é útil depois das definições; recursos e opções ganham
                # uma descrição por item para não depender de leitura de células.
                if colunas[0].casefold() in ('componente', 'opção', 'recurso', 'conceito', 'ferramenta', 'etapa'):
                    for linha_tabela in tabela[2:]:
                        valores = [v.strip() for v in linha_tabela.strip('|').split('|')]
                        assert len(valores) == len(colunas), f'Tabela irregular: {linha_tabela}'
                        saida += [f'**{simples(valores[0])}**', '', self.vocabulario(linha_tabela)]
                        for coluna, valor in zip(colunas[1:], valores[1:]):
                            if valor != '—':
                                # O rótulo explicita se o trecho é definição, escolha
                                # ou detalhe. Não inventa uma finalidade a partir do nome.
                                saida += [f'**{coluna}:** {valor}', '']
                else:
                    saida.append(self.vocabulario(texto_tabela))
                    saida += [texto_tabela, '']
                continue
            if re.match(r'^#{2,6} ', linha):
                titulo = re.sub(r'^#+ ', '', linha)
                saida += ['#' * min(nivel + 1, 6) + ' ' + titulo, '']
                i += 1
                continue
            if linha.startswith('- ') or re.match(r'^\d+\. ', linha):
                # Cada observação passa a um parágrafo, com vocabulário imediatamente
                # anterior. Listas numeradas reais são mantidas para mostrar ordem.
                trecho = linha[2:] if linha.startswith('- ') else linha
                saida += [self.vocabulario(trecho), trecho, '']
            else:
                if linha.strip() and not linha.startswith(('<!--', '>')):
                    saida.append(self.vocabulario(linha))
                saida.append(linha)
            i += 1
        return '\n'.join(saida).strip()


def compactar(texto):
    """Remove linhas em branco sobrando, sem alterar blocos de código."""
    partes = re.split(r'(```.*?```|~~~.*?~~~)', texto, flags=re.S)
    for i in range(0, len(partes), 2):
        partes[i] = re.sub(r'\n{3,}', '\n\n', partes[i])
    return ''.join(partes)


def secoes(texto):
    partes = re.split(r'^## (.+)\n', texto, flags=re.M)
    inicio = partes[0].strip()
    return inicio, [(partes[i], partes[i+1].strip()) for i in range(1, len(partes), 2)]


def chave(texto):
    return re.sub(r'[^\w ]', '', simples(texto)).casefold().strip()


def fundamentos_resposta(pergunta, resposta, corpo):
    """Localiza o fundamento original; não gera uma justificativa por associação livre."""
    alvo = simples(resposta).casefold()
    fatos = []
    for linha in corpo.splitlines():
        # Linhas de pergunta e gabarito ("pergunta" → resposta) não fundamentam a
        # própria resposta: citá-las só repetiria a associação (AP-02).
        if '→' in linha:
            continue
        if linha.startswith(('- ', '|')) and not re.match(r'^\|[\s:|-]+$', linha):
            fatos.append(linha)
    palavras = set(re.findall(r'\w{4,}', simples(pergunta).casefold()))
    texto_pergunta = simples(pergunta).casefold().strip().strip('"\'?.!: ')
    candidatos = []
    for fato in fatos:
        limpo = simples(fato).casefold()
        # Uma linha que já cita a pergunta (como as listas "Cai na prova") repetiria o par
        # pergunta/resposta em vez de explicar o fundamento (AP-02).
        if len(texto_pergunta) >= 10 and texto_pergunta in limpo:
            continue
        # Listas de palavra-chave ("frase do enunciado" = Serviço) são gabarito, não explicação.
        if re.search(r'"[^"]+"\s*=', fato):
            continue
        # Exige a resposta literal e algum contexto da pergunta. Caso contrário,
        # a revisão fica curta e o caso resolvido fornece o comentário detalhado.
        score = len(palavras & set(re.findall(r'\w{4,}', limpo)))
        if len(alvo) >= 3 and alvo in limpo and score:
            candidatos.append((score, fato))
    if candidatos:
        fato = max(candidatos, key=lambda x: x[0])[1]
        if fato.startswith('|'):
            fato = '; '.join(c.strip() for c in fato.strip('|').split('|') if c.strip())
        return fato.removeprefix('- ')
    return ''


def perguntas_comentadas(texto, corpo, leitura):
    saida = []
    for linha in texto.splitlines():
        if '→' in linha and linha.startswith('- '):
            pergunta, resposta = linha[2:].split('→', 1)
            fundamento = fundamentos_resposta(pergunta, resposta.strip(), corpo)
            saida += [f'**Pergunta:** {pergunta.strip()}', '', f'**Resposta curta:** {resposta.strip()}', '']
            if fundamento:
                saida += [leitura.vocabulario(fundamento), '**Fundamento explicado no capítulo:** ' + fundamento, '']
            else:
                saida += [leitura.vocabulario(resposta), '']
        elif linha.strip():
            saida.append(linha)
    return '\n'.join(saida)


def capitulo_servico(nome):
    base = BASE[nome]
    cabecalho, grupos = secoes(base)
    leitura = Leitura()
    recursos, escolhas, economia, revisao, referencias = [], [], [], [], []
    for titulo, texto in grupos:
        c = chave(titulo)
        item = (titulo, texto)
        if 'documentação oficial' in c:
            referencias.append(item)
        elif 'perguntas típicas' in c:
            revisao.append(item)
        elif any(p in c for p in ('não confundir', 'pegadinha', 'regra prática', 'tabela de decisão', 'qual banco', 'na prova', 'como isso aparece')):
            escolhas.append(item)
        elif any(p in c for p in ('cobrança', 'preço', 'segurança e responsabilidade', 'atualiza', 'alternativas atuais')):
            economia.append(item)
        else:
            recursos.append(item)
    assert referencias, f'Fontes ausentes: {nome}'
    d = ABERTURAS[nome]
    # Seções sem conteúdo próprio não são criadas; a numeração segue o que existe.
    numero = iter(range(1, 20))
    def titulo_secao(nome_secao):
        return f'## {next(numero)}. {nome_secao}'
    partes = [cabecalho, '', titulo_secao('A sequência de funcionamento'), '']
    texto_passos = '\n\n'.join(f'**Passo {i}.** {p}' for i, p in enumerate(PASSOS[nome], 1))
    partes += [leitura.vocabulario(texto_passos), texto_passos, '']
    if recursos:
        partes += [titulo_secao('Recursos e opções, com significado'), '']
        for titulo, texto in recursos:
            partes += ['### ' + titulo, '', leitura.trecho(texto), '']
    partes += [titulo_secao('Como escolher e reconhecer os limites'), '',
               'Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, '
               'responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.', '',
               leitura.trecho(d['limite']), '']
    for titulo, texto in escolhas:
        partes += ['### ' + titulo, '', leitura.trecho(texto), '']
    if economia:
        partes += [titulo_secao('Operação, segurança e custo'), '',
                   'Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que '
                   'continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.', '']
        for titulo, texto in economia:
            partes += ['### ' + titulo, '', leitura.trecho(texto), '']
    recursos_praticos, decisoes, fluxo, capacidade, limite, caso = PRATICAS[nome]
    partes += [titulo_secao('Caso resolvido: ligando as peças'), '']
    if nome in CASOS_ESTENDIDOS:
        caso_texto = '\n\n'.join(CASOS_ESTENDIDOS[nome])
        partes += [leitura.vocabulario(caso_texto), caso_texto, '']
    else:
        partes += [d['exemplo'], '', '**Aplicando a sequência à situação:**', '',
                   *[f'**Etapa {i}:** {p}' for i, p in enumerate(PASSOS[nome], 1)], '',
                   '**Resultado e responsabilidade:** ' + d['explicacao'], '']
    partes += [
               '**Recursos envolvidos:** ' + recursos_praticos + '.', '',
               '**Decisões que precisam ser tomadas:** ' + decisoes + '.', '',
               leitura.vocabulario(caso + limite), '**Outra situação comentada:** ' + caso, '',
               '**Por que não concluir mais do que isso:** ' + limite, '']
    if revisao:
        partes += [titulo_secao('Revisão e perguntas'), '']
        for titulo, texto in revisao:
            partes += ['### ' + titulo, '', perguntas_comentadas(texto, base, leitura), '']
    partes += [titulo_secao('Fontes e próximos passos'), '',
               'Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo '
               'servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.', '']
    for titulo, texto in referencias:
        partes += ['### ' + titulo, '', texto, '']
    return compactar('\n'.join(partes)).rstrip() + '\n'


def capitulo_topico(sec, corpo):
    leitura = Leitura()
    d = TOPICOS[sec]
    _, grupos = secoes(corpo)
    # O conteúdo antes do primeiro título também faz parte do capítulo.
    inicio = secoes(corpo)[0]
    perguntas, material = [], []
    for titulo, texto in grupos:
        (perguntas if 'perguntas típicas' in chave(titulo) else material).append((titulo, texto))
    funcionamento, decisao, limite, cenario, resposta = CASOS[sec]
    aula = '\n\n'.join(LICOES[sec])
    partes = ['## 1. Entenda as peças e a relação entre elas', '',
              leitura.vocabulario(aula), aula, '',
              '<details>', '<summary>Uma analogia para revisar esta ideia</summary>', '', d['analogia'], '', '</details>', '',
              '## 2. Conceitos e opções explicados', '',
              leitura.trecho(inicio), '']
    for titulo, texto in material:
        partes += ['### ' + titulo, '', leitura.trecho(texto), '']
    partes += ['## 3. Como analisar uma situação', '',
               leitura.vocabulario(funcionamento + decisao + limite),
               '**Primeiro, identifique o funcionamento:** ' + funcionamento, '',
               '**Depois, compare as escolhas:** ' + decisao, '',
               '**Por fim, verifique o limite:** ' + limite, '',
               '## 4. Caso resolvido', '', cenario, '',
               '**Raciocínio e resposta:** ' + resposta, '',
               '## 5. Revisão do capítulo', '',
               '**Objetivos de aprendizagem:**', '',
               *[f'- [ ] {item}' for item in d['saber']], '',
               '**Dica de revisão para a prova:** ' + d['dica'], '']
    for titulo, texto in perguntas:
        partes += ['### ' + titulo, '', perguntas_comentadas(texto, corpo, leitura), '']
    return compactar('\n'.join(partes)).rstrip()


def capitulos_apoio():
    """Páginas de orientação: preserva suas funções, acrescentando vocabulário local."""
    base = json.loads((Path(__file__).parent / 'conteudo_apoio.json').read_text())
    resultado = {}
    for nome, texto in base.items():
        titulo, _, corpo = texto.partition('\n')
        leitura = Leitura()
        resultado[nome] = compactar(titulo + '\n\n' + leitura.trecho(corpo, nivel=1)) + '\n'
    return resultado
