from numpy import array


for i in range(5):
    print(str(i) + "= 반복 변수")
print()

for i in range(5 , 10):
    print(str(i) + "= 반복 변수")
print()

for i in range(0 , 10, 3):
    print(str(i) + "= 반복 변수")
print()

array = [1, 2, 3, 4, 5]
for element in array: # 리스트의 갯수가 5 이므로 0~4 까지 5번 반복
    print(element)
print()

#리스트를 이용할 때에는 이 방법을 많이 씀
for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))
print()

# 큰 수 부터 작은 수 까지
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))
print()