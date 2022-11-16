from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())

v = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()
    
def bfs(s):
    q = deque([s])
    cnt = 1
    v[s] = cnt
    while q:
        x = q.popleft()
        for i in graph[x]:
            if v[i] == 0:
                cnt += 1
                q.append(i)
                v[i] = cnt
                
bfs(r)
for i in v[1::]:
    print(i)