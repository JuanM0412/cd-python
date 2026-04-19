# tests/test_calculadora.py
import pytest
import math
from app.calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(5, 2) == 3
    assert restar(1, -1) == 2
    assert restar(0, 0) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 5) == -5
    assert multiplicar(0, 10) == 0

def test_dividir():
    assert math.isclose(dividir(10, 2), 5.0, rel_tol=1e-09, abs_tol=1e-09)
    assert math.isclose(dividir(5, -1), -5.0, rel_tol=1e-09, abs_tol=1e-09)
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert math.isclose(potencia(4, 0.5), 2.0, rel_tol=1e-09, abs_tol=1e-09)

def test_raiz_cuadrada():
    assert math.isclose(raiz_cuadrada(9), 3.0, rel_tol=1e-09, abs_tol=1e-09)
    assert math.isclose(raiz_cuadrada(0), 0.0, rel_tol=1e-09, abs_tol=1e-09)
    with pytest.raises(ValueError, match="No se puede calcular la raíz cuadrada de un número negativo"):
        raiz_cuadrada(-1)