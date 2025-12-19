from src.check_colors import check_colors
import random


def select_parents(generation, last_try):
    fitness_values = []
    for individual in generation:
        fitness = check_colors(individual, last_try)
        fitness_values.append(fitness)

    parents = random.choices(
        generation, weights=fitness_values, k=int((len(generation) / 100) * 40)
    )

    return parents
