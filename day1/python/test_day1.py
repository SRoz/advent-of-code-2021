from day1.day1 import part1, part2

with open("day1/inputs/test1.txt", "r") as f:
    test1 = f.readlines()
    test1 = [int(t) for t in test1]

def test_part1():
    assert part1(test1)==7

def test_part2():
    assert part2(test1, window_size=3)==5