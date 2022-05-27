#주차의 신

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    result = 0
    for i in range(1, len(l)):
        result += l[i] - l[i-1]
    print(result*2)