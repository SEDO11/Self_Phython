#정렬된 배열에서 특정 수 구하기

from bisect import *

n, x = map(int, input().split())
l = list(map(int, input().split()))
r = bisect_right(l, x) - bisect_left(l, x)
if r > 0:
    print(r)
else:
    print(-1)