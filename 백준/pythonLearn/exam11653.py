# 소인수 분해

num = int(input()) 
x = 2 # 소인수 초기값

while num != 1:
    if num % x == 0: # x로 나누어지는경우
        num /= x
        print(x)
    else : # x로 나누어 지지 않는경우
        x += 1