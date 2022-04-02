#토너먼트

cnt = 0
result = 0
for i in range(6):
    wl = input()
    if wl == "W":
        cnt += 1
if cnt >= 5:
    result = 1
elif cnt >= 3:
    result = 2
elif cnt >= 1:
    result = 3
else :
    result = -1
print(result)