# 뒤집힌 덧셈

a, b = map(str, input().split())
c = int(a[::-1]) + int(b[::-1])
print(int(str(c)[::-1]))