student_list = list()
check_list = list()
for i in range(28):
    student_list.append(int(input()))
for j in range(30):
    if j + 1 not in student_list:
        check_list.append(j + 1)
print(min(check_list))
print(max(check_list))
