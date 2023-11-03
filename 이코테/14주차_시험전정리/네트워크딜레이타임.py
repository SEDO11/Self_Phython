# 네트워크 딜레이 타임

import collections
import heapq

times = [[1, 2, 1]]
n = 2
k = 1
result = -1
graph = collections.defaultdict(list)

for u, v, w in times:
    graph[u].append((v, w))
    
q = [(0, k)]
dist = collections.defaultdict(int)

while q:
    time, node = heapq.heappop(q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(q, (alt, v))
            
if len(dist) == n:
    result = max(dist.values())

print(result)