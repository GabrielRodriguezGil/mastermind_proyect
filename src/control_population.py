import random


def control_population(generation, fitness_values, childs, fitness_childs):
    
    new_generation = generation.copy() + childs
    fitness_values_copy = fitness_values.copy() + fitness_childs

    fitness_inverted = [1 / fitness_value for fitness_value in fitness_values_copy]

    for _ in range(len(childs)):   
        elegido = random.choices(new_generation, weights=fitness_inverted, k=1)[0]
        index = new_generation.index(elegido)
        new_generation.pop(index)
        fitness_inverted.pop(index)
        
    return new_generation
