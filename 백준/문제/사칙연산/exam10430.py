al = input().split(" ")

a = int(al[0])
b = int(al[1])
c = int(al[2])

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)