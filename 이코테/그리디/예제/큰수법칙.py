# 큰수 법칙
# for 문은 사용할 필요가 없음
import time

n, m, k = map(int, input().split())
l = list(map(int, input().split()))
stime = time.time()
l.sort()
r = (m//k) * l[len(l)-1] * k
r += (m%k) * l[len(l)-2]
print(r)
etime = time.time()
print(etime-stime)