"""Mastermind solver entry point."""

import matplotlib.pyplot as plt

from src.input_user import color_input
from src.generate_combinations import generate_conbinations
from src.create_fitness_dictionary import create_fitness_dictionary
from src.select_parents import select_parents
from src.mix_generations import mix_generations
from src.control_population import control_population
from src.interpretate_dictionary import interpretate_dictionary
from src.return_colors import return_colors
from src.global_constants import MAX_ATTEMPTS, BEST_FITNESS





def mastermind():
    """Run the mastermind solver loop until solution or max attempts.

    The function prints the best guess and its fitness on each iteration,
    and displays a plot of fitness evolution at the end.
    """
    solution = color_input()
    attempts = 0
    best_score = 0
    population = generate_conbinations()
    fitness_history = []
    print(f"--Solución a encontrar-- {return_colors(solution)}")
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

        average_fitness = sum(fitness_values) / len(fitness_values) if fitness_values else 0
        fitness_history.append(average_fitness)
        print(f"{return_colors(population[best_index])} {best_score}")

    plt.plot(range(1, len(fitness_history) + 1), fitness_history, marker='o')
    plt.xlabel('Generación')
    plt.ylabel('Fitness Promedio')
    plt.title('Evolución del Fitness Promedio en Mastermind')
    plt.grid(True)
    plt.show()
