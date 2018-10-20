import random

def roll_dice(dice, lock):
    for i in range(5):
        if(lock[i] == 0):
            dice[i] = random.randint(1,6)

def calc_most(dice):
    number = dice[0]
    max_count = 0
    for i in range(1,7):
        count = 0
        for j in range(5):
            if(dice[j] == i):
                count += 1
        if(count > max_count):
            max_count = count
            number = i
    return number


def test_for_yatzee(dice):
    n = dice[0]
    all_same = True
    for i in range(5):
        if(dice[i] != n):
            all_same = False
    return all_same

def attempt_yatzee():
    dice = [0,0,0,0,0]
    lock = [0,0,0,0,0]
    roll_dice(dice, lock)

    print("First roll: ", dice)
    lock = [0,0,0,0,0]
    save = calc_most(dice)
    print("We will save: " , save)
    for i in range(5):
        if(dice[i] == save):
            lock[i] = 1
    roll_dice(dice, lock)

    print("Second roll: ", dice)
    lock = [0,0,0,0,0]
    save = calc_most(dice)
    print("We will save: " , save)
    for i in range(5):
        if(dice[i] == save):
            lock[i] = 1
    roll_dice(dice, lock)

    print("Final roll: " , dice)
    print()
    return test_for_yatzee(dice)


def play_game():
    score = 0
    for i in range(13):
        print("New try: ")
        t = attempt_yatzee()
        if(t):
            if score == 0:
                print("Yatzee found in round " , i)
                score += 50
            else:
                print("Yatzee found in round " , i)
                score += 100
    return score

def play_games(games):
    scores = []
    for i in range(games):
        scores.append(play_game())
    av = sum(scores) / len(scores)
    print("Average: " ,  av)
    print("Max: ", max(scores))

play_games(1000)
