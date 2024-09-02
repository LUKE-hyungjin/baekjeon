temp = list(map(int, input().split()))
hour = temp[0]
min = temp[1]
time = int(input())
add_hour = int(time / 60)
add_min = time % 60
if min + add_min >= 60:
    hour = hour + add_hour + 1
    min = min + add_min - 60
    if hour + add_hour >= 24:
        hour = hour % 24
else:
    hour = (hour + add_hour) % 24
    min = min + add_min
print(f"{hour} {min}")
