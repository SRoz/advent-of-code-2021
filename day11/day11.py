import numpy as np

def add_one(input):
    output = list()
    for line in input:
        line_out = list()
        for n in line:
            line_out.append(n+1)
        output.append(line_out)
    return output


def step(input):
    # Add 1
    octs = input + 1

    all_flashers = np.zeros_like(octs)

    while (flashers := octs > 9).any():
        # 8 directions:
        ul = np.pad(flashers, 1)[2:,2:]
        um = np.pad(flashers, 1)[2:,1:-1]
        ur = np.pad(flashers, 1)[2:,:-2]
        ml = np.pad(flashers, 1)[1:-1:,2:]
        mr = np.pad(flashers, 1)[1:-1:,:-2]
        ll = np.pad(flashers, 1)[:-2:,2:]
        lm = np.pad(flashers, 1)[:-2:,1:-1]
        lr = np.pad(flashers, 1)[:-2:,:-2]

        octs = octs + ul+um+ur+ml+mr+ll+lm+lr

        all_flashers = flashers | all_flashers
        octs[all_flashers.astype(bool)] = 0

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
    n_total_flashes = 0

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