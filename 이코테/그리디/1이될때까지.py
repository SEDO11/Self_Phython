# 1이 될 때까지

import time

n, k = map(int, input().split())
stime = time.time()
cnt = 0
while n > 1:
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
etime = time.time()
print(cnt)
print('{:.3f}s'.format(etime - stime))