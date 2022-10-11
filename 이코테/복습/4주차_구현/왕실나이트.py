#왕실 나이트

x, y = map(str, input())
x = ord(x)-96
y = int(y)

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0
for ix, iy in steps:
        rx = x + ix
        ry = y + iy
        if 1 <= rx <= 8 and 1 <= ry <= 8:
            cnt += 1
print(cnt)