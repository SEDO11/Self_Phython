#XOR

t = int(input())
    
def fn(v):
    if v%4==0:
        return v
    elif v%4==1:
        return (v-1)^v
    elif v%4==2:
        return (v-2) ^ (v-1) ^ v
    else:
        return 0
    
for _ in range(t):
    s, f = map(int, input().split())
    print(fn(s-1) ^ fn(f))