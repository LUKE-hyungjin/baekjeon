import sys

add_num = list()
while True:
    try:
        add_num.append(sys.stdin.readline().rstrip().split())
        print(int(add_num[-1][0]) + int(add_num[-1][1]))
    except:
        break
