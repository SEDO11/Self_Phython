#안테나

import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()
m = (l[0] + l[-1]) // 2
k = 10e9
r = 0
for i in l:
    a = abs(m - i)
    k = min(k, a)
    r = i   
print(r)