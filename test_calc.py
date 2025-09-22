import pytest
from calc import somar, subtrair, multiplicar, dividir, eh_par

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(10, 4) == 6

def test_multiplicar():
    assert multiplicar(3, 7) == 21

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    import pytest
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_eh_par_true():
    assert eh_par(8) is True

def test_eh_par_false():
    assert eh_par(7) is False
