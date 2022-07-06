#알고리즘 수업 - 피보나치
    
# 동적 계획법
def fn2(n):
    global l, c
    if n == 0: return l[0]
    elif n == 1: return l[1]
    else:
        for i in range(2, n+1):
            c += 1
            num = l[i-1] + l[i-2]
            l.append(num)
        return l[n]
        
l = [0, 1]
c = 0

s = int(input())
print(fn2(s), c-1)
print(list(l))