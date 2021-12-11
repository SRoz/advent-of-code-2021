pairs = (
    ('(', ')'),
    ('<', '>'),
    ('[', ']'),
    ('{', '}')
)
openers = tuple([p[0] for p in pairs])
closers = tuple([p[1] for p in pairs])
closer_dict = {p[0]: p[1] for p in pairs}
opener_dict = {p[1]: p[0] for p in pairs}

points_lookup1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

points_lookup2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def part1(input):
    breakers = []
    for line in input:
        open = []
        for bracket in line:
            if bracket in openers:
                open.append(bracket)
            elif opener_dict[bracket]==open[-1]:
                open = open[:-1]
            else:
                breakers.append(bracket)
                break

    return sum([points_lookup1[b] for b in breakers])

def get_unbroken_lines(input):
    still_open = list()
    for line in input:
        open = []
        for bracket in line:
            if bracket in openers:
                open.append(bracket)
            elif opener_dict[bracket]==open[-1]:
                open = open[:-1]
            else:
                break
        else:
            still_open.append(open)
    return still_open

def get_score(line):
    score = 0
    for bracket in reversed(line):
        score = (score * 5) + points_lookup2[closer_dict[bracket]]
    return score

def median(x):
    assert len(x) % 2 == 1, "We were promised odd lengths"
    return sorted(x)[int(len(x)/2)]

def part2(input):
    still_open = get_unbroken_lines(input)
    scores = [get_score(line) for line in still_open]
    return median(scores)


if __name__=='__main__':
    with open("day10/inputs/input1.txt", "r") as f:
        input1 = [[c for c in l if c!='\n'] for l in f.readlines()]

    print(part1(input1))
    print(part2(input1))