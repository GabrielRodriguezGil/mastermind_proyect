import random


def mix_generations(parents):
    colors = ["rojo", "azul", "verde", "amarillo", "morado", "blanco"]

    childs = []
    parents_copy = parents[:]
    while 0 < len(parents_copy):
        pair_parents = random.sample(parents_copy, 2)
        childs.append(pair_parents[0][0:2] + pair_parents[1][2:4])
        childs.append(pair_parents[1][0:2] + pair_parents[0][2:4])
        parents_copy.remove(pair_parents[0])
        parents_copy.remove(pair_parents[1])

    ONE_PERCENTAGE = round(len(childs) * 0.01)

    if ONE_PERCENTAGE <= 0.5:
        mutation_number = 1
    else:
        mutation_number = ONE_PERCENTAGE

    for _ in range(mutation_number):
        childs[random.randint(0, len(childs) - 1)][random.randint(0, 3)] = (
            random.sample(colors, 1)
        )[0]
    return childs
