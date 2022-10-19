numbers = list(range(1, 10+1)) # 1~10까지 값 저장

print("홀수만 추출")
print(list(filter(lambda x : x % 2 != 0 ,numbers)))

print("3이상, 7미만 추출 ")
print(list(filter(lambda x : 7 > x >= 3  ,numbers)))

print("제곱해서 50 미만 추출")
print(list(filter(lambda x : x ** 2 < 50 ,numbers)))