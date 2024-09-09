input_list = list()
for _ in range(10):
    input_list.append(int(input()) % 42)
input_list.sort()
count = 0
check_num = -1
for i in range(len(input_list)):
    if check_num != input_list[i]:
        count += 1
        check_num = input_list[i]
print(count)
