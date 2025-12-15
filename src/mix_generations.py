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
        )
    return childs


if __name__ == "__main__":
    mix_generations(
        [
            ["blanco", "azul", "verde", "verde"],
            ["rojo", "blanco", "verde", "morado"],
            ["morado", "rojo", "rojo", "blanco"],
            ["rojo", "rojo", "verde", "amarillo"],
            ["rojo", "blanco", "amarillo", "blanco"],
            ["blanco", "amarillo", "blanco", "amarillo"],
            ["verde", "rojo", "blanco", "amarillo"],
            ["verde", "verde", "verde", "rojo"],
            ["morado", "morado", "azul", "amarillo"],
            ["blanco", "rojo", "morado", "morado"],
            ["morado", "verde", "blanco", "rojo"],
            ["amarillo", "amarillo", "verde", "blanco"],
            ["verde", "azul", "verde", "verde"],
            ["blanco", "azul", "verde", "amarillo"],
            ["blanco", "verde", "morado", "verde"],
            ["amarillo", "azul", "verde", "azul"],
            ["rojo", "blanco", "rojo", "blanco"],
            ["verde", "morado", "morado", "blanco"],
            ["amarillo", "verde", "amarillo", "blanco"],
            ["azul", "morado", "blanco", "amarillo"],
        ]
    )
