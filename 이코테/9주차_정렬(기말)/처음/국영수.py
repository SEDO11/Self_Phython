#국영수

import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    name, kor, eng, mat = input().split()
    l.append((name, int(kor), int(eng), int(mat)))

l.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in l:
    print(i[0])