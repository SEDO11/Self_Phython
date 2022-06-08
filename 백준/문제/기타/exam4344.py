# 평균은 넘겠지
from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    cnt = 0
    l = list(map(int, stdin.readline().strip().split()))
    del l[0]  
    f = sum(l) / len(l)
    for i in l:
        if f < i:
            cnt += 1
    r = ((100 / len(l)) * cnt)
    print("{:.3f}%".format(r))
