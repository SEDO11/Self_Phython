# 스택
import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
        a = sys.stdin.readline().split()
        o = a[0]
    
        if o == "top":
            if len(l) == 0:
                print(-1)
            else:
                print(l[-1])
        elif o == "pop":
            if len(l) == 0:
                print(-1)
            else:
                print(l[-1])
                del l[-1]
        elif o == "size":
            print(len(l))
        elif o == "empty":
            if len(l) == 0:
                print(1)
            else:
                print(0)
        elif o == "push":
            l.append(int(a[1]))