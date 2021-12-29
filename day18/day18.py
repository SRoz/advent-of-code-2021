import ast
import math
from itertools import permutations

def add(x, y):
    return ["["] + x + y + ["]"]

def process_input(inp):
    inp = [i for i in str(inp) if i not in (" ", ",") ]
    return [i if i in ("[", "]") else int(i) for i in inp]

def read_input(fn):
    with open(fn, "r") as f:
        output = [inp.replace("\n", "") for inp in f.readlines()]
        output = [ast.literal_eval(inp) for inp in output]
        output = [process_input(inp) for inp in output]
    return output

def explode_one(inp):
    n_open = 0
    output = list()
    n_exploded=0
    exploded_idxs = list()
    for i, l in enumerate(inp):
        if l == "[":
            n_open += 1
        if n_open > 4 and n_exploded <= 3:
            exploded_idxs.append(i)
            if n_exploded==1:
                output.append(0)
                explode_left = l
            if n_exploded==2:
                explode_right = l
            n_exploded+=1
        else:
            output.append(l)
        if l == "]":
            n_open -= 1

    if n_exploded>0:
        # Add left number
        for i in reversed(range(exploded_idxs[0])):
            if output[i] not in (["[", "]"]):
                output[i] += explode_left
                break

        # Add right number
        for i in range(exploded_idxs[1], len(output)):
            if output[i] not in (["[", "]"]):
                output[i] += explode_right
                break
    return output, n_exploded>0

def split_one(inp):
    split=False
    output = list()
    for i in inp:
        if i not in ("[", "]"):
            if i>9 and not split:
                output += ["[", math.floor(i/2), math.ceil(i/2), "]"]
                split = True
            else:
                output.append(i)
        else:
            output.append(i)
    return output, split


def magnitude(inp):
    x, y = inp
    if isinstance(x, list):
        x = magnitude(x)
    if isinstance(y, list):
        y = magnitude(y)

    return 3*x + 2*y
    

def to_list(inp):
    to_ret = ",".join([str(i) for i in inp]).replace("[,", "[").replace(",]","]")
    return ast.literal_eval(to_ret)

def reduce(inp):
    while True:
        inp, changed1 = explode_one(inp)
        if not changed1:
            inp, changed2 = split_one(inp)

        if not changed1 and not changed2:
            break
    
    return inp

def part1(input):
    num = input[0]
    for inp in input[1:]:
        num = reduce(add(num, inp))
    
    list_res = to_list(num)
    print(magnitude(list_res))


def part2(input):
    max = 0
    for x, y in permutations(input, 2):
        num = reduce(add(x,y))
        mag = magnitude(to_list(num))
        if mag > max:
            max = mag
    print(max)


if __name__=='__main__':
    test1 = read_input("day18/inputs/test1.txt")
    input1 = read_input("day18/inputs/input1.txt")

    part1(test1)
    part1(input1)

    part2(test1)
    part2(input1)