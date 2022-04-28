#점수 집계

t = int(input())
for _ in range(t):
    n = list(map(int,input().split()))
    n.sort()
    r = 0
    for i in range(len(n)):
        if i > 0 and i < 4:
            r += n[i]
    if n[3] - n[1] >= 4:
        print("KIN")
    else:
        print(r)