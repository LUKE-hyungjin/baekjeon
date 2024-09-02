import sys

num = int(input())
add_num = list()
for i in range(num):
    add_num.append(sys.stdin.readline().rstrip().split())
    print(
        f"Case #{i+1}: {int(add_num[i][0])} + {int(add_num[i][1])} = {int(add_num[i][0]) + int(add_num[i][1])}"
    )
