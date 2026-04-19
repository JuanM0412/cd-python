"""
Módulo principal de la aplicación web Flask para la calculadora.
"""

import os
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Maneja la ruta principal y procesa las operaciones matemáticas
    enviadas a través del formulario web.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            operacion = request.form["operacion"]
            
            num2_str = request.form.get("num2", "")
            num2 = float(num2_str) if num2_str else 0.0

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            elif operacion == "potencia":
                resultado = potencia(num1, num2)
            elif operacion == "raiz_cuadrada":
                resultado = raiz_cuadrada(num1)
            else:
                resultado = "Operación no válida"
        except ValueError as e:
            if "raíz cuadrada" in str(e):
                resultado = f"Error: {str(e)}"
            else:
                resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


@app.route("/health", methods=["GET"])
def health():
    """
    Endpoint de monitoreo (healthcheck) para validar que la aplicación esté operativa.
    """
    return "OK", 200


if __name__ == "__main__":  # pragma: no cover
    # Quitar debug=True en producción
    app.run(debug=True, port=5000, host="0.0.0.0")
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-only-insecure-key")
