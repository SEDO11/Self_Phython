# 셀프 넘버
# *******
natural_num = set(range(1, 10001)) # 1~10000 세트 생성
generated_num = set() # 생성자가 있는 숫자를 저장할 세트

for i in range(1, 10001):       # i = 850       
    for j in str(i):            # j = "8", "5", "0"
        i += int(j)             # 850 + 8 + 5 + 0, i = 863
    generated_num.add(i)        # 생성자가 있는 숫자들

self_num = sorted(natural_num - generated_num) #생성자가 없는 세트로 만듬
for i in self_num:
    print(i) # 생성자가 없는 숫자 출력