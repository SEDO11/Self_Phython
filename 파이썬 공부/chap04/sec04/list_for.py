# for문을 사용하지 않은 경우
array1 = []
for i in range(0, 20, 2):
    array1.append(i * i)
print(array1)
print()

array2 = [i * i for i in range(0, 20, 2)] #for 앞 부분이 최종 결과
print(array2)