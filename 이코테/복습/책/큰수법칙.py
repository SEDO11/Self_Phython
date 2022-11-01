#큰수법칙

from audioop import reverse


n, m, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
cnt = 0
r = 0
while m > 0:
    if cnt < k:
        r += l[0]
        cnt += 1
    else:
        r += l[1]
        cnt = 0
    m -= 1
print(r)