import numpy as np
from itertools import product

def read_input(fn):
    with open(fn, "r") as f:
        enhancement = f.readline().replace("\n", "")
        _ = f.readline()
        lines = [inp.replace("\n", "") for inp in f.readlines()]

    return enhancement, np.array([[s for s in t] for t in lines])

def enhance(enhancement, image, pad='.'):
    image = np.pad(image, pad_width=1, constant_values=pad)
    output = np.zeros_like(image)
    padded = np.pad(image, pad_width=1, constant_values=pad)
    for i, j in product(range(image.shape[0]), range(image.shape[1])):
        window = padded[i:i+3,j:j+3]
        idx = int("".join(window.flatten()).replace("#","1").replace(".","0"),2)
        output[i,j] = enhancement[idx]
    return output

def solve(input, n=2):
    enhancement, image = input

    for i in range(n):
        if i % 2 == 0 or enhancement[0]=='.':
            image = enhance(enhancement, image, pad=".")
        else:
            image = enhance(enhancement, image, pad="#")
    
    print((image=='#').sum())

if __name__=='__main__':
    test1 = read_input("day20/inputs/test1.txt")
    input1 = read_input("day20/inputs/input1.txt")

    solve(test1, n=2)
    solve(input1, n=2)

    solve(test1, n=50)
    solve(input1, n=50)
