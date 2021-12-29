from functools import lru_cache
import numpy as np
from itertools import combinations, product

def read_input(fn):
    with open(fn, "r") as f:
        lines = [inp.replace("\n", "") for inp in f.readlines()]

    output = list()
    current_line = list()

    for line in lines[1:]:
        if line.startswith("---"):
            output.append(np.array(current_line))
            current_line = list()
        elif line!='':
            current_line.append([int(i) for i in line.split(",")])
    else:
        output.append(current_line)
    return output

def compare_sets(set1,set2):
    vectors1 = list()
    for X,Y in combinations(set1,2):
        vectors1.append(tuple([x-y for x,y in zip(X,Y)]))
    vectors2 = list()
    for X,Y in combinations(set2,2):
        vectors2.append(tuple([x-y for x,y in zip(X,Y)]))
    return sum([v in vectors1 for v in vectors2])

def get_all_relative_vecs(set1):
    d = (set1-set1[:,None,:])
    valid_mask = ~np.logical_or.reduce([np.eye(d.shape[0], k=i, dtype=bool) for i in range(d.shape[0]+1)])
    return d[valid_mask]

# def get_num_matches(A, B):
#     return np.apply_along_axis(lambda x: np.any(np.all(x == B, axis=1)), axis=1, arr=A).sum()

def get_num_matches(A,B):
    return sum([1 for l in A if l.tolist() in B.tolist()])

def gen_all_3d_rotations():
    rotate_x = np.array([[1,0,0], [0,0,-1],[0,1,0]])
    rotate_y = np.array([[0,0,1], [0,1,0],[-1,0,0]])

    all_rots = list()
    for i,j,k,l in product(*[[0,1,2,3]]*4):
        all_rots.append(
            np.matmul(np.linalg.matrix_power(rotate_x, i),
                np.matmul(np.linalg.matrix_power(rotate_y, j),
                    np.matmul(np.linalg.matrix_power(rotate_x, k),
                        np.linalg.matrix_power(rotate_y, l)
        ))))
    return np.unique(np.array(all_rots),axis=0)

ALL_3D_ROTATIONS = gen_all_3d_rotations()

def add_points(set1, set2):

    rotations = list()
    relative_vecs1 = get_all_relative_vecs(set1)
    relative_vecs2 = get_all_relative_vecs(set2)
    for rot in ALL_3D_ROTATIONS:
        transformed = np.matmul(relative_vecs2, rot)
        if get_num_matches(relative_vecs1, transformed)>10:
            rotations.append(rot)

    if len(rotations)==0:
        return set1, False
    elif len(rotations)>1:
        raise ValueError("Too many rotations")
    else:
        rot = rotations[0]

    rotated_set2 = np.matmul(set2, rot)
    transformations, counts = np.unique(np.concatenate((rotated_set2 - set1[:,None,:])),axis=0, return_counts=True)

    if max(counts) < 12:
        return set1, False

    transform = transformations[np.argmax(counts)]
    transformed_set2 = rotated_set2 - transform

    # for rot, i, j in product(rotations, range(set1.shape[0]), range(set2.shape[0])):
    #     rotated_set2 = np.matmul(set2, rot)
    #     transform = set1[i] - rotated_set2[j]
    #     transformed_set2 = rotated_set2 + transform
    #     n_match = get_num_matches(transformed_set2, set1)
                
    #     if n_match>=11:
    #         break
    # else:
    #     return set1, False

    return np.unique(np.concatenate([set1,transformed_set2]), axis=0), True


def explore_matching(input):

    pairs = list()
    for i, j in combinations(range(len(input)),2):
        _, paired = add_points(np.array(input[i]), np.array(input[j]))
        if paired:
            pairs.append((i,j))
    return pairs

def part1(input):
    
    points = input[0]
    next = input[1:]
    n_added = 0
    while True:
        rest = next
        next = list()
        for new_points in rest:
            before = len(points)
            points, _ = add_points(points, np.array(new_points))
            if before != len(points):
                n_added += 1
                print(f"n points: {len(points)}")
                if n_added >= (len(input)-1):
                    break
            else:
                next.append(new_points)
        else:
            continue
        break

    print(len(points))

if __name__=='__main__':
    test1 = read_input("day19/inputs/test1.txt")
    input1 = read_input("day19/inputs/input1.txt")

    #part1(test1)
    #explore_matching(test1)
    part1(input1)