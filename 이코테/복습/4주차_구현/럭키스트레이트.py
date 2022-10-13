#럭키스트레이트

n = list(map(int, input()))
c = len(n)//2
a = sum(n[0:c])
b = sum(n[c:])
if a == b:
    print('LUCKY')
else:
    print('READY')