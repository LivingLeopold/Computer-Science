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

Dices = eval(input('Please input dices:'))

print("The best dice is:" + str(find_the_best_dice(Dices)))
