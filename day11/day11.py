import numpy as np
from scipy.signal import convolve2d

def step(input):
    octs = input + 1
    all_flashers = np.zeros_like(octs, dtype=bool)

    while (flashers := octs > 9).any():
        octs += convolve2d(flashers, np.array([[1,1,1],[1,0,1], [1,1,1]]), mode='same')
        all_flashers = flashers | all_flashers
        octs[all_flashers] = 0

    return octs, all_flashers.sum()

def part1(input):
    octs = np.array(input)
    n_total_flashes = 0
    for _ in range(100):
        octs, n_flashes = step(octs)
        n_total_flashes += n_flashes
    return n_total_flashes

def part2(input):
    octs = np.array(input)
    n_steps = 0
    while not (octs==0).all():
        octs, _ = step(octs)
        n_steps += 1
    return n_steps

if __name__=='__main__':
    with open("day11/inputs/input1.txt", "r") as f:
        input1 = [[int(n) for n in l if n!='\n'] for l in f.readlines()]

    print(part1(input1))
    print(part2(input1))
