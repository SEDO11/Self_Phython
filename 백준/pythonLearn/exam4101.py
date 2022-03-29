#크냐?

while True: #0 0이 나올때까지 반복 실행
    list_a = input().split()
    a = int(list_a[0])
    b = int(list_a[1])
    if a > b: # 앞에 숫자가 더 크면 Yes
        print("Yes")
    elif a == 0 and b == 0: # 0 0 이면 No
        break
    else: # a , b 이면 No
        print("No")