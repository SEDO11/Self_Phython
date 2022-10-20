#문자열 뒤집기

from numpy import zeros


l = list(map(int, input()))
zero = 0
one = 0
r = l[0]
if r == 0:
    zero += 1
else:
    one += 1

for i in l:
    if r != i and i == 1:
        one += 1
        r = i
    elif r != i and i == 0:
        zero += 1
        r = i
print(min(one, zero))