numbers = list(range(1, 10+1)) # 1~10까지 리스트 형태로 값 생성

#홀수 추출
print(list(filter(lambda x: x % 2, numbers))) # 1은 Ture 이므로 홀수만 빠져나옴

#3이상 7미만 추출
print(list(filter(lambda x: 3<=x<7, numbers)))

#제곱해서 50미만 추출
print(list(filter(lambda x: x**2<50, numbers)))

#숫자 사이에 ::를 넣어서 출력
print("::".join(map(str, numbers)))