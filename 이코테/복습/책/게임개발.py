# 게임개발

def turn_left():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1

def fn(a, b):
    pass

n, m = map(int, input().split())
a, b, d = map(int, input().split())
l = []
for _ in range(n):
    l = l.append(list(map(int, input().split())))
