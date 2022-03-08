import math

str_input = input("원의 반지름> ")
num_input = float(str_input)

area = math.pi * (num_input ** 2)
cir = 2 * math.pi * num_input

print("반지름: ", num_input)
print("넓이: ", area)
print("둘레: ", cir)
