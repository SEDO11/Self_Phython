# 연산자 끼워넣기

import sys
input = sys.stdin.readline

mn = 10e9
mx = -10e9

def dfs(i, arr):
    global add, sub, mul, div, mx, mn
    if i == n:
        mx = max(mx, arr)
        mn = min(mn, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + l[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - l[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * l[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr / l[i]))
            div += 1

n = int(input())
cnt = n
l = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

dfs(1, l[0])
print(mx)
print(mn)