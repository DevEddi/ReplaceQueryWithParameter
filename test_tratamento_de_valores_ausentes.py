import pytest
from testbook import testbook

@testbook('./notebookApp.ipynb', execute=True)
def test_retorna_substituicao_valores_ausentes(tb):
    tratar_ausentes = tb.ref("tratar_ausentes_refatora")
    lista = ['BI-RADS', 'Idade', 'Forma', ' Margem', ' Densidade', 'Severidade']
    assert tratar_ausentes(lista) == None

@testbook('./notebookApp.ipynb', execute=True)
def test_retorna_substituicao_pela_moda(tb):
    moda = tb.ref("substitui_valores_ausentes_com_moda")
    lista = ['BI-RADS', 'Forma', ' Margem', ' Densidade', 'Severidade']
    for lis in lista:
        assert moda(lis) == None


@testbook('./notebookApp.ipynb', execute=True)
def test_retorna_substituicao_pela_media(tb):
    media = tb.ref("substitui_valores_ausentes_com_media")
    assert media('Idade') == None


