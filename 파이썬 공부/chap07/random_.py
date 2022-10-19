# 랜덤 모듈
from random import *

list_n = [1, 2, 3, 4, 5]

# 0.0 <= x < 1.0 사이의 float 리턴
print(random())

#uniform(min, max): 지정한 범위 사이의 float을 리턴
print(uniform(10, 20))

# randrange(max): 0부터 max사이의 값 리턴
# randrange(min, max): min 부터 max 사이의 값 리턴
print(randrange(10)) 
print(randrange(10, 20))

#리스트 내부 요소를 랜덤하게 선택
print(choice(list_n))

#리스트 내부 요소를 랜덤하게 섞음
print(list(list_n))
print(shuffle(list_n))
print(list(list_n))

#sample 리스트의 요소중에 랜덤으로 k개를 뽑습니다.
print(sample(list_n, k=2))