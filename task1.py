def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for a in dice1:
        for b in dice2:
            if a>b:
                dice1_wins+=1
            elif b>a:
                dice2_wins+=1
    print('Dice1_wins = %d' %(dice1_wins))
    print('Dice2_wins = %d' %(dice2_wins))
    return (dice1_wins, dice2_wins)

dice1 = list(eval(input('Please input dice1:')))
dice2 = list(eval(input('Please input dice2:')))
count_wins(dice1, dice2)


