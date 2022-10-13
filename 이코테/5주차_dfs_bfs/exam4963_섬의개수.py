def dfs(x, y):
    if x <= -1 or x >= b or y <= -1 or y >= a:
        return False
    if graph[x][y] == 1:
        # print('x, y: {}:{}'.format(x, y))
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x-1, y-1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        dfs(x, y-1)
        dfs(x-1, y+1)
        dfs(x, y+1)
        dfs(x+1, y-1)
        return True

while True:
    graph = []

    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    cnt = 0
    for _ in range(b):
        graph.append(list(map(int, input().split())))

    for i in range(b):
        for j in range(a):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)