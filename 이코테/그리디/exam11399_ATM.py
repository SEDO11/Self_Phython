# 백준 ATM

n = int(input())
k = list(map(int, input().split()))
k.sort()
r = 0
for i in range(1, n+1):
    r += sum(k[0:i])
print(r)