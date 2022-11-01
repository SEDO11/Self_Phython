# 3이 하나라도 포함되는 시간 수 구하기
# 완전탐색: 가능한 모든 경우의 수를 모두 검사한다.

h = int(input())
ms = 60
cnt = 0
for i in range(h+1): #for문을 3600 * (h+1)번 수행
    for j in range(ms):
        for k in range(ms):
            if '3' in str(i)+str(j)+str(k) :
                cnt += 1
print(cnt)

# 시간복잡도가 더 낮은 방법 for문을 3600번만 실행
n = int(input())
cnt = 0
for i in range(1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

if n >= 3:
    cnt *= (n+1)
    cnt += (60 * 60) - 1575
else:
    cnt *= (n+1)
print(cnt)