s = input()
r = 0
for si in s:
    i = int(si)
    if i <= 1 or r <= 1:
        r += i
    else:
        r *= i
print(r)