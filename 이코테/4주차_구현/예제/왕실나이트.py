# 좌표가 8x8의 체스판에서 나이트의 좌표가 주어졌을 때 이동할 수 있는 경우의 수

import time

def fn(nx, ny):
    global cnt
    for i in nx:
        for j in ny:
            dx = x
            dy = y
            dx += i
            dy += j
            if 1 <= dx <= 8 and 1<= dy <=8:
                cnt += 1

xy = input()
stime = time.time()
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = l.index(xy[0])+1
y = int(xy[1])
cnt = 0

ax = [1, -1]
ay = [2, -2]
fn(ax, ay)

ax = [2, -2]
ay = [1, -1]
fn(ax, ay)
print(cnt)
etime = time.time()
print(etime - stime)