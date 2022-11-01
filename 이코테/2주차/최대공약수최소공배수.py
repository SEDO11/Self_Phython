# 모듈 이용
from math import *
a, b = map(int, input().split())
print('{}\n{}'.format(gcd(a, b), lcm(a, b)))

# 직접 구현
def gcd(a, b):
    if a < b:
        a, b = b, a
    m = a % b
    if m == 0:
        return b
    return gcd(b, m)

a, b = map(int, input().split())
c = gcd(a, b)
d = (a * b) // c
print('{}\n{}'.format(c, d))