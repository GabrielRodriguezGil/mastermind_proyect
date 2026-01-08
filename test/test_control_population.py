from src.control_population import control_population
import pytest

population = [
    ["amarillo", "morado", "morado", "blanco"],
    ["amarillo", "azul", "verde", "azul"],
    ["rojo", "morado", "blanco", "rojo"],
    ["blanco", "azul", "amarillo", "verde"],
    ["rojo", "verde", "morado", "blanco"],
    ["rojo", "blanco", "rojo", "blanco"],
    ["azul", "amarillo", "verde", "rojo"],
    ["verde", "morado", "rojo", "rojo"],
    ["verde", "verde", "amarillo", "rojo"],
    ["amarillo", "rojo", "azul", "amarillo"],
    ["rojo", "verde", "azul", "amarillo"],
    ["amarillo", "azul", "verde", "azul"],
    ["rojo", "morado", "blanco", "rojo"]
]
childs = [
    ["rojo", "verde", "azul", "amarillo"],
    ["amarillo", "azul", "verde", "azul"],
    ["rojo", "morado", "blanco", "rojo"],
]


@pytest.mark.test_control_population
def test_control_population():
    assert len(control_population(population,[1, 4, 3, 3, 4, 3, 4, 3, 5, 6,4,5,6],childs)) == len(population)-len(childs)
