# 상하좌우

import time

n = int(input())
l = list(map(str, input().split()))
x = 1
y = 1
mx = n
my = n
stime = time.time()
for i in l:
    if i == 'R' and y < 5:
        y += 1
    elif i == 'L' and y > 1:
        y -= 1
    elif i == 'U' and x > 1:
        x -= 1
    elif i == 'D' and x < 5:
        x += 1
print(x, y)
etime = time.time()
print(etime - stime)
