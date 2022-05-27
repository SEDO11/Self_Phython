# 좌표 정렬하기, y좌표
import sys 
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append((b, a))
l.sort()
for i in range(n):
    print(l[i][1], l[i][0])