#파도반수열

def bottom_up(v):
    for i in range(6, v+1):
        dp[i] = dp[i-1] + dp[i-5]

dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
l = []
n = int(input())
for _ in range(n):
    l.append(int(input()))
bottom_up(max(l))
for i in l:
    print(dp[i])