import random

def mix_generations(parents):

    childs = []

    for i in range(len(parents)-1):
        pair_parents = random.sample(parents,2)
        childs.append(pair_parents[0][0:2] + pair_parents[1][2:4])
        childs.append(pair_parents[1][0:2] + pair_parents[0][2:4])

    return childs