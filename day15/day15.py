import numpy as np
import networkx as nx
from itertools import product
from networkx.algorithms.shortest_paths.generic import shortest_path
from networkx.classes.function import path_weight

def part1(input):
    max_x = input.shape[0]
    max_y = input.shape[1]

    # Contruct multi digraph with inputs weighted as per given weight
    G = nx.MultiDiGraph()
    for i, j in product(range(max_x), range(max_y)):
        for di, dj in ((0,-1), (0,1), (-1,0), (1,0)):
            if (i+di in range(max_x)) and (j+dj in range(max_y)):
                G.add_edge((i+di,j+dj), (i,j), weight=input[i,j])

    path = shortest_path(G, (0,0), (max_x-1, max_y-1), weight='weight')
    return path_weight(G, path, "weight")

def wrap(input):
    """ modular arithmatic"""
    return np.where(input % 9==0, 9, input % 9)

def duplicate_grid(input):
    dup_x = np.concatenate([wrap(input + n) for n in range(5)], axis=1)
    dup_y = np.concatenate([wrap(dup_x + n) for n in range(5)], axis=0)
    return dup_y

def part2(input):
    expanded_grid = duplicate_grid(input)
    return part1(expanded_grid)

if __name__=='__main__':
    with open("day15/inputs/input1.txt", "r") as f:
        input1 = np.array([[int(c) for c in l.replace("\n", "")] for l in f.readlines()])

    print(part1(input1))
    print(part2(input1))
