check_num = list(map(int, input().split()))
num_list = list(map(int, input().split()))
print_list = list()
for i in range(len(num_list)):
    if num_list[i] < check_num[1]:
        print_list.append(num_list[i])
for j in range(len(print_list)):
    print(print_list[j], end=" ")
