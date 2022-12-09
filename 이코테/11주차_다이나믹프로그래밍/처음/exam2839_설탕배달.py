# 설탕 배달 다이나믹 알고리즘
x = int(input())
dp = [5001] * 5001
dp[3] = 1
dp[5] = 1
for i in range(6, x+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1
print(dp[x] if dp[x] <= 5000 else -1)