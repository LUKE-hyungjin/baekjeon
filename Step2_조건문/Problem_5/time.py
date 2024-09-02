num = list(map(int, input().split()))
if num[1] >= 45:
    num[1] = num[1] - 45
    print(f"{num[0]} {num[1]}")
elif num[1] < 45:
    if num[0] >= 1:
        num[0] = num[0] - 1
        num[1] = num[1] + 60 - 45
        print(f"{num[0]} {num[1]}")
    elif num[0] == 0:
        num[0] = 23
        num[1] = num[1] + 60 - 45
        print(f"{num[0]} {num[1]}")
