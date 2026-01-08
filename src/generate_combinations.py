import random
from src.global_constants import POPULATION_SIZE

def generate_conbinations():
    colors = ["rojo", "azul", "verde", "amarillo", "morado", "blanco"]

    return [[random.choice(colors)  for i in range(4)]for i in range(POPULATION_SIZE)]

