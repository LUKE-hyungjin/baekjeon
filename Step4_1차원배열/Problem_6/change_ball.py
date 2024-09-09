num = list(map(int, input().split()))
space = [i + 1 for i in range(num[0])]
for i in range(num[1]):
    change_list = list(map(int, input().split()))
    temp = space[change_list[0] - 1]
    space[change_list[0] - 1] = space[change_list[1] - 1]
    space[change_list[1] - 1] = temp
for k in range(len(space)):
    print(space[k], end=" ")
