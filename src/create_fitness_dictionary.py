from check_colors import check_colors


def create_fitness_dictionary(population, solution):
    fitness_dictionary = {}
    for individual in population:
        fitness_dictionary[population] = check_colors(individual, solution)
    return fitness_dictionary
