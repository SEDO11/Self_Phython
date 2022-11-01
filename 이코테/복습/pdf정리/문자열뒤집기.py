#문자열 뒤집기

n = input()
r = n[0]
zero = 0
one = 0
if r == '0':
    zero += 1
else:
    one += 1

for i in range(1, len(n)):
    if n[i] != r:
        if n[i] == '1':
            one += 1
        else:
            zero += 1
        r = n[i]
print(min(one, zero))