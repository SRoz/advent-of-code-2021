import numpy as np

def part1(input):
    return np.sum(np.abs(input - np.floor(np.median(input))))

def triangular(n):
    return n*(n+1)/2

def part2(input):
    return np.sum(triangular(np.abs(np.array(input) - np.floor(np.mean(input)))))

if __name__=="__main__":
    with open("day7/inputs/input1.txt", "r") as f:
        input1 = [int (n) for n in f.readline().split(",")]

    print(part1(input1))
    print(part2(input1))
    