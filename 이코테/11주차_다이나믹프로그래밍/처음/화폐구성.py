#화폐

n, m = map(int ,input().split())
l = []
dp = [10001] * 10001
l.sort()
for i in range(n):
    l.append(int(input()))

for i in l:
    dp[i] = 1

dp[0] = 0
for i in range(n):
    for j in range(l[i], m+1):
        if dp[j-l[i]] != 10001:
            dp[j] = min(dp[j], dp[j-l[i]]+1)
            
print(dp[m] if dp[m] <= 10000 else -1)