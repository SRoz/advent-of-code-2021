def get_complete_edges(input):
    all_edges = list()
    for edge_from, edge_to in input:
        all_edges.append([edge_from, edge_to])
        all_edges.append([edge_to, edge_from])
    return all_edges

def solve(current_path, all_edges, n_paths, q2=False): 
    lowercase_caves = [p for p in current_path if p.lower()==p and p not in ['start', 'end']]
    revisit_not_happened = len(set(lowercase_caves))==len(lowercase_caves)
    
    next_edges = list()

    for p in all_edges:
        if q2:
            allowable_cave = p[1]==p[1].upper() or (p[1] not in current_path) or ((p[1] in lowercase_caves) and revisit_not_happened)
        else:
            allowable_cave = p[1]==p[1].upper() or (p[1] not in current_path)

        if p[0]==current_path[-1] and allowable_cave:
            next_edges.append(p[1])

    for edge in next_edges:
        if edge!='end':
            n_paths = solve(current_path + [edge], all_edges, n_paths, q2=q2)
        else:
            n_paths += 1
    return n_paths

def part1(input):
    all_paths = get_complete_edges(input)
    print(solve(['start'], all_paths, 0))

def part2(input):
    all_paths = get_complete_edges(input)
    print(solve(['start'], all_paths, 0, q2=True))


if __name__=='__main__':
    with open("day12/inputs/input1.txt", "r") as f:
        input1 = [l.replace("\n", "").split("-") for l in f.readlines()]

    part1(input1)
    part2(input1)