#dfs

def dfs(s):
    v[s] = True
    print(s, end=' ')
    for i in graph[s]:
        if not v[i]:
            dfs(i)

graph = [[], [2, 3], [1, 6, 8], [1, 4, 5], [3], [3], [2, 7], [6, 8], [2, 7]]
v = [False] * 9
dfs(1)