def get_path(velocity, target_box):

    path = [(0,0)]
    max_y = 0

    while True:
        if velocity[0]==0:
            velocity_x = 0
        elif velocity[0] > 0:
            velocity_x = velocity[0]-1
        elif velocity[0] < 0:
            velocity_x = velocity[0]+1
        velocity = (velocity_x, velocity[1]-1)
        
        new_x = path[-1][0] + velocity[0]
        new_y = path[-1][1] + velocity[1]
        path.append((new_x, new_y))

        if new_y > max_y:
            max_y = new_y

        if all([
            new_x >= min(target_box[0]),
            new_x <= max(target_box[0]),
            new_y >= min(target_box[1]),
            new_y <= max(target_box[1]),
        ]):
            hits_box = True
            break
        if new_x > max(target_box[0]) or new_y < min(target_box[1]):
            hits_box = False
            break
    
    return path, hits_box, max_y


def answers(input):
    all_ys = list()
    for i in range(0,400):
        for j in range(-300,300):
            _, hits_box, max_y = get_path((i,j), input)
            if hits_box:
                all_ys.append(max_y)
    
    print(max(all_ys))
    print(len(all_ys))

if __name__=='__main__':
    test1 = (20,30), (-10,-5)
    input1 = (241,273), (-97, -63)

    answers(test1)
    answers(input1)