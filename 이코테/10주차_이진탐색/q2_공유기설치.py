import sys
input = sys.stdin.readline

# 집의 개수(N)과 공유기의 개수(C)를 입력받기
n, c = map(int, input().split())

# 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(n):
    array.append(int(input()))
# 이진 탐색 위해 정렬 수행
array.sort()

start = array[1] - array[0] # 공유기 사이 거리 최솟값(첫번째 집엔 무조건 공유기를 설치하니까)
end = array[-1] - array[0] # 공유기 사이 거리 최댓값
result = 0

while start <= end:
    mid = (start + end) // 2 # 가장 인접한 공유기 사이의 거리
    print('start: {}, end: {}, mid: {}'.format(start, end, mid))
    value = array[0] # 공유기 초기 설치 위치
    count = 1 # 공유기 설치 개수
    # 현재의 mid(공유기 사이 거리)를 이용한 공유기 설치
    for i in range(1, n): # 앞에서부터 설치
        if array[i] >= value + mid:
            print('array[i] = ', array[i], end=' ')
            # 공유기 설치 위치 변경
            value = array[i]
            # 개수 증가
            count += 1
            print('count: ', count)
    # mid 길이로 c개 이상의 공유기를 설치할 수 있는 경우, 공유기 사이 거리 증가
    if count >= c: 
        start = mid + 1
        result = end
    # mid 길이로 c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
    else:
        end = mid - 1
print(result)