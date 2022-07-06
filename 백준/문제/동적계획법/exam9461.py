#파도반 수열

def p(n):
    global l
    if n < 6:
        return l[n]
    else:
        for i in range(6, n+1):
            num = l[i-1] + l[i-5]
            l.append(num)
        return l[n]
    
s = int(input())
for i in range(s):
    l = [0, 1, 1, 1, 2, 2]
    n = int(input())
    print(p(n))