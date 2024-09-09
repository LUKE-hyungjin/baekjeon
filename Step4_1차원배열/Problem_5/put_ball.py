num = list(map(int, input().split()))
space = [0 for count in range(num[0])]
for i in range(num[1]):
    list_input = list(map(int, input().split()))
    for j in range(list_input[1] - list_input[0] + 1):
        space[int(list_input[0]) - 1 + j] = list_input[2]
for k in range(len(space)):
    print(space[k], end=" ")
