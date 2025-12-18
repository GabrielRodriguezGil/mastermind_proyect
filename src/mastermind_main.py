from input_user import color_input
from generate_combinations import generate_conbinations
from create_fitness_dictionary import create_fitness_dictionary
from select_parents import select_parents
from mix_generations import mix_generations
from control_population import control_population
from interpretate_dictionary import interpretate_dictionary
from return_colors import return_colors


def mastermind():
    solution = color_input()
    BEST_FITNESS = 12
    best_try = 0
    tries = 0
    last_population = generate_conbinations()
    while best_try != BEST_FITNESS and tries < 14:
        fitness_dictionary = create_fitness_dictionary(last_population, solution)
        fitness_values = interpretate_dictionary(fitness_dictionary, last_population)
        parents = select_parents(last_population, solution)
        childs = mix_generations(parents)
        fitness_dictionary = create_fitness_dictionary(
            last_population + childs, solution
        )
        fitness_values = interpretate_dictionary(fitness_dictionary, last_population)
        next_population = control_population(last_population, fitness_values, childs)
        tries += 1
        last_population = next_population
        best_try = max(fitness_values)
