# 한수
# ****
cnt = 0
x = int(input())
for i in range(1, x+1):
    n = i
    if n < 100: # 100 이하인 수는 모두 한수 이므로
        cnt += 1
    elif i >= 1000: # 1000 이상일 경우 종료
        break
    else: # 세자리 부터 한 수 구하기
        l = []
        k = 0
        while n != 0:
            l.append(n % 10)
            n = n // 10
        if l[0] - l[1] == l[1] - l[2]:
            cnt += 1
print(cnt)