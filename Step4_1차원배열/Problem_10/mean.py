num = int(input())
input_list = list(map(int, input().split()))
sum = 0
for i in range(len(input_list)):
    sum += input_list[i] / max(input_list) * 100
print(sum / num)
