# 내가 쓴 코드
# output = [value for value in range(1, 101)]
# result = 0
# print(output)
# print(type(output))
# for i in output:
#     if "{:b}".format(i).count("0") == 1:
#         print("{} : {}".format(i, "{:b}".format(i)))
#         result += i
# print(result)

# 책 코드
output = [ value for value in range(1, 101) if "{:b}".format(value).count("0") == 1]
for i in output:
     if "{:b}".format(i).count("0") == 1:
        print("{} : {}".format(i, "{:b}".format(i)))
print(sum(output))