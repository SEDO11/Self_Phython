#피보나치 탑다운

def top_down(i):
    global cnt
    cnt += 1
    if i <= 2:
        return 1
    if dp[i]>0: # 이미 연산을 했으면 바로 출력
        return dp[i]
    dp[i] = top_down(i-1) + top_down(i-2)
    return dp[i]

n = int(input())
dp = [0] * (n+1)
cnt = 0
print(top_down(n), cnt)