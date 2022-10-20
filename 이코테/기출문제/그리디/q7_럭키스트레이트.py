
s = input()
a = list(map(int, s[:len(s)//2]))
b = list(map(int, s[len(s)//2:]))
r = 'READY'
if sum(a) == sum(b):
    r = 'LUCKY'
print(r)