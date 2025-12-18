"""Mastermind solver entry point."""

from input_user import color_input
from generate_combinations import generate_conbinations
from create_fitness_dictionary import create_fitness_dictionary
from select_parents import select_parents
from mix_generations import mix_generations
from control_population import control_population
from interpretate_dictionary import interpretate_dictionary
from return_colors import return_colors


BEST_FITNESS = 12
MAX_ATTEMPTS = 14


def mastermind():
    """Run the mastermind solver loop until solution or max attempts.

    The function prints the best guess and its fitness on each iteration.
    """
    solution = color_input()
    attempts = 0
    best_score = 0
    population = generate_conbinations()

    while best_score != BEST_FITNESS and attempts < MAX_ATTEMPTS:
        fitness_dictionary = create_fitness_dictionary(population, solution)
        fitness_values = interpretate_dictionary(fitness_dictionary, population)

        parents = select_parents(population, solution)
        children = mix_generations(parents)
        population.extend(children)

        fitness_dictionary = create_fitness_dictionary(population, solution)
        fitness_values = interpretate_dictionary(fitness_dictionary, population)

        next_population = control_population(population, fitness_values, children)

        attempts += 1
        population = next_population

        fitness_values = interpretate_dictionary(fitness_dictionary, population)
        best_score = max(fitness_values)
        best_index = fitness_values.index(best_score)

        print(f"{return_colors(population[best_index])} {best_score}")
