limit = 10000
i = 1
sum_value = 0

while sum_value < limit:
    sum_value += i
    i += 1 #i++, 증가 연산자
    
print("{}를 더할 때 {}을 넘으면 그때의 값은 {}입니다.".format(i-1, limit, sum_value))