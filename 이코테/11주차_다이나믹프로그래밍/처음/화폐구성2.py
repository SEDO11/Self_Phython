#화폐구성

n, m = map(int, input().split())
dp = [10001] * 10001
c = []

for _ in range(n):
    c.append(int(input())) # 화폐단위 정보 저장

dp[0] = 0
for i in range(n):
    for j in range(c[i], m+1):
        if dp[j-c[i]] != 10001:
            dp[j] = min(dp[j], dp[j-c[i]] + 1)
            print('화폐: {} / 동전수: {} / (i-k)원 만드는법 : {}'.format(j, dp[j], dp[j-c[i]]))

print(dp[m])