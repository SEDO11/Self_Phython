string1 = input().split(" ")
timer = int(input())
hour = int(string1[0])
minute = int(string1[1])
max_min = 60
add = 0

# 분 계산
minute += timer % max_min
add = int(minute / max_min)
minute %= max_min

# 시간 계산
hour += int(timer / max_min) + add
if hour >= 24:
    hour %= 24

# 출력
print(hour, minute)