#식량창고 털기

n = int(input())

array = list(map(int, input().split()))

dp = [0] * 100
dp[0] = array[0]
dp[1] = max(dp[0], array[1])
for i in range(2, n):
    print('d[{}] = max({}, {})'.format(i, dp[i-1], dp[i-2] + array[i]))
    dp[i] = max(dp[i-1], dp[i-2] + array[i])
print(dp[n-1])