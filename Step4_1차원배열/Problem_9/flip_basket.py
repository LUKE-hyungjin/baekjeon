num = list(map(int, input().split()))
space = [i + 1 for i in range(num[0])]
for i in range(num[1]):
    list_input = list(map(int, input().split()))
    for j in range(int((list_input[1] - list_input[0] + 1) / 2)):
        temp = space[list_input[0] - 1 + j]
        space[list_input[0] - 1 + j] = space[list_input[1] - 1 - j]
        space[list_input[1] - 1 - j] = temp
for k in range(len(space)):
    print(space[k], end=" ")
