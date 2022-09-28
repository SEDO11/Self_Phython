# 럭키스트라이크

s = input()
l = s[:len(s)//2]
il = 0
r = s[len(s)//2:]
ir = 0
for i in l:
    il += int(i)
for i in r:
    ir += int(i)
print('LUCKY' if il == ir else 'READY')