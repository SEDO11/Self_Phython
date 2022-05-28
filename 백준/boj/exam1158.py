#요세푸스 문제
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque([i+1 for i in range(n)]) # 1~n까지 list 값 생성
print('<', end='')
for i in range(n - 1):
    for _ in range(k - 1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=', ')
print(queue.popleft(), end='>')