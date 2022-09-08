# 선택 정렬과 기번정렬 라이브러리의 수행시간 비교
from random import randint
import time
# 배열에 1~99사이의 값을 갖는 정수를 10000개 삽입
array = list(randint(1, 100) for _ in range(10000)) 

s_time = time.time()

# 선택 정렬 코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

e_time = time.time()
print('선택 정렬 걸린 시간: {:.3f} s'.format(e_time-s_time))

array = [] # 배열 초기화
array = list(randint(1, 100) for _ in range(10000))

s_time = time.time()

# 기본정렬 측정
array.sort()

e_time = time.time()
print('기본 정렬 걸린 시간: {:.3f} s'.format(e_time-s_time))