string = input()
num = int(string)
result = num
run = True
i = 0

while run:
    a = num // 10 # 입력 십의 자리
    b = num % 10 # 압력 일의 자리
    c = (a + b) % 10 # 출력 일의 자리
    num = (b * 10) + c # 각각의 일의 자리를 더함
    i += 1
    if result == num: 
        break
print(i)