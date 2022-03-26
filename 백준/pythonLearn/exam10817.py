# 세 수 / 세 개의 수 중에서 두번째로 큰 수 구하기

a = input().split() # 숫자 입력
list_a = list(map(int, a)) # 리스트의 값들을 정수형으로 변환
list_a.sort() # 차순 정렬
print(list_a[1]) # 중간값 출력