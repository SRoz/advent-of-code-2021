def part1(puzzle_input):
    """Count the number of increases in input"""
    n_increases = 0
    
    for prev, next in zip(puzzle_input[:-1], puzzle_input[1:]):
        if next > prev:
            n_increases +=1 
    return n_increases

def part2(puzzle_input, window_size):
    """Sliding window of n: 
    - Create sum of n vector
    - Feed into part1
    """
    window_sums = list()
    for i in range(len(puzzle_input)-window_size + 1):
        window = puzzle_input[i : i + window_size]
        window_sums.append(sum(window))
    return part1(window_sums)
        

if __name__=="__main__":
    with open("day1/inputs/input1.txt", "r") as f:
        puzzle_input = f.readlines()
        puzzle_input = [int(t) for t in puzzle_input]

    with open("day1/inputs/test1.txt", "r") as f:
        test1 = f.readlines()
        test1 = [int(t) for t in test1]

    part1_answer = part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

    part2_answer = part2(puzzle_input, window_size=3)
    print(f"Part 2: {part2_answer}")