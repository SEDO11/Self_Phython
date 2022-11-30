# 떡볶이 떡 만들기
# 이진 트리 탐색
# 백준 2805 나무자르기와 같은 문제
# 테스트를 해봤는데 백준의 문제 자체가 조금 이상한 것 같다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 1, max(arr)

while start <= end:
    result = 0 # 기존에서 잘린 후 떡볶이 길이 총 합
    mid = (start + end) // 2 # 떡볶이 자른 길이
    for i in arr:
        if i > mid: # 떡볶이의 길이가 자를 길이보다 큰 경우만 실행
            result += i - mid
    if result < m: 
        end = mid-1
    else:
        start = mid+1

print(end)