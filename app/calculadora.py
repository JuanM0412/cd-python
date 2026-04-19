"""
Módulo que proporciona funciones para operaciones matemáticas básicas.
"""

# IMPORTANTE: Reemplaza con tu nombre completo (debe coincidir con el nombre
# que uses en cualquier otro identificador del proyecto.
# Sugerencia: Usuario de correo de EAFIT)
AUTOR = "jmgomezp, mahoyosv, asjimenezm"


def sumar(a, b):
    """Suma dos números retornando su resultado."""
    return a + b


def restar(a, b):
    """Resta el segundo número al primero y devuelve el resultado."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números y devuelve el resultado."""
    return a * b


def dividir(a, b):
    """
    Divide el primer número por el segundo.
    Genera un error ZeroDivisionError si el segundo número es 0.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """Eleva el primer número a la potencia del segundo."""
    return a**b


def raiz_cuadrada(a):
    """
    Calcula la raíz cuadrada del primer número.
    Genera un error ValueError si el número es negativo.
    """
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return a**0.5
