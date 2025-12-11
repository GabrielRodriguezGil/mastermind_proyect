import random


def control_population(generation, fitness_values, childs):
    last_generation = generation.copy()
    fitness_values_copy = fitness_values.copy()

    null_deaths = 0
    for index, fitness in enumerate(fitness_values_copy):
        if fitness == 0:
            del last_generation[index]
            del fitness_values_copy[index]
        null_deaths += 1

    fitness_inversed = [1 / v for v in fitness_values_copy]

    deaths = random.choices(
        last_generation, weights=fitness_inversed, k=int((len(childs) - null_deaths))
    )

    new_generation = [x for x in last_generation if x not in deaths]
    return new_generation
