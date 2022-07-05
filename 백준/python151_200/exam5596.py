# 일본 올림피아드 문제
#시험점수

s = list(map(int, input().split()))
t = list(map(int, input().split()))
print(sum(s) if sum(s) >= sum(t) else sum(t))