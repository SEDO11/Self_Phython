#게임개발

def turn_left():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1

n, m = map(int, input().split())
di = [[0] * m for _ in range(n)]
x, y, d = map(int, input().split())

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if l[nx][ny] == 0 and di[nx][ny] == 0:
        l[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        if turn_time == 4:
            nx = x + dx[d]
            ny = y + dy[d]
            
            if l[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0
            
print(cnt)