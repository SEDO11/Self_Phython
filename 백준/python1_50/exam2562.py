# 최댓값 
# 리스트 만들어서 9개의 자연수 입력 받고 
# 차순 정렬해서 최솟값과 최댓값 출력하면 될듯

list_a = []
max_a = 0
max_i = 0

for i in range(9): 
    num = int(input())
    list_a.append(num)

for i in range(9): #range(9) 대신 list_a 넣어도 되지만 몇 번째 수가 최대 인지 알기 위해 range 이용
    if list_a[i] > max_a:
        max_a = list_a[i]
        max_i = i+1
        
print(max_a)
print(max_i)