#나이순 정렬
import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    a, b = map(str, input().strip().split())
    l.append((int(a), b))
l.sort(key = lambda x:x[0])
for i in range(len(l)):
    print("{} {}".format(l[i][0], l[i][1]))