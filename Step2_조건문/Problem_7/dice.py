dice = list(map(int, input().split()))
dice1 = dice[0]
dice2 = dice[1]
dice3 = dice[2]

if dice1 == dice2 == dice3:
    print(10000 + dice1 * 1000)
elif dice1 == dice2:
    print(1000 + dice1 * 100)
elif dice1 == dice3:
    print(1000 + dice1 * 100)
elif dice2 == dice3:
    print(1000 + dice2 * 100)
else:
    max_dice = max(dice)
    print(max_dice * 100)
