#크로아티아 알파벳

c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
cnt = 0
for i in c:
    s = s.replace(i, '*')
print(len(s))