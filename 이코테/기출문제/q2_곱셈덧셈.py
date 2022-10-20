#곱하기 혹은 더하기

n = list(map(int, input()))
r = n[0]
for i in range(1, len(n)):
    r = max(r+n[i], r*n[i])
print(r)