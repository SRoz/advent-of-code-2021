def most_common(vec):
    zeroes = 0
    ones = 0

    for i in vec:
        if i ==0:
            zeroes +=1
        if i ==1:
            ones +=1
    
    if zeroes <= ones:
        to_ret = 1
    elif ones < zeroes:
        to_ret = 0
    return to_ret

def binary_to_decimal(binary_vec):
    total = 0
    power = 1
    for b in reversed(binary_vec):
        total += b*power
        power *= 2

    return total

def part1(input):
    gamma_binary = list()
    epsilon_binary = list()
    for pos in zip(*input):
        gamma_binary.append(most_common(pos))
        epsilon_binary.append(1-gamma_binary[-1])
    
    print(binary_to_decimal(gamma_binary) * \
        binary_to_decimal(epsilon_binary))
    

def get_rating(input, type='oxy'):
    current = input
    for i in range(len(input[0])):
        # keep only numbers selected by bit criteria until 1 left

        vec_i = [c[i] for c in current]

        if type=='oxy':
            rating = most_common(vec_i)
        else:
            rating = 1-most_common(vec_i)

        # reconstruct current
        new = list()
        for c in current:
            if c[i] == rating:
                new.append(c)
        current = new

        if len(current)==1:
            break
    return current[0]

def part2(input):


    oxy_rating = get_rating(input, type='oxy')
    co2_rating = get_rating(input, type='co2')
        
    print(binary_to_decimal(oxy_rating) * 
     binary_to_decimal(co2_rating))


if __name__=="__main__":

    with open("day3/inputs/test1.txt", "r") as f:
        test1 = [[int(d) for d in f if d!= "\n"] for f in f.readlines()]

    with open("day3/inputs/input1.txt", "r") as f:
        input1 = [[int(d) for d in f if d!= "\n"] for f in f.readlines()]

    part1(input1)
    part2(input1)