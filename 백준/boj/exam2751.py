# 수 정렬하기 2
import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
for i in l:
    print(i)