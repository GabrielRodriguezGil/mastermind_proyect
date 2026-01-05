from src.select_parents import select_parents
from src.global_constants import PARENT_SELECTION_PERCENTAGE
import pytest

population =         [
            ["rojo", "verde", "blanco", "rojo"],
            ["amarillo", "amarillo", "verde", "morado"],
            ["azul", "azul", "blanco", "verde"],
            ["blanco", "amarillo", "rojo", "azul"],
            ["blanco", "azul", "azul", "rojo"],
            ["amarillo", "blanco", "amarillo", "amarillo"],
            ["verde", "rojo", "azul", "verde"],
            ["azul", "rojo", "azul", "amarillo"],
            ["azul", "morado", "amarillo", "amarillo"],
            ["morado", "verde", "morado", "azul"],
            ["rojo", "azul", "morado", "verde"],
            ["verde", "amarillo", "amarillo", "amarillo"],
            ["verde", "rojo", "amarillo", "rojo"],
            ["azul", "rojo", "blanco", "amarillo"],
            ["blanco", "verde", "verde", "blanco"],
            ["blanco", "azul", "amarillo", "verde"],
            ["rojo", "rojo", "blanco", "azul"],
            ["verde", "amarillo", "amarillo", "morado"],
            ["verde", "amarillo", "amarillo", "verde"],
            ["blanco", "verde", "verde", "morado"]
        ]

@pytest.mark.test_select_parents
def test_select_parents():
    parents = select_parents( population,["rojo", "rojo", "blanco", "azul"])
    assert len(parents) == len(population) * PARENT_SELECTION_PERCENTAGE
