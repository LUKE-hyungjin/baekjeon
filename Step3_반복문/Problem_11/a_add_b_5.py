import sys

add_num = list()
while True:
    add_num.append(sys.stdin.readline().rstrip().split())
    if int(add_num[-1][0]) == 0 and int(add_num[-1][1]) == 0:
        break
    else:
        print(int(add_num[-1][0]) + int(add_num[-1][1]))
