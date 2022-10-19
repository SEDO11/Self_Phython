numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}

for number in numbers:
    if number == 0:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
    elif number == 1:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
    elif number == 2:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
    elif number == 3:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
    elif number == 4:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
    elif number == 5:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
    elif number == 6:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
    elif number == 7:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
    elif number == 8:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
    else:
        if number in counter: #카운터 딕셔너리 내부에 값이 있을 경우
            counter[number] += 1
        else: #카운터 딕셔너리 내부에 값이 없을 경우
            counter[number] = 1
        
print(counter)