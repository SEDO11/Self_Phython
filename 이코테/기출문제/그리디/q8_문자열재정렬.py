#문자열 재정렬

a = input()
s = []
n = 0
for i in a:
    if i.isdigit():
        n += int(i)
    else:
        s.append(i)
s.sort()
s.append(str(n))
print(''.join(s))