# #201
# def print_coin():
#     for i in range():

# #202
# print_coin()

# #203
# def print_coin(num):
#     for i in range(num):
#         print("비트코인", i+1) 
# print_coin(100)

#215
# def print_with_smile(result):
#     print("{}:D".format(result))
# print_with_smile("hello")

#217
# def pup(price):
#     price = price * 1.3
#     print(price) 
# pup(1000)

#220
# def print_max(a, b, c):
#     if a > b and a > c:
#         print("a가 제일 크다", a)
#     elif b > a and b > c:
#         print("b가 제일 크다", b)
#     else:
#         print("c가 제일 크다", c)
# print_max(10, 20, 30)

#221
# def print_reverse(string1):
#     result = string1[::-1]
#     print(result)
# print_reverse("python")

#222
# result = 0
# score = [1, 2, 3]
# def print_score(num):
#     result = sum(num) / len(num)
#     print(result)
# print_score(score)

#223
# def print_even(num):
#     for i in num:
#         if i % 2 == 0:
#             print(i)
# print_even([1, 3, 2, 10, 12, 11, 15])

#224
# key = {"이름":"김말똥", "나이":30, "성별":0}
# def print_keys(k):
#     for i in k:
#         print(i, k[i])
# print_keys(key)

#225
# my_dic = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# def print_value_by_key(my_dict, string1):
#     print(my_dict.get(string1))
# print_value_by_key(my_dic, "10/26")

# 226, 모르겠어서 답 봤음
# def print_5xn(line):
#     chunk_num = int(len(line) / 5)
#     for x in range(chunk_num + 1) :
#         print(line[x * 5: x * 5 + 5])      
# print_5xn("아이엠어보이유알어걸")

#227
# def printmxn(string, length):
#     chunk_num = int(len(string) / length)
#     for x in range(chunk_num + 1) :
#         print(string[x * length: x * length + length])
# printmxn("아이엠어보이유알어걸", 3)

#228
def calc_monthly_salary(annual_salary):
    print(int(annual_salary / 12))

calc_monthly_salary(12000000)