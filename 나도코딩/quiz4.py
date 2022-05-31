# 추첨
from random import *
l = list(range(1, 21)) # 1~20까지 리스트 작성
shuffle(l) # 리스트 섞기
w = sample(l, 4) # 리스트 내에서 4개의 값을 뽑음
print("----당첨자 발표----")
print(" 치킨 당첨자 : {}".format(w[0])) # 첫번째 인덱스를 치킨
print(" 커피 당첨자 : {}".format(w[1:])) # 두번째 부터는 커피
print("----축하합니다----")