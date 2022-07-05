# 가장 많은 글자
import sys
s = sys.stdin.read()

s.replace(' ', '')
t = []
r = []
for i in range(97, 123):
    t.append((s.count(chr(i)), chr(i)))
t.sort(reverse=True)

m = t[0][0]
for i in range(len(t)):
    if t[i][0] == m:
        r.append(t[i])
r.sort(key=lambda x: x[1])
for i in range(len(r)):
    print(r[i][1], end='')