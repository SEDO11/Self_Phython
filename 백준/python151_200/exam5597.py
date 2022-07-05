# 일본 올림피아드 문제
# 과제 안 내신분
import sys
l = [x for x in range(1, 31)]
for i in range(28):
    s = int(sys.stdin.readline())
    if s in l:
        l.remove(s)
for i in l:
    print(i)