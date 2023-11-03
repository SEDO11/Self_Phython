#행성수익

print('행성 별 수익(공백으로 나눠서 입력): ', end=' ')
l = list(map(int, input().split()))

dp = [0] * len(l)
dp[0] = l[0]
dp[1] = max(l[1], l[0])

for i in range(2, len(l)):
    dp[i] = max(dp[i-1], dp[i-2] + l[i])
print('최대 이익: ', dp[len(l)-1])