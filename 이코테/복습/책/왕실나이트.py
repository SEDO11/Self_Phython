#왕실나이트

n = input()
x = ord(n[0]) - 96
y = int(n[1])

dx = [2, -2]
dy = [1, -1]
cnt = 0
for i in dx:
    for j in dy:
        nx = x + i
        ny = y + j
        if 1 <= nx <= 8 and 1 <= ny <= 8:
            cnt += 1
            
dx = [1, -1]
dy = [2, -2]
for i in dx:
    for j in dy:
        nx = x + i
        ny = y + j
        if 1 <= nx <= 8 and 1 <= ny <= 8:
            cnt += 1
print(cnt)
