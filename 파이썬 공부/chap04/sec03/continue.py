numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10: # 10보다 작으면 출력하지 않고 다음으로 넘어감
        continue
    print(number)