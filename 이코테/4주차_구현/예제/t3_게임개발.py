
def turn_left():
    global f
    f -= 1
    if f < 0:
        f = 3

mx, my = map(int, input().split())
x, y, f = map(int, input().split())
l = []
cnt = 0
for i in range(mx):
    l.append(list(map(int, input().split())))
l[x][y] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[f]
    ny = y + dy[f]
    
    if l[nx][ny] == 0:
        l[nx][ny] = 1
        cnt += 1
        x = nx
        y = ny
        turn_time  = 0
        continue
    turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[f]
        ny = y - dy[f]
        if l[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(cnt)