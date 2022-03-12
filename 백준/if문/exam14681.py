#사분면 고르기

string1 = input()
string2 = input()

x = int(string1)
y = int(string2)

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)