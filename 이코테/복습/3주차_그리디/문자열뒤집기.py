#문자열 뒤집기

s = list(map(int, input()))
z = 0
o = 0
r = s[0]
if r == 1:
    o = 1
else:
    z = 1
for i in s:
    if r != i:
        if i == 1:
            o += 1
        else:
            z += 1
        r = i
print(min(o, z))