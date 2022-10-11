#bfs 

from collections import deque

def bfs(s, v, g):
    q = deque()
    q.append(s)
    v[s] = True
    while q:
        p = q.popleft()
        print(p, end=' ')
        for i in g[p]:
            if v[i] == False:
                v[i] = True
                q.append(i)

graph = [[0],
         [2, 3, 8],
         [1, 7],
         [4, 5],
         [3, 5],
         [3, 4],
         [7],
         [6, 8],
         [1, 7]]
v = [False] * 9
bfs(1, v, graph)
