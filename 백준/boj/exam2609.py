#최대공약수 최소공배수
# 유클리드호제법

# 내가 작성한 코드
def gcd(a, b):
    a %= b
    if a == 0:
        return b
    return gcd(b, a)
a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print((a*b)//g)

# gcd 함수 사용
from math import gcd
a,b = map(int,input().split())
k = gcd(a,b)
print(k)
print((a*b)//k)