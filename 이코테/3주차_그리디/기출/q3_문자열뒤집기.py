#문자열 뒤집기

s = input()
z = 0
o = 0
if s[0] == '0':
    o += 1
else:
    z += 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            o += 1
        else:
            z += 1
print(min(z, o))