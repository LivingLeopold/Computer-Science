def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for a in dice1:
        for b in dice2:
            if a>b:
                dice1_wins+=1
            elif b>a:
                dice2_wins+=1

    return (dice1_wins, dice2_wins)

def find_the_best_dice(Dices):

    for dice in Dices:
        assert len(dice) == 6

    solution = -1
    for i in range(0, len(Dices)):

        dices = []
        dices.extend(Dices)
        current_dice = Dices[i]
        del dices[i]
        for another_dice in dices:
            a, b = count_wins(current_dice, another_dice)
            if a > b:
                flag = 1
            elif a <= b:
                flag = 0
                break
        if flag == 1:
            solution = i
            break
    return solution

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    answer = find_the_best_dice(dices)
    if answer != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = answer
    else:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            better_dice = -1
            better_dice_wins = -1
            current_dice = dices[i]
            for t in range(len(dices)):
                potential_better_dice = dices[t]
                if t == i:
                    continue
                else:
                    x, y = count_wins(current_dice, potential_better_dice)
                    possibility = y / (x + y)
                    if possibility > better_dice_wins:
                        better_dice_wins = possibility
                        better_dice = t
            strategy[i] = better_dice


    return strategy

dices = eval(input('Please input dices:'))
print(compute_strategy(dices))
