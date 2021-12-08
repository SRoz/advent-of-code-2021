def part1(input):
    total_easy_digets = 0
    for _, outs in input:
        for out in outs:
            if len(out) in [2, 3, 4, 7]:
                total_easy_digets += 1
    return total_easy_digets


def decode_input(input):
    input = [sorted(inp) for inp in input]
    map = {}

    for inp in input:
        if len(inp) == 2:
            map[1] = set(inp)
        if len(inp) == 3:
            map[7] = set(inp)
        if len(inp) == 4:
            map[4] = set(inp)
        if len(inp) == 7:
            map[8] = set(inp)

    map['bd'] = map[4] - map[1]

    for inp in input:
        if len(inp) == 6:
            # 9 is len(6) and has inscribed 4
            if map[4] - set(inp) == set():
                map[9] = set(inp)

            # 0: is len(6) and doesnt have both of (b, d)
            elif map['bd'].intersection(set(inp)) != map['bd']:
                map[0] = set(inp)

            # 6: is len(6) and neither above above
            else:
                map[6] = set(inp)

        if len(inp) == 5:
            # 3: is len(5) and has (c,f) from (1)
            if map[1].intersection(set(inp)) == map[1]:
                map[3] = set(inp)

            # 5: is len(5) and has (b,d)
            elif map['bd'].intersection(set(inp)) == map['bd']:
                map[5] = set(inp)

            else:
                map[2] = set(inp)

    assert len(map) == 11

    return {str(v): k for k, v in map.items()}


def part2(input):
    total = 0
    for line in input:
        map = decode_input(line[0])

        line_ans = ''
        for ans in line[1]:
            line_ans += str(map[str(set(sorted(ans)))])

        total += int(line_ans)
    print(total)


if __name__ == "__main__":
    with open("day8/inputs/input1.txt", "r") as f:
        input1 = [[[p.replace("\n", "") for p in parts.split(" ") if p != ""]
                   for parts in line.split("|")] for line in f.readlines()]

    print(part1(input1))
    print(part2(input1))
