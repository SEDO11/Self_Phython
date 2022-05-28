#AC
# import sys
# from collections import deque
# t = int(sys.stdin.readline())
# for _ in range(t):
#     a = list(sys.stdin.readline())
#     b = int(sys.stdin.readline())
#     c = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
#     queue = deque(c)
#     try:
#         if b == 0:
#             print("error")
#         if a.count("R")%2 == 1:
#                 queue.reverse()
#         for _ in range(a.count("D")):
#             queue.popleft()
#         print("[" + ",".join(queue) + "]")
#     except Exception:
#         print("error")
        
        
import sys
from collections import deque
t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")