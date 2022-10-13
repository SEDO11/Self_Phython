def gcd(x, y):
    if x < y:
        x, y = y, x
    m = x % y
    if m == 0:
        return y
    return gcd(y, m)
c = int(input())
for _ in range(c):
    r = 0
    s = list(map(int, input().split()))
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
                r = max(r, gcd(s[i], s[j]))
    print(r)