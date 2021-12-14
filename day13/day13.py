def read_input(file):
    with open(file, "r") as f:
        lines = [l.replace("\n", "") for l in f.readlines()]

    folds = list()
    coords = list()
    
    for l in lines:
        if len(l)==0:
            continue
        if l[:10]=='fold along':
            folds.append([l[11], int(l[13:])])
        else:
            coords.append([int(i) for i in l.split(",")])

    return coords, folds


def fold_point(point, fold):
    x, y = point
    if fold[0]=='x':
        x_t = x - 2*max(0, x-fold[1])
        y_t = y
    elif fold[0]=='y':
        x_t = x
        y_t = y - 2*max(0, y-fold[1])        

    return [x_t, y_t]

def fold_grid(coords, fold):
    output_coords = list()
    for point in coords:
        folded_point = fold_point(point, fold)
        if folded_point not in output_coords:
            output_coords.append(folded_point)
    return output_coords

def part1(coords, folds):
    print(len(fold_grid(coords, folds[0])))

def print_grid(coords):
    max_x = max([c[0] for c in coords])+1
    max_y = max([c[1] for c in coords])+1

    canvas = [[" " for _ in range(max_x)] for _ in range(max_y)]

    for point in coords:
        canvas[point[1]][point[0]] = "#"
    
    for line in canvas:
        print("".join(line))

def part2(coords, folds):
    for fold in folds:
        coords = fold_grid(coords, fold)
    print_grid(coords)


if __name__=='__main__':
    test1 = read_input("day13/inputs/test1.txt")
    input1 = read_input("day13/inputs/input1.txt")

    part1(*input1)
    part2(*input1)