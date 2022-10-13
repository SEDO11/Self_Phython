# 음료수 얼려먹기 dfs

from collections import deque

def dfs(x, y):
    if a > x >= 0 and b > y >= 0 and graph[x][y] == '0':
        print('x, y: {}:{}'.format(x, y))
        graph[x][y] = '1'
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

#음료수 얼려먹기 bfs
def bfs(x, y):
    q = deque()

graph = []

a, b = map(int, input().split())

cnt = 0
for _ in range(a):
    graph.append(list(input()))

for i in range(a):
    for j in range(b):
        if dfs(i, j) == True:
            cnt += 1
print(cnt)

#음료수 얼려먹기 bfs