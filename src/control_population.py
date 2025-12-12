import random


def control_population(generation, fitness_values, childs):
    last_generation = generation.copy()
    fitness_values_copy = fitness_values.copy()

    fitness_inversed = [1 / fitness_value for fitness_value in fitness_values_copy]

    deaths = random.choices(
        last_generation, weights=fitness_inversed, k=int(len(childs))
    )

    new_generation = [
        individual for individual in last_generation if individual not in deaths
    ] + childs
    return new_generation
