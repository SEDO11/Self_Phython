# 곱하기 혹은 더하기를 활요하여 만들 수 있는 가장 큰 수 출력
import time

s = input()
stime = time.time()
li = list(s)
li = list(map(int, li))
for i in range(1, len(li)):
    if 1 >= li[i-1] or 1 >= li[i]:
        li[i] = li[i-1] + li[i]
    else:
        li[i] = li[i-1] *  li[i]
print(li[len(li)-1])
etime = time.time()
print('{:.3f}s'.format(etime-stime))