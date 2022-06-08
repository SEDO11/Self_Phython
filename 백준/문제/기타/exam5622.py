#다이얼

d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
t = 0
for i in range(len(s)):
    for j in d:
        if s[i] in j:
            t += d.index(j) + 3
print(t)