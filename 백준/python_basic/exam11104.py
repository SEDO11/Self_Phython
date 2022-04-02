#2진수 -> 10진수, 리스트를 이용해 연산
run1 = int(input())
for i in range(run1):
    list_num = list(map(int, input()))
    result = 0
    for i in range(len(list_num)-1, -1, -1): # 맨 뒤부터 앞으로 이동하면서 연산
        result += list_num[i] * (2 ** (len(list_num)-i-1)) #맨뒤 부터 시작
    print(result)
    
# 2진수 -> 10진수 출력, 2진수 입력 받은걸 10진수로 변환
run2 = int(input())
for j in range(run2):
    b = input()
    print(int(b, 2))