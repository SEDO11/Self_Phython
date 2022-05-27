#대회 자리
t = int(input())
for _ in range(t):
    l = []
    a, b = map(int, input().split())
    for i in range(a):
        l.append(int(input()))
    r = set(l)
    if a <= b:
        print(a-len(r))
    else:
        print(a-b)
        