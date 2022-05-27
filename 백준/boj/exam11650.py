# 좌표 정렬하기, x좌표
import sys 
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append((a, b))
l.sort()
for i in range(n):
    print(l[i][0], l[i][1])