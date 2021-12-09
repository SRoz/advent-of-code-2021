import numpy as np
explored_already = []

def part1(input):
    input = np.array(input)
    x = np.concatenate([np.ones_like(input[:1,:])*10, input, np.ones_like(input[:1,:])*10])
    x = np.concatenate([np.ones_like(x[:,:1])*10, x, np.ones_like(x[:,:1])*10], axis=1)

    total_risk_level = 0
    for j in range(1, x.shape[1]-1):
        for i in range(1, x.shape[0]-1):
            if all([
                x[i,j] < x[i-1, j],
                x[i,j] < x[i+1, j],
                x[i,j] < x[i, j-1],
                x[i,j] < x[i, j+1],
            ]):
                total_risk_level += (1 + x[i,j])
    return total_risk_level


def explore_path(grid, loc, count):
    global explored_already 
    i, j = loc

    if loc in explored_already:
        return count
    else:
        explored_already.append(loc)

    if grid[i, j] >=9:
        return count
    else:
        d1 = explore_path(grid, (i-1, j), count)
        d2 = explore_path(grid, (i+1, j), count)
        d3 = explore_path(grid, (i, j-1), count)
        d4 = explore_path(grid, (i, j+1), count)
        return 1+d1+d2+d3+d4


def part2(input):
    input = np.array(input)
    x = np.concatenate([np.ones_like(input[:1,:])*10, input, np.ones_like(input[:1,:])*10])
    x = np.concatenate([np.ones_like(x[:,:1])*10, x, np.ones_like(x[:,:1])*10], axis=1)

    # find lowpoints:
    lowpoints = []
    for j in range(1, x.shape[1]-1):
        for i in range(1, x.shape[0]-1):
            if all([
                x[i,j] < x[i-1, j],
                x[i,j] < x[i+1, j],
                x[i,j] < x[i, j-1],
                x[i,j] < x[i, j+1],
                ]):
                lowpoints.append([i,j])
    
    basin_sizes = []
    for lowpoint in lowpoints:
        explored_already = []
        basin_size = explore_path(x, lowpoint, 0) -1
        basin_sizes.append(basin_size)
    return np.product(sorted(basin_sizes)[-3:])


if __name__ == "__main__":
    with open("day9/inputs/input1.txt", "r") as f:
        input1 = [[int(i) for i in f if i != "\n"] for f in f.readlines()]

    print(part1(input1))
    print(part2(input1))
