#숫자로 변환되는 것들만 리스트에 넣기
list_a = ["52", "273", "32", "스파이", "103"]

list_n = [] # 숫자로 된 것들만 저장할 리스트 변수
for i in list_a:
    try:
        float(i) #숫자형이 아니면 여기서 예외가 발생
        list_n.append(i)
    except:
        pass
print("{} 내부에 있는 숫자는 ".format(list_a))
print(" {} 입니다.".format(list_n))