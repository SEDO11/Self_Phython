#첫글자를대문자로

n = int(input())
for _ in range(n):
    t = input()
    tF = t[0].upper()
    t = tF + t[1:]
    print(t)