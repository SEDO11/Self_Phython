# 소인수 분해 유클리드호제법

def gcd(a, b):
    if a < b:
        a, b = b, a
    m = a % b
    if m == 0:
        return b
    return gcd(b, m)

print(gcd(162, 192))