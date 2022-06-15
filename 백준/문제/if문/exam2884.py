string = input().split(" ")
time = int(string[0])
minute = int(string[1])

if minute < 45:
    if time == 0:
        time = 23
    else:
        time -= 1
    minute += 60
minute -= 45

print(time, minute)