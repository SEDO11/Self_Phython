#문자열 분석
while True :
    try :
        s=input()
        r1 = 0
        r2 = 0
        r3 = 0
        for w in range(97, 123):
            r1 += s.count(chr(w))
        for W in range(65, 91):
            r2 += s.count(chr(W))
        for n in range(10):
            r3 += s.count(str(n))
        r4 = s.count(chr(32))
        print(r1, r2, r3, r4)
    except Exception:
        break