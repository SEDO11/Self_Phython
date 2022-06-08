#직사각형에서 탈출

x, y, w, h = map(int, input().split())
a1 = w - x
b1 = h - y
l = [x, y, a1, b1]
print(min(l))