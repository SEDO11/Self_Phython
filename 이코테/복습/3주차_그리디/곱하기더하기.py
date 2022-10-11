#곱하기 더하기

n = list(map(int, input()))
r = n[0]
for i in range(1, len(n)):
    if n[i] > 1 and r > 1:
        r *= n[i]
    else:
        r += n[i]
print(r)