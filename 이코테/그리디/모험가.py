# 모험가 공포도

import time

v = int(input())
n = list(map(int, input().split()))
n.sort()
cnt = 0
r = 0

for i in n:
    cnt += 1
    if cnt >= i:
        r += 1
        cnt = 0
print(r)