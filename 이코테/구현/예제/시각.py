# 3이 하나라도 포함되는 시간 수 구하기
# 완전탐색: 가능한 모든 경우의 수를 모두 검사한다.

h = int(input())
ms = 60
cnt = 0
for i in range(h+1):
    for j in range(ms):
        for k in range(ms):
            if '3' in str(i)+str(j)+str(k) :
                cnt += 1
print(cnt)