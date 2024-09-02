budget = int(input())
count = int(input())
things = list()
for _ in range(count):
    things.append(input().split())

for i in range(count):
    budget -= int(things[i][0]) * int(things[i][1])
if budget == 0:
    print("Yes")
else:
    print("No")
