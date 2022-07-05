#좋은 자동차 번호판
t = int(input())
for i in range(t):
    a, b = input().split('-')
    a = 26*26*(ord(a[0])-65)+26*(ord(a[1])-65)+(ord(a[2])-65)
    b = int(b)
    print("nice" if max(a, b) - min(a, b) <= 100 else "not nice")