num = int(input())
add_num = list()
for _ in range(num):
    add_num.append(input().split())
for i in range(num):
    print(int(add_num[i][0]) + int(add_num[i][1]))
