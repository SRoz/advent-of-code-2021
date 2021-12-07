import numpy as np

def part1(input):
    return np.sum(np.abs(input - np.floor(np.median(input))))

def triangular(n):
    return n*(n+1)/2

def part2(input):
    round_up = np.sum(triangular(np.abs(np.array(input) - np.floor(np.mean(input)))))
    round_down = np.sum(triangular(np.abs(np.array(input) - np.ceil(np.mean(input)))))
    return min([round_up, round_down])

if __name__=="__main__":
    with open("day7/inputs/input1.txt", "r") as f:
        input1 = [int (n) for n in f.readline().split(",")]
    with open("day7/inputs/test1.txt", "r") as f:
        test1 = [int (n) for n in f.readline().split(",")]

    print(part1(input1))
    print(part2(test1))
    print(part2(input1))
    