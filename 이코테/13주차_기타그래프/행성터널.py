#행성터널
#크루스칼 알고리즘

import sys
import copy
input = sys.stdin.readline
n = int(input())
def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b: parent[b] = a
	else: parent[a] = b
graph = []
for i in range(n):
	x, y, z = map(int, input().split())
	graph.append([x, y, z, i])

x = copy.deepcopy(graph)
y = copy.deepcopy(graph)
z = copy.deepcopy(graph)
x.sort(key=lambda x : x[0])
y.sort(key=lambda x : x[1])
z.sort(key=lambda x : x[2])
edges = []
for i in range(len(x)-1):
	edge = (abs(x[i+1][0] - x[i][0]), x[i][-1], x[i+1][-1])
	edges.append(edge)
for i in range(len(y)-1):
	edge = (abs(y[i+1][1] - y[i][1]), y[i][-1], y[i+1][-1])
	edges.append(edge)
for i in range(len(z)-1):
	edge = (abs(z[i+1][2] - z[i][2]), z[i][-1], z[i+1][-1])
	edges.append(edge)
edges.sort()
parent = [0] * n
for i in range(n):
	parent[i] = i
answer = 0
for edge in edges:
	dist, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		answer += dist
print(answer)