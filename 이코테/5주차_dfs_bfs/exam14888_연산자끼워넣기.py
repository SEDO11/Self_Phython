#연산자 끼워넣기

from collections import deque

# 최댓값, 최솟값 초기화
ma = -1e9
mi = 1e9

# 입력
n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

def dfs(i, arr):
    global ma, mi, add, sub, mul, div
    
    if i==n:
        ma = max(ma, arr)
        mi = min(mi, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + a[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - a[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * a[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr/a[i])) # 여기는 //이 아닌 /로 해서 int()로 묶어 주어야 제대로된 결과 도출
            div += 1

dfs(1, a[0])
print(ma)
print(mi)