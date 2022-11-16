#1로 만들기
x = int(input())
dp = [0] * 1000001

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1 # 현재의 수에서 1을 뺀다
    if i%2 == 0: # 2로 나누어 지는 경우
        dp[i] = min(dp[i], dp[i//2] +1)
    if i%3==0: # 3으로 나누어지는 경우
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[x])