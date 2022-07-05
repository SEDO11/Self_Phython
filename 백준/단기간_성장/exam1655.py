#가운데를 말해요

import sys
import heapq

# n = int(sys.stdin.readline())
# l = []
# for i in range(1, n+1):
#     l.append(int(sys.stdin.readline()))
#     l.sort()
#     if i == 1:
#         print(l[0])
#     elif i % 2 == 0:
#         print(l[i//2-1])
#     else:
#         print(l[i//2])

leftHeap=[]
rightHeap=[]
n = int(sys.stdin.readline())
for i in range(n):
    s = int(sys.stdin.readline())
    
    if len(leftHeap) == len(rightHeap): # 왼쪽에서 부터 값을 집어 넣음
        heapq.heappush(leftHeap, -s) # 왼쪽 힙에 값 저장
    else:
        heapq.heappush(rightHeap, s) # 오른쪽 힙에 값 저장
    
    # 오른쪽 힙에 값이 들어 있으면서 오른쪽 힙의 최솟값보다 왼쪽힙의 최대값이 더 큰 경우
    # 서로 값을 바꿔줌
    if rightHeap and rightHeap[0] < -leftHeap[0]: 
        t1 = heapq.heappop(leftHeap)
        t2 = heapq.heappop(rightHeap)
        
        heapq.heappush(leftHeap, -t2)
        heapq.heappush(rightHeap, -t1)
    print(-leftHeap[0]) # 왼쪽 힙의 제일 큰 값이 중간값이므로 출력
print(list(leftHeap), list(rightHeap))

#https://www.youtube.com/watch?v=BOnNK-NiPIs&ab_channel=%EC%9D%80%EC%84%9C%ED%8C%8C%EC%9D%98%EB%8C%80%EC%B6%A9APS