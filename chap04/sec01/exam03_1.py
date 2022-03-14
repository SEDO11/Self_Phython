numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    result = number % 2
    if result == 0:
        print(number, "는 짝수 입니다.")
    else:
        print(number, "는 홀수 입니다.")