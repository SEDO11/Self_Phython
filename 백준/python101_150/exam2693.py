#n번째 큰 수

t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    l.sort()
    print(l[-3])