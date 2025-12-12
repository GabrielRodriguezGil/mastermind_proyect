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
]


@pytest.mark.test_control_population
def test_control_population():
    assert len(control_population(population)) == len(population)
