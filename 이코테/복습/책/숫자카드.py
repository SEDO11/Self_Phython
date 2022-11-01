#숫자 카드 게임

n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
r = min(l[0])
for i in range(1, len(l)):
    r = max(r, min(l[i]))
print(r)