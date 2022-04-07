#플러그
import sys
input = sys.stdin.readline # for문 안에서 반복적으로 입력 받을 때 안 쓰면 시간 초과 오류 뜸

n = int(input())
p = 1
for i in range(n):
    p += int(input())
print(p-n)