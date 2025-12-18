from src.input_user import color_input
from src.generate_combinations import generate_conbinations
from src.create_fitness_dictionary import create_fitness_dictionary
from src.select_parents import select_parents
from src.mix_generations import mix_generations
from src.control_population import control_population
from src.interpretate_dictionary import interpretate_dictionary
from src.return_colors import return_colors


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
        last_population.extend(childs)
        fitness_dictionary = create_fitness_dictionary(last_population, solution)
        fitness_values = interpretate_dictionary(fitness_dictionary, last_population)
        next_population = control_population(last_population, fitness_values, childs)
        tries += 1
        last_population = next_population
        fitness_values = interpretate_dictionary(fitness_dictionary, last_population)
        best_try = max(fitness_values)

        print(return_colors(last_population[fitness_values.index(best_try)]), best_try)
