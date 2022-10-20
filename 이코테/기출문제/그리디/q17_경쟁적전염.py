from collections import deque

n, k = map(int, input().split())
array = []
data = []
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        if array[i][j] != 0:
            data.append((array[i][j], 0, i, j))  # 시간을 넣는 아이디어..
target_t, target_x, target_y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

data.sort()
queue = deque(data)

while queue:
    virus, s, x, y = queue.popleft()
    if s == target_t:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny  < n:
            if array[nx][ny] == 0:
                array[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

print(array[target_x-1][target_y-1])