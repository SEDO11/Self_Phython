#문자열 재정렬

l = list(map(str, input()))
r = []
n = 0
for i in l:
    if i.isdigit():
        n += int(i)
    else:
        r.append(i)
r.sort()
r = ''.join(r)
print(r+str(n))