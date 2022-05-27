#중복 빼고 정렬하기
import sys
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
s = set(l)
l = list(s)
l.sort()
for i in l:
    print(i, end=" ")