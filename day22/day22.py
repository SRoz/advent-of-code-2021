from collections import Counter
import numpy as np

def read_input(fn):
    with open(fn, "r") as f:
        lines = [inp.replace("\n", "").split(" ") for inp in f.readlines()]

    return lines

def parse_inp(line):
    output = [t.split("=")[1] for t in line[1].split(",")]
    return line[0], np.array([[int(j) for j in l.split("..")] for l in output])

def part1(input):
    xd, yd, zd = 50, 50, 50

    cube = np.zeros([101,101,101])

    for line in input:
        onoff, coords = parse_inp(line)

        X = max(0, coords[0][0]+xd), min(101, coords[0][1]+xd+1)
        Y = max(0, coords[1][0]+yd), min(101, coords[1][1]+yd+1)
        Z = max(0, coords[2][0]+zd), min(101, coords[2][1]+zd+1)

        cube[X[0]:X[1],Y[0]:Y[1],Z[0]:Z[1]] = 1 if onoff == 'on' else 0

    print((cube==1).sum())

def get_max_coord(input):
    overall_max = 0
    for line in input:
        max_coord = np.abs(np.array(parse_inp(line)[1])).max()
        if max_coord > overall_max:
            overall_max = max_coord
    return overall_max

def intersect_cubes(X, Y):
    return np.array([
    np.array([X.min(axis=1), Y.min(axis=1)]).T.max(axis=1),
    np.array([X.max(axis=1), Y.max(axis=1)]).T.min(axis=1)
    ]).T 

def cube_size(X):
    X = np.array(X).astype(float)
    diff = X[:,1]-X[:,0]+1
    if (diff>0).all():
        return np.product(diff)
    else:
        return 0.

def make_key(input):
    return tuple([tuple(c) for c in input])

def part2(input):
    cubes = Counter()
    
    for line in input:
        onoff, new_cube = parse_inp(line)
        
        update = Counter()
        for cube, n in cubes.items():
            cube = np.array(cube)
            intersection = intersect_cubes(new_cube, cube)
            if cube_size(intersection)>0:
                update[make_key(intersection)] -= n
        cubes.update(update)
        
        if onoff == 'on':
            cubes[make_key(new_cube)] += 1
    print(sum([cube_size(cube)*n for cube, n in cubes.items()]))

if __name__=='__main__':
    input1 = read_input("day22/inputs/input1.txt")

    part1(input1)
    part2(input1)
