import random

def mix_generations(parents):

    childs = []
    parents_copy = parents[:]
    while  0 < len(parents_copy):
        pair_parents = random.sample(parents_copy,2)
        childs.append(pair_parents[0][0:2] + pair_parents[1][2:4])
        childs.append(pair_parents[1][0:2] + pair_parents[0][2:4])
        parents_copy.remove(pair_parents[0])
        parents_copy.remove(pair_parents[1])

    return childs

