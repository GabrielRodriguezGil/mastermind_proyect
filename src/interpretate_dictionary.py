def interpretate_dictionary(fitness_dictionary, population):
    fitness_list = []
    for individual in population:
        fitness_list.append(fitness_dictionary[individual])
    return fitness_list
