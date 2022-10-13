# 게임 개발

def turn_left():
    # 0북, 1동, 2남, 3서
    global s
    if s == 0:
        s = 3
    else:
        s -= 1

def solution(x, y):
    global cnt
    if graph[x][y] == 0 and 0 <= x <= m and 0 <= y <= n:
        graph[x][y] = 1
        cnt += 1
        c = 0
        for _ in range(4):
            c += 1
            turn_left()
            if s == 3:
                solution(x-1, y)
            elif s == 2:
                solution(x, y+1)
            elif s == 1:
                solution(x+1, y)
            else:
                solution(x, y-1)

        if c == 4:
            if s == 3:
                solution(x+1, y)
            elif s == 2:
                solution(x, y-1)
            elif s == 1:
                solution(x-1, y)
            else:
                solution(x, y+1)

cnt = 0
n, m = map(int, input().split())
x, y, s = map(int, input().split())

graph = []

for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)

solution(x, y)
print(cnt)