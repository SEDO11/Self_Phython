# bfs 구현

from collections import deque

def bfs(stack, s, v):
    q = deque([s])
    v[s] = True
    
    while q:
        value = q.popleft()
        print(value, end=' ')
        for i in stack[value]:
            if v[i] == False:
                q.append(i)
                v[i] = True

stack = [
    [], #0
    [2, 3, 8], #1
    [1, 7], #2
    [4, 5], #3
    [3, 5], #4 
    [3, 4], #5
    [7], #6
    [2, 6], #7
    [1, 7] #8
]

v = [False] * 9

bfs(stack, 1, v)