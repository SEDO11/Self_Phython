#해당 범위 숫자 출력

a, b = map(int, input().split())
result = ""
n1 = min(a, b) #둘중에 작은 수 저장
n2 = max(a, b) # 둘중에 큰 수 저장
n = n2 - n1 -1 # 두 수 사이값 개수
if n2 == n1 or n2 == n1 + 1: # 두 수가 일치하거나 1 차이날 경우
    n = 0 # 두 수 사이의 정수 값이 없으므로 0
for i in range(n1+1, n2): # 두 수 사이값 출력
    if i == n1+1:
        result = str(i)
    else :
        result += " " + str(i)
print(n) # 개수 출력
print(result) # 수 출력