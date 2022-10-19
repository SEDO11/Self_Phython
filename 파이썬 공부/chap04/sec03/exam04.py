max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i 
    mul = j * i #값 계산
    
    if max_value < mul: #최대값이 되는 경우에 a, b, max값을 넣어줌
        max_value = mul
        a = j
        b = i
        
print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))