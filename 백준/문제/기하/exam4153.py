#직각삼각형

while True:
    l = []
    l = list(map(int, input().split()))
    l.sort()
    if sum(l) == 0:
        break
    elif l[2] ** 2 == l[1] **2 + l[0] ** 2:
        print("right")
    else:
        print("wrong")