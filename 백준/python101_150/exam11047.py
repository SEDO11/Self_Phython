# 동전 0

n, k = map(int, input().split())
l = []
m = 0
for _ in range(n):
    l.append(int(input()))
l.sort(reverse=True)
for i in l:
    m += k // i
    k %= i
print(m)    