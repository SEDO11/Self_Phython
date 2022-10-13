# 특정 거리의 도시 찾기

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x =map(int, input().split())
graph = [[] for _ in range(n+1)]
d = [0] * (n+1)
v = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(x):
    answer = []
    q = deque([x])
    v[x] = True
    d[x] = 0
    while q:
        p = q.popleft()
        for i in graph[p]:
            if v[i] == False:
                v[i] = True
                d[i] = d[p] + 1
                q.append(i)
                if d[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer

for i in bfs(x):
    print(i)