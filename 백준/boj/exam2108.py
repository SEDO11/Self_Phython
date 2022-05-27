#통계학
# 산술평균 / 중앙값 / 최빈값 / 범위
import sys
from collections import Counter

# 개수 입력
n = int(sys.stdin.readline())
l = []
cnt = 0

# 값 입력
for _ in range(n):
    l.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(l)/n))

# 중앙값
l.sort()
print(l[int((n-1)/2)])

# 최빈값
r = Counter(l).most_common() # 내림차순 정렬
if len(r) > 1: # 값이 두 개 이상일 경우
    if r[0][1] == r[1][1]: # 두 개의 값이 일치할 경우
        print(r[1][0]) # 두번 째 최빈값 출력
    else:
        print(r[0][0]) # 최빈값 출력
else:
    print(r[0][0]) # 최빈값 출력

# 범위
print(max(l)-min(l))