#이진수 덧셈
a, b = input().split()
s = bin(int(a, 2) + int(b, 2))
print(s[2:])