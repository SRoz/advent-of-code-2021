from copy import deepcopy
from collections import defaultdict, Counter

def read_input(file):
    with open(file, "r") as f:
        lines = [l.replace("\n", "") for l in f.readlines()]

    polymer = lines[0]    
    instructions = [l.replace(" ", "").split("->") for l in lines[2:]]

    return polymer, instructions

def insertion_round(polymer, instructions):
    instructions = defaultdict(lambda: "", instructions)

    output = polymer[0]
    for c1, c2 in zip(polymer, polymer[1:]):
         output += instructions[c1+c2] + c2

    return output

def part1(polymer, instructions):
    for _ in range(10):
        polymer = insertion_round(polymer, instructions)

    counts = Counter(polymer)
    return max(counts.values()) - min(counts.values())    

def insertion_round2(polymer_pairs, instructions):
    instructions = dict(instructions)
    output = deepcopy(polymer_pairs)
    for key in polymer_pairs.keys():
        if key in instructions:
            insertion = key[0] + instructions[key] + key[1]
            output[insertion[:2]] += polymer_pairs[key]
            output[insertion[1:]] += polymer_pairs[key]
            output[key] -= polymer_pairs[key]

    return output

def count_elements(polymer_pairs):
    element_counts = Counter()
    for k, v in polymer_pairs.items():
        element_counts[k[0]] += v
        element_counts[k[1]] += v
    
    return element_counts

def part2(polymer, instructions):

    polymer_pairs = [c1+c2 for c1, c2 in zip(polymer, polymer[1:])]
    polymer_pairs = Counter(polymer_pairs)

    for _ in range(40):
        polymer_pairs = insertion_round2(polymer_pairs, instructions)
    
    element_counts = count_elements(polymer_pairs)
    element_counts[polymer[0]] += 1
    element_counts[polymer[-1]] += 1

    return int((max(element_counts.values()) - min(element_counts.values()))/2)


if __name__=='__main__':
    test1 = read_input("day14/inputs/test1.txt")
    input1 = read_input("day14/inputs/input1.txt")

    print(part1(*input1))
    print(part2(*input1))
