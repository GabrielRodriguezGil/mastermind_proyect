import random
from src.global_constants import MUTATION_RATE

def mix_generations(parents):
    colors = ["rojo", "azul", "verde", "amarillo", "morado", "blanco"]

    childs = []
    parents_copy = parents[:]
    while 0 < len(parents_copy):
        pair_parents = random.sample(parents_copy, 2)
        childs.append(pair_parents[0][0:1] + pair_parents[1][1:2]+ pair_parents[0][2:3] + pair_parents[1][3:4])
        childs.append(pair_parents[1][0:1] + pair_parents[0][1:2] + pair_parents[1][2:3] + pair_parents[0][3:4])
        parents_copy.remove(pair_parents[0])
        parents_copy.remove(pair_parents[1])

    mutation_number = round(len(childs) * MUTATION_RATE)

    if mutation_number < 1:
        mutation_number = 1

    for _ in range(mutation_number):
        childs[random.randint(0, len(childs) - 1)][random.randint(0, 3)] = (
            random.sample(colors, 1)
        )[0]
    return childs
