"""Gera e confere os relatórios de xadrez do 1º ano do Arena (padrão em agentes/arena/relatorios.md).

Uso:
  python3 relatorios_docx.py relatorios.json saida.docx [--lista lista.json] [--anterior antigo.docx ...]

relatorios.json:
  {"1º ANO A": [{"nome": "Fulana de Tal", "texto": "Parágrafo..."}, ...], "1º ANO B": [...], ...}

lista.json (lista oficial): {"1º ANO A": ["Fulana de Tal", ...], ...}

A conferência aponta: alunos faltando ou sobrando por turma, travessões, frases repetidas entre alunos
e frases já usadas nos relatórios anteriores. Se houver problema, o arquivo é gerado mesmo assim, mas o
script sai com código 1.
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

AZUL_TITULO = RGBColor(0x1A, 0x3F, 0x6F)
AZUL_BORDA = "2C5F9E"
TRAVESSOES = ("—", "–")


def _arial(doc):
    estilo = doc.styles["Normal"]
    estilo.font.name = "Arial"
    estilo.font.size = Pt(11)
    rpr = estilo.element.get_or_add_rPr()
    fontes = rpr.find(qn("w:rFonts"))
    if fontes is None:
        fontes = OxmlElement("w:rFonts")
        rpr.append(fontes)
    for atr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fontes.set(qn(atr), "Arial")


def _borda_inferior(par):
    ppr = par._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), AZUL_BORDA)
    pbdr.append(bottom)
    ppr.append(pbdr)


def gerar(dados, saida):
    doc = Document()
    _arial(doc)
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = sec.top_margin = sec.bottom_margin = Cm(2)

    for i, (turma, alunos) in enumerate(dados.items()):
        if i:
            doc.add_page_break()
        t = doc.add_paragraph()
        r = t.add_run(turma)
        r.bold = True
        r.font.size = Pt(14)
        r.font.color.rgb = AZUL_TITULO
        _borda_inferior(t)
        t.paragraph_format.space_after = Pt(12)
        for aluno in alunos:
            n = doc.add_paragraph()
            n.add_run(aluno["nome"]).bold = True
            n.paragraph_format.space_after = Pt(2)
            n.paragraph_format.keep_with_next = True
            p = doc.add_paragraph(aluno["texto"].strip())
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_after = Pt(12)
    doc.save(saida)


def _norm(s):
    s = unicodedata.normalize("NFC", s)
    return re.sub(r"\s+", " ", s).strip()


def _frases(texto):
    partes = re.split(r"(?<=[.!?])\s+", _norm(texto))
    return [p.lower().rstrip(".!? ") for p in partes if len(p.split()) >= 5]


def _texto_docx(caminho):
    return "\n".join(p.text for p in Document(caminho).paragraphs)


def conferir(dados, lista=None, anteriores=()):
    problemas = []
    if lista:
        for turma in sorted(set(lista) | set(dados)):
            oficiais = [_norm(n) for n in lista.get(turma, [])]
            gerados = [_norm(a["nome"]) for a in dados.get(turma, [])]
            for n in oficiais:
                if n not in gerados:
                    problemas.append(f"{turma}: falta relatório de {n}")
            for n in gerados:
                if n not in oficiais:
                    problemas.append(f"{turma}: nome fora da lista oficial (grafia?): {n}")
            for n in set(gerados):
                if gerados.count(n) > 1:
                    problemas.append(f"{turma}: {n} aparece {gerados.count(n)} vezes")

    vistas = defaultdict(list)
    for turma, alunos in dados.items():
        for a in alunos:
            if any(t in a["texto"] or t in a["nome"] for t in TRAVESSOES):
                problemas.append(f"{turma}: travessão no relatório de {a['nome']}")
            for f in _frases(a["texto"]):
                vistas[f].append(a["nome"])
    for f, nomes in vistas.items():
        if len(nomes) > 1:
            problemas.append(f"frase repetida em {', '.join(nomes)}: \"{f}\"")

    # trechos de 7 palavras iguais entre alunos diferentes (pega frase igual com outro nome)
    trechos = defaultdict(set)
    for alunos in dados.values():
        for a in alunos:
            palavras = re.findall(r"\w+", _norm(a["texto"]).lower())
            for i in range(len(palavras) - 6):
                trechos[" ".join(palavras[i:i + 7])].add(a["nome"])
    ja = set()
    for t, nomes in trechos.items():
        chave = tuple(sorted(nomes))
        if len(nomes) > 1 and chave not in ja:
            ja.add(chave)
            problemas.append(f"trecho parecido em {', '.join(chave)}: \"{t}...\"")

    antigas = set()
    for c in anteriores:
        antigas.update(_frases(_texto_docx(c)))
    for f, nomes in vistas.items():
        if f in antigas:
            problemas.append(f"frase já usada em bimestre anterior ({', '.join(nomes)}): \"{f}\"")
    return problemas


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    entrada, saida, resto = argv[1], argv[2], argv[3:]
    lista, anteriores = None, []
    while resto:
        op = resto.pop(0)
        if op == "--lista":
            lista = json.load(open(resto.pop(0), encoding="utf-8"))
        elif op == "--anterior":
            anteriores.append(resto.pop(0))
    dados = json.load(open(entrada, encoding="utf-8"))
    gerar(dados, saida)
    total = sum(len(v) for v in dados.values())
    print(f"Gerado {saida} com {total} relatórios em {len(dados)} turmas.")
    problemas = conferir(dados, lista, anteriores)
    if problemas:
        print("PROBLEMAS NA CONFERÊNCIA:")
        for p in problemas:
            print(" -", p)
        return 1
    print("Conferência sem problemas.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
