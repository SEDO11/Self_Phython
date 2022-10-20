# 무지의 먹방

import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    foods = len(food_times)  
    previous = 0  
    while True:
        
        now = q[0][0]  
        
        t = foods*(now-previous)
        if k >= t:
            k -= t
            foods -= 1
            previous = heapq.heappop(q)[0]
        else:
            i = k % foods
            q.sort(key=lambda x: x[1])  
            return q[i][1]
