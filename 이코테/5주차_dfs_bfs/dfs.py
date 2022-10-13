
def dfs(stack, s, v):
    v[s] = True
    print(s, end=' ')
    
    for i in stack[s]:
        if v[i] == False:
            dfs(stack, i, v)

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

dfs(stack, 1, v)