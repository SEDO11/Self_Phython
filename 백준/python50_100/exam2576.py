#홀수
# 출력1: 모든 홀 수 덧셈
# 출력2: 최솟값 홀 수 출력
import sys
input = sys.stdin.readline
list_n = [] # 모든 홀 수를 저장할 리스트 선언

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        list_n.append(n) # 홀 수 일 경우 리스트에 저장
if len(list_n) == 0:
    print(-1)
else:
    print(sum(list_n))
    print(min(list_n))