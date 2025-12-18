from check_colors import check_colors


def create_fitness_dictionary(population, solution):
    fitness_dictionary = {}
    for individual in population:
        individual = "".join(individual)
        if individual not in fitness_dictionary:
            fitness_dictionary[individual] = check_colors(individual, solution)
    return fitness_dictionary
