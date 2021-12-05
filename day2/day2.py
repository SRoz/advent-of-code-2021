
def parse_input(input):
    direction, magnitude = input.split(" ")
    return direction, int(magnitude)

unitary_map = {
    'forward': (1, 0),
    'backward': (-1, 0),
    'up': (0, -1),
    'down': (0, 1)
}

def project(direction_vector, magnitude):
    """Does not normalise, only works on unitary vecs"""
    output = list() 
    for dim in direction_vector:
        output.append(dim*magnitude)
    return output

def move(starting_coords, movement):
    output = list()
    for s, m in zip(starting_coords, movement):
        output.append(s + m)
    return output

def vector_product(vector):
    running_prod = 1
    for v in vector:
        running_prod = running_prod * v
    return running_prod


def question1(inputs):
    
    current_coords = [0,0]

    for instruction in inputs:
        direction, magnitude = parse_input(instruction)
        movement = project(unitary_map[direction], magnitude)
        current_coords = move(current_coords, movement)
    return vector_product(current_coords)


def move_q2(starting_coords, movement, magnitude):
    output = list()

    # Forwards
    output.append(starting_coords[0] + movement[0]*magnitude)

    # Up/ down
    output.append(starting_coords[1] + starting_coords[2]*movement[0]*magnitude)

    # aim
    output.append(starting_coords[2] + movement[1]*magnitude)

    return output


def question2(inputs):

    #coords: x,y,aim
    current_coords = [0,0,0]
    for instruction in inputs:
        direction, magnitude = parse_input(instruction)
        current_coords = move_q2(current_coords, unitary_map[direction], magnitude)
    return vector_product(current_coords[:2])


if __name__ == "__main__":
    with open("day2/inputs/test1.txt", "r") as f:
        test1 = f.readlines()
        test1 = [t.replace("\n", "") for t in test1]

    with open("day2/inputs/input1.txt", "r") as f:
        input1 = f.readlines()
        input1 = [t.replace("\n", "") for t in input1]

    print(question1(input1))
    print(question2(input1))
