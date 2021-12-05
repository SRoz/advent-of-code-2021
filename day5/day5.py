def part1(lines):
    keep_lines = list()
    for line in lines:
        before, after = line.split("->")
        before = [int(b) for b in before.split(",")]
        after = [int(b) for b in after.split(",")]

        if (before[0]==after[0]) or (before[1]==after[1]):
            keep_lines.append([before,after])


    covered_points = list()
    for line in keep_lines:
        
        if line[0][0]==line[1][0]:
            min_val = min(line[0][1], line[1][1])
            max_val = max(line[0][1], line[1][1])

            for i in range(min_val, max_val+1):
                covered_points.append([line[0][0], i])

        else:
            min_val = min(line[0][0], line[1][0])
            max_val = max(line[0][0], line[1][0])

            for i in range(min_val, max_val+1):
                covered_points.append([i, line[0][1]])

    counter = {}
    for point in covered_points:
        counter[str(point)] = counter.get(str(point), 0) + 1
  
    return sum([1 for v in counter.values() if v >1])

def sign(n):
    if n >0:
        return 1
    elif n <1:
        return -1
    else:
        return 0

def part2(lines):
    keep_lines = list()
    for line in lines:
        before, after = line.split("->")
        before = [int(b) for b in before.split(",")]
        after = [int(b) for b in after.split(",")]
        keep_lines.append([before,after])


    covered_points = list()
    for line in keep_lines:
        [x1, y1], [x2, y2] = line
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        if x1==x2:
            for i in range(min_y, max_y+1):
                covered_points.append([x1, i])

        elif y1==y2:
            for i in range(min_x, max_x+1):
                covered_points.append([i, y1])

        else:
            if sign(x1-x2) == sign(y1-y2):       
                zipped_range = zip(range(min_x, max_x+1), range(min_y, max_y+1))

            else:
                zipped_range = zip(range(min_x, max_x+1), range(max_y, min_y-1, -1))

            for i, j in zipped_range:
                covered_points.append([i,j])

    counter = {}
    for point in covered_points:
        counter[str(point)] = counter.get(str(point), 0) + 1
  
    return sum([1 for v in counter.values() if v >1])

if __name__=="__main__":    
    with open("day5/inputs/input1.txt", "r") as f:
        input1 = [l.rstrip("\n") for l in f.readlines()]

    print(part1(input1))    
    print(part2(input1))