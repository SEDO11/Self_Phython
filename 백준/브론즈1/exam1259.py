#팰린드롬수

while True:
    s = input()
    t = 0
    if s == '0':
        break
    for i in range(len(s)//2):
        if(s[i] != s[-(i+1)]):
            t = 1
    print("yes" if t == 0 else "no")