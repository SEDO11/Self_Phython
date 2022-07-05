#국회의원 선거
import sys
input = sys.stdin.readline

t = int(input())
d = 0
l = []
cnt = 0
for i in range(t):
    if i == 0:
        d = int(input())
    else:
        l.append(int(input()))
        
if len(l) > 0:
    while d <= max(l):
        l.sort()
        d += 1
        l[-1] -= 1
        cnt += 1
print(cnt)