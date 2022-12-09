#우선순위 큐를 구현하기 위한 힙

import heapq

def heapsort(iterable):
    h = []
    result = []
    
    # 데이터가 입력된 순으로 힙에 저장
    for value in iterable:
        heapq.heappush(h, value)
    
    # 제일 작은 값 부터 힙에서 추출하여 result에 저장
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# value와 heapq.heappop(h)에 음수를 취하면 큰 수부터 출력
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)