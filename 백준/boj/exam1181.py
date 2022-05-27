#덱
import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
        a = sys.stdin.readline().split()
        o = a[0]
        if o == "push_front":
            l.insert(0, a[1])
        elif o == "push_back":
            l.append(int(a[1]))
        elif o == "pop_front":
            if len(l) == 0:
                print(-1)
            else:
                print(l[0])
                del l[0]
        elif o == "pop_back":
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
        elif o == "front":
            if len(l) == 0:
                print(-1)
            else:
                print(l[0])
        elif o == "back":
            if len(l) == 0:
                print(-1)
            else:
                print(l[-1])