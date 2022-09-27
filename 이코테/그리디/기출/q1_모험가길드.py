#공포도

n = int(input())
l = list(map(int, input().split()))
l.sort()
r = 0
g = 0
for i in l:
    g += 1
    if g >= i:
        r+=1
        g=0
print(r)