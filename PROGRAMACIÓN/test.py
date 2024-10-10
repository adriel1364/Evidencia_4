import pytest
from cafetera import Cafetera

def test_preparar_cafe_suficiente_agua_y_temperatura(cafetera):
    resultado = cafetera.preparar_cafe(0.5)
    assert resultado == "Preparando 0.5 litros de café."
    assert cafetera.nivel_agua == 0.5

def test_preparar_cafe_no_suficiente_agua(cafetera):
    resultado = cafetera.preparar_cafe(1.5)
    assert resultado == "No hay suficiente agua para preparar esa cantidad de café."

def test_preparar_cafe_temperatura_baja(cafetera):
    cafetera.temperatura = 80
    resultado = cafetera.preparar_cafe(0.5)
    assert resultado == "La temperatura del agua no es suficiente para preparar café."

def test_calentar_agua(cafetera):
    resultado = cafetera.calentar_agua(10)
    assert resultado == "Temperatura actual del agua: 95°C"
    assert cafetera.temperatura == 95

def test_calentar_agua_maxima(cafetera):
    resultado = cafetera.calentar_agua(20)
    assert resultado == "Temperatura actual del agua: 100°C"
    assert cafetera.temperatura == 100

def test_llenar_agua(cafetera):
    resultado = cafetera.llenar_agua(0.5)
    assert resultado == "Nivel de agua actual: 1.5 litros"
    assert cafetera.nivel_agua == 1.5

def test_llenar_agua_exceso(cafetera):
    resultado = cafetera.llenar_agua(2)
    assert resultado == "No se puede llenar más allá de la capacidad máxima."