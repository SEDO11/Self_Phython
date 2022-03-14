run = True

while run:
    for i in range(10):
        print(i)
    run = False
print()
    
# while을 for문 처럼 사용하기
j = 0
while j < 10:
    print("{}번째 반복문 입니다.".format(j))
    j += 1