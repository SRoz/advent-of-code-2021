def read_day4_input(fn):
    with open(fn, "r") as f:
        calls =  [int(c) for c in f.readline().rstrip('\n').split(",")]
        _ = f.readline()
        
        boards = list()
        board = list()
        for line in f.readlines():
            clean_line = line.rstrip('\n').split(" ")
            if clean_line != ['']:
                board.append([int(c) for c in line.rstrip('\n').split(" ") if c!=''])
            else:
                boards.append(board)
                board = list()
        else:
            boards.append(board)
    return calls, boards

def test_bingo(boards):
    for board_number, board in enumerate(boards):
        for row in board:
            if all([n=="*" for n in row]):
                return board, board_number

        for col in zip(*board):
            if all([n=="*" for n in col]):
                return board, board_number

    else:
        return False    

def get_score(board, call):
    return call * sum([i  for line in board for i in line if i!= "*"])


def part1(boards, calls):
    boards = boards[:]
    
    n_boards = len(boards)
    board_size = len(boards[0])

    for call_n, call in enumerate(calls):
        print(f"Call: {call}")
        for b in range(n_boards):
            for i in range(board_size):
                for j in range(board_size):
                    if boards[b][j][i]==call:
                        boards[b][j][i] = "*"
                    if res:=test_bingo(boards):
                        winning_board, board_number =  res
                        print(winning_board)
                        winning_score = get_score(winning_board, call)
                        print(winning_score)
                        return winning_score, board_number, calls[(call_n):]
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

def part2(boards, calls):
    boards = boards[:]
    calls = calls[:]

    while len(boards) > 0:
        winning_score, board_number, calls = part1(boards, calls)
        winning_board = boards.pop(board_number)

if __name__ == "__main__":
    test_calls, test_boards = read_day4_input("day4/inputs/test1.txt")
    calls, boards = read_day4_input("day4/inputs/input1.txt")
    
    _ = part1(test_boards, test_calls)
    part2(test_boards, test_calls)
    
    #part1(boards, calls)
    part2(boards, calls)