#정수 삼각형

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(2):
        if i == 1 or i == n-1:
            dp[i][i-1] = max(dp[i][i-1], dp[i][i-1] + dp[i-1][i-1])
            dp[i][i] = max(dp[i][i], dp[i][i] + dp[i-1][i-1])
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
print(list(dp))