import pandas as pd
from collections import Counter
from copy import deepcopy

def det_dice(n):
    return 9*n -3

def move1(position, score, move_number):
    roll = det_dice(move_number)
    position = (position + roll) % 10
    if position == 0:
        position = 10
    score += position
    return position, score


def part1(input):
    p1_pos, p1_score = input[0], 0
    p2_pos, p2_score = input[1], 0

    i = 0
    while True:
        i+=1
        if i % 2 ==1:
            p1_pos, p1_score = move1(p1_pos, p1_score, i)
        else:
            p2_pos, p2_score = move1(p2_pos, p2_score, i)

        if max(p1_score, p2_score) >= 1000:
            break
    
    print(min(p1_score, p2_score) * 3 * i)

def dirac_dice():
    return [3] + [4]*3 + [5]*6 + [6]*7 + [7]*6 + [8]*3 + [9]


def move2(position, roll):
    return ((position + roll) % 10).mask(lambda x: x==0, 10)

def play(games, player, roll):
    games = games.copy()

    games.loc[games.active, f"p{player}_position"] = move2(
        games.loc[games.active, f"p{player}_position"], roll)
    games.loc[games.active,
              f"p{player}_score"] += games.loc[games.active, f"p{player}_position"]
    games.loc[games[f"p{player}_score"]>=21, 'active'] = False
    return games

def combine(games):
    return (games
            .groupby(
                ['p1_position', 'p1_score', 'p2_position', 'p2_score', 'active']
            )
            .num_games
            .sum()
            .reset_index()
            )

def play_round(games, player):
    output = list()

    active_games = games[games.active]
    finished_games = games[~games.active]

    for roll in dirac_dice():
        output.append(play(active_games, player, roll))

    return combine(pd.concat(output + [finished_games]))

def part2(input):
    games = pd.DataFrame({
            'p1_position': input[0],
            'p1_score' : 0,
            'p2_position': input[1],
            'p2_score' : 0,
            'num_games' : 1.0,
            'active': True
            }, index=[0])

    player = 1
    while True:
        games = play_round(games, player)
        if not games.active.any():
            break
        else:
            player = 1 if player == 2 else 2
    
    p1_wins = games.loc[(games.p1_score > games.p2_score), 'num_games'].sum()
    p2_wins = games.loc[(games.p1_score < games.p2_score), 'num_games'].sum()
    print(max(p1_wins, p2_wins))


if __name__=='__main__':
    test1 = (4,8)
    input1 = (6,2)

    #part1(test1)
    part1(input1)

    #part2(test1)
    part2(input1)

