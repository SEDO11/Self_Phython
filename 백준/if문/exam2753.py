#윤년

string = input()
num = int(string)

if num % 4 == 0 and num % 100 != 0: #윤년
    print(1)
elif num % 400 == 0:
    print(1)
else:
    print(0)