#일곱 난쟁이
l = []
t = 0
for _ in range(9):
    r = int(input())
    l.append(r)
    t += r
    
for i in range(9):
    for j in range(i+1, 9):
        if t - l[i] - l[j] == 100:
            n1, n2 = l[i], l[j] 
            l.remove(n1)
            l.remove(n2)
            
            for i in l:
                print(i)
            break
     
    if len(l) < 9:
        break