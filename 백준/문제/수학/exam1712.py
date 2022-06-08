#손인분기점
import sys

a, b, c = map(int, sys.stdin.readline().strip().split())
if b >= c:
    cnt = -1
else:
    cnt = a//(c-b) + 1
print(cnt)